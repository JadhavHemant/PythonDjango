from django.shortcuts import render
import mysql.connector
def PageData(request):
    con=mysql.connector.connect(host="localhost",user="root",password="@vedika",database="class")
    mycursor=con.cursor()
    if(request.method=="GET"):
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        return render(request,"register.html")

    elif(request.method=="POST"): 
        name=request.POST["first"]
        las=request.POST["last"]
        contact=request.POST["contact"]
        add=request.POST["address"]
        intst='INSERT INTO student(first_name,last_name,contact_number,address) VALUES(%s,%s,%s,%s)'
        
        val=(name,las,contact,add,)
        mycursor.execute(intst,val)
        con.commit()
        mycursor.execute("select * from user")
        data=mycursor.fetchall()
        return render(request,"register.html",{"user":data,"msg":"done"})

