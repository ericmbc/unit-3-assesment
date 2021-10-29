from django.shortcuts import render
from .models import Widget

# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    print(widget_list)
    return render(request, 'index.html', {"widget_list": widget_list})

