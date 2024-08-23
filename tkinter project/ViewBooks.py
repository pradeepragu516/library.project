from tkinter import *
import pymysql
from tkinter import messagebox

def viewBooks():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="Pradeep_ragu16", database="connectionsnew")
        cursor = conn.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.08)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.4)

    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s%-20s" % ('BID', 'Title', 'Author', 'Status'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black', fg='white').place(relx=0.05, rely=0.2)

    getBooks = "SELECT * FROM books"
    try:
        cursor.execute(getBooks)
        conn.commit()
        for i in cursor:
            Label(labelFrame, text="%-10s%-40s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except Exception as e:
        messagebox.showerror('Error', f"Error fetching data: {e}")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
viewBooks()