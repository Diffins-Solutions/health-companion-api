from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import DailyLog
from .serializers import DailyLogSerializers
from .utils import get_emotion
# import os
# from django.conf import settings

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
#
# def get_emotion(text):
#     model_path = os.path.join(settings.BASE_DIR, 'mood_api', 'models')
#     tokenizer = AutoTokenizer.from_pretrained(model_path)
#     model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
#     input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')
#     output = model.generate(input_ids=input_ids,
#                             max_length=2)
#     dec = [tokenizer.decode(ids) for ids in output]
#     label = dec[0].replace('<pad> ','')
#     return label

# Create your views here.
@api_view(['POST'])
def get_mood(request):
    serializer = DailyLogSerializers(data=request.data)
    if serializer.is_valid():
        # print(serializer.data['log'])
        mood = get_emotion(serializer.data['log'])
        return Response({"mood": mood}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "invalid input"}, status=status.HTTP_400_BAD_REQUEST)
