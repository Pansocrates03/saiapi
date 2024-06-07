# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
import base64
import uuid
from django.core.files.base import ContentFile
import cv2
import mediapipe as mp
import pickle
import numpy as np

# Load your model once at the module level
model_dict = pickle.load(open('./api/model_PRO3.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"detail": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Aquí puedes manejar el archivo como prefieras
        # Por ejemplo, guardarlo en el sistema de archivos:
        with open(f'media/{file_obj.name}', 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
                print(destination.name)

        data_aux = []
        # Leer la imagen
        frame = cv2.imread(destination.name)
        if frame is not None:
            frame = cv2.flip(frame, 1)
            H, W, _ = frame.shape  # Asegúrate de que la imagen se ha leído correctamente
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
        #muesta imagen con landmarks
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, #imagen a dibujar
                        hand_landmarks, #output del modelo
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()            
                )
           

                if hand_landmarks is not None:
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

                        x1 = int(min(X_) * W)
                        y1 = int(min(Y_) * H)
                        x2 = int(max(X_) * W)
                        y2 = int(max(Y_) * H)

                        prediction = model.predict([np.asarray(data_aux)])
                        predicted_character = prediction[0]
            else:
                predicted_character = 'No se detecto mano'

        print(predicted_character)
        return Response({'letra':predicted_character}, status=status.HTTP_201_CREATED)
        




