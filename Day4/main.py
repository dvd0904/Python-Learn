todos = []
try:
    while True:
        user_act = input("Type add, show, edit or exit: ").strip()
        match user_act:
            case "add":
                todo = input("Enter a todo: ")
                todos.append(todo)
            case "show" | "display":
                for item in todos:
                    print(item.title())
            case "edit":
                number = int(input("Number of the todo to edit: "))
                todos[number - 1] = input("Enter a new item: ")
            case "exit":
                break
            case _:
                print("Not match")

except KeyboardInterrupt:
    print("Finished")