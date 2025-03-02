from tkinter import*
from PIL import Image, ImageTk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Basic ERP System")

        #==title==#
        self.icon_title= PhotoImage(file="img/icon.png")
        title = Label(self.root, text = "IMS Initial Draft", image=self.icon_title, compound=LEFT, font = ("times new roman", 40, "bold"), bg="#90EE90", fg="black", anchor="w", padx=20).place(x = 0, y=0, relwidth=1, height= 70)
        
        #==button===
        btn_logout = Button(self.root, text="Logout", font=("times new roman",15,"bold"),bg="yellow", cursor="hand2").place(x=1150,y=10, height=50, width=150)
        #clock
        self.lbl_clock = Label(self.root, text = "System Content\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="green", fg="white")
        self.lbl_clock.place(x = 0, y=70, relwidth=1, height= 30)

        #side bar LEFT
        LeftMenu= Frame(self.root, bd=2, relief=RIDGE)
        LeftMenu.place(x=0,y=102,width=200,height=565)
        
root = Tk()
obj = IMS(root)
root.mainloop()