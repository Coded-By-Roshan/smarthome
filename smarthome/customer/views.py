from django.shortcuts import render,redirect
import speech_recognition as sr
from .models import AudioModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pyttsx3
from playsound import playsound
from django.core import serializers
from django.views import View
s = sr.Recognizer()


@csrf_exempt
def record_audio(request):
    if request.method == 'POST':
        audio_data = json.loads(request.body)
        audio_text = audio_data['audio_data']
        engine = pyttsx3.init()
        file_count = 1
        file_path = f"media/audios/audio{1}.mp3"
        engine.save_to_file(audio_text, 'speech.mp3')
        engine.runAndWait()
        file_count += 1
        audio_model = AudioModel(audio_text = audio_text)
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
        return JsonResponse({'message':'Wrong validation'})


# def submitted(request):
#     params = {}
#     return redirect("home")