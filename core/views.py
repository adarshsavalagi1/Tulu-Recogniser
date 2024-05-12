from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from .serializer import ImageUploadSerializer  # Import your serializer

class_to_char = {1: 'ಅ', 2: 'ಆ', 3: 'ಎ', 4: 'ಏ', 5: 'ಅಃ', 6: 'ಅಂ', 7: 'ಬ', 8: 'ಭ', 9: 'ಚ', 10: 'ಛ', 11: 'ಡ',
                 12: 'ಢ', 13: 'ದ', 14: 'ಧ', 15: 'ಇ', 16: 'ಈ', 17: 'ಗ', 18: 'ಘ', 19: 'ಹ', 20: 'ಐ', 21: 'ಜ', 22: 'ಝ',
                 23: 'ಕ', 24: 'ಖ', 25: 'ಲ', 26: 'ಳ', 27: 'ಮ', 28: 'ನ', 29: 'ಣ', 30: 'ಞ', 31: 'ಙ', 32: 'ಒ', 33: 'ಓ',
                 34: 'ಔ', 35: 'ಪ', 36: 'ಫ', 37: 'ರ', 38: 'ಋ', 39: 'ೠ', 40: 'ಸ', 41: 'ಶ', 42: 'ಷ', 43: 'ಟ', 44: 'ತ',
                 45: 'ಥ', 46: 'ಠ', 47: 'ಉ', 48: 'ಊ', 49: 'ವ', 50: 'ಯ'}

@api_view(['POST'])
def predict_character(request):
    if request.method == 'POST':
        # Create an instance of the serializer with request data
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Get the uploaded image from the validated data
            uploaded_image = serializer.validated_data['image']

            # Load your Keras model and process the image here
            model_path = 'core/ml-models/thulu_model.h5'
            model = load_model(model_path)
            img = Image.open(uploaded_image).convert('L')
            img = img.resize((100, 100))
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = np.expand_dims(img_array, axis=-1)
            img_array = img_array.astype('float32') / 255.0

            # Make predictions using the loaded model
            prediction = model.predict(img_array)
            predicted_character = np.argmax(prediction)

            predicted_char = class_to_char.get(predicted_character, 'Unknown')

            return Response({
                'Predicted Character': predicted_char,
                'predicted_label': predicted_char,
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Only POST method is allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def testing(request):
    return Response({'test': 'test'})




@api_view(['POST'])
def upload_image(request):
    if request.method == 'POST':
        # Create an instance of the serializer with request data
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Get the uploaded image from the validated data
            uploaded_image = serializer.validated_data['image']

            return Response({'message': 'Image uploaded successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Only POST method is allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)