from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    print(widget_list)
    widget_form = WidgetForm()
    return render(request, 'index.html', { 'widget_list': widget_list, 'form': widget_form})

def add_widget(request):
    widget = Widget.objects.create(
        description = request.POST['description'],
        quantity = request.POST['quantity'],
    )
    return redirect('/')

def delete_widget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('/') 