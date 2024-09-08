from django.shortcuts import render
from .models import Image
from .forms import ImageForm

# Create your views here.


def Home(request):
    if request.method == 'POST':
        fm = ImageForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = ImageForm()
    img = Image.objects.all()
    return render(request, 'index.html',{'form':fm,'img':img})