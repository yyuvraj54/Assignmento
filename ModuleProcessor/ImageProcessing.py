from PIL import Image, ImageDraw, ImageFont
from string import ascii_letters



def ImageRender(filename,text,font_name='SourceCodePro-Bold.ttf',font_size=18,color_tuple=(211,211,211),mode='portrait'):


    if mode=='landscape':font = ImageFont.truetype(font=f'{font_name}', size=15)
    else:font = ImageFont.truetype(font=f'{font_name}', size=font_size)

    if len(text)<30:
        font = ImageFont.truetype(font=f'{font_name}', size=28)
    


    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
    avg_char_height=sum(font.getsize(char)[1] for char in ascii_letters) / len(ascii_letters)
    print(f"{font_name} : {avg_char_width} x {avg_char_height}")

    list_of_lists = text.splitlines()    
    max_char_in_Line = 0
    lines=len(list_of_lists)

    for le in list_of_lists:
        if max_char_in_Line<len(le):
            max_char_in_Line=len(le)

    if mode=='portrait':
        image_width=int(max_char_in_Line*avg_char_width*1.2)
        image_height=int(lines*avg_char_height*1.4)
    elif mode=='landscape':
        image_width=int(max_char_in_Line*avg_char_width*1.3)
        image_height=int(lines*avg_char_height*1.3)
        if image_height>image_width:
            image_width=image_height+30

    elif mode=='same':
        image_width=int(max_char_in_Line*avg_char_width*1.2)
        image_height=int(lines*avg_char_height*1.2)
        if image_height>image_width:
            image_width=image_height
        else:
            image_height=image_width

        




    print(f"{font_name} : {image_width} x {image_height}")
    
    

    if image_width>3500 or image_height>3500:print("Code is too big")
    else:

        img = Image.new('RGB', (image_width, image_height), color_tuple)
        draw = ImageDraw.Draw(im=img)
        if len(text)<30:
            draw.text(xy=(1, 1), text=text, font=font, fill='black')
        else:    
            draw.text(xy=(img.size[0]/img.size[0] +15, img.size[1]/ img.size[1] +5), text=text, font=font, fill='black')
        try:
            img.save(filename)
        except:pass
    




if __name__=='__main__':
    
    
    
    text = """
from asyncore import write
import csv
from tempfile import NamedTemporaryFile
import shutil
from os import path
from pathlib import Path

    
def File_exist(filename_with_extention):
    return Path(filename_with_extention).exists()

def createFile(filename):
    f=open(f"{filename}.csv",'w',newline='')
from asyncore import write
import csv
from tempfile import NamedTemporaryFile
import shutil
from os import path
    f=open(f"{filename}.csv",'w',newline='')
from asyncore import write
import csv
from tempfile import NamedTemporaryFile
import shutil

from os import path
from pathlib import Path
f createFile(filename):
    f=open(f"{filename}.csv",'w',newline='')


from pathlib import Path
f createFile(filename):


    f=open(f"{filename}.csv",'w',newline='')
from asyncore import write
import csv
from tempfile import NamedTemporaryFile
import shutil
from os import path
from pathlib import Path
f createFile(filename):
    f=open(f"{filename}.csv",'w',newline='')


"""
    text="""Enter your length:10
ans of number is:1432"""
    
    font_name='Times New Roman Bold.ttf'
    color_tup=(169,169,169)
    ImageRender('sample.jpg',text=text,color_tuple=color_tup)
