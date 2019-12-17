import json
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from insta_django.models import Photo


def index(request):
    return HttpResponse("HI!🤟")

@csrf_exempt
def photos(request):
    if request.method == 'POST':
        photo = Photo(filename=request.POST['filename'], file=request.FILES['image'].file.read())
        photo.save()
        return HttpResponse("OK 👾")
    else:
        data = Photo.objects.all()
        serialized = serializers.serialize('python', data, fields=['filename', 'file'])
        photos = [d['fields'] for d in serialized]
        return HttpResponse(json.dumps(photos), content_type="application/json")

