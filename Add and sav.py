from tkinter import *
from tkinter import messagebox
import csv

def update_file():
    global total
    with open('movie_file.csv', mode='a') as movie_file:
        movie_writer = csv.writer(movie_file, delimiter=',')
        movie_writer.writerow([movie_code_entry.get(), movie_name_entry.get(), author_entry.get()])
    total = total + 1

def next_item():
    movie_code_entry.delete(0, END)
    movie_name_entry.delete(0, END)
    author_entry.delete(0, END)

def total_books():
    global total
    messagebox.showinfo(title="Total number of books", message=total)

total = 0
root = Tk()

root.geometry('600x400')
root.configure(bg="black")

movie_code_label = Label(text="MOVIE CODE", font=('Verdana', 14))
movie_name_label = Label(text='MOVIE NAME', font=('Verdana', 14))
author_label = Label(text='AUTHOR NAME', font=('Verdana', 14))

movie_code_entry = Entry(font=('Verdana', 14), width=10)
movie_name_entry = Entry(font=('Verdana', 14), width=20)
author_entry = Entry(font=('Verdana', 14), width=20)

update_button = Button(text='SAVE', font=('Verdana', 14), command = update_file)
next_button = Button(text='NEXT', font=('Verdana', 13), command = next_item)
total_button = Button(text='TOTAL', font=('Verdana', 13), command = total_books)

movie_code_label.grid(row=0, column=0)
movie_name_label.grid(row=2, column=0)
author_label.grid(row=4, column=0)

movie_code_entry.grid(row=0, column=1)
movie_name_entry.grid(row=2, column=1)
author_entry.grid(row=4, column=1)

update_button.grid(row=40, column=0)
next_button.grid(row=40, column=1)
total_button.grid(row=35, column=2)

mainloop()