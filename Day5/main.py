todos = []
try:
    while True:
        user_act = input("Type add, show, edit, complete or exit: ").strip()
        match user_act:
            case "add":
                todo = input("Enter a todo: ")
                todos.append(todo)
            case "show" | "display":
                for index, item in enumerate(todos):
                    print(f"{index + 1}-{item}")
            case "edit":
                number = int(input("Number of the todo to edit: "))
                todos[number - 1] = input("Enter a new item: ")
            case "complete":
                number = int(input("Number of the todo to complete: "))
                todos.pop(number - 1)
            case "exit":
                break
            case _:
                print("Not match")
 
except KeyboardInterrupt:
    print("Finished")


