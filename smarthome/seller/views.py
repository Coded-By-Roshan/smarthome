from django.shortcuts import render
from customer.models import AudioModel

def audio_list(request):
    datas = AudioModel.objects.all().order_by('-id')
    params = {'datas':datas}
    return render(request,'audio_list.html',params)
