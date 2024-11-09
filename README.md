![Convolutional Neural Network](https://img.shields.io/badge/Implementation-Convolutional%20Neural%20Network-darkgreen)

# Face Recognition System

This project is a **Face Recognition System** that uses a Convolutional Neural Network (CNN) for image classification. The model is trained on labeled image data and can recognize faces based on the provided dataset.

## Project Structure


### Directory Breakdown:
- **`.ipynb_checkpoints/`**: Contains Jupyter notebook checkpoints for version control.
- **`Data/`**: Contains raw image data for training.
- **`dataset/`**: Stores the dataset used for training the model.
- **`Labelled_Data/`**: Contains labeled data (images with face labels).
- **`static/`**: Static files such as images or CSS.
- **`templates/`**: Templates for the user interface.
- **`Data_Prep/`**: Python scripts or notebooks for data preparation and preprocessing.
- **`face.ipynb`**: Jupyter notebook that handles image processing, data loading, and model training.
- **`Model.ipynb`**: Jupyter notebook for defining and training the CNN model.
- **`model.keras`**: The saved model after training. It contains the architecture, weights, and training configuration.
- **`README.md`**: This file, which explains the project.
- **`UI.py`**: Python script for the user interface of the face recognition system.

## Code Explanation

### 1. **Data Preparation**
The `Data_Prep` module processes the image data into a suitable format for training. The images are resized and normalized to ensure they can be fed into the CNN model.

### 2. **Model Definition**
In `Model.ipynb`, we define a Convolutional Neural Network (CNN) using Keras. The CNN consists of two convolutional layers followed by pooling layers, flattening the output, and passing it through dense layers to classify the images.

### 3. **Training the Model**
We compile the model using the Adam optimizer and categorical cross-entropy loss function. The model is trained on the prepared data for several epochs.

### 4. **Prediction**
Once the model is trained, we use it to make predictions on new images. The predicted class label is mapped back to the corresponding face name.

### 5. **Saving the Model**
The trained model is saved in the `model.keras` file, which can be reloaded later for predictions without retraining.

## Running the Code
1. Prepare the data and preprocess it as shown in the `Data_Prep` section.
2. Train the model by running `Model.ipynb`.
3. Use the saved model in `model.keras` to make predictions on new images.

## Requirements
- Python 3.x
- TensorFlow/Keras
- NumPy, pandas, seaborn, matplotlib
- OpenCV (for image processing)

## Get Started with 
  ```bash
  git clone <repository_url>
```
