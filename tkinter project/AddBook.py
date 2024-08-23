from tkinter import *
from tkinter import messagebox
import pymysql

def addBook():
    # Establish database connection
    try:
        conn = pymysql.connect(host="localhost", user="root", password="Pradeep_ragu16", database="connectionsnew")
        cursor = conn.cursor()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
        return

    # Define the function to add a book
    def bookRegister():
        book_id = bookInfo1.get()
        title = bookInfo2.get()
        author = bookInfo3.get()
        status = bookInfo4.get().lower()

        insertBooks = "INSERT INTO books VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(insertBooks, (book_id, title, author, status))
            conn.commit()
            messagebox.showinfo('Success', "Book added successfully")
        except Exception as e:
            messagebox.showerror('Error', f"Error adding book: {e}")

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

    headingLabel = Label(headingFrame1, text="Add Book Details", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.4)

    lb1 = Label(labelFrame, text="Book ID: ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame, text="Title: ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62)

    lb3 = Label(labelFrame, text="Author: ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.5)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.5, relwidth=0.62)

    lb4 = Label(labelFrame, text="Status(Available/Issued): ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62)

    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

# Call the addBook function to run the application
addBook()
