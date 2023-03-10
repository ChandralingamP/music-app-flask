from flask import Flask, request, jsonify, send_file
from flask_restx import Api, Resource, fields
from flask_cors import CORS
import cv2
import base64
import numpy as np
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

@app.route("/")
def Home():
    return "ksjbdf"

@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    print(data["imgURL"])
    return jsonify(data)

@app.route('/image', methods=['POST'])
def get():
    data = request.json
    encoded_data = data["imgURL"].split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img_file = open('image.jpg', 'wb')
    img_file.write(nparr)
    input_image = cv2.imread('./image.jpg')
    result = DeepFace.analyze(input_image,enforce_detection=False ,actions = ['emotion'])
    respone = jsonify(result=result)
    print(result)
    respone.headers.add("Access-Control-Allow-Origin", "*")
    return respone
    # return "result"


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    app.run(port=5001, debug=True)
