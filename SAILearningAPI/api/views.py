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
model_dict = pickle.load(open('./api/model_PRO.p', 'rb'))
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

        data = []
        labels = []
        # Leer la imagen
        img = cv2.imread(destination.name)
        if img is not None:  # Asegúrate de que la imagen se ha leído correctamente
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Procesar la imagen con mediapipe
            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x)
                        data_aux.append(y)

                # Asegúrate de que tienes las 42 coordenadas (21 puntos de referencia, cada uno con x e y)
                if len(data_aux) == 42:
                    data.append(data_aux)
                    labels.append(letra_carpeta)

    # Cerrar el objeto mediapipe
        hands.close()



        return Response({'edi': predictions}, status=status.HTTP_201_CREATED)
        




