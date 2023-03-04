#ASHWIN SURESH 


from tkinter import *
import mysql.connector as m
import tkinter.messagebox as mb

a=Tk()
a.geometry('950x550')
a.title("                                                                                                                               IndusInd Bank")
a.iconphoto(True,PhotoImage(file="D:\Class XII\CS\Python Works\Logo.png"))

imag=PhotoImage(file="D:\Class XII\CS\Python Works\Bg.png")
b=Label(a,image=imag,width=950,height=550).pack()

def insert():
    accname=na.get()
    accno=nu.get()
    dob=da.get()
    ifsccode=co.get()
    balance=it.get()
    pstcode=z.get()
    
    if (accname=='' or accno=='' or dob=='' or ifsccode=='' or balance=='' or pstcode==''):
        mb.showinfo('               CAUTION!!',"   All fields are to be filled   ")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",auth_plugin='mysql_native_password',database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("insert into acchold values('"+accname+"','"+accno+"','"+dob+"','"+ifsccode+"','"+balance+"','"+pstcode+"')")
        mydb.commit()
        mb.showinfo("","Values are inserted")
        mydb.close()

def delete():
    if (nu.get()==''):
        mb.showinfo("","All fields are to be filled")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",auth_plugin='mysql_native_password',database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("delete from acchold where accno='"+nu.get()+"'")
        mydb.commit()
        mb.showinfo("","Values are deleted")
        mydb.close()

def show():
    if (nu.get()==''):
        mb.showinfo("","All fields are to be filled")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",auth_plugin='mysql_native_password',database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("select distinct * from acchold where accno='"+nu.get()+"'")
        r=mycursor.fetchall()

        for i in r:
            na.insert(0,i[0])
            da.insert(0,i[2])
            co.insert(0,i[3])
            it.insert(0,i[4])
            z.insert(0,i[5])
        mb.showinfo('','Values are shown')
        mydb.close()

def update():
    if (nu.get()==''):
        mb.showinfo('',"Account Number is compulsory for update")
    else:
        mydb=m.connect(host="localhost",user="root",passwd="1234",auth_plugin='mysql_native_password',database="bank")
        mycursor=mydb.cursor()
        mycursor.execute("update acchold set accname='"+na.get()+"',dob='"+da.get()+"',ifsccode='"+co.get()+"',balance='"+it.get()+"',pstcode='"+z.get()+"' where accno='"+nu.get()+"'")
        mydb.commit()
        mb.showinfo('',"Values are updated")
        mydb.close()

def clear():
    na.delete(0,'end')
    nu.delete(0,'end')
    da.delete(0,'end')
    co.delete(0,'end')
    it.delete(0,'end')
    z.delete(0,'end')

def all():
    mydb=m.connect(host="localhost",user="root",passwd="1234",auth_plugin='mysql_native_password',database="bank")
    mycursor=mydb.cursor()
    mycursor.execute("select * from acchold")
    r=mycursor.fetchall()
    mb.showinfo('',print(r))

form=Label(a,text="Account Holders",width=40,font=("bold",15)).place(x=250,y=20)

accname=Label(a,text="Account Holder Name",width=15,font=("bold",10)).place(x=320,y=100)

accno=Label(a,text="Account Number",width=20,font=("Times 32",10)).place(x=320,y=140)

dob=Label(a,text="Date of Birth",width=20,font=("underline",10)).place(x=320,y=180)

ifsccode=Label(a,text="IFSC Code",width=20,font=("underline",10)).place(x=320,y=220)

balance=Label(a,text="Balance",width=20,font=("underline",10)).place(x=320,y=260)

pstcode=Label(a,text="Postal/Zip Code",width=20,font=("underline",10)).place(x=320,y=300)

na=Entry()
na.place(x=455,y=100)

nu=Entry()
nu.place(x=455,y=140)

da=Entry()
da.place(x=455,y=180)

co=Entry()
co.place(x=455,y=220)

it=Entry()
it.place(x=455,y=260)

z=Entry()
z.place(x=455,y=300)

insert=Button(a,text="Insert",width=20,bg="black",fg="white",command=insert).place(x=280,y=350)

delete=Button(a,text="Delete",width=20,bg="white",fg="red",command=delete).place(x=482,y=350)

up=Button(a,text="Update",width=20,bg="pink",fg="green",command=update).place(x=280,y=400)

dis=Button(a,text="Show Records",width=20,bg="red",fg="blue",command=show).place(x=482,y=400)

cl=Button(a,text="Clear",width=20,bg="blue",fg="white",command=clear).place(x=482,y=450)

alll=Button(a,text="All records",width=20,bg='yellow',fg='red',command=all).place(x=280,y=450)

a.mainloop()




