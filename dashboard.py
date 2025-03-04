from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Basic ERP System")
        self.root.config(bg="white")
        #==title==#
        self.icon_title= PhotoImage(file="img/icon.png")
        title = Label(self.root, text = "IMS Initial Draft", image=self.icon_title, compound=LEFT, font = ("times new roman", 40, "bold"), bg="#90EE90", fg="black", anchor="w", padx=20).place(x = 0, y=0, relwidth=1, height= 70)
        
        #==button===
        btn_logout = Button(self.root, text="Logout", font=("times new roman",15,"bold"),bg="yellow", cursor="hand2").place(x=1150,y=10, height=50, width=150)

        #clock
        self.lbl_clock = Label(self.root, text = "System Content\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="green", fg="white")
        self.lbl_clock.place(x = 0, y=70, relwidth=1, height= 30)

        #side bar LEFT
        self.MenuLogo= Image.open("img/sb.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu= Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill = X)
        
        self.icon_emp= PhotoImage(file="img/emp.png")
        self.icon_sales= PhotoImage(file="img/sales.png")
        self.icon_supply= PhotoImage(file="img/supply.png")
        self.icon_stock= PhotoImage(file="img/stock.png")
        self.icon_help= PhotoImage(file="img/help.png")
        self.icon_exit= PhotoImage(file="img/exit.png")

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman",20),bg="#2E5984", fg="white").pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, image=self.icon_emp, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", image=self.icon_sales, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supply = Button(LeftMenu, text="Supplier", image=self.icon_supply, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_stock = Button(LeftMenu, text="Stock", image=self.icon_stock, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_help = Button(LeftMenu, text="Help", image=self.icon_help, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", image=self.icon_exit, compound=LEFT, padx=10,anchor="w", font=("times new roman",20, "bold"),bg="light blue", fg="black", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        #==content===
        self.lbl_employee=Label(self.root, text="Total Employee\n [  0  ]", bd=5, relief=RIDGE, bg="pink", fg="black", font=("goudy old style",20, "bold"))
        self.lbl_employee.place(x=300,y=200, height=150, width=300)

        self.lbl_sales=Label(self.root, text="Total Sales\n [  0  ]", bd=5, relief=RIDGE, bg="#89CFF0", fg="black", font=("goudy old style",20, "bold"))
        self.lbl_sales.place(x=700,y=200, height=150, width=300)

        self.lbl_supply=Label(self.root, text="Total Supplier\n [  0  ]", bd=5, relief=RIDGE, bg="#FFC39B", fg="black", font=("goudy old style",20, "bold"))
        self.lbl_supply.place(x=300,y=450, height=150, width=300)

        self.lbl_stock=Label(self.root, text="Total Stocks\n [  0  ]", bd=5, relief=RIDGE, bg="#D8BEE5", fg="black", font=("goudy old style",20, "bold"))
        self.lbl_stock.place(x=700,y=450, height=150, width=300)

        #footer
        lbl_footer = Label(self.root, text = "IMS Inventory Management System\n @Sneha Rugmini", font = ("times new roman", 12), bg="green", fg="white").pack(side=BOTTOM, fill=X)
#====================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

if __name__=="__main__":       
    root = Tk()
    obj = IMS(root)
    root.mainloop()