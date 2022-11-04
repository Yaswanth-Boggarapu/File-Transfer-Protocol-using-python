from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os


root=Tk()
root.title("USE ME")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)


    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('file_type','.txt''.pdf''.mp4'),('all files','*.*')))
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connection...')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(6500000)
        conn.send(file_data)
        print("Data has been transmitted successfully...")

    image_icon1=PhotoImage(file="images/send.png")
    window.iconphoto(False,image_icon1)

    sbackground=PhotoImage(file="images/sender.png")
    Label(window,image=sbackground).place(x=-2,y=0)
 
    Mbackground=PhotoImage(file="images/id.png")
    Label(window,image=Mbackground,bg='#f3fdfe').place(x=100,y=260)
    
    #hostname
    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)
    


    Button(window,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg='#000',fg="#fff",command=sender).place(x=300,y=150)

    window.mainloop()
def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID=SenderId.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(6500000)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    image_icon1=PhotoImage(file="images/receive.png")
    main.iconphoto(False,image_icon1)

    Hbackground=PhotoImage(file='images/receiver.png')
    Label(main,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file='images/profile.png')
    Label(main,image=logo,bg="#f4fdfe").place(x=10 ,y=250)

    Label(main,text="Input Sender id",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SenderId = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderId.place(x=20,y=370)
    SenderId.focus()


    Label(main,text="filename for the incoming file:",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    incoming_file = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    incoming_file.place(x=20,y=450)

    imageicon=PhotoImage(file="images/arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)
    

    main.mainloop()

image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,image_icon)

Label(root,text="FIle Transfer",font=('Acumin variable concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="images/send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)


receive_image=PhotoImage(file="images/receive.png")
send=Button(root,image=receive_image,bg="#f4fdfe",bd=0,command=Receive)
send.place(x=300,y=100)

Label(root,text="Send",font=('Acumin variable concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receiver",font=('Acumin variable concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="images/background.png")
Label(root,image=background).place(x=-2,y=323)

root.mainloop()
