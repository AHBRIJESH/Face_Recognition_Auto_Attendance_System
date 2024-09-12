const image = document.getElementById('photo');
const canva = document.getElementById('display');
const button = document.getElementById('capture_button');
const context = canva.getContext('2d');

function display_camera()
{ navigator.mediaDevices.getUserMedia({video: true})
    .then(stream =>{image.srcObject = stream;})
    .catch(err =>{console.error('Please Allow the camera to access the camer',err)})}

button.addEventListener('click',()=>{ context.drawImage(image, 0, 0, canva.width, canva.height);
                                      const cap_image = canva.toDataURL('image/png');
                                      console.log(cap_image);
                                      fetch('/send', {method:'POST',headers:{'Content-Type':'application/json'}, body: JSON.stringify({image: cap_image}) })

                                      .then(response => response.json())
                                      .then(data=> console.error('Attendence Punched'))
                                      .catch(error => console.error("Error Occured",error))})

window.addEventListener('load', display_camera);