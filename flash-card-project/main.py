from tkinter import *
import csv
import pandas
from random import randint,choice

BACKGROUND_COLOR = "#B1DDC6"
SEC_COUNT = 3
timer = None
data = pandas.read_csv("D:/my_python_learning/udemy_projects/day_31/flash-card-project-start/data/french_to_marathi.csv")
hindi_words = data["Hindi"].to_list()
french_words = data["French"].to_list()
known_word_list =[]

def choose_the_word_index():
    global word_index
    word_index = randint(0,len(hindi_words)-1)

def time_over ():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="मराठी")
    canvas.itemconfig(word_text, text=hindi_words[word_index])



def counter (count):
    global timer
    if count >  0:
        timer = window.after(1000,counter,count -1)

    else :
        time_over()



def known_word():
    known_word_list.append(word_index)  
    next_word() 

def next_word():
    try:
        window.after_cancel(timer)
    except:
        pass

    choose_the_word_index()
    while word_index in known_word_list :
        choose_the_word_index()
    
    canvas.itemconfig(canvas_image,image=card_front )
    canvas.itemconfig(title_text,text= "French")
    canvas.itemconfig(word_text,text=french_words[word_index] )
    counter(SEC_COUNT)


# UI setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="udemy_projects/day_31/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="udemy_projects/day_31/flash-card-project-start/images/card_back.png")
wrong_img = PhotoImage(file="udemy_projects/day_31/flash-card-project-start/images/wrong.png")
right_img = PhotoImage(file="udemy_projects/day_31/flash-card-project-start/images/right.png")

choose_the_word_index()

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text=french_words[word_index], font=("Arial", 60, "bold"))


right_button = Button(image=right_img, highlightthickness=0,command=known_word)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0,command=next_word)
wrong_button.grid(column=0, row=1)
next_word()



window.mainloop()
