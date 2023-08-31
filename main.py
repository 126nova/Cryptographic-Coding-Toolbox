#=============================================导入库===============================================

import tkinter as tk
from tkinter import ttk
import ctypes
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
import pyperclip
import webbrowser
import os
import random
import traceback

import hashlib
import base64
import pybase100 as pb

#=============================================多语言===============================================
#读取当前语言
language_name = str(open(os.path.dirname(os.path.abspath(__file__))+'\\'+'languages\\language.txt', 'r').read())
#读取语言
try:
    with open(os.path.dirname(os.path.abspath(__file__))+'\\languages\\'+language_name+'.txt', 'r', encoding='utf-8') as the_language_file:
        language = result = [line.strip() for line in the_language_file]
except:
    tkinter.messagebox.showerror('ERROR!',str(traceback.format_exc()))  
#分割语言为列表
languages = [os.path.splitext(file_name)[0] for file_name in os.listdir(os.path.dirname(os.path.abspath(__file__))+'\\'+'languages') if file_name != 'language.txt']

#=============================================添加窗口==============================================

window = tk.Tk()
window.title(language[0])
window.geometry('1280x720')
window.resizable(0,0)
window.iconphoto(True, tk.PhotoImage(file='icon.png'))

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
window.tk.call('tk', 'scaling', ScaleFactor/75)

#=============================================建变量===============================================

encode = 'base16'
AutoCopy = True
ReverseMode = False
RanbowMode = False
entry_box = ''
export_text_all = ''

base100_tips = False

#=============================================函数定义==============================================

#01为加密,02为解密

#以下是可解并且可用的

def base16_01(text):
    aaaaa = base64.b16encode(text.encode('utf-8'))
    aaaaa= aaaaa.decode('utf-8')
    return str(aaaaa)

def base32_01(text):
    aaaaa = base64.b32encode(text.encode('utf-8'))
    aaaaa= aaaaa.decode('utf-8')
    return str(aaaaa)

def base64_01(text):
    aaaaa = base64.b64encode(text.encode('utf-8'))
    aaaaa= aaaaa.decode('utf-8')
    return str(aaaaa)

def base85_01(text):
    aaaaa = base64.b85encode(text.encode('utf-8'))
    aaaaa= aaaaa.decode('utf-8')
    return str(aaaaa)

def base16_02(text):
    aaaaaa = base64.b16decode(str(text))
    aaaaaa = aaaaaa.decode('utf-8')
    return str(aaaaaa)

def base32_02(text):
    aaaaaa = base64.b32decode(str(text))
    aaaaaa = aaaaaa.decode('utf-8')
    return str(aaaaaa)

def base64_02(text):
    aaaaaa = base64.b64decode(str(text))
    aaaaaa = aaaaaa.decode('utf-8')
    return str(aaaaaa)

def base85_02(text):
    aaaaaa = base64.b85decode(str(text))
    aaaaaa = aaaaaa.decode('utf-8')
    return str(aaaaaa)

def base100_01(text):
    return str(pb.encode(text))

def base100_02(text):
    return str(pb.decode(text))

def binary_01(text):
    return ' '.join(format(ord(c), 'b') for c in text)

def binary_02(text):
    return ''.join([chr(i) for i in [int(b, 2) for b in text.split(' ')]])

def OCT_01(text):
    return ' '.join([oct(ord(char))[2:].zfill(3) for char in text])

def OCT_02(text):
    return  ''.join([chr(int(octal_digit, 8)) for octal_digit in text.split()])

def hexadecimal_01(text):
    return ' '.join([text.encode().hex()[i:i+2] for i in range(0, len(text.encode().hex()), 2)])

def hexadecimal_02(text):
    aaaa = bytes.fromhex(text)
    bbbb = aaaa.decode()
    return bbbb

def Caesar_01(text,offset):
    return ''.join([chr((ord(char) - 97 + offset) % 26 + 97) for char in text])

def Caesar_02(text,offset):
    return ''.join([chr((ord(char) - 97 - offset) % 26 + 97) for char in text])

def SHA1_01(text):
    return hashlib.sha1(str(text).encode('utf-8')).hexdigest()  

def SHA224_01(text):
    return hashlib.sha224(str(text).encode('utf-8')).hexdigest()

def SHA256_01(text):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

def SHA384_01(text):
    return hashlib.sha384(str(text).encode('utf-8')).hexdigest()    

def SHA512_01(text):
    return hashlib.sha512(str(text).encode('utf-8')).hexdigest()

def MD5_01(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()

#以下是功能
def RanbowModePro(text):
    return  ''.join(random.sample(text, len(text)))

def Encrypt():
    try:

        global export_text_all

        if encode_option_box.get() == 'base16':
            export_text = base16_01(entry_box.get())
        elif encode_option_box.get() == 'base32':
            export_text = base32_01(entry_box.get())
        elif encode_option_box.get() == 'base64':
            export_text =base64_01(entry_box.get())
        elif encode_option_box.get() == 'base85':
            export_text = base85_01(entry_box.get())
        elif encode_option_box.get() ==  language[1]:
            export_text = binary_01(entry_box.get())
        elif encode_option_box.get() == language[21]:
            export_text = OCT_01(entry_box.get())
        elif encode_option_box.get() == language[17]:
            export_text = hexadecimal_01(entry_box.get())
        elif encode_option_box.get() == language[22]:
            export_text = Caesar_01(entry_box.get(),int(OffsetEntry.get()))
        elif encode_option_box.get() == language[25]:
            export_text = SHA1_01(entry_box.get())
        elif encode_option_box.get() == language[26]:
            export_text = SHA224_01(entry_box.get())
        elif encode_option_box.get() == language[27]:
            export_text = SHA256_01(entry_box.get())
        elif encode_option_box.get() == language[28]:
            export_text = SHA384_01(entry_box.get())
        elif encode_option_box.get() == language[29]:
            export_text = SHA512_01(entry_box.get())
        elif encode_option_box.get() == language[30]:
            export_text = MD5_01(entry_box.get())
        elif encode_option_box.get() == 'base100':
            export_text = base100_01(entry_box.get())

        if RanbowMode:
            export_text = RanbowModePro(export_text)

        if ReverseMode:
            export_text = export_text[::-1]

        export_text_all = export_text

        export_text_tips_box.place(x=995,y=265)
        export_text_box.place(x=900,y=350)
        export_text_copy_box.place(x=1025,y=625)


        if len(export_text) >= 174:
            export_text_.set(export_text[0:174] + '...')
        else:
            export_text_.set(export_text)

        if AutoCopy:
            pyperclip.copy(export_text)
            tips.set(language[2])
        else:
            tips.set(language[3])

    except:
        tips.set(language[4])

def Decrypt():
    try:
        global export_text_all

        if encode_option_box.get() == 'base16':
            export_text = base16_02(entry_box.get())
        elif encode_option_box.get() == 'base32':
            export_text = base32_02(entry_box.get())
        elif encode_option_box.get() == 'base64':
            export_text = base64_02(entry_box.get())
        elif encode_option_box.get() == 'base85':
            export_text = base85_02(entry_box.get())
        elif encode_option_box.get() == language[1]:
            export_text = binary_02(entry_box.get())
        elif encode_option_box.get() == language[21]:
            export_text = OCT_02(entry_box.get())
        elif encode_option_box.get() == language[17]:
            export_text = hexadecimal_02(entry_box.get())
        elif encode_option_box.get() == language[22]:
            export_text = Caesar_02(entry_box.get(),int(OffsetEntry.get()))
        elif encode_option_box.get() == 'base100':
            export_text = base100_02(entry_box.get())

        if ReverseMode:
            export_text = export_text[::-1]

        export_text_all = export_text

        export_text_tips_box.place(x=995,y=265)
        export_text_box.place(x=900,y=350)
        export_text_copy_box.place(x=1025,y=625)


        if len(export_text) >= 174:
            export_text_.set(export_text[0:174] + '...')
        else:
            export_text_.set(export_text)

        if AutoCopy:
            pyperclip.copy(export_text)
            tips.set(language[2])
        else:
            tips.set(language[5])
    except:
        tips.set(language[6])

def LanguageComboboxSelected(event):
    file = open(os.path.dirname(os.path.abspath(__file__))+'\\languages\\language.txt', 'w')
    file.write(language_option_box.get())
    tips.set(language[20])

def ExportTextCopy():
    pyperclip.copy(export_text_all)
    tips.set(language[7])

def AutoCopyTrueOrFalse():
    global AutoCopy
    if AutoCopy:
        AutoCopy = False
    else:
        AutoCopy = True


def ReverseModeTrueOrFalse():
    global ReverseMode
    if ReverseMode:
        ReverseMode = False
    else:
        ReverseMode = True

def RandomModeTrueOrFalse():
    global RanbowMode
    if RanbowMode:
        RanbowMode = False
    else:
        RanbowMode = True

def EncodeOptionComboboxSelected(event):
    global base100_tips

    #需要依靠偏移值
    if encode_option_box.get() == language[22]:
        OffsetEntry.configure(state='normal')
    else:
        OffsetEntry.configure(state='disabled')

    #不能解密

    if encode_option_box.get() == language[25] or encode_option_box.get() == language[26] or encode_option_box.get() == language[27] or encode_option_box.get() == language[28] or encode_option_box.get() == language[29] or encode_option_box.get() == language[30]:
        DecryptButtonBox.configure(state='disabled')
    else:
        DecryptButtonBox.configure(state='normal')

    #不能加密
    if encode_option_box.get() == 'base100':
        EncryptButtonBox.configure(state='disabled')
        if base100_tips == False:
            tkinter.messagebox.showinfo(title='tip',message=language[31])
            base100_tips = True

    else:
        EncryptButtonBox.configure(state='normal')

#Github

def Github():
    webbrowser.open('https://github.com/SilverWhite233/Cryptographic-Coding-Toolbox')


#=============================================内容添加==============================================

#自带ui
tips = tk.StringVar()
tips.set(language[8])
options_text_tips = tk.Label(window,text='Options',bg='silver',font=('微软雅黑',24),width=15,height=1,anchor='nw')
switch_text_tips = tk.Label(window,text='Switch',bg='silver',font=('微软雅黑',24),width=100,height=1,anchor='ne')

#tips
tip = random.randint(1,6)
if tip == 1:
    tip = language[8]
elif tip == 2:
    tip = language[32]
elif tip == 3:
    tip = language[33]
elif tip == 4:
    tip = language[34]
elif tip == 5:
    tip = language[35]
else:
    tip = language[36]

tips.set(tip)

tips_box = tk.Label(window,textvariabl=tips,bg='silver',font=('微软雅黑',12),width=300)

#分割线
line1 = Separator(window,orient=VERTICAL)

#选择编码
encode_option_box_tips = tk.Label(window,text=language[9],font=('微软雅黑',12))
encode_option_box = ttk.Combobox(window, state="readonly")
encode_option_box.bind("<<ComboboxSelected>>",EncodeOptionComboboxSelected)
encode_option_box['values'] = ('base16', 'base32', 'base64','base85','base100',language[1],language[21],language[17],language[22],language[25],language[26],language[27],language[28],language[29],language[30])
encode_option_box.current(0)

#语言选项
language_option_box_tips = tk.Label(window,text=language[19],font=('微软雅黑',12))
language_option_box = ttk.Combobox(window, state="readonly")
language_option_box['values'] = (languages)
language_option_box.set(language_name)

#输入框
entry_box = ttk.Entry(window,width=25)
entry_box_tips = tk.Label(window,text=language[10],font=('微软雅黑',12))

#加密解密按钮
EncryptButtonBox = ttk.Button(window,text=language[11],command=Encrypt)
DecryptButtonBox = ttk.Button(window,text=language[12],command=Decrypt)

#输出结果显示
export_text_tips_box = tk.Label(window,text=language[13],font=('微软雅黑',20))
export_text_ = tk.StringVar()
export_text_.set('')
export_text_box = tk.Label(window,textvariable=export_text_,wraplength=350,font=('微软雅黑',12))

#复制按钮
export_text_copy_box = ttk.Button(window,text=language[14],command=ExportTextCopy)

#自动复制按钮
AutoCopyBoxVar = tk.StringVar()
AutoCopyBoxVar.set(1)
AutoCopyBox = ttk.Checkbutton(window, text=language[15],style="TCheckbutton",command=AutoCopyTrueOrFalse,variable=AutoCopyBoxVar)

#倒序模式按钮
ReverseModeBoxVar = tk.StringVar()
ReverseModeBoxVar.set(0)
ReverseModeBox = ttk.Checkbutton(window, text=language[16],style="TCheckbutton",command=ReverseModeTrueOrFalse,variable=ReverseModeBoxVar)

#随机排列按钮
RanbowModeBoxVar = tk.StringVar()
RanbowModeBoxVar.set(0)
RanbowModeBox = ttk.Checkbutton(window, text=language[24],style="TCheckbutton",command=RandomModeTrueOrFalse,variable=RanbowModeBoxVar)

#偏移值
OffsetEntryTips = tk.Label(window,text=language[23],font=('微软雅黑',12))
OffsetEntry = ttk.Spinbox(window,from_=1,to=99,state='disabled')
OffsetEntry.set(1)
OffsetEntry.bind("<Key>", lambda event: "break")

#Github开源库
GithubButtonBox = ttk.Button(window,text=language[18],command=Github)

#=============================================执行脚本===============================================

tips_box.pack(side='bottom')

options_text_tips.pack(side='left',anchor='nw')
switch_text_tips.pack()

encode_option_box_tips.place(x=10,y=100)
encode_option_box.place(x=10,y=150)

language_option_box_tips.place(x=310,y=100)
language_option_box.place(x=310,y=150)
language_option_box.bind('<<ComboboxSelected>>',LanguageComboboxSelected)

OffsetEntryTips.place(x=10,y=250)
OffsetEntry.place(x=10,y=300)

AutoCopyBox.place(x=680,y=100)
ReverseModeBox.place(x=680,y=150)
RanbowModeBox.place(x=680,y=200)

EncryptButtonBox.place(x=925,y=205)
DecryptButtonBox.place(x=1125,y=205)

entry_box.place(x=950,y=105)
entry_box_tips.place(x=975,y=145)

GithubButtonBox.place(x=10,y=650)

line1.pack(fill='y',expand=True)

#===============================================结束=================================================

window.mainloop()