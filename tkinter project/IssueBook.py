from tkinter import *
from tkinter import messagebox
import pymysql

def issueBook():
    try:
        con = pymysql.connect(host="localhost", user="root", password="Pradeep_ragu16", database="connectionsnew")
        cur = con.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return

    def issue():
        book_id = bookInfo1.get()
        issued_to = bookInfo2.get()

        issueSql = "INSERT INTO books_issued (bid, issued_to) VALUES (%s, %s)"
        updateStatus = "UPDATE books SET status = 'issued' WHERE bid = %s"
        try:
            cur.execute(issueSql, (book_id, issued_to))
            cur.execute(updateStatus, (book_id,))
            con.commit()
            messagebox.showinfo('Success', "Book issued successfully")
        except Exception as e:
            messagebox.showerror('Error', f"Error issuing book: {e}")

        root.destroy()

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.08)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.4)

    lb1 = Label(labelFrame, text="Book ID: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Issued To: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.4, relwidth=0.62)

    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
