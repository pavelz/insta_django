from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from insta_django.models import Photo


def index(request):
    return HttpResponse("HI!🤟")

@csrf_exempt
def photos(request):
    if request.method == 'POST':
        return HttpResponse("OK 👾")
    else:
        data = Photo.objects.all()
        return HttpResponse(serializers.serialize('json', data), content_type="application/json")


