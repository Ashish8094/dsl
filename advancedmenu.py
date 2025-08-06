content = ""
undostack = []
redostack = []
undohistory = []
redohistory = []

def makechange(newtext):
    global content
    undostack.append(content)
    content = newtext
    redostack.clear()
    redohistory.clear()
    print("Change made.")

def undo():
    global content
    if undostack:
        redostack.append(content)
        undohistory.append(content)
        content = undostack.pop()
        print("Undo performed.")
    else:
        print("Nothing to undo.")

def redo():
    global content
    if redostack:
        undostack.append(content)
        redohistory.append(content)
        content = redostack.pop()
        print("Redo performed.")
    else:
        print("Nothing to redo.")

def display():
    print("Current Content: " + content)

def show_undo_history():
    if undohistory:
        print("Undo History:")
        for item in reversed(undohistory):
            print("- " + item)
    else:
        print("Undo History is empty.")

def show_redo_history():
    if redohistory:
        print("Redo History:")
        for item in reversed(redohistory):
            print("- " + item)
    else:
        print("Redo History is empty.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Make Change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display Content")
        print("5. Show Undo History")
        print("6. Show Redo History")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            text = input("Enter new text: ")
            makechange(text)
        elif choice == "2":
            undo()
        elif choice == "3":
            redo()
        elif choice == "4":
            display()
        elif choice == "5":
            show_undo_history()
        elif choice == "6":
            show_redo_history()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

menu()
