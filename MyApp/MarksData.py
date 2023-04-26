from django.shortcuts import render
import mysql.connector
def Data(request):
    con=mysql.connector.connect(host="localhost",user="root",password="@vedika",database="class")
    mycursor=con.cursor()
    if(request.method=="GET"):
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        return render(request,"student.html")

    elif(request.method=="POST"): 
        name=request.POST["stud"]
        las=request.POST["roll"]
        contact=request.POST["java"]
        add=request.POST["pyt"]
        re=request.POST["react"]
        
        intst='INSERT INTO student(name,rollnumb,java,python,react) VALUES(%s,%s,%s,%s,%s)'
        
        val=(name,las,contact,add,re)
        mycursor.execute(intst,val)
        con.commit()
        mycursor.execute("select name,rollnumb,(java+python+react)*100/150 from student;")
        data=mycursor.fetchall()
        return render(request,"student.html",{"student":data,"msg":"done"})

