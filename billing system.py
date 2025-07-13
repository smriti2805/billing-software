import os
import tempfile
from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # product categories list
        
        self.Category = ["Select Option", "Clothing", "LifeStyle", "Mobiles"]
        self.SubCategory = {
            "Clothing": {
                "Pant": {"Levis": 5000, "Mufti": 700, "Spykar": 8000},
                "T-Shirt": {"Polo": 1500, "Roadster": 1800, "Jack&Jones": 1700},
                "Shirt": {"Ptere England": 2100, "Louis Phillipe": 2700, "Park Avenue": 1740},
            },
            "LifeStyle": {
                "Bath Soap": {"LifeBoy": 20, "Lux": 20, "Santoor": 20, "Pearl": 30},
                "Face Cream": {"Fair&Lovely": 20, "Ponds": 20, "Garniar": 30},
                "Hair Oil": {"Parachute": 25, "Jashmin": 22, "Bajaj": 30},
            },
            "Mobiles": {
                "IPhone": {"Iphone X": 40000, "Iphone 11": 60000, "Iphone 12": 85000},
                "Samsumg": {"Samsung M16": 16000, "Samsumg M12": 12000, "Samsung M21": 18000},
                "Xiome": {"Redmi 11": 11000, "Redmin 12": 12000, "Redmi 12 pro": 13000},
                "Realme": {"Realme 12": 25000, "Realme 13": 22000, "Realme 14": 30000},
                "One+": {"ONePlus 1": 10000, "OnePlus 2": 12000, "OnePlus 3": 16000},
            },
        }

        # ============variables===================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_email = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.sub_total = StringVar()
        self.total = StringVar()
        self.tax_input = StringVar()
        self.prices = IntVar()
        self.qty = IntVar()
        self.total_list = []

        self.bill_no.set(random.randint(10000, 99999))

        # image 1 Load and resize the image
        img = Image.open("image/b1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Create a label to display the image
        lb1_img = Label(self.root, image=self.photoimg)
        lb1_img.place(x=0, y=0, width=500, height=130)

        #  image 2 Load and resize the image
        img_1 = Image.open("image/good.jpg")
        img_1 = img_1.resize((500, 130), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        # Create a label to display the image
        lb1_img_1 = Label(self.root, image=self.photoimg_1)
        lb1_img_1.place(x=500, y=0, width=500, height=130)

        # image 3 Load and resize the image
        img_2 = Image.open("image/girl1.jpg")
        img_2 = img_2.resize((500, 130), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        # Create a label to display the image
        lb1_img_2 = Label(self.root, image=self.photoimg_2)
        lb1_img_2.place(x=1000, y=0, width=520, height=130)

        lbl_title = Label(self.root, text="BILLING SOFTWARE USING PYTHON", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        lbl_title.place(x=0, y=130, width=1530, height=45)

        self.lbl_time = Label(lbl_title, font=("times new roman",16,'bold'),background="white",foreground="red")
        self.lbl_time.place(x=0,y=0,width=120,height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=175, width=1530, height=620)

        # Customer LabelFrame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mobile = Label(Cust_Frame, text="Mobile No.", font=("times new roman", 12, "bold"), bg="white")
        self.lbl_mobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, textvariable=self.c_phone, font=("times new roman", 12, "bold"), width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName = Label(Cust_Frame, font=("arial", 10, "bold"), bg="white", text="Customer Name", bd=4)
        self.lblCustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame, textvariable=self.c_name, font=("arial", 10, "bold"), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(Cust_Frame, font=("arial", 12, "bold"), bg="white", text="Email", bd=4)
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email, font=("arial", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=5, width=620, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Select categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, values=self.Category, font=("arial", 10, "bold"), width=24, state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        # subcategory
        self.lblSubCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="subcategories", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Combo_SubCategory = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=24, state="readonly")
        self.Combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.SubCategories)

        # product_Name
        self.lblProduct = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Product Name", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Product = ttk.Combobox(Product_Frame, textvariable=self.product, font=("arial", 10, "bold"), width=24, state="readonly")
        self.Combo_Product.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Product.bind("<<ComboboxSelected>>", self.Product)

        # Price
        self.lblPrice = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.Combo_Price = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), textvariable=self.prices, width=24, state="readonly")
        self.Combo_Price.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Qty
        self.lblQty = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.Combo_Qty = ttk.Entry(Product_Frame, textvariable=self.qty, font=("arial", 10, "bold"), width=26)
        self.Combo_Qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # middle_frame
        Middle_Frame = Frame(Main_Frame, bd=10)
        Middle_Frame.place(x=10, y=150, width=980, height=340)

        # image 1 Load and resize the image
        img12 = Image.open("image/mall.jpg")
        img12 = img12.resize((490, 340), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        # Create a label to display the image
        lb1_img12 = Label(Middle_Frame, image=self.photoimg12)
        lb1_img12.place(x=0, y=0, width=490, height=340)

        #  image 2 Load and resize the image
        img_13 = Image.open("image/good.jpg")
        img_13 = img_13.resize((490, 340), Image.LANCZOS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        # Create a label to display the image
        lb1_img_13 = Label(Middle_Frame, image=self.photoimg_13)
        lb1_img_13.place(x=490, y=0, width=490, height=340)

        # search
        Search_Frame = Frame(Main_Frame, bd=2, bg="white")
        Search_Frame.place(x=1020, y=10, width=500, height=40)

        self.lblBill = Label(Search_Frame, font=("arial", 12, "bold"), bg="red", fg="white", text="Bill Number", bd=4)
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.Txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=("arial", 10, "bold"), width=26)
        self.Txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.Btn_Search = Button(Search_Frame, command=self.find_bill, text="Search", font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.Btn_Search.grid(row=0, column=2)

        # Right_frame Bill_area
        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Area", font=("times new roman", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=1000, y=45, width=480, height=440)

        # scrool bar
        scrool_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scrool_y.set, bg="white", fg="blue", font=("times new roman", 12, "bold"))
        scrool_y.pack(side=RIGHT, fill=Y)
        scrool_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill counter LabelFrame
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roamn", 12, "bold"), bg="white", fg="red")
        Bottom_Frame.place(x=0, y=485, width=1520, height=125)

        self.lblSubTotal = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubToatal = ttk.Entry(Bottom_Frame, textvariable=self.sub_total, font=("arial", 10, "bold"), width=26)
        self.EntrySubToatal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Gov Tax", bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame, font=("arial", 10, "bold"), textvariable=self.tax_input, width=26)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblAmountTotal = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Total", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtAmountTotal = ttk.Entry(Bottom_Frame, font=("arial", 10, "bold"), textvariable=self.total, width=26)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Botton_Frame
        Bottom_Frame = Frame(Bottom_Frame, bd=2, bg="white")
        Bottom_Frame.place(x=320, y=0)

        self.BottonAddtoCart = Button(Bottom_Frame, text="Add To Cart", command=self.add_item, height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BottonAddtoCart.grid(row=0, column=0)

        self.BtnGenarate_Bill = Button(Bottom_Frame, command=self.gen_bill, text="Generate Bill", height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnGenarate_Bill.grid(row=0, column=1)

        self.BtnSave = Button(Bottom_Frame, command=self.save_bill, text="Save Bill", height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Bottom_Frame, command=self.print_bill, text="Print", height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Bottom_Frame, command=self.clear, text="Clear", height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Bottom_Frame, command=self.root.destroy, text="Exit", height=2, font=("arial", 10, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)

        self.welcome()
        self.time()

    #=================functionns===============

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl_time.config(text=string)
        self.lbl_time.after(1000,self.time)

    def Categories(self, e):
        self.Combo_SubCategory.config(values=list(self.SubCategory[self.Combo_Category.get()].keys()))
        self.Combo_SubCategory.current(0)

    def SubCategories(self, e):
        self.Combo_Product.config(values=list(self.SubCategory[self.Combo_Category.get()][self.Combo_SubCategory.get()].keys()))
        self.Combo_Product.current(0)

    def Product(self, e):
        self.Combo_Price.config(values=self.SubCategory[self.Combo_Category.get()][self.Combo_SubCategory.get()][self.Combo_Product.get()])
        self.Combo_Price.current(0)
        self.qty.set(1)

    def add_item(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            tax = 1
            self.cost = self.prices.get() * self.qty.get()
            self.total_list.append(self.cost)
            self.textarea.insert(END, f"{self.product.get()}\t\t\t{self.qty.get()}\t{self.cost}\n")
            self.sub_total.set(f"Rs.{sum(self.total_list):.2f}")
            self.tax_input.set(f"Rs.{sum(self.total_list)*tax/100:.2f}")
            self.total.set(f"Rs.{sum(self.total_list)+(sum(self.total_list))*tax/100:.2f}")

    def save_bill(self):
        op = messagebox.askyesnocancel("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
                f.write(self.textarea.get(1.0, END))
            messagebox.showinfo("Saved", f"Bill No.:{self.bill_no.get()} saved successfully.")

    def find_bill(self):
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.search_bill.get():
                self.textarea.delete(1.0, END)
                with open(f"bills/{i}", "r") as f:
                    for line in f:
                        self.textarea.insert(END, line)
                break
        else:
            messagebox.showerror("Error", "Bill not found")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.qty.set(0)
        self.bill_no.set(random.randint(10000, 99999))
        self.total_list = []
        self.welcome()

    def print_bill(self):
        with open(temp := tempfile.mktemp(".txt"), "w") as f:
            f.write(self.textarea.get(1.0, END))
            os.startfile(temp, "print")

    def gen_bill(self):
        if self.product.get() == "":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            text = self.textarea.get(10.0, 10.0 + float(len(self.total_list)))
            self.welcome()
            self.textarea.insert(
                END,
                f"""{text}
==========================================
 Sub Amount:\t\t\t{self.sub_total.get()}
 Tax Amount:\t\t\t{self.tax_input.get()}
 Total Amount:\t\t\t{self.total.get()}
==========================================
""",
            )

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(
            END,
            f""" Welcome Mini Mall
 Bill Number: {self.bill_no.get()}
 Customer Name: {self.c_name.get()}
 Phone Number: {self.c_phone.get()}
 Customer Email: {self.c_email.get()}

==========================================
 Products\t\t\tQTY\tPrice
==========================================
""",
        )


if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
