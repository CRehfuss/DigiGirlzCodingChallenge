# samplecode.py
# Import statements that are needed to make sure the files run!
from flask import Flask
from flask import render_template
import requests
import json
app = Flask(__name__)
 

# This is what is output when you go to http://127.0.0.1:5000/ After it's running. 
@app.route('/')
def test():
    return "Welcome to DigiGirlz!"

#This is what will output when you go to <your url>/hello or <YOUR URL>/hello/<A NAME>
# Render template returns what's in the templates/hello.html
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name =name)

# This method makes an API call to Microsoft's Face Detection API
# Read more about this Machine Learning API and play with a demo here: https://azure.microsoft.com/en-us/services/cognitive-services/face/
@app.route('/facePhoto')
def facephoto():
    # The subscription key and face_api_url allow us to connect to the service that holds the face recognition API
    subscription_key = '<TO FILL OUT>'

    face_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'

    # The image_url is the photo that will be sent to the machine learning model.
    image_url = "https://image.freepik.com/free-photo/top-view-of-friends-having-fun_1098-980.jpg"

    # Headers is needed for all API calls. Here is where we specify how to connect.
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    # Here is where we specify what we want to return. 
    # Read more here: https://docs.microsoft.com/en-us/azure/cognitive-services/face/concepts/face-detection
    # This is unique to the FACE api
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    # Here is where we specify the image we want to send
    data = {"url": image_url}

    #Here is where we make the API call to the algorithm
    response = requests.post(face_api_url, params=params, headers=headers, json = data)

    # Getting back the response and serializing it so it's readable
    faceResponse = response.json()

    #This prints out to the terminal all the output.
    print("Here is the entire response from the API call!!!")
    print(faceResponse)
    print("End response")
    
    facelist = []

    # Each face is a different object in faceResponse.
    # See an example output here: https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/python#examine-the-response
    # This loops through each face that was detected in the image.
    # You can specify what you what to see here
    for item in faceResponse:
        # facelist.append([item['faceAttributes']['gender'], item['faceAttributes']['age']])
        facelist.append(item['faceAttributes'])

    #This outputs to the photo.html file that's located under /templates
    return render_template('photo.html', img_url = image_url, numfaces = len(facelist), facelist = facelist)


# TODO: Fill out this method and make a call to the Microsoft Computer Vision API.
# Play with a Computer Vision demo here: https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/
@app.route('/itemPhoto')
def itemphoto():
    subscription_key = '<TO FILL OUT>'

    face_api_url = 'https://eastus.api.cognitive.microsoft.com//vision/v2.0/analyze'

    # TODO: Add an image URL
    image_url = None

    # TODO: Fill out the headers, params, and data
    # HINT: Only one of them need to be different than the Face API
    # HINT: Look at this page https://westcentralus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa
    headers = None
    params  = None
    data    = None
    
    response = requests.post(face_api_url, headers=headers, params=params, json=data)

    imageResponse = response.json()

    
    print("Here is the entire response from the API call!!!")
    print(imageResponse)
    print("End response")

    return "Fill this out as a challenge!"
    # uncomment out the below line when you get to the last challenge  
    # return render_template('itemphoto.html', img_url = image_url,  imageResponse = imageResponse)


if __name__ == '__main__':
    app.run(debug=True)