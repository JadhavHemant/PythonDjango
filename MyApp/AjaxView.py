from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from MyApp.StudentDatabaseOperations import Operations
def StudentView(request):
    return render(request,"studentjson.html")

def studentlist(request):
    op=Operations("localhost","root","@vedika","class")
    data=op.Execute("FetchAll",0,"",0,0,0)
    return JsonResponse(data,safe=False)


def StudentbyRnoView(request):
    rno=request.GET["rno"]
    
    op=Operations("localhost","root","@vedika","class")
    data=op.Execute("FetchById",rno,"",0,0,0)
    return JsonResponse(data,safe=False)

def DeleteStudentView(request):
    rno=request.GET["rno"]
    
    op=Operations("localhost","root","@vedika","class")
    data=op.Execute("Delete",rno,"",0,0,0)
    return JsonResponse(data,safe=False)


def AddStudentView(request):
    if(request.method=="POST"):
        print("Inside Post Method")
        name=request.POST["name"]
        # print(data)
        e=int(request.POST["english"])
        m=int(request.POST["maths"])
        s=int(request.POST["science"])
        op=Operations("localhost","root","@vedika","class")
        data=op.Execute("Insert",0,name,e,m,s)
  
    return HttpResponse(data)

def UpdateStudentView(request):
    if(request.method=="POST"):
        print("Inside Post Method")
        id=int(request.POST["rno"])
        name=request.POST["name"]
        # print(data)
        e=int(request.POST["english"])
        m=int(request.POST["maths"])
        s=int(request.POST["science"])
        op=Operations("localhost","root","@vedika","class")
        data=op.Execute("Update",id,name,e,m,s)
  
    return HttpResponse(data)