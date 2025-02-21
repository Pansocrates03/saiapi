# consumers.py
import cv2
import mediapipe as mp
import pickle
import numpy as np
from channels.generic.websocket import WebsocketConsumer
from threading import Thread
import time

class VideoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.model_dict = pickle.load(open('C:/Users/dsanc/Desktop/SAILearning/SAILearningWeb/SAILEARN/model_PRO.p', 'rb'))
        self.model = self.model_dict['model']
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
        self.capture = cv2.VideoCapture(0)
        self.thread = Thread(target=self.send_frames)
        self.thread.start()
        self.correct_response = None

    def disconnect(self, close_code):
        self.capture.release()
        self.hands.close()

    def send_frames(self):
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    data_aux = []
                    X_ = []
                    Y_ = []
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x)
                        data_aux.append(y)
                        X_.append(x)
                        Y_.append(y)

                    prediction = self.model.predict([np.asarray(data_aux)])
                    if prediction[0] == 'A':
                        print("Se identificó la letra 'A'.")
                        self.correct_response = 'A'

                    else:
                        self.correct_response = None

            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            self.send(bytes_data=frame_bytes)
            time.sleep(0.1)

        self.disconnect(1000)