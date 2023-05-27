import time
from tkinter import *
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import face_recognition
import imutils
import mysql.connector
import numpy as np
import pandas as pd
from threading import Thread
import requests
import cv2
import os
import operation

url='http://192.168.178.123:8080/shot.jpg'


global newface,ClassN,Subject,Name,tableN,path
bface=[]
Subject="Face Detector"
Name='Asur'
ClassN =''
tableN=''
path=ClassN +"_data"

# url='http://198.168.'+input("Enter the IP:")+':8080/shot.jpg'

recdb=mysql.connector.connect(
  host="localhost",
  user="mayur",
  password="Mayurss#791",
  database="attendence"
)
print("Database Connected")
rec=recdb.cursor()
global li
global atdata


def set(nam,clas,sub,tablen):
    global ClassN, Subject, Name, tableN, path
    Name=nam
    ClassN=clas
    Subject=sub
    tableN=tablen
    path=ClassN+"_data"

def findEncode():
    global classNames
    classNames=[]
    global facedata
    facedata= os.listdir(path)
    for line in facedata:
        ids=line.split(sep=".")[0]
        rec.execute("select Name from "+ClassN +"_stud_info where RollNo="+ids)
        res=rec.fetchall()
        names=res[0][0]
        classNames.append(names)

    encodefaces=[]
    for name in facedata:
        filename=f'{ClassN }_data/{name}'
        encode=np.fromfile(filename)
        encodefaces.append(encode)
    return encodefaces


def recongnizer():

    encodeknownfaces = findEncode()
    print("Encoding done...")

    while True:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        # camera,img=cap.read()
        img = imutils.resize(img, width=860, height=1360)
        # imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Finding the  face location in camera image
        faces = face_recognition.face_locations(imgS)
        #Finding the encodings of that faces
        encode = face_recognition.face_encodings(imgS,faces)

        # for each face found and its encodes
        for encodeface,faceloc in zip(encode,faces):

            matches = face_recognition.compare_faces(encodeknownfaces,encodeface)
            # print(matches)


            facedis = face_recognition.face_distance(encodeknownfaces,encodeface)
            # print(facedis)
            y1, x2, y2, x1 = faceloc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,70, 255),2)
            matchid =np.argmin(facedis)
            # for i in range(1,len(facedis)):
            #     if(facedis[i]<0.5):
            #         matchid=i

            if matches[matchid] and facedis[matchid]<0.500000:
                name=classNames[matchid].upper()
                rec.execute(f"select {classNames[matchid]} from {tableN} where Date='{date}'")
                res=rec.fetchall()
                if res[0][0] == 0:
                    query=f"update {tableN} set {classNames[matchid]} = 1 where Date='{date}'"
                    # print(query)
                    rec.execute(query)
                    recdb.commit()
                    print('updated')
                #Add the name of the face
                cv2.rectangle(img,(x1,y2),(x2,y2+15),(0,70,255),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2+10),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255),1)



        cv2.imshow("Attendence Started", img)
        #Esc key close cam
        if cv2.waitKey(1) == 27:
            cv2.destroyWindow("Attendence Started")
            break




def show_frames():
    global cantadd
    regi=[]
    newface=[]
    cantadd=True
    def timer():
        global cantadd
        time.sleep(60)
        cantadd=False
        messagebox.showerror('Error',"Can't Add the Face")


    Thread(target=timer).start()
    def addit():
        stid=int(entID.get())
        stN=entN.get()
        stM=entM.get()
        val=(stid,stN,stM)
        # rec.execute("select ")
        if len(classNames)!=0:
            qu=f"Alter Table {tableN} add " + stN + " int after " + classNames[len(classNames) - 1]
        else:
            qu=f"Alter Table {tableN} add " + stN + " int after Date"
        print(qu)
        rec.execute(qu)
        recdb.commit()
        rec.execute("insert into "+ClassN +"_stud_info (RollNo,Name,MobileNo) values (%s,%s,%s)",val)
        recdb.commit()
        np.ndarray.tofile(result, ClassN +"_data/" +entID.get())
        name.destroy()
    while len(regi)<=5 and cantadd:
        img_res=requests.get(url)
        img_arr=np.array(bytearray(img_res.content),dtype=np.uint8)
        img=cv2.imdecode(img_arr,-1)
        img=imutils.resize(img,width=600)
        imgS=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        faces=face_recognition.face_locations(imgS)
        encode=face_recognition.face_encodings(imgS,faces)

        for encodeface,faceloc in zip(encode,faces):
            matches = face_recognition.compare_faces(encodeknownfaces,encodeface)

            y1, x2, y2, x1 = faceloc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 70, 255), 2)
            if len(encodeknownfaces)!=0:
                facedis = face_recognition.face_distance(encodeknownfaces, encodeface)
                matchid = np.argmin(facedis)
                if not (matches[matchid] and facedis[matchid] < 0.500000):
                    regi.append(encodeface);
                else:
                    cv2.putText(img, "Already Present", (x1 + 6, y2 + 10), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255), 1)
                    print("already Present")
            else:
                regi.append(encodeface);


        cv2.imshow("Adding Face...", img)
        # Esc key close cam
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    if len(regi)<5:
        return
    trail=regi[len(regi)-1]
    matches=face_recognition.compare_faces(regi.pop(),[trail])
    facedis=face_recognition.face_distance(regi.pop(),[trail])
    # print(facedis)
    for i in range(0,len(matches)):
        if matches[i] and facedis[i]<0.500000:
            newface.append(regi[i])
    result=newface[np.argmin(facedis)]
    global name,curframe
    name=Tk()
    curframe.append(name)
    name.geometry('300x200')
    name.title("Add The Student")
    Label(name,text="Enter the ID: ").grid(row=0,column=0)
    Label(name,text="Enter the Name: ").grid(row=1,column=0)
    Label(name,text="Enter the Mobile No.: ").grid(row=2,column=0)

    rec.execute('select max(RollNo) from '+ClassN +'_stud_info')
    res=rec.fetchall()
    if res[0][0]==None:
        Id=1
    else:
        Id=res[0][0]+1
    entID=Entry(name)
    entID.insert(END,Id)
    entID.config(state='disabled')
    entN=Entry(name)
    entM=Entry(name)
    entID.grid(row=0,column=1)
    entID.insert(END,"")
    entN.grid(row=1,column=1)
    entN.insert(END,"")
    entM.grid(row=2,column=1)
    entM.insert(END," ")
    btn=Button(name,text="Add Face.",command=addit,width=10,height=2)
    btn.place(x=100,y=100)
    name.mainloop()


def start():
    global ms,curframe
    ms=Tk()
    curframe.append(ms)

    ms.title("Select Date")
    def run():
        global date
        date=end.get()
        dd=date[0:2]
        mm=date[3:5]
        yy=date[6:]
        try:
            d,m,y=int(dd),int(mm),int(yy)
            date=dd + "-" + mm + '-' + yy
            qu=f'insert into {tableN} (Date,'
            v=" Values(%s,"
            val=[date]
            for i in range(len(classNames)):
                if i==len(classNames)-1:
                    qu+=classNames[i]+")"
                    v+="%s)"
                else:
                    qu+=classNames[i]+","
                    v+="%s,"
                val.append(0)
            qu+=v
            val = tuple(val)
            if len(classNames)==0:
                qu=f'insert into {tableN} (Date) Values(%s)'
                val=tuple(date)
            qur=f"select * from {tableN} where Date='{date}'"
            print(qur)
            rec.execute(qur)
            print('executed')
            res=rec.fetchall()
            print(res)
            if len(res)==0:
                print(qu, val)
                rec.execute(qu,val)
                recdb.commit()

            ms.destroy()
            recongnizer()

        except TypeError:
            Label(ms,text="invalid date").place(x=100,y=100)

        # print(dd,mm,yy)
        # rec.execute("Select * from {tableN} where Date='"+date+"'")
        # if len(rec.fetchall())==0:
        #     recongnizer()

    ms.geometry('500x300')
    Label(ms,width=10,height=3).grid(row=0,column=0)
    lbd=Label(ms,text="Enter Date(dd/mm/yyyy): ",height=2)
    lbd.grid(row=1,column=2)
    end=DateEntry(ms,date_pattern='dd-mm-yyyy')
    end.config(state='disabled')
    end.grid(row=1,column=3,padx=10)
    btnsub=Button(ms,text="Submit",width=10,height=2,command=run)
    btnsub.place(x=200,y=150)
    ms.mainloop()

def generate():
    global table,scroller,enfrom,ento,save,clear,Delete,atdata
    try:
        table.destroy()
        save.destroy()
        clear.destroy()
        Delete.destroy()
    except:
        pass
    save=Button(mid,text='Save as File(.xlsx)',command=datasave,font=('Times New Roman',15),bg='white',width=15,anchor='w',relief="solid", borderwidth=1)
    save.place(x=400,y=450)
    clear = Button(mid, text='Clear All Data',command=cleardata, font=('Times New Roman', 15), bg='white', width=15, anchor='w',relief="solid", borderwidth=1)
    clear.place(x=600, y=450)
    Delete = Button(mid, text='Delete Records',command=deletRec, font=('Times New Roman', 15), bg='white', width=15, anchor='w',relief="solid", borderwidth=1)
    Delete.place(x=800, y=450)
    df=enfrom.get()
    dt=ento.get()
    atdata=[["ID","Name"]]
    rec.execute("Select * from "+ClassN +"_stud_info")
    info=rec.fetchall()
    rec.execute(f"Select * from {tableN} Order By Date Desc")
    data=rec.fetchall()
    for i in range(0,len(info)):
        li = []
        id=info[i][0]
        li.append(id)
        li.append(info[i][1])
        for j in range(0,len(data)):
            date = data[j][0]
            if i==0:
                if date>=df and date<=dt:
                    # print(date)
                    atdata[0].append(date)
            flg = True if date>=df and date<=dt else False
            if flg:
                pre="Present" if data[j][id] == 1 else "Absent"
                li.append(pre)

        atdata.append(tuple(li))
    column=range(1,len(atdata[0])+1)

    atdata[0]=tuple(atdata[0])
    # print(column,atdata[0])
    # for i in range(len(atdata)):
    #     for j in range(len(atdata[0])):
    #         e = Entry(mid)
    #         e.grid(row=i, column=j, sticky=NSEW)
    #         e.insert(END, atdata[i][j])
    #         e.configure(state='disabled')

    if len(atdata[0])>10:
        table=ttk.Treeview(tab,columns=tuple(column),show='headings',height=15,xscrollcommand=scrollerx.set,yscrollcommand=scrollery.set)
        scrollerx.pack(fill=X,side=BOTTOM)
        table.pack(side=LEFT)
        scrollery.pack(fill=Y,side=RIGHT)
        wid=960//(len(atdata[0])-2)
        for i in range(0,len(atdata[0])):
            if i==0:
                table.column(i+1,width=10,minwidth=50,anchor='w')
            elif i==1:
                table.column(i+1,width=10,minwidth=150,anchor='w')
            else:
                table.column(i+1, width=wid,minwidth=100,anchor='center')
            table.heading(i+1,text=atdata[0][i])
        for x in range(1,len(atdata)):
            table.insert('','end',values=atdata[x])
        scrollerx.config(command=table.xview)
        scrollery.config(command=table.yview)
    else:
        table=ttk.Treeview(tab,columns=tuple(range(1,12)),show='headings',height=15,xscrollcommand=scrollerx.set,yscrollcommand=scrollery.set)
        table.pack(side=LEFT)
        for i in range(0,11):
            if i<len(atdata[0]):
                table.heading(i+1,text=atdata[0][i])
            else:
                table.heading(i+1,text="--")
            table.column(i + 1, width=100, anchor='center')
        for x in range(1,len(atdata)):
            li=list(atdata[x])
            for m in range(1,11):
                li.append("__")
            table.insert('','end',values=tuple(li))

def cleardata():
    global enfrom,ento
    en=DateEntry(mid,date_pattern="dd-mm-yyyy")
    today=int(en.get()[6:])
    enfrom.set_date(f'15-06-{today-1}')
    ento.set_date(en.get())
    generate()
    datasave(f'{today-1}-{today}')
    rec.execute(f'TRUNCATE {tableN}')

def deletRec():
    global delf,curframe
    delf=Tk()
    curframe.append(delf)
    delf.geometry('300x200')
    delf.title('Delete Record')
    def deltit():
        rec.execute(f"delete from {tableN} where Date='{den.get()}'")
        recdb.commit()
        den.config(state='normal')
        btn.config(text='Fetch Record',command=fetch)
        err.config(text='')
    def fetch():
        global resd
        rec.execute(f"select * from {tableN} where Date='{den.get()}'")
        resd=rec.fetchall()
        if len(resd)!=0:
            err.config(text='record Found',fg='green')
            den.config(state='disabled')
            btn.config(text='Delete record',command=deltit)
        else:
            err.config(text='Record Not Found',fg='Red')

    lb=Label(delf,text='Select the Date To Delete')
    lb.place(x=20,y=60)
    lb = Label(delf, text='Delete Record',font=('Times New Roman',16),width=20)
    lb.place(x=20, y=20)
    den=DateEntry(delf,date_pattern='dd-mm-yyyy')
    den.place(x=180,y=60)
    err = Label(delf, text='', font=('Times New Roman', 16), width=20)
    err.place(x=30, y=100)
    btn=Button(delf,text='Fetch Record',command=fetch)
    btn.place(x=100,y=150)

    delf.mainloop()
def datasave(fileN=None):
    global atdata,enfrom,ento
    if fileN!=None:
        fileName=fileN
    else:
        fileName=enfrom.get()[:5]+'to'+ento.get()
    data={}
    valtotal=[]
    # for loop in id,name,date
    for i in range(0,len(atdata[0])):
        key=atdata[0][i]
        val=[]
        toTotal=0
        for j in range(1,len(atdata)):
            s=atdata[j][i]
            if s=='Present':
                toTotal+=1
            val.append(s)
        if i==0:
            val.append("ToTal")
        elif i==1:
            val.append("")
        else:
            val.append(toTotal)
        data[key]=val

    for i in range(1,len(atdata)):
        valoverall = 0
        for j in range(2,len(atdata[i])):
            s=atdata[i][j]
            if s=='Present':
                valoverall+=1
        valtotal.append(valoverall)
    valtotal.append("")
    data['Total']=valtotal
    try:
        writer = pd.ExcelWriter(f'{Name}\\Data\\{fileName}.xlsx', engine='xlsxwriter')
    except:
        os.makedirs(f'{Name}\\Data')
        writer = pd.ExcelWriter(f'{Name}\\Data\\{fileName}.xlsx', engine='xlsxwriter')
    data = pd.DataFrame(data)
    data.to_excel(writer, sheet_name='sheet1', index=False)

    workbook = writer.book
    # Get Sheet1
    worksheet = writer.sheets['sheet1']
    chart = workbook.add_chart({'type': 'column'})
    rowC=len(data['ID'])+1
    columnC=convtoColumn(len(data.count())-1)

    # Configure the series of the chart from the dataframe data.
    chart.add_series({ 'categories':f'=sheet1!$C$1:${columnC}$1',
                        'values': f'=sheet1!$C${rowC}:${columnC}${rowC}'})

    # Insert the chart into the worksheet
    worksheet.insert_chart('D2', chart)

    writer.close()

def convtoColumn(num,count=1):
    if num==0:
        return "1"
    if num<=(26^count):
        return chr(num+64)
    else:
        return convtoColumn(num//(26^count),count+1)+chr((num%26)+64)


def logo():
    global root
    root.destroy()
    operation.logout()
def go():
    global mid,tab,root,scrollerx,scrollery,enfrom,ento,encodeknownfaces,curframe
    curframe=[]
    encodeknownfaces = findEncode()
    root = Tk()
    root.geometry("1000x600")
    root.title("Student Attendence & Report Using Face-Recoginition/-By Asur")
    root.config(bg='red')


    head = LabelFrame(root, width=1000, height=100,bg='#06abcc')
    head.place(x=0, y=0)

    mid = Frame(root, width=1000, height=500,bg='#fc8403')
    mid.place(x=0, y=100)

    fnt=('Times New Roman',16)

    Label(mid,text="User Name : ",font=fnt,bg='white',width=13,anchor='w',relief="solid", borderwidth=1).place(x=50,y=10)
    uNl=Label(mid,text=Name,width=20,font=fnt,fg="white",bg='#bd7306',relief='sunken', borderwidth=1)
    uNl.place(x=220,y=10)

    Label(mid, text="Subject Name : ", font=fnt,bg='white',width=13,anchor='w',relief="solid", borderwidth=1).place(x=50, y=60)
    uNl = Label(mid, text=Subject, width=20, font=fnt, fg="white", bg='#bd7306',relief='sunken', borderwidth=1)
    uNl.place(x=220, y=60)

    Label(mid, text="Class Name : ", font=fnt,bg='white',width=13,anchor='w',relief="solid", borderwidth=1).place(x=530, y=10)
    uCl = Label(mid,text=ClassN,width=20 ,font=fnt, fg="white",bg='#bd7306',relief='sunken', borderwidth=1)
    uCl.place(x=710, y=10)

    Label(mid, text="From : ", font=fnt, bg='white', width=7, anchor='center', relief="solid", borderwidth=1).place(x=530, y=60)
    Label(mid, text="to : ", font=fnt, bg='white', width=3, anchor='center', relief="solid", borderwidth=1).place(x=750, y=60)
    enfrom=DateEntry(mid,date_pattern='dd-mm-yyy')
    enfrom.place(x=630,y=60)
    ento=DateEntry(mid,date_pattern='dd-mm-yyy')
    ento.place(x=800,y=60)



    tab = Frame(mid, width=1000, height=500, bg='#fc8403')
    tab.place(x=0, y=100)

    logout = Button(mid, text='Log Out', command=logo,font=('Times New Roman', 15), bg='white', width=10, anchor='w', relief="solid",borderwidth=1)
    logout.place(x=50, y=450)

    scrollerx=Scrollbar(tab,orient='horizontal')
    scrollery=Scrollbar(tab,orient='vertical')
    btnadd = Button(head, text="Add New Student", width=40, height=2, command=show_frames)
    btnadd.grid(row=1, column=0, padx=22,pady=20)

    btngo = Button(head, text="Start Todays Attendence", width=40, height=2, command=start)
    btngo.grid(row=1, column=1, padx=22,pady=20)

    btnrec = Button(head, text="Genrate Report", width=40, height=2, command=generate)
    btnrec.grid(row=1, column=2, padx=22,pady=20)



    root.mainloop()


# print(convtoColumn(72))
# go()