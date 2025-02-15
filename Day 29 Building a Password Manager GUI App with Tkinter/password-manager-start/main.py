import tkinter
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
    """
    Generate a random password, insert it into the password input field, and copy it to the clipboard.

    This function creates a random password using a combination of letters, numbers, and symbols.
    The generated password is then inserted into the password input field and copied to the clipboard.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordLetters = [choice(letters) for _ in range(randint(8, 10))]
    passwordSymbols = [choice(symbols) for _ in range(randint(2, 4))]
    passwordNumbers = [choice(numbers) for _ in range(randint(2, 4))]

    passwordList = passwordLetters + passwordSymbols + passwordNumbers
    shuffle(passwordList)

    password = "".join(passwordList)
    passwordInput.delete(0, tkinter.END)
    passwordInput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Save the website, email/username, and password to a file and clear the website and password fields.

    This function retrieves the values from the website, email/username, and password input fields.
    If any field is empty, it shows an error message. Otherwise, it asks for confirmation to save the data.
    Upon confirmation, it writes the data to a file named 'data.txt' and clears the website and password input fields.
    """
    website = str(websiteInput.get())
    email = str(emailUsernameInput.get())
    password = str(passwordInput.get())
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: "
                                                      f"{password} \nIs it ok to save?")
        if is_ok == True:
            with open("data.txt", "a") as file:
                file.write(f"{website} || {email} || {password}\n")

            #Clear the input website and password fields
            websiteInput.delete(0, tkinter.END)
            passwordInput.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
#Create the main window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create and place the logo image
canvasLogo = tkinter.Canvas(width=200, height=200)
logoImage = tkinter.PhotoImage(file="logo.png")
canvasLogo.create_image(100, 100, image=logoImage)
canvasLogo.grid(column=1, row=0)

#Create and place the website label
websiteLabel = tkinter.Label(text="Website:")
websiteLabel.grid(column=0, row=1, sticky="E")

#Create and place the website entry field
websiteInput = tkinter.Entry(width=35)
websiteInput.focus()
websiteInput.grid(column=1, row=1, columnspan=2, sticky="EW")

#Create and place the email/username label
emailUsernameLabel = tkinter.Label(text="Email/Username:")
emailUsernameLabel.grid(column=0, row=2, sticky="E")

#Create and place the email/username label
emailUsernameInput = tkinter.Entry(width=35)
emailUsernameInput.insert(0, "riyanmartin@gmail.com")
emailUsernameInput.grid(column=1, row=2, columnspan=2, sticky="EW")

#Create and place the password label
passwordLabel = tkinter.Label(text="Password:")
passwordLabel.grid(column=0, row=3, sticky="E")

#Create and place the password entry field
passwordInput = tkinter.Entry(width=21)
passwordInput.grid(column=1, row=3, padx=(0, 3), sticky="EW")

#Create and place the generate password button
generatePasswordButton = tkinter.Button(text="Generate Password", command=generatePassword)
generatePasswordButton.grid(column=2, row=3, sticky="W")

#Create and place the add button
addButton = tkinter.Button(text="Add", command=save, width=36)
addButton.grid(column=1, row=4, columnspan=2, sticky="EW")

#Start the main event loop
window.mainloop()