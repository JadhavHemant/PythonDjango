from django.shortcuts import render
from MyApp.models import Student
from MyApp.Ormforms import Studentform


def StudentView(request):
    if(request.method=="GET"):
        sform=Studentform()
        data=Student.objects.all()
        return render(request,"studentOrm.html",{"studentform":sform,"students":data})
    elif(request.method=="POST"):
        
        sform=Studentform(request.POST)
        if(sform.is_valid):
            sform.save()
        data=Student.objects.all()
        sform=Studentform()
        return render(request,"studentOrm.html",{"studentform":sform,"students":data})
