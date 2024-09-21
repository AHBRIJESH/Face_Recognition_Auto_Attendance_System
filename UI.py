# importing Necessary Libraries
import io
import os
import cv2
import pyodbc
import base64
import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime 
from tensorflow.keras.models import load_model
from flask import Flask,render_template,request,jsonify

# defining flask app
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')  # rendering the html page to the flask app

@app.route('/send', methods=['POST'])    #flask app to get image from the web page
def return_image():                      # function to get image from the web page
    
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image = base64.b64decode(image_data)
    img = Image.open(io.BytesIO(image))        # retreving the image in base64 encodded format 
    
    cap_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    g_img = cv2.resize(cap_img,(300,300))
    in_img = g_img.reshape(1,300,300,1)        # converting the image into the predection model specific size

    cnn = load_model('model.keras')
    predection = cnn.predict(in_img)
    labels = ['donald','mickey','minion','olfa','pooh','pumba']
    Name = labels[np.argmax(predection)]       # performing the predection

    currunt_time = datetime.now()
    Date = currunt_time.strftime('%Y-%m-%D')
    time = currunt_time.strftime('%H:%M:%S')   # determing the currunt time and date

    connection = pyodbc.connect("DSN=SQL")     # establishing connection to the MySql Database
    cur = connection.cursor()
    cur.execute("truncate table Attendence_Record")
    cur.commit()
    cur.execute('INSERT INTO Attendence_Record (Date, Name, Entry_time) VALUES (?, ?, ?)', (Date, Name, time))   # pusing the attendence into the database
    cur.commit()

    return jsonify({'message': 'Image processed successfully'})

if __name__ == "__main__":
    app.run()