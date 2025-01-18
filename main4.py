import os
from datetime import datetime
import fpdf
from fpdf import FPDF
from tkinter import ttk
from tkinter import *

outText=''
client=''
pic=[]

picd = os.listdir('pic')
for i in picd:
    pic.append(str(i.replace('.jpeg','')))

def d_now():
    dt_in=(str(datetime.now()))
    dt=dt_in[8:10]+'.'+dt_in[5:7]+'.'+dt_in[:4]+' '+dt_in[11:16]
    return dt

def pdf_out():
    global  dt,client, offer_number, pic

    pdf = FPDF()
    pdf.add_font('Segoe UIB', '', 'segoeuib.ttf', uni=True)
    pdf.add_font('Segoe UI', '', 'segoeui.ttf', uni=True)
    pdf.add_page()

    image_path ='logo.png'#логотип
    pdf.image(image_path, x=10, y=7, w=40)
    pdf.set_font("Arial", size=12)
    pdf.ln(0)  # ниже


    pdf.line(5, 5, 5, 292)
    pdf.line(5, 292, 205, 292)
    pdf.line(5, 5, 205, 5)
    pdf.line(205, 5, 205, 292)
    pdf.line(5, 19, 205, 19)
    

    pdf.set_font("Segoe UIB", size=20)
    pdf.cell(190, 0, txt="PIEDĀVĀJUMS", ln=1, align="C")
    pdf.set_font("Segoe UI", size=8)
    client=entry.get()
    pdf.cell(220, 15, txt="RIEPAS1 Matīsa 78 Rīga T-System Services SIA "+"     Piedāvājuma numurs "+offer_number+"     Klients: "+client+'    '+dt, ln=1, align="C")
    
    pdf.set_font("Segoe UIB", size=10)
   
    spacing=1
    row_height = 15 #pdf.font_size
    
    pic_y=18
    for row in data:
        pdf.cell(35, row_height*spacing, txt=row[0], border=0)
        img=''
        for i in pic:
            if i in (row[1]).upper():
                img='pic//'+i+'.jpeg'
                pic_y += 30
                pdf.image(img, x=25, y=pic_y, w=25)
                break
        #if img=='':
            #pic_y += 30
            #pdf.image('pic//none.jpeg', x=25, y=pic_y, w=20)
            
        
        if len(row[1])<50:
            pdf.cell(120, row_height*spacing, txt=row[1], border=0,align="C")
            pdf.cell(20, row_height*spacing, txt=row[2]+' €', border=0)
            pdf.cell(30, row_height*spacing, txt=row[3], border=0)
            pdf.ln(row_height*spacing)
            pdf.ln(row_height*spacing)
        else:
            pn=(row[1])[49:]
            pn1=(row[1])[:49]
            pdf.cell(120, row_height*spacing, txt=pn1, border=0,align="C")
            pdf.cell(20, row_height*spacing, txt=row[2]+' €', border=0)
            pdf.ln(row_height*spacing)
            pdf.cell(35, row_height*spacing, txt=' ', border=0)
            pdf.cell(120, row_height*spacing, txt=pn, border=0,align="C")
            pdf.ln(row_height*spacing)
        

    pdf.output("Offer"+offer_number+".pdf")
    window.destroy()
    return


with open('settings.txt','r', encoding='UTF-8') as f:
        o_num = (str(f.readline())).replace('\n','')
offer_number=str((int(o_num))+1)
with open('settings.txt','w', encoding='UTF-8') as f:
            f.write(offer_number)

def plus():
    global data
    outText = ''
    data1=[str(entry1.get()),str(entry1a.get()),str(entry1b.get()),str(entry1c.get())]
    if str(entry1a.get())=='':
        return
    data.append(data1)
    entry1.delete(0,END)
    entry1a.delete(0,END)
    entry1b.delete(0,END)
    entry1c.delete(0,END)
    for i in data:
        outText += '\n'
        for j in i:
            outText = outText + j + '    '
    label['text']= outText
    return

dt=d_now()

data = [['Artikuls', 'Apraksts', 'Cena', 'Piezīmes'],
            ]
           


window = Tk()
window.title("Offerist")
window.geometry("1000x600")
window.configure(background="grey")

f0 = Frame(window)
f_0 = Frame(window)
f_1 = Frame(window)
f_2 = Frame(window)
f0.pack()
f_0.pack()
f_1.pack()
f_2.pack()

label = Label(f_0, text = outText, width=130, height=30)
label.pack()

entry = Entry(f0, width=40)
entry.pack(side=LEFT, pady=10)
entry1 = Entry(f_1, width=10)
entry1.focus()
entry1.pack(side=LEFT, pady=10)
entry1a = Entry(f_1, width=80)
entry1a.pack(side=LEFT, pady=10)
entry1b = Entry(f_1, width=10)
entry1b.pack(side=LEFT, pady=10)
entry1c = Entry(f_1, width=50)
entry1c.pack(side=LEFT, pady=10)




button1 = Button(f_2,width=15, text="PDF", command=pdf_out)
button1.pack(side=RIGHT, expand=1)

button2 = Button(f_2,width=15, text="+", command=plus)
button2.pack(side=RIGHT, expand=1)

#close_button = Button(f_2, width=15, text="Close", command=lambda: window.destroy())
#close_button.pack(side=LEFT, expand=1)

window.mainloop()

