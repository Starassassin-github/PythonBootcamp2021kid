# GUITranslator.py
from tkinter import *
#จากไลบรารีชื่อ tkinter, * คือให้ดึงความสามารถทั้งหมด
from tkinter import ttk # tkk is theme of tk
### ----- Google Translate-----
from googletrans import Translator
translator = Translator() #สร้างฟังก์ชันแปลภาษา
    

GUI = Tk() #สร้่างหน้าต่างหลัก
GUI.geometry('500x300') #กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by ฟุ้กฟัก')

# -----config-----
FONT = ('Angsana New',15)

# -------Label-------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font = FONT)
L.pack()

# ----Entry (ช่องกรอกข้อความ)-----
v_vocab = StringVar() # กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font = FONT, width = 40)
E1.pack(pady=10)

# ----Button (ปุ่มแปล)-----
def Translate():
    vocab = v_vocab.get() # .get สั่งให้แสดงผลออกมา
    meaning = translator.translate(vocab, dest='th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text) # สั่งโชว์ใน GUI
    

B1 = ttk.Button(GUI,text='Translate', command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20, ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง

# -------Label-------
L = ttk.Label(GUI,text='คำแปล',font = FONT)
L.pack()

# -----result-----
v_result = StringVar() #นี่คือกล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New', 20)
r1 = ttk.Label(GUI,textvariable = v_result, font = FONT2, foreground='green')
r1.pack()


GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด (บรรทัดสุดท้าย)

