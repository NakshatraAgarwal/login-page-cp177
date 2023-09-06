from tkinter import *
root = Tk()
root.title("login page")
root.geometry("600x600")

label = Label(root, text="Name:")
label.place(relx = 0.3, rely = 0.2, anchor=CENTER)
inp = Entry(root)
inp.place(relx = 0.6, rely=0.2, anchor=CENTER)

passw = Label(root, text="Password:")
passw.place(relx = 0.3, rely = 0.3, anchor=CENTER)
inpass = Entry(root)
inpass.place(relx = 0.6, rely=0.3, anchor=CENTER)

capt = Label(root, text="Captcha:")
capt.place(relx = 0.3, rely = 0.4, anchor=CENTER)
incap = Entry(root)
incap.place(relx = 0.6, rely=0.4, anchor=CENTER)

newpass = Label(root)
newpass.place(relx=0.4, rely=0.7, anchor=CENTER)

newcap = Label(root)
newcap.place(relx=0.4, rely=0.8, anchor=CENTER)

class userDB():
    def __init__(self):
        self.__name = "James"
        self.__pass = "JamesPro1234"
        self.__captcha = "captcha123"
    
    def showUser(self):
        label["text"] = "Name: " + self.__name
        passw["text"] = "Password: " + self.__pass
        capt["text"] = "Captcha: " + self.__captcha
        print(self.__captcha)

def addUser():
    global obj
    obj.showUser()
    label["text"] = "Name: " + inp.get()
    passw["text"] = "Password: " + inpass.get()
    capt["text"] = "Captcha: " + incap.get()
    
    

obj = userDB()
btn = Button(root,text="Update Login Details",command=addUser)
btn.place(relx=0.2,rely=0.7,anchor=CENTER)

btn2 = Button(root,text="Show Profile",command=obj.showUser)
btn2.place(relx=0.2,rely=0.9,anchor=CENTER)
        

root.mainloop()

