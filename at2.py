def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

user_input = input("Введите строку для проверки: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")