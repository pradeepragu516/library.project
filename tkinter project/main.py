from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import addBook # Import the function you need from the module
from DeleteBook import deleteBook  # Adjust the import if needed
from ViewBooks import viewBooks  # Adjust the import if needed
from IssueBook import issueBook  # Adjust the import if needed
from ReturnBook import returnBook  # Import the returnBook function

mypass = "Pradeep_ragu16"  # Use your own password
mydatabase = "connectionsnew"  # The database name

# Database connection
try:
    conn = pymysql.connect(host="localhost", user="root", password="Pradeep_ragu16", database="connectionsnew")
    cursor = conn.cursor()
except pymysql.MySQLError as e:
    messagebox.showerror("Database Error", f"Error connecting to the database: {e}")
    exit(1)  # Exit the script if the database connection fails

# Tkinter window
root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

bg_image = PhotoImage(file=r"C:\Users\prade\OneDrive\Documents\lib.jpg")
label = Label(root, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)


headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n DataFlair Library", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons
btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=deleteBook)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=viewBooks)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()
