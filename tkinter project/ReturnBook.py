from tkinter import *
from tkinter import messagebox
import pymysql

def returnBook():
    try:
        con = pymysql.connect(host="localhost", user="root", password="Pradeep_ragu16", database="connectionsnew")
        cur = con.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return

    def return_book():
        book_id = bookInfo1.get()

        deleteIssue = "DELETE FROM books_issued WHERE bid = %s"
        updateStatus = "UPDATE books SET status = 'available' WHERE bid = %s"
        try:
            cur.execute(deleteIssue, (book_id,))
            cur.execute(updateStatus, (book_id,))
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")
        except Exception as e:
            messagebox.showerror('Error', f"Error returning book: {e}")

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

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.4)

    lb2 = Label(labelFrame, text="Book ID: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    returnBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=return_book)
    returnBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
