def main():
    filename = "mytext.txt"

    while True:
        print("Выберите действие:")
        print("1. Записать текст в файл")
        print("2. Прочитать текст из файла")
        print("3. Очистить содержимое файла")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            text = input("Введите текст для записи: ")
            with open(filename, "a") as f:  
                f.write(text + " ")  
            print("Текст записан в файл.")

        elif choice == '2':
            try:
                with open(filename, "r") as f:  
                    content = f.read()
                    print("Содержимое файла:", content)
            except FileNotFoundError:
                print("Файл не найден.")

        elif choice == '3':
            with open(filename, "w") as f:  
                pass  
            print("Содержимое файла очищено.")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()