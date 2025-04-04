import cv2
import numpy as np
import os

class VideoCamera:
    def __init__(self):
        if not os.path.exists('static'):
            os.makedirs('static')
        self.camera = None
        self.last_hist = np.zeros((256, 1))

    def start(self):
        if self.camera is None or not self.camera.isOpened():
            self.camera = cv2.VideoCapture(0)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def release(self):
        if self.camera and self.camera.isOpened():
            self.camera.release()
            self.camera = None

    def capture_frame(self):
        self.start()  # Ensure camera is active
        success, frame = self.camera.read()
        if not success:
            raise Exception("Failed to capture frame")

        # Save frame
        frame_path = 'static/frame.jpg'
        cv2.imwrite(frame_path, frame)

        # Calculate histogram
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        self.last_hist = hist

        return frame_path

    def get_last_histogram(self):
        return self.last_hist
