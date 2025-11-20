from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password ():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_number =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_number + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
 
def save_to_file ():
    email = email_entry.get()
    website = web_entry.get()
    password = password_entry.get()

    new_data = {website:{"email" : email,"password":password}}
    
    if len(email) ==0 or len(password) == 0:
        messagebox.showerror(title="opps " , message="Please don't leave any field empty.")
    else:
        try :
            with open ("data.json",mode="r") as data_file :
                data = json.load(data_file)
        except FileNotFoundError :
            with open ("data.json",mode="w") as data_file :
                json.dump(new_data,data_file,indent=4)
                
        else:
            data.update(new_data)
            with open ("data.json","w") as data_file :
                json.dump(data,data_file,indent=4) 

        finally :
            password_entry.delete(0,END)
            web_entry.delete(0,END)
            web_entry.focus()
#----------------------------serching password-------------------------#

def search():
    website_name = web_entry.get()
    try :
        with open ("data.json","r") as data_file :
            data = json.load(data_file)
    except FileNotFoundError :
        messagebox.showerror(title="oops",message=f"Data file not found.")

    else :
        if website_name in data :
            email =data[website_name]["email"]
            password = data[website_name]["password"]

            messagebox.showinfo(title=website_name,message=f"Email :{email}\nPassword : {password} ")
        else :
            messagebox.showerror(title="oops",message=f"You don't save the password of the {website_name}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height= 200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0) 

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)
web_entry = Entry(width=31)
web_entry.grid(column=1 ,row=1)
web_entry.focus()


email_label = Label(text="Email/username: ")
email_label.grid(column=0,row=2)
email_entry = Entry(width=50)
email_entry.insert(0,"mangesham001@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1,row=3)

gen_button = Button(text="Generate password",command=generate_password)
gen_button.grid(column=2 ,row=3)

add_button = Button(text="Add",width=45,command=save_to_file)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width=13,command=search)
search_button.grid(column=2 ,row=1)

window.mainloop()