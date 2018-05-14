# -*- coding: UTF-8 -*-

def init():
	pass
def getJSONText():
	with open('cliper.json', 'r') as f:
		dictData = json.load(f)
		# print(dictData)
		f.close()
	return dictData

# 获取剪切板内容
def getClipText(*args):
	w.OpenClipboard()
	var = w.GetClipboardData(win32con.CF_UNICODETEXT)
	w.CloseClipboard()
	text.delete('1.0','end')
	text.insert('end',var)

def setClipText():
	w.OpenClipboard()
	w.EmptyClipboard()
	contents = text2.get('1.0',END)
	w.SetClipboardData(win32con.CF_UNICODETEXT, contents)
	# print(contents)
	w.CloseClipboard()

def import_to_json():
	dictData = getJSONText()
	contents = text.get('1.0',END)
	name = e1.get()
	# print(contents)
	dictData[name] = contents
	# print(dictData)
	with open('cliper.json', 'w+') as f:
		json.dump(dictData, f)

def show_msg(*args):
	indexs = listbox.curselection()
	# print(indexs)
	if len(indexs) == 0:
		indexs = (0)
	stringText = listbox.get(indexs)
	text2.delete('1.0','end')
	JSONText = getJSONText()
	# print(JSONText[stringText])
	text2.insert('end',JSONText[stringText])

def refresh():
	listbox.delete(0,END)
	keys = getJSONText().keys() 
	for key in keys:
		listbox.insert('end', key)

from tkinter import *
from tkinter import ttk
import win32clipboard as w 
import win32con
import json
window = Tk()   
window.geometry('500x500')      
window.title("剪切板")
notebook = ttk.Notebook(window)  # notebook属于ttk
# notebook.bind("Button-1",getClipText)
frame1 = Frame(notebook)
label_name  = Label(frame1,text="输入名称") 
e1 = Entry(frame1)
label  = Label(frame1,text="输入内容")          	#  创建Label组件
text = Text(frame1,height=20)		#  创建Text组件
text.bind('<Button-1>',getClipText)
button = Button(frame1, 
    text='加入列表',      # 显示在按钮上的文字
    width=15, height=2,
    command=import_to_json)     # 点击按钮式执行的命令

label_name.pack()                    # 将小部件放置到主窗口中
e1.pack()
label.pack()
text.pack() 
button.pack() 
# label1 = Label(frame1, text="I love Beijing!!!\nI love China!!!")

frame2 = Frame(notebook)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)  
listbox = Listbox(frame2,yscrollcommand=scrollbar.set)
keys = getJSONText().keys() 
for key in keys:
	listbox.insert('end', key)
listbox.bind("<<ListboxSelect>>",show_msg)
listbox.focus_set()
text2 = Text(frame2,height=20)
button2 = Button(frame2, 
    text='加入剪切板',      		# 显示在按钮上的文字
    command=setClipText)    	# 点击按钮式执行的命令
button3 = Button(frame2, 
    text='刷新',      		# 显示在按钮上的文字
    command=refresh)    	# 点击按钮式执行的命令
listbox.pack(side=LEFT, fill=BOTH)
text2.pack()
button2.pack()
button3.pack()

notebook.add(frame1, text="导入到JSON")
notebook.add(frame2, text="从JSON导出")
notebook.pack(fill=X)

getClipText()

window.mainloop()                 # 进入消息循环 

