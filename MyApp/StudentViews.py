from django.shortcuts import render
from MyApp.StudentDatabaseOperations import Operations
def StudentView(request):
    op= Operations("localhost","root","@vedika","class")
    if(request.method=="GET"):
        
        data=op.Execute("FetchAll",0,"",0,0,0)
        return render(request,"StudentForm.html",{"students":data,"message":"Welcome to Student Operations"})
    elif(request.method=="POST"):
        n=request.POST["txtname"]
        e=int(request.POST["txtenglish"])
        m=int(request.POST["txtmaths"])
        s=int(request.POST["txtscience"])
        msg=op.Execute("Insert",0,n,e,m,s)
        data=op.Execute("FetchAll",0,"",0,0,0)
        return render(request,"StudentForm.html",{"students":data,"message":msg})
    

    