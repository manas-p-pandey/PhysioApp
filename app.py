from flask import Flask, render_template, send_file, make_response, jsonify
from camera import VideoCamera
import os

app = Flask(__name__)
camera = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frame_image')
def frame_image():
    frame_path = camera.capture_frame()
    response = make_response(send_file(frame_path, mimetype='image/jpeg'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

@app.route('/histogram_data')
def histogram_data():
    hist_data = camera.get_last_histogram()
    return jsonify(hist_data.tolist())

@app.route('/stop_camera')
def stop_camera():
    camera.release()
    return "Camera stopped"


# ✅ Proper entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5500,debug=True)
