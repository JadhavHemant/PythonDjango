import mysql.connector
class Operations:
    host=""
    user=""
    database=""
    password=""
    def __init__(self,h,u,p,d) -> None:
        self.host=h
        self.user=u
        self.password=p
        self.database=d
    def Execute(self,type,r,n,e,m,s):
        con=mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        mycursor=con.cursor()
        if(type=="FetchAll"):
        
            mycursor.execute("select * from tblstudents")
            data=mycursor.fetchall()
            stdata=[]
            for d in data:
                    st={"rno":d[0],"name":d[1],"english":d[2],"maths":d[3],"science":d[4]}
                    stdata.append(st)
            return stdata
        
        elif(type=="FetchById"):
        
            mycursor.execute("select * from tblstudents where rno="+str(r))
            data=mycursor.fetchall()
            stdata=[]
            for d in data:
                    st={"rno":d[0],"name":d[1],"english":d[2],"maths":d[3],"science":d[4]}
                    stdata.append(st)
            return stdata[0]
        elif(type=="Insert"):
            mycursor.execute("insert into tblstudents(name,english,maths,science)values('"+n+"',"+str(e)+","+str(m)+","+str(s)+")")
            con.commit()
            return  "Student Added Successfully"
        elif(type=="Update"):
            mycursor.execute("update tblstudents set name='"+n+"', english="+str(e)+", maths="+str(m)+", science="+str(s)+" where rno="+str(r))
            con.commit()
            return  "Student Updated Successfully"

        elif(type=="Delete"):
            mycursor.execute("delete from tblstudents  where rno="+str(r))
            con.commit()
            return  "Student Deleted Successfully"
        
        
        