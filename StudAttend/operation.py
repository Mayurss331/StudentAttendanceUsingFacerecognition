import re
from tkinter import *
import requests
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import main




root=Tk()
root.config(bg='#06abcc')
root.title("Student Attendence & Report Using Face-Recoginition/-By Asur")
root.geometry("1000x600")
Label(root,text='Student Attendence & Report Using Face-Recoginition',fg='white',bg='Red',font=('Times New Roman',30)).place(x=80,y=15)
Label(root,text='By Asur',fg='white',bg='#06abcc',font=('Times New Roman',10)).place(x=900,y=60)

def logout():

    global root
    root=Tk()
    root.config(bg='#06abcc')
    root.geometry("1000x600")
    logP()
    root.mainloop()


def logP():
    global pane3
    try:
        pane3.destroy()
    except:
        pass

    wid, hei = 750, 440
    global pane

    pane = Frame(root, width=wid, height=hei, bg='#fcb130')
    pane.pack(pady=80)

    im1 = ImageTk.PhotoImage(Image.open('Image\\pane1.jpg'))
    pane1 = Label(pane, height=hei, image=im1)
    pane1.image = im1
    pane1.grid(row=0, column=0)

    pane2 = LabelFrame(pane, width=420, height=hei, bg='#fcb130')
    pane2.grid(row=0, column=1)

    bg = ImageTk.PhotoImage(Image.open('Image\\bgpage.jpg'))
    pane3 = Label(pane2, width=(wid // 2) - 100, height=hei - 150, bg='#fcb130', image=bg)
    pane3.image = bg
    pane3.pack(padx=50,pady=72)


    def logCheck(en=0):
        eml=enn.get().lower()
        psw=enp.get()
        main.rec.execute(f"select * from user_data where Email='{eml}'")
        res=main.rec.fetchall()
        for x in res:
            if psw!=x[7]:
                res.remove(x)
        if len(res)!=0:
            root.destroy()
            fr=Tk()
            fr.geometry('600x500')
            def sub():
                main.url='http://'+en.get()+":8080/shot.jpg"
                try:
                    requests.get(main.url)
                    fr.destroy()
                except:
                    err.config(text='Invalid Ip')

            Label(fr,text="Enter the Ip:",font=("Times New Roman",18)).place(x=50,y=20)
            en=Entry(fr,font=("Times New Roman",16))
            en.place(x=250,y=20)
            err=Label(fr,text="",font=("Times New Roman",18),fg='Red')
            err.place(x=200,y=70)
            btn=Button(fr,text='Submit',width=20,command=sub,font=("Times New Roman",14))
            btn.place(x=200,y=110)
            img=ImageTk.PhotoImage(Image.open('Image\\intro.jpg').resize((600,350)))
            lb=Label(fr,image=img)
            lb.image=img
            lb.place(x=0,y=150)


            fr.mainloop()
            tableN = TableName(res[0][0],res[0][1],res[0][8],res[0][6])
            main.set(res[0][1], res[0][8], res[0][6],tableN)
            main.go()


        else:
            erl.config(text='Invalid Credential')

    def forgot():
        global pane3
        pane3.destroy()
        def checkAv(en=0):
            eml=enn.get().lower()
            psw=enp.get()
            main.rec.execute(f"select * from user_data where Email='{eml}' and DoB='{psw}'")
            res=main.rec.fetchall()
            if len(res)!=0:
                global fgId
                fgId=res[0][0]
                setPass()
            else:
                err.config(text="User Not Found")
        bg = ImageTk.PhotoImage(Image.open('Image\\bgpage.jpg'))
        pane3 = Label(pane2, width=(wid // 2) - 100, height=hei - 150, bg='#fcb130',image=bg)
        pane3.image=bg
        pane3.pack(padx=50, pady=72)

        Label(pane3, text="Forgot Password", font=('Times New Roman', 16), bg='white', anchor='center', width=21).place(x=10, y=10)
        lbn = Label(pane3, text="Email id :", font=('Times New Roman', 16), bg='white')
        lbn.place(x=10, y=85)
        enn = Entry(pane3, font=('Times New Roman', 11))
        enn.place(x=100, y=90)

        lbp = Label(pane3, text="D.O.B :", font=('Times New Roman', 16), bg='white')
        lbp.place(x=10, y=135)
        enp = DateEntry(pane3, font=('Times New Roman', 11),date_pattern='dd-mm-yyyy')
        enn.bind('<Return>', checkAv)
        enp.place(x=100, y=140)

        err = Label(pane3, fg='red', font=('Times New Roman', 11), width=20,bg='white')
        err.place(x=80, y=170)

        Button(pane3, text='Set Password', font=('Times New Roman', 11), bg='#033027', fg='white', width=20,
               command=checkAv).place(x=55, y=200)
        Button(pane3,text='Sign In',font=('Times New Roman',11),bg='white',width=15,command=login).place(x=5,y=240)


    def setPass():
        global pane3,fgId
        pane3.destroy()
        def setit():
            Psw=psw.get()
            Rpsw=rpsw.get()
            mat=None
            if Psw==Rpsw:
                mat=re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$^&+=_-])(?=\\S+$).{8,20}$",Psw)
            if mat!=None:
                main.rec.execute(f"update user_data set Password='{Psw}' where ID={fgId}")
                main.recdb.commit()
                login()
            else:
                err.config(text="Password Not Matching")
        bg = ImageTk.PhotoImage(Image.open('Image\\bgpage.jpg'))
        pane3 = Label(pane2, width=(wid // 2) - 100, height=hei - 150, bg='#fcb130', image=bg)
        pane3.image = bg
        pane3.pack(padx=50, pady=72)

        Label(pane3, text="Set Password", font=('Times New Roman', 16), bg='white', anchor='center', width=21).place(x=10, y=10)

        lbn = Label(pane3, text="Enter Password :", font=('Times New Roman', 10), bg='white')
        lbn.place(x=10, y=90)
        psw = Entry(pane3, font=('Times New Roman', 10))
        psw.place(x=130, y=90)

        lbp = Label(pane3, text="Re-Enter Password :", font=('Times New Roman', 10), bg='white')
        lbp.place(x=10, y=140)
        rpsw = Entry(pane3, font=('Times New Roman', 10))
        rpsw.place(x=130, y=140)

        err = Label(pane3, fg='red', font=('Times New Roman', 11), width=20, bg='white')
        err.place(x=80, y=170)

        Button(pane3, text='Set Password', font=('Times New Roman', 11), bg='#033027', fg='white',command=setit, width=20).place(x=55, y=200)

    lbn=Label(pane3,text="Login Page",font=('Times New Roman',16),bg='white',anchor='center',width=21)
    lbn.place(x=10,y=10)

    lbn=Label(pane3,text="Email :",font=('Times New Roman',14),bg='white')
    lbn.place(x=10,y=90)
    enn=Entry(pane3,font=('Times New Roman',11))
    enn.place(x=100,y=90)

    lbp=Label(pane3,text="Password :",font=('Times New Roman',14),bg='white')
    lbp.place(x=10,y=140)
    enp=Entry(pane3,font=('Times New Roman',11),show="*")
    enp.bind('<Return>',logCheck)
    enp.place(x=100,y=140)

    erl = Label(pane3, fg='red', font=('Times New Roman', 11), width=20, bg='white')
    erl.place(x=80, y=170)

    Button(pane3,text='Sign In',font=('Times New Roman',11),bg='#033027',fg='white',width=20,command=logCheck).place(x=55,y=200)

    Button(pane3,text='Forgot Password',font=('Times New Roman',11),bg='white',width=15,command=forgot).place(x=5,y=240)

    Button(pane3,text='Sign Up',font=('Times New Roman',11),width=15,bg='white',command=signUp).place(x=140,y=240)

def login():
    global pane
    try:
        pane.destroy()
    except:
        pass
    logP()


def signUp():
    global pane
    pane.destroy()
    main.rec.execute("select max(Id) from user_data")
    id=main.rec.fetchall()[0][0]+1
    print(id)

    def valid():
        Name=name.get()
        Dob=dob.get()
        Email=email.get().lower()
        Mobile=cont.get()
        Gender=gen.get()
        ClassN=clas.get()
        Subject=sube.get()
        Psw=psw.get()
        Cpsw=repass.get()
        dt=int(Dob[8:])<=10
        ema=re.match("[a-z A-Z 0-9+_.-]+[@]{1}[a-z A-Z]+[.]{1}[a-z A-Z]{1,3}",Email)
        mob=re.match("^([+]\d{2})?\d{10}$",Mobile)
        nc=len(Name)<2
        sc=len(Subject)!=0

        pswv=None
        if(Psw==Cpsw):
            pswv=re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$^&+=_-])(?=\\S+$).{8,20}$",Psw)
        if ema!=None and mob!=None and pswv!=None and not nc and sc and dt:
            val=(id,Name,Email,Mobile,Gender,Dob,Subject,Psw,ClassN)
            main.rec.execute("insert into user_data(ID,Name,Email,MobileNo,Gender,DoB,Subject,Password,ClassName) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",val)
            main.recdb.commit()
            err.config(text="User Created",fg='green')
            creTable(id,Name,ClassN,Subject)
            btnr.config(state='disabled')

        else:
            if pswv==None:
                err.config(text="Password Must Contain 8 Characters(1 UpperCase,1 LowerCase,1 Numeric,1 Special char)")
            elif ema==None:
                err.config(text="Invalid Email")
            elif mob==None:
                err.config(text="Invalid Mobile Number")
            elif nc:
                err.config(text="Enter Name")
            elif not sc:
                err.config(text="Enter the Subject")
            elif not dt:
                err.config(text="Select Correct DoF")

    wid, hei = 750, 440
    im2 = ImageTk.PhotoImage(Image.open('Image\\bgpane.jpg'))
    pane = Label(root, width=wid, height=hei, bg='#06abcc',image=im2)
    pane.image=im2
    pane.pack(pady=80)
    fnt=("Times New Roman", 12)

    Label(pane, text="New Registration", font=('Times New Roman', 22), anchor='center', width=38).place(x=80,y=20)

    lb1 = Label(pane,anchor='w', text="Enter Name :", width=10, font=fnt)
    lb1.place(x=60, y=100)
    name = Entry(pane,width=30)
    name.place(x=200, y=100)

    lbp = Label(pane, text="D.O.B :", font=fnt,anchor='w',width=10)
    lbp.place(x=400, y=100)
    dob = DateEntry(pane,date_pattern='dd-mm-yyyy')
    dob.set_date("20-10-2010")
    dob.place(x=540, y=100)

    lb3 = Label(pane,anchor='w', text="Enter Email :", width=10, font=fnt)
    lb3.place(x=60, y=140)
    email = Entry(pane,width=30)
    email.place(x=200, y=140)

    lb4 = Label(pane,anchor='w', text="Contact Number :", width=13, font=fnt)
    lb4.place(x=60, y=180)
    cont = Entry(pane,width=20,font=("Times New Roman",13))
    cont.place(x=200, y=180)

    lb5 = Label(pane,anchor='w', text="Select Gender :", width=15, font=fnt)
    lb5.place(x=60, y=220)
    gen = StringVar(pane,'Male')
    Radiobutton(pane, text="Male", padx=5, variable=gen, value='Male').place(x=190, y=220)
    Radiobutton(pane, text="others", padx=15, variable=gen, value='Others').place(x=320, y=220)
    Radiobutton(pane, text="Female", padx=10, variable=gen, value='Female').place(x=250, y=220)


    list_of_class = ("FyBSc", "SyBSc", "TyBSc")
    clas = StringVar()
    drplist = OptionMenu(pane, clas, *list_of_class)
    drplist.config(width=10)
    clas.set("TyBSc")
    lb2 = Label(pane,anchor='w', text="Select Class :", width=13, font=fnt)
    lb2.place(x=60, y=260)
    drplist.place(x=200, y=255)

    sub = Label(pane, anchor='w', text="Subject Name :", width=10, font=fnt)
    sub.place(x=400, y=140)
    sube = Entry(pane, width=20)
    sube.place(x=540, y=140)

    lb6 = Label(pane,anchor='w', text="Enter Password :", width=13, font=fnt)
    lb6.place(x=400, y=180)
    psw = Entry(pane, show='*',width=18,font=("Times New Roman",13))
    psw.place(x=540, y=180)

    lb7 = Label(pane,anchor='w', text="Re-Enter Password :", width=15, font=fnt)
    lb7.place(x=400, y=220)
    repass = Entry(pane,width=18,font=("Times New Roman",13))
    repass.place(x=540, y=220)

    err = Label(pane, anchor='center', text="", width=70, fg="red",font=fnt)
    err.place(x=70, y=300)
    btnr=Button(pane, text="Register", font=('Times New Roman', 11), width=20,height=2,command=valid)
    btnr.place(x=310, y=350)
    Button(pane, text='Sign In', font=('Times New Roman', 11),  width=15,height=2, command=login).place(x=25, y=350)


def TableName(Id,Name,Class,Subject):
    table=f'{Name[:3]}{Id}{Class[:3]}{Subject}'
    return table

def creTable(Id,Name,Class,Subject):
    table=f'{Name[:3]}{Id}{Class[:3]}{Subject}'
    print(table)
    # CREATE TABLE `attendence`.`asdf` ( `asddf` INT NOT NULL , `asdf` INT NOT NULL , `asdff` INT NOT NULL )
    rep='INT '
    qury="CREATE TABLE "+table+" (Date text"
    main.rec.execute(f'select * from {Class}_stud_info')
    res=main.rec.fetchall()
    li=[]
    for x in res:
        li.append(x[1])
    # print(li)
    for x in li:
        qury+=f", {x} {rep}"
    qury+=")"
    print(qury)
    main.rec.execute(qury)
logP()
root.mainloop()