import json

def load_new_phone_book(list):
    user_name = input("Give me the name: ")
    user_number = input("Give me the number: ")

    try:
        user_number = int(user_number)
    except ValueError:
        print("Phone number cannot have letters, please try again: ")
    else:
        phone_book = {'imie': user_name, 'numer':  user_number}
        list.append(phone_book)

def load_phone_book():
    try:
        with open("book_number.json", encoding="UTF-8") as f:
            numbers_list = json.load(f)
            number_of_phone_books = len(numbers_list)
            print(f"The current number of phone books is {number_of_phone_books}")
            return numbers_list
    except (FileExistsError, FileNotFoundError):
        return []
    
# ---- main code -------------------------------------------------------------

if __name__ == '__main__':
    numbers_list = load_phone_book()
    while True:
        user_answer = input("Do you want to add a new phone number to phone book? If yes - write 't', if not - write 'n': ")
        if user_answer == "t":
            load_new_phone_book(numbers_list)
        elif user_answer == "n":
            break
        else:
            continue

    with open ("book_number.json", "w", encoding="UTF-8") as f:
        json.dump(numbers_list, f, ensure_ascii=False)






