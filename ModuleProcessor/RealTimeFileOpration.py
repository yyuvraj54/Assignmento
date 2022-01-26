import csv
from tempfile import NamedTemporaryFile
import shutil
from os import path
from pathlib import Path
import os, glob
 

def write_value(value):
    with open('ModuleProcessor//Visited_value.txt','w') as f:
        f.write(value)
        

def create_file_visited_file():
    with open('ModuleProcessor//Visited_value.txt','w+') as f:
        f.write('0')
        
        



def read_visited_value():
    with open('ModuleProcessor//Visited_value.txt','r') as f:
        r=f.readlines()
        r=r[0]
        if r in '1':
            return '1'
        else:return '0'

def Kill_Wast_Memory(dir):
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

def kill_Specfic_target(directory):
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

def readData(filename):
    with open(f'{filename}.csv') as f:
        fr = csv.reader(f)
        data=[]
        a=0
        for row in fr:
            if a==0:
                a=1
                continue
            else:
                data.append(row)
    return data


def File_exist(filename_with_extention):
    return Path(filename_with_extention).exists()

def createFile(filename):
    f=open(f"{filename}.csv",'w',newline='')
    header = ['Page', 'Assignment_number', 'Questions', 'Code' , 'Output' , 'futterL' , 'futterR']
    writer = csv.writer(f)
    writer.writerow(header)
    f.close() 

def add_data(filename,data):
    with open(f"{filename}.csv",'a',newline="") as f:

        writer = csv.writer(f)
        writer.writerow(data)
    

def modify_data_set(filename,page,dict_new_row_data):

    tempfile = NamedTemporaryFile(mode='w', delete=False)
    header = ['Page', 'Assignment_number', 'Questions', 'Code' , 'Output' , 'futterL' , 'futterR']
    

    with open(f"{filename}.csv", 'r') as csvfile, tempfile:
        r = csv.DictReader(csvfile, fieldnames=header)
        writer = csv.DictWriter(tempfile, fieldnames=header)
        for row in r:
            if row['Page']==page:
                row['Page'], row['Assignment_number'] , row['Questions'] , row['Code'] , row['Output'] , row['futterL'] , row['futterR'] = dict_new_row_data[0],dict_new_row_data[1],dict_new_row_data[2],dict_new_row_data[3],dict_new_row_data[4],dict_new_row_data[5],dict_new_row_data[6]
            row = {'Page': row['Page'], 'Assignment_number': row['Assignment_number'], 'Questions': row['Questions'], 'Code': row['Code'], 'Output':row['Output'],'futterL':row['futterL'],'futterR':row['futterR']}
            writer.writerow(row)
    shutil.move(tempfile.name, f"{filename}.csv")

    


if __name__=='__main__':
    pass
    #print(File_exist("page1.csv"))
    #data=[10,20,'qussssssestion',"Code is","Outpput",'Flutl33333',"flutr"]
    #add_data('page1',data)
    #modify_data_set('page1','5',data)