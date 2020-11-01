import cv2
import os


class FaceDetector:
    def __init__(self, log):
        self.log = log
        self.face_cascade = cv2.CascadeClassifier('./src/haarcascade_frontalface_default.xml')

    def detect_all(self, filepath):
        self.log.info('Detect faces.')

        frames = {}
        file_list = os.listdir(filepath)
        for file in file_list:
            faces = self.detect(os.path.join(filepath, file))
            frames[file] = faces
        return frames

    def detect(self, file, faces_count=1):
        img = cv2.imread(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return self.face_cascade.detectMultiScale(gray, 1.1, faces_count)
