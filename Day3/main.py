todos = []
try:
    while True:
        user_act = input("Type add, show or exit: ").strip()
        match user_act:
            case "add":
                todo = input("Enter a todo: ")
                todos.append(todo)
            case "show" | "display":
                for item in todos:
                    print(item.title())
            case "exit":
                break
            case _:
                print("Not match")

except KeyboardInterrupt:
    print("Finished")