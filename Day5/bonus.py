waiting_list = ["and", "or", "xor"]

waiting_list.sort(reverse=True)

for i, item in enumerate(waiting_list):
    row = f"{i + 1}.{item.capitalize()}"
    print(row)