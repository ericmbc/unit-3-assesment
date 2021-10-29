from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    print(widget_list)
    widget_form = WidgetForm()
    return render(request, 'index.html', { 'widget_list': widget_list, 'form': widget_form})

