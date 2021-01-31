from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('700x500')
GUI.title("Calculate Vat 7%")

# FONT ทั้งหมด
FONT1 = ("4805KwangMD_Influenza", 20)

######ช่องกรอกข้อมูล (ราคาสินค้า) #########
L = ttk.Label(GUI, text='Enter Your Product',font=FONT1).pack() #ข้อความแสดง

v_product = StringVar() # ตัวแปรสำหรับเก็บชื่อสินค้า
E1 = ttk.Entry(GUI,textvariable=v_product, font=FONT1)
E1.pack()

######ช่องกรอกข้อมูล (ราคาสินค้า) #########
L = ttk.Label(GUI, text='Price Of Product',font=FONT1).pack() #ข้อความแสดง

v_price = StringVar() # ตัวแปรสำหรับเก็บราคา
E2 = ttk.Entry(GUI,textvariable=v_price, font=FONT1)
E2.pack()

######ช่องกรอกข้อมูล (ราคาสินค้า) #########
L = ttk.Label(GUI, text='Volume',font=FONT1).pack() #ข้อความแสดง

v_quantity = StringVar() # ตัวแปรสำหระบเก็บจำนวน
E3 = ttk.Entry(GUI,textvariable=v_quantity, font=FONT1)
E3.pack()

########## ปุ่มกดเพื่อคำนวณ #######
def calc(event=None):
	product = v_product.get()
	price = int(v_price.get())
	quantity = int(v_quantity.get())
	total = price * quantity
	vat7 = total * (7 / 107)
	nettotal = total * (100 / 107)
	print('ราคาก่อน Vat: {:,.2f} (vat 7%: {:,.2f})'.format(nettotal,vat7))
	v_result.set('Product : {} |  Amount : {:,.0f}   \nYour Purchase : {:,.0f} Bath ({:,.0f} / piece) \n***(Net Price : {:,.2f} .- | Vat 7% : {:,.2f} .-)'.format(product,
																								quantity,
																								total,
																								price,
																								nettotal,
																								vat7))

B1 = ttk.Button(GUI,text='Calculate',command=calc)
B1.pack(ipadx=25,ipady=10,pady=12)

E3.bind('<Return>',calc)
###### ผลลัพธ์จากการคำนวณ #####
v_result = StringVar()
v_result.set('Show Detail') # โชว์ข้อมูลเริ่มต้น

R1 = ttk.Label(GUI, textvariable=v_result, font=FONT1, foreground='green')
R1.pack()

GUI.mainloop()
