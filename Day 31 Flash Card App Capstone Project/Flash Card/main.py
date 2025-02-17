import tkinter
import pandas
import random


# Import data to list of dictionaries
data = pandas.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"
START_APP = True
word = None
flip = None

def start_app():
    global START_APP
    if START_APP:
        next_card_no()
        START_APP = False

# Random word
def next_card_yes():
    global flip, word
    try:
        window.after_cancel(flip)
    except ValueError:
        pass
    word = random.choice(data)
    know_the_word(word)
    french_word = word["French"]
    # Front card
    cardImage.itemconfig(cardImageCanvas, image=cardFrontImage)
    cardImage.itemconfig(cardImageTitle, text="French", fill="black")
    cardImage.itemconfig(cardImageWord, text=french_word, fill="black")
    flip = window.after(3000, flip_card, word)

def next_card_no():
    global flip, word
    try:
        window.after_cancel(flip)
    except ValueError:
        pass
    word = random.choice(data)
    french_word = word["French"]
    # Front card
    cardImage.itemconfig(cardImageCanvas, image=cardFrontImage)
    cardImage.itemconfig(cardImageTitle, text="French", fill="black")
    cardImage.itemconfig(cardImageWord, text=french_word, fill="black")
    flip = window.after(3000, flip_card, word)

def flip_card(word):
    english_word = word["English"]
    cardImage.itemconfig(cardImageCanvas,  image=cardBackImage)
    cardImage.itemconfig(cardImageTitle, text="English", fill="white")
    cardImage.itemconfig(cardImageWord, text=english_word, fill="white")

def know_the_word(word):
    new_know_word = word
    try:
        know_word = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        know_word = pandas.DataFrame([new_know_word])
        know_word.to_csv("data/words_to_learn.csv", index=False)
    else:
        new_know_word_save = pandas.DataFrame([new_know_word])
        know_word = pandas.concat([know_word, new_know_word_save], ignore_index=True)
        know_word.to_csv("data/words_to_learn.csv", index=False)

        # Removing list from CSV
        _data = data
        index_word = _data.index(new_know_word)
        _data.remove(_data[index_word])
        _data = pandas.DataFrame(_data)
        _data.to_csv("data/french_words.csv", index=False)


# Create a window
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create a canvas for Card
cardImage = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFrontImage = tkinter.PhotoImage(file="images/card_front.png")
cardBackImage = tkinter.PhotoImage(file="images/card_back.png")
cardImageCanvas = cardImage.create_image(400, 263, anchor="center", image=cardFrontImage)
cardImageTitle = cardImage.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
cardImageWord = cardImage.create_text(400, 263, text="Word" , font=("Ariel", 60, "bold"))
cardImage.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create a wrong button
wrongImage = tkinter.PhotoImage(file="images/wrong.png")
wrongButton = tkinter.Button(image=wrongImage, highlightthickness=0, command=next_card_yes)
wrongButton.grid(row=1, column=0)

# Create a right button
rightImage = tkinter.PhotoImage(file="images/right.png")
rightButton = tkinter.Button(image=rightImage, highlightthickness=0, command=next_card_no)
rightButton.grid(row=1, column=1)

start_app()
window.mainloop()