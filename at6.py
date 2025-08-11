def analyze_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
        return line_count, word_count
    except FileNotFoundError:
        return "Файл не найден!"

filename = input("Введите имя файла: ")
result = analyze_file(filename)
if isinstance(result, tuple):
    print(f"Количество строк: {result[0]}")
    print(f"Количество слов: {result[1]}")
else:
    print(result)