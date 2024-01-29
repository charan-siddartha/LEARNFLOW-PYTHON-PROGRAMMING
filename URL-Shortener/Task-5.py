import tkinter
import pyshorteners
import pyperclip

root=Tk()
root.geometry('600x300')
root.title("URL Shortener")
root.config(bg='#CAE1FF')


url1=StringVar()
url2=StringVar()



lb1=Label(root,text="Enter URL Here",font=('Arial,20,bol'),bg='#CAE1FF')
lb1.pack(pady=5)
En1=Entry(root,textvariable=url1,font=('Arial,20,bold'))
En1.pack()




lb2=Label(root,text="Shortened URL",font=('Arial,20,bold'),bg='#CAE1FF')
lb2.pack(pady=5)
En2=Entry(root,textvariable=url2,font=('Arial,20,bold'))
En2.pack()

bt1=Button(root,text="Generate URL",font=('Arial,20,bold'),bg='#6E7B8B',fg='white',bd=5,command=shorturl)
bt1.pack(pady=10)
btn2=Button(root,text="Copy URL",font=('Arial,20,bold'),bg='#6E7B8B',fg='white',bd=5,command=copyurl)
btn2.pack(pady=10)

def shorturl():
   urls=pyshorteners.Shortener().tinyurl.short(url1.get())
   url2.set(urls)

def copyurl():
   c_url=url2.get()
   pyperclip.copy(c_url)


root.mainloop()
