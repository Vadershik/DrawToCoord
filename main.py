from tkinter import *

class Paint(Frame):
	def __init__(self,turtle):
		Frame.__init__(self,turtle)
		self.turtle = turtle
		#кисть
		self.brush_size = 5
		self.color = "black"
		#счётчик рисования
		self.clock = 0
		#проверка новых объектов
		self.lastx = 0
		self.lasty = 0
		with open('script.py','w') as file:
			file.writelines('from turtle import *\npencolor("black")\nwindow=Screen()\nwindow.tracer(1)\nwidth(5)\ndef coord():\n    #coord\n')
			file.close()

		self.GUI()
	def GUI(self):
		self.turtle.title("Soft Paint")
		self.pack(expand=1,fill=BOTH)

		self.cvs = Canvas(self, bg="white",width=1280,height=500)
		self.cvs.grid(row=3,column=0,columnspan=7)
		self.cvs.bind('<Button-1>',self.clicked)
		self.cvs.bind('<B1-Motion>',self.draw)
		color_lab = Label(self,text="Цвет: ").grid(row=0,column=0)

		#выбор цвета
		black_btn = Button(self, text="Black", width=10,command=lambda: self.set_color('black')).grid(row=0, column=3)
 
		white_btn = Button(self, text="White", width=10,command=lambda: self.set_color('white')).grid(row=0, column=4)
		
		red_btn = Button(self, text="Red", width=10,command=lambda: self.set_color('red')).grid(row=0,column=1)
		blue_btn = Button(self, text="Blue", width=10,command=lambda: self.set_color('blue')).grid(row=0,column=2)

        # метка для кнопок изменения размера кисти
		size_lab = Label(self, text="Размер кисти: ").grid(row=1, column=0, padx=5)

		#размер кисти
		one_btn = Button(self, text="2", width=10,command=lambda: self.set_brush_size(2)).grid(row=1, column=1)
 
		two_btn = Button(self, text="5", width=10,command=lambda: self.set_brush_size(5)).grid(row=1, column=2)
 
		five_btn = Button(self, text="8", width=10,command=lambda: self.set_brush_size(8)).grid(row=1, column=3)
 
		seven_btn = Button(self, text="10", width=10,command=lambda: self.set_brush_size(10)).grid(row=1, column=4)
 
		ten_btn = Button(self, text="15", width=10,command=lambda: self.set_brush_size(15)).grid(row=1, column=5)
 
		twenty_btn = Button(self, text="20", width=10,command=lambda: self.set_brush_size(20)).grid(row=1, column=6, sticky=W)
		
		#очистка
		clear_btn = Button(self, text="Clear all", width=10, command=self.clear)
		clear_btn.grid(row=0, column=6, sticky=W)
	
	#рисование
	def draw(self,event):
		if self.clock < 10:
			self.cvs.create_oval(event.x - self.brush_size,event.y - self.brush_size,event.x + self.brush_size,event.y + self.brush_size,fill=self.color,outline=self.color)
			self.clock += 1
		else:
			self.cvs.create_oval(event.x - self.brush_size,event.y - self.brush_size,event.x + self.brush_size,event.y + self.brush_size,fill=self.color,outline=self.color)

			print(f"    goto({event.x/2-200},-{event.y/2})")
			with open('script.py','a') as file:
				file.write(f'    goto({event.x/2-200},-{event.y/2})\n')
				file.close()
			self.clock = 0
	#выбор цвета
	def set_color(self,new_color):
		self.color = new_color
		print(f'changed color {new_color}')
		with open('script.py','a') as file:
			file.writelines(f'    up()\n    pencolor("{new_color}")\n    down()\n')

	#выбор размера кисти
	def set_brush_size(self,new_size):
		self.brush_size = new_size
		print(f'changed brush size {new_size}')
		with open('script.py','a') as file:
			file.writelines(f'    width({new_size})\n')

	def clear(self):
		self.cvs.delete("all")
		print('Clear')
		with open('script.py','w') as file:
			file.writelines('from turtle import *\npencolor("black")\nwindow=Screen()\nwindow.tracer(1)\nwidth(5)\ndef coord():\n    #coord\n')
			file.close()

	def clicked(self,event):
		print('up()')

		print(f'goto({event.x/2-200},-{event.y/2})')

		print('down()')
		with open('script.py','a') as file:
			file.writelines(f'    up()\n    goto({event.x/2-200},-{event.y/2})\n    down()\n')
			file.close()
#сборка
def Main():
	root = Tk()
	root.geometry("1280x600")
	root.resizable(False,False)
	app = Paint(root)
	root.mainloop()

Main()
with open('script.py','a') as file:
			file.writelines('\nspeed(2)\ncoord()\n\nexitonclick()')
