user_prompt = "Enter a todo: "

todos = []
try:
    while True:
        todo = input(user_prompt)
        todos.append(todo.title())
        print(todos)
except KeyboardInterrupt:
    print("Finished")