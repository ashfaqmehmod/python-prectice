with open("notes.txt", "w") as file:
    file.write("This is my program file part 2.\n")
    notes = file.read()
    print(notes)

with open("notes.txt", "w") as file:
        notes = file.read()
    