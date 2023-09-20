from django.shortcuts import render,redirect
import speech_recognition as sr
from .models import AudioModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pyttsx3
from django.contrib.auth.decorators import login_required
from playsound import playsound
from django.core import serializers
from django.views import View

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
username = ''
room_no = ''



def login_page(request):
    return render(request,'login.html')
    



@csrf_exempt
def record_audio(request):
  
    if request.method == 'POST':
        audio_data = json.loads(request.body)
        print(audio_data)
        audio_text = audio_data['audio_text']
        username = audio_data['username']
        room_no = audio_data['room_no']
        print(audio_text)
        print(username)
        print(room_no)
        audio_model = AudioModel(audio_text = audio_text,username=username,roomno=room_no)
        audio_model.save()
        if ('help' in (audio_text.lower())):
            return JsonResponse("Help on a way", safe=False)
            a1 = AudioDataView()
            a1.get(request)
        else:
            return JsonResponse("Voice Recognized", safe=False) 
    print("BAD REQUEST")
    return JsonResponse('Invalid request method.', status=400)

def home(request):
    return render(request,'home.html')
    


class AudioDataView(View):
    def get(self, request,*args,**kwargs):
        if request.is_ajax():
            audios = AudioModel.objects.all().order_by('-id')
            audio_serializer = serializers.serialize('json',audios)
            return JsonResponse(audio_serializer, safe=False)
        return JsonResponse({'message':'Wrong validation'},safe=False)


# def submitted(request):
#     params = {}
#     return redirect("home")