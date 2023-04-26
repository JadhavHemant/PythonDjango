from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def FirstView(request):
    return HttpResponse("<h2>Welcome to DJango Application</h2>")

def PageView(request):
    # m=request.method
    # print(m)
    if(request.method=="GET"):
        return render(request,"index.html",{"result":"Welcome"})
    elif(request.method=="POST"):
        n1=int(request.POST["txtnum1"])
        n2=int(request.POST["txtnum2"])
        c=n1+n2
     
        return render(request,"index.html",{"result":"Addition="+str(c)})



    