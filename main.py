from tkinter import *
from tkinter import messagebox
import threading
import os
from ModuleProcessor import RealTimeFileOpration
from ModuleProcessor import sysInfo

oss=sysInfo.getSystemOS()

def showtutorial():
    try:
        from PIL import Image
        im = Image.open(r"accet//Guide.png")
        im.show()
    except:print("Image Open Error")

def Install_modules():
    print(oss)
    
    if oss=='MacOs':
        try:
            os.system('python3 -m pip install python-docx')
            os.system('python3 -m pip install Pillow')
        except:
            messagebox.showinfo("software Requirment",'Internet Connection required: As the sofware under development so you need to install python modules manually that are listed in readme.txt file')
            
    elif oss=='Windows':
        try:
           os.system('python -m pip install Pillow')
           os.system('python -m pip install python-docx')
        except ModuleNotFoundError:messagebox.showinfo("software Requirment",'Internet Connection required: As the sofware under development so you need to install python modules manually that are listed in readme.txt file')
    
    else :
        try:
            os.system('python3 -m pip install python-docx')
            os.system('python3 -m pip install Pillow')
        except:
            messagebox.showinfo("software Requirment",'As the sofware is not fully supported in linux/ubantu OS so you need to install python modules manually that are listed in readme.txt file')
            

if RealTimeFileOpration.File_exist('ModuleProcessor//Visited_value.txt'):
    if RealTimeFileOpration.read_visited_value()=='1':
        pass
    else:
    
        Install_modules()
        showtutorial()
        RealTimeFileOpration.write_value('1')
    
else:
    RealTimeFileOpration.create_file_visited_file()
    Install_modules()
    showtutorial()
    RealTimeFileOpration.write_value('1')

from ModuleProcessor import ImageProcessing
from ModuleProcessor import DocFileProcessment
from ModuleProcessor import ScreenProcessor

pageCounter=0
def getAllMetaData():
    data=[]
    try:
        data=[getPageSelectedValue(),Assignment_Num.get(),Question_entry.get(1.0, "end-1c"),MainCode.get(1.0, "end-1c"),Mainoutput.get(1.0, "end-1c"),NameOfStudent.get(),RollNumber.get()]

    except:print("DataSet grap error")
    return data 
    
def clrSrc():
     ScreenProcessor.clearScreen(Assignment_Num,Question_entry,MainCode,Mainoutput)
    
    
def getPageSelectedValue():
    data=Page_Selected_Label['text']
    
    if data==None or data=='':
        Page_Selected_Label['text']="selected Page No: 1"
    
    new_data = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in data)
    numbers = [i for i in new_data.split()]
    
    return numbers[-1]



def changeDataSet():
    data=getAllMetaData()
    RealTimeFileOpration.modify_data_set(filename.get(),getPageSelectedValue(),data)
    

def loadScreenWithNewData():
    ScreenProcessor.DataLoader(filename.get(),getPageSelectedValue(),Assignment_Num,Question_entry,MainCode,Mainoutput,NameOfStuden_var,RollNumber)


def FinalStageSave():
    changeDataSet()
    sure=messagebox.askquestion("Convert to Document", "Are you sure?\nyou want to create word doc of given data?")
    
    if sure=='yes':
        try:
            path= os.path.expanduser("~/Desktop")
        except:
            path=''
        DocFileProcessment.CreateDoc(f'{path}//{filename.get()}')
        AllRow_data=RealTimeFileOpration.readData(filename=filename.get())
        Image_path=[]

        AllRow_data_copy=[]
        for y in AllRow_data:
            if len(y)==0:continue
            else:AllRow_data_copy.append(y)
                
        for each in range(pageCounter):
            for image in range(2):
                if image==0:
                    FileNameForImageSave=f'ModuleProcessor//LogFiles//log_{AllRow_data_copy[each][0]}_Code.jpg'
                    Image_path.append(f'log_{AllRow_data_copy[each][0]}_Code.jpg')
                    text=AllRow_data_copy[each][3]
                else:
                    FileNameForImageSave=f'ModuleProcessor//LogFiles//log_{AllRow_data_copy[each][0]}_Out.jpg'
                    Image_path.append(f'log_{AllRow_data_copy[each][0]}_Out.jpg')
                    text=AllRow_data_copy[each][4]
                
                ImageProcessing.ImageRender(FileNameForImageSave, text)

            Heading=AllRow_data_copy[each][1]
            ques=AllRow_data_copy[each][2]
            fullterl=AllRow_data_copy[each][5]
            futterr=AllRow_data_copy[each][6]    
            DocFileProcessment.NewDocumentPage(f'{path}//{filename.get()}',Heading,ques ,Image_path[0],Image_path[1],fullterl,futterr)
            Image_path.clear()

    else:pass

    


#default_Window_Size
Window_Height=270
Window_Width=600

framecolor='#66669A'
back_first='#BCCBEE'
idle='#282C34'
white='white'
footer_color='#292C34'

Main_window=Tk()
Main_window.minsize(Window_Width,Window_Height)
Main_window.title("Assignmento")
Main_window.config(bg=back_first)

logoimg =Image("photo", file="accet//logo.png")
try:
    Main_window.tk.call('wm','iconphoto', Main_window._w, logoimg)
except:pass

Bodyframe=Frame(Main_window,bg=back_first)
Bodyframe.pack()
try:
    logolabel=Label(Bodyframe,image=logoimg)
    logolabel.pack(pady=10)
except:pass


LabelWelcome=Label(Bodyframe,text="Welcome To Assignmento",bg="#0e7be0").pack(pady=10)


entryFrame=Frame(Bodyframe,bg=back_first)
entryFrame.pack()
Labelfile_name=Label(entryFrame,text="Enter your file name:",bg='grey')
Labelfile_name.grid(row=0,column=0,padx=5)




filename=StringVar()
filename.set("Untitled")
EntryFileName=Entry(entryFrame,textvariable=filename,bg=back_first)
EntryFileName.grid(row=0,column=1)


Labelfile_name_Extention=Label(entryFrame,text="(.docs)",bg=back_first)
Labelfile_name_Extention.grid(row=0,column=3)





def CurSelet(evt):
    global selected_value_of_page
        
    try:
        changeDataSet()
        selected_value_of_page=str((ListofPage.get(ListofPage.curselection())))
        Page_Selected_Label.config(text=f"selected: {selected_value_of_page}",bg='red')
        

        clrSrc()
        loadScreenWithNewData()
    except :
        print("lisbox index error")



    



 

def setting_up_files(filename):
    
    if RealTimeFileOpration.File_exist(f"{filename}.csv"):
        return True
    else:
        return False

    






def pageDown():
    global pageCounter
    pageCounter +=1
    ListofPage.insert(END,f"Page No: {pageCounter}")
    ListofPage.select_set(pageCounter-1)
    Page_Selected_Label.config(text=f'selected: Page No: {pageCounter}')
    


def ToMainEditScreen():

    myfile=filename.get()

    if setting_up_files(myfile):
        ErrorLabel.config(text=f"Try another name , file exist with same\n{filename.get()}",bg='red')
        try:
            RealTimeFileOpration.kill_Specfic_target(f'{os.getcwd()}')
        except ModuleNotFoundError:
            print("Error")
    else:
        try:
            RealTimeFileOpration.Kill_Wast_Memory('ModuleProcessor//LogFiles')
        except:print('Error')
        pageDown()
        RealTimeFileOpration.createFile(myfile)
        data=[getPageSelectedValue(),'','','','','','']
        RealTimeFileOpration.add_data(myfile,data)

        global height,width
        Window_Height=700
        Window_Width=900
        Bodyframe.destroy()
        Main_window.minsize(Window_Width,Window_Height)
        BackgroundFrame.pack(expand=True,fill=BOTH)
        
        ListofPage.select_set(0)
        Create_New_Button.destroy()



Create_New_Button=Button(Bodyframe,text="Create New Document",fg='red',command=ToMainEditScreen,bg=back_first)
Create_New_Button.pack(pady=10)
ErrorLabel=Label(Bodyframe,text="No need to provide extention",bg='grey')
ErrorLabel.pack(side=BOTTOM,pady=20)


BackgroundFrame=Frame(Main_window,bg=framecolor)

#>>>>>>>LEFT LAB
LeftPageManagerFrame=Frame(BackgroundFrame,bg='#555555')
LeftPageManagerFrame.pack(side=LEFT,anchor=NW,fill=Y,padx=5,pady=5)


listboxElement=StringVar()
Label(LeftPageManagerFrame,text="Page Management",bg='#555555',fg='skyblue').pack(pady=10)
ListofPage=Listbox(LeftPageManagerFrame,height=26,listvariable=listboxElement,bg='#424242',borderwidth=5,selectbackground='#3498FD',fg=white,relief=FLAT,bd=0)
ListofPage.pack(padx=5,pady=5)
ListofPage.bind('<<ListboxSelect>>',CurSelet)

def newPageRequest():
    try:
        changeDataSet()
        pageDown()
        clrSrc()
        data=[pageCounter,'','','','','','']
        RealTimeFileOpration.add_data(filename.get(),data)

        
    except (ModuleNotFoundError):pass


buttonsframe=Frame(LeftPageManagerFrame,bg='#555555')
buttonsframe.pack(padx=2,pady=3)

guidBut=Button(LeftPageManagerFrame,text="Guide",bg="green",command=showtutorial)
guidBut.pack(pady=3,side=BOTTOM)

New_Page_Button=Button(buttonsframe,text="New Page",bg="green",command=newPageRequest)
New_Page_Button.pack(pady=3)



#Update_rec=Button(LeftPageManagerFrame,text="Update",bg="green",command=changeDataSet)
#Update_rec.pack(side=BOTTOM,pady=5)

def startFinalEvaluation():
    threading.Thread(target=FinalStageSave).start()


def aboudPage():
    about=Toplevel()
    about.minsize(500,500)
    about.maxsize(500,500)
   
    about.title("About Assignmento")
    try:
        about.tk.call('wm','iconphoto', about._w, logoimg)
    except:pass

    logolabel=Label(about,image=logoimg)
    logolabel.pack(pady=10)

    aboutlabel=Label(about,text='Assignmento').pack()
    

    aboutlabel=Label(about,text='Assignmento is a software that is used to store programming question\nand answer in a readable mannered of docx files.',fg='red').pack(pady=5)

    global trademarklogo
    trademarklogo=PhotoImage(file="accet//mainlogo.png")

    aboutlabel=Label(about,image=trademarklogo)
    aboutlabel.pack(pady=4)

    aboutlabel=Label(about,text='Design and Developed by Yuvraj Singh Yadav')
    aboutlabel.pack()
    





about=Button(LeftPageManagerFrame,text="About Assignmento",bg="green",command=aboudPage)
about.pack(side=BOTTOM,pady=5)

Save_rec=Button(LeftPageManagerFrame,text="Convert to Doc",bg="green",command=startFinalEvaluation)
Save_rec.pack(side=BOTTOM,pady=3)




TopMetaDataFrame=Frame(BackgroundFrame,bg=framecolor)
TopMetaDataFrame.pack(anchor=NW,padx=10)
filenameLabel=Label(TopMetaDataFrame,text=f"Filename: {filename.get()}.docs",fg='white' ,bg=framecolor)
filenameLabel.pack(pady=2)

Page_Selected_Label=Label(buttonsframe,text="selected: Page No: 1",bg='red')
Page_Selected_Label.pack(pady=5)




titleDataFrame=Frame(BackgroundFrame,bg=framecolor)
titleDataFrame.pack(anchor=NW,fill=X)

AssignmentFrmae=Frame(titleDataFrame,bg=framecolor)
AssignmentFrmae.pack(anchor=NW,fill=X)

QuestionFrame=Frame(titleDataFrame,bg=framecolor)
QuestionFrame.pack(anchor=NW,fill=X)


Assignment_Number=Label(AssignmentFrmae,text="Assignment Number:",bg=framecolor,fg=white)
Assignment_Number.grid(row=0,column=0,padx=5)
Assignment_Num=StringVar() #--------------------------------------------------------->Assignment Number
Assignment_Number_entry=Entry(AssignmentFrmae,textvariable=Assignment_Num,relief=FLAT,bg=footer_color,insertbackground=white,highlightbackground=footer_color,fg=white)
Assignment_Number_entry.grid(row=0,column=1)




Question=StringVar() #--------------------------------------------------------------->Question 
QuestionLabel=Label(QuestionFrame,text="Question:",fg=white,bg=framecolor)
QuestionLabel.pack()

Question_entry=Text(QuestionFrame,height=6,wrap=WORD,fg=white,bg=idle,padx=5,pady=5,highlightbackground=idle,insertbackground=white,font="TimesNewRoman",relief=FLAT)
Question_entry.pack(fill=X,padx=10)





CodeFrame=Frame(BackgroundFrame,bg=framecolor)
CodeFrame.pack(anchor=NW,fill=X)

Label(CodeFrame,text="Code:",fg=white,bg=framecolor).pack()
MainCode=Text(CodeFrame,height=15,wrap=WORD,bg=idle,fg=white,padx=5,pady=5,highlightbackground=idle,insertbackground=white,font="TimesNewRoman",relief=FLAT)
MainCode.pack(fill=X,padx=10)



OutputFrame=Frame(BackgroundFrame,bg=framecolor)
OutputFrame.pack(anchor=NW,fill=X)

Label(OutputFrame,text="Output:",fg=white,bg=framecolor).pack()
Mainoutput=Text(OutputFrame,height=7,bg=idle,wrap=WORD,fg=white,padx=5,pady=5,highlightbackground=idle,insertbackground=white,font="TimesNewRoman",relief=FLAT)
Mainoutput.pack(fill=X,padx=10)





FutterFrame=Frame(BackgroundFrame,bg=framecolor)
FutterFrame.pack(anchor=NW,fill=X)

Label(FutterFrame,text="footer Info",fg=white,bg='#E88778').pack(pady=5)

NameOfStuden_var=StringVar()
NameOfStudent=Entry(FutterFrame,textvariable=NameOfStuden_var,bg=footer_color,fg=white,highlightbackground=footer_color,insertbackground=white,relief=FLAT)
NameOfStudent.pack(side=LEFT,padx=10)
RollNumber=StringVar()
StudentRollNumber=Entry(FutterFrame,textvariable=RollNumber,bg=footer_color,fg=white,highlightbackground=footer_color,insertbackground=white,relief=FLAT)
StudentRollNumber.pack(side=RIGHT,padx=10)

Main_window.mainloop()

