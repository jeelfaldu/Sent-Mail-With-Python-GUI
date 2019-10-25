from tkinter import *
from mailsend import MailSent as mail
from database import * 
import re
from tkinter import messagebox

def send():
    try:
        mail(uemail.get() , password.get() ,sentto.get().split(",") ,msg.get("1.0",'end-1c'))
        messagebox.showinfo("Sucessful sent", "Mail sent..")
    except:
        messagebox.showerror("Error", "Somthing went wrong")

def show():
    listdata = []
    conn = sqlite3.connect('data.db')
    fqurey = "select Email from maildata"
    c = conn.execute(fqurey)
    for row in c:
      listdata.append(row[0])
    conn.close()
    for i in range(len(listdata)):
        email.insert(END,str(listdata[i])+"\n")
    listdata.clear()

def save():
    lst = re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email.get("1.0",'end-1c'))
    print(lst)
    for i in range(len(lst)):
        insert(lst[i])
        print(lst[i])
    lst.clear()
    email.insert(END,"\n")

def select():
    lst = re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email.get("1.0",'end-1c'))
    sentto.delete(0, 'end')
    for i in range(len(lst)):
        sentto.insert(END,str(lst[i])+',')
    lst.clear()
    

main=Tk()
main.title('Mail menegment project')
main.geometry("800x260")
main.maxsize(800,260)
main.minsize(800,260) 

fram = Frame(main)
fram.grid(row=0)

Label(fram,text="Email").grid(pady=10,row=0)
Label(fram,text="Password").grid(row=1)
Label(fram,text="To").grid(pady=10,row=2)
Label(fram,text="Massage").grid(pady=10,row=3)

uemail = Entry(fram)
password = Entry(fram)
sentto=Entry(fram)
msg=Text(fram,height="5", width="40")

uemail.grid(row=0,column=1 , ipadx="100")
password.grid(row=1,column=1,ipadx="100")
sentto.grid(row = 2 , column=1,ipadx="100")
msg.grid(row = 3 , column=1 )
      
btn = Button(fram,text= "send" ,command=send ,padx = 30).grid(pady=30,row=5,column=1)

m = Frame(main)
m.grid(row=0 , column=1)
fram = Frame(m)
fram.pack(padx = 15,fill = Y)
Label(fram,text="Enter Email").grid(row=1)
email = Text(fram,height= 10, width="40")
email.grid(row=1,column = 1,pady=10 ,padx=5)

frambtn = Frame(m)
frambtn.pack()
btnsave = Button(frambtn,text="Save Email Data",command=save,width = 15).grid(row=0,column = 1 , padx = 5)
btnshow = Button(frambtn,text="Show Email Data",command = show,width = 15).grid(row=0,column = 2, padx = 5)
btnselect = Button(frambtn,text="Select All Email And Mail",command = select,width = 19).grid(row=0,column = 3, padx = 5)

main.mainloop()



