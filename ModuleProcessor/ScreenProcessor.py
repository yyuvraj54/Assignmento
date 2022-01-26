from tkinter import *
import csv
def clearScreen(exp_num_variable,Question,Code,Output):
    
    exp_num_variable.set('')
    Question.delete(1.0, END)
    Code.delete(1.0, END)
    Output.delete(1.0, END)

def DataLoader(filename,PageNumber,exp_num_variable,Question,Code,Output,NameOfStudent,RollNumber):
    f=open(f"{filename}.csv",'r')
    reader = csv.reader(f)

    for row in reader:
        if len(row)==0:continue
        else:
            if row[0]==PageNumber:
                exp_num_variable.set(row[1])
                Question.insert(END,row[2])
                Code.insert(END,row[3])
                Output.insert(END,row[4])

                break
    f.close()
    

