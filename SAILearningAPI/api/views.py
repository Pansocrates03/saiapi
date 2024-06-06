# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status

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
        
        return Response({"detail": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
