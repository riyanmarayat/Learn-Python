#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Input/Letters/starting_letter.txt", mode='r') as starting_file:
    starting_letter = starting_file.read()
with open("Input/Names/invited_names.txt", mode='r') as names_file:
    temp_names = names_file.readlines()
    names = []
    for name in temp_names :
        names.append(name.split("\n")[0])
for name in names:
    file_name = f"letter_for_{name}"
    with open(f"Output/ReadyToSend/{file_name}.txt", mode='w') as letter_file:
        letter_file.write(starting_letter.replace("[name]", name))

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp