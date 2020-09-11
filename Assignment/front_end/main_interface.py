from tkinter import *
from tkinter import ttk
from back_end.connector import Staff
from model.model import *
from tkinter import messagebox

def linear_search(record, Name):
    for i in record:
        print(i)
        if i == Name:
            return True
    return False

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Party Management System")
        self.root.geometry("1350x700+0+0")
        title = Label(self.root, text='CHRISTMAS Event Management System', bd=10, relief=RIDGE, font=("arial", 40, 'bold'),
                      bg='grey')
        title.pack(side=TOP, fill=X)

        self.connect = Staff()

        # ALl Variables==========================================
        self.ID_var = StringVar()
        self.Name_var = StringVar()
        self.Address_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.Email_var = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

        # ==========Mange Frame=================================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='sky blue')
        Manage_Frame.place(x=20, y=100, width=450, height=560)
        m_title = Label(Manage_Frame, text="Student info", bg="sky blue",font=("arial", 30, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_ID = Label(Manage_Frame, text="ID:", bg="sky blue",font=("arial", 20, 'bold'))
        lbl_ID.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        self.txt_ID = Entry(Manage_Frame, textvariable=self.ID_var, font=("arial", 15, 'bold'), bd=5,relief=GROOVE)
        self.txt_ID.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_Name = Label(Manage_Frame, text="Name:", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        self.txt_Name = Entry(Manage_Frame, textvariable=self.Name_var, font=("arial", 15, 'bold'), bd=5, relief=GROOVE)
        self.txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address:", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_Address.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Entry(Manage_Frame, textvariable=self.Address_var,font=("arial", 15, 'bold'),bd=5, relief=GROOVE)
        self.txt_Address.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender:", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        self.combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("arial", 13, "bold"),
                                    state='readonly')
        self.combo_Gender['values'] = ("male", "female", "other")
        self.combo_Gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact:", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        self.txt_Contact = Entry(Manage_Frame, textvariable=self.Contact_var, font=("arial", 15, 'bold'), bd=5,
                            relief=GROOVE)
        self.txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="DOB:", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        self.txt_DOB = Entry(Manage_Frame, textvariable=self.DOB_var, font=("arial", 15, 'bold'), bd=5, relief=GROOVE)
        self.txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Email = Label(Manage_Frame, text="Email", bg="sky blue", font=("arial", 20, 'bold'))
        lbl_Email.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_Email = Entry(Manage_Frame, textvariable=self.Email_var, font=("arial", 15, 'bold'), bd=5, relief=GROOVE)
        self.txt_Email.grid(row=7, column=1, pady=10, padx=20, sticky="w")


        # Button Frame==================================================
        btn_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="light blue")
        btn_frame.place(x=10, y=500, width=430)

        Addbtn = Button(btn_frame, text="Add",bg='blue', width=10, command=self.add_student).grid(row=0, column=0, padx=10,pady=10)
        updatebtn = Button(btn_frame, text="update",bg='blue',command=self.update_data, width=10).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="delete", bg='blue',width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="clear",bg='blue', width=10,command= self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ========Detail Frame========================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='yellow')
        Detail_Frame.place(x=500, y=100, width=800, height=560)
        lbl_search = Label(Detail_Frame, text="Search By Full Name", bg="yellow", fg="black",font=("times new roman", 20, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")
        self.txt_Search = Entry(Detail_Frame, textvariable=self.search_text, width=15,font=("times new roman", 14, 'bold'),bd=5,relief=GROOVE)
        self.txt_Search.grid(row=0, column=2, pady=10, padx=5, sticky="w")
        saerchbtn = Button(Detail_Frame, text="search", command=self.search_data,width=20, pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame, text="showall", command=self.fetch_data, width=20, pady=5).grid(row=0,column=4,padx=10,pady=10)

        # Table Frame===============================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='yellow')
        Table_Frame.place(x=10, y=70, width=760, height=470)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame,
                                          columns=("ID", "Name", "Address", "Gender", "Contact", "DOB", "Email"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("ID", text="ID")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Address", text="Address")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("DOB", text="DOB")
        self.Student_Table.heading("Email", text="Email")
        self.Student_Table['show'] = 'headings'
        self.Student_Table.column("ID", width=100)
        self.Student_Table.column("Name", width=100)
        self.Student_Table.column("Address", width=150)
        self.Student_Table.column("Gender", width=100)
        self.Student_Table.column("Contact", width=100)
        self.Student_Table.column("DOB", width=100)
        self.Student_Table.column("Email", width=100)
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_student(self):
        st_ref = Members(self.txt_ID.get(), self.txt_Name.get(),self.txt_Address.get(),self.combo_Gender.get(),self.txt_Contact.get(), self.txt_DOB.get(), self.txt_Email.get())
        query = 'insert into kalay values(%s,%s,%s,%s,%s,%s,%s);'
        values = (
            int(st_ref.get_ID()), st_ref.get_Name(), st_ref.get_Address(), st_ref.get_Gender(),
            st_ref.get_Contact(), st_ref.get_DOB(), st_ref.get_Email())
        self.connect.insert(query, values)
        messagebox.showinfo("Success", "Data inserted sucessfully")

    def update_data(self):
        st_ref = Members(self.txt_ID.get(), self.txt_Name.get(), self.txt_Address.get(),
                         self.combo_Gender.get(), self.txt_Contact.get(), self.txt_DOB.get(), self.txt_Email.get())
        query = 'update kalay set name=%s,address=%s,gender=%s,Contact=%s,DOB=%s,Email=%s where ID=%s;'
        values = (
            st_ref.get_Name(), st_ref.get_Address(), st_ref.get_Gender(),
            st_ref.get_Contact(), st_ref.get_DOB(), st_ref.get_Email(),st_ref.get_ID())
        self.connect.update(query, values)
        messagebox.showinfo("Success", "Data updated sucessfully")

    def delete_data(self):
        st_ref = Members(self.txt_ID.get(), self.txt_Name.get(), self.txt_Address.get(),
                         self.combo_Gender.get(), self.txt_Contact.get(), self.txt_DOB.get(), self.txt_Email.get())
        query = 'delete from kalay where ID=%s;'
        values = (int(st_ref.get_ID()),)
        self.connect.delete(query, values)
        messagebox.showinfo("Success", "Data deleted sucessfully")

    def clear(self):
        self.txt_ID.delete(0, END)
        self.txt_Name.delete(0, END)
        self.txt_Address.delete(0, END)
        self.txt_DOB.delete(0, END)
        self.combo_Gender.delete(0, END)
        self.txt_Contact.delete(0, END)
        self.txt_Email.delete(0, END)

    def fetch_data(self):
        query = "select * from kalay;"
        records = self.connect.select(query)

        if len(records) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in records:
                self.Student_Table.insert('', END, values=row)

    def get_cursor(self, ev):
        curosor_row = self.Student_Table.focus()
        contents = self.Student_Table.item(curosor_row)
        row = contents['values']
        self.ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.Address_var.set(row[6])

    def search_data(self):
        global row
        if self.txt_Search.get() == "":
            messagebox.showinfo("Error", "Searching information required")
        else:
            query = "select * from kalay where Name=%s;"
            values = (self.txt_Search.get(),)
            records = self.connect.search(query, values)
            list = []
            for row in records:
                list.append(row[1])
            if not linear_search(list, self.txt_Search.get()):
                messagebox.showinfo("Error", "This Name doesnot exist")
            elif len(records) != 0:
                self.Student_Table.delete(*self.Student_Table.get_children())
                for row in records:
                    self.Student_Table.insert('', END, values=row)




root = Tk()
ob = Student(root)
root.mainloop()
