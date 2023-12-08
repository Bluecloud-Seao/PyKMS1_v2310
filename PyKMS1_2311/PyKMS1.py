import tkinter as tk
import tkinter.ttk as ttk
import os
import time
from tkinter import messagebox
root=tk.Tk()
root.geometry("350x300")
root.resizable(False,False)
root.title("PyKMS1(BETA)")
root.iconbitmap('D:\python_files\BluecloudOS\IMG\icon.ico')
messagebox.showinfo("使用需知","请确认您以管理员方式启动,提倡购买正版,仅供个人学习使用。开源软件,禁止商用。")
white=ttk.Frame(root,height="40")
white.pack()
def win11():
    os.system("cmd.exe /c slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    os.system("cmd.exe /c slmgr /skms kms8.msguides.com")
    os.system("slmgr /xpr")
    messagebox.showinfo("激活","已完成")
def win10():
    os.system("cmd.exe /c slmgr /ipk VK7JG-NPHTM-C97JM-9MPGT-3V66T")
    os.system("cmd.exe /c slmgr /skms http://kms.xspace.in")
    os.system("slmgr /ato")
    messagebox.showinfo("激活","已完成")
def win7():
    os.system("cmd.exe /c slmgr /ipk slmgr /ipk 33PXH-7Y6KF-2VJC9-XBBR8-HVTHH")
    os.system("cmd.exe /c slmgr /skms zh.us.to")
    os.system("slmgr /ato")
    messagebox.showinfo("激活","已完成")
def start_win():
    if key and kms_s == "ㅤ":
        messagebox.showerror("错误","不是有效参数")
    while loading.cget("value") <= loading["maximum"]:
        loading.step(5)
        root.update()
        time.sleep(0.05)
    os.system("cmd.exe /c slmgr /ipk slmgr /ipk %s"%key)
    os.system("cmd.exe /c slmgr /skms %s"%kms_s)
    os.system("slmgr /ato")
    loading.stop()
    messagebox.showinfo("激活","已完成")
def info():
    messagebox.showinfo("关于","2023 版权所有 SEAO PyKMS1激活程序 BETA0.01 提倡购买正版,仅供个人学习使用 开源软件,禁止商用")
def update():
    subwindow=tk.Toplevel()
    subwindow.geometry("200x100")
    subwindow.title("Update")
    subwindow.resizable(False,False)
    def Find():
        messagebox.showwarning("注意","BETA版本未开放服务器,找不到新版本,请关注微信号Seao159400")
    subwindow_l=tk.Label(subwindow,text="您是最新版")
    subwindow_l.pack()
    update_button=ttk.Button(subwindow,text="Find the new",command=Find)
    update_button.pack()
    subwindow.mainloop()

munuhub=tk.Menu(root)#创建菜单栏
fast=tk.Menu(munuhub,tearoff=0)
more=tk.Menu(munuhub,tearoff=0)
munuhub.add_cascade(label="快速激活",menu=fast)

fast.add_command(label="激活Windows11",command=win11)

fast.add_command(label="激活Windows10",command=win10)

fast.add_command(label="激活Windows7",command=win7)

munuhub.add_cascade(label="更多",menu=more)

more.add_command(label="更新",command=update)

more.add_command(label="关于",command=info)
root.config(menu=munuhub)

kms_s=tk.Label(root,text="  KMS服务器:")#指示输入KMS服务器文字
kms_s.pack(side="top",anchor="nw")

kms_t=ttk.Entry(root,width="45")#输入KMS服务器
kms_t.pack()

keytext=ttk.Label(root,text="  Key:")#指示输入Key文字
keytext.pack(side="top",anchor="nw")

key=ttk.Entry(root,width="45")#输入Key
key.pack()

white_a=ttk.Frame(root,height=10)#空白处
white_a.pack()

loading=ttk.Progressbar(root,mode="indeterminate",length=200)#进度条
loading["maximum"]=100
loading['value']=0
loading.pack()

status = tk.Label(root, text="输入KMS服务器以激活", bd=1, relief=tk.SUNKEN, anchor=tk.W)#底部栏
status.pack(side=tk.BOTTOM, fill=tk.X)

start=ttk.Button(root,text="开始激活",command=start_win)#激活按钮
start.pack(side=tk.BOTTOM)

root.mainloop()