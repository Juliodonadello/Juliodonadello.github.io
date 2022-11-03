from django.shortcuts import render
from .models import Project
#en django cualquier carpeta que se llame templates va a poder ser accesidad por el metodo render

def home(request):
    projects = Project.objects.all()
    return render(request,'home.html',{'projects':projects})
