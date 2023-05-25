from django.shortcuts import render
from travelapplication.models import Place


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, 'index.html', {'result': obj})