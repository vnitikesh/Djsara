from django.shortcuts import render
import qrcode
import qrcode.image.svg
from django.urls import reverse
from io import BytesIO
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
# from .models import UserActivity

# Create your views here.

def landing(request):
    return render(request, 'saraap/landing.html')

def index(request):
    return render(request, 'saraapp/index.html')

def room(request, room_name):
    factory = qrcode.image.svg.SvgImage
    current_site = SimpleLazyObject(lambda: get_current_site(request))
    
    print(current_site)
    url = "http://" + str(current_site) + "/chat/" + room_name
    img = qrcode.make(url, image_factory = factory, box_size = 20)
    stream = BytesIO()
    img.save(stream)
    context = {
        'room_name': room_name,
        'svg': stream.getvalue().decode()
    }
    
    return render(request, 'saraapp/room.html', context = context)


