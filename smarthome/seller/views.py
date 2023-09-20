from django.shortcuts import render,HttpResponse
from customer.models import AudioModel
import json
import requests



def audio_list(request):
    datas = AudioModel.objects.all().order_by('-id')
    params = {'datas':datas}
    return render(request,'audio_list.html',params)

