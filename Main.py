from Logic import Source
from Logic.ImageCreation import create_image
from datetime import datetime

def main():
    time = datetime.now().strftime("%b %d %Y %H,%M")
    created = 0

    print(Source.banner)
    print("Введите название проекта")
    name = str(input("-> "))
    folder_name = f"[{name}] {time}"
    print("Сколько изображений сгенерировать?")
    amount = int(input("-> "))

    for number in range(amount):
        try:
            created = number + 1
            create_image(f"№{str(number)} [{name}]", folder_name)
            print(f"Изображение №{created} [{created}/{amount}] - успешно создано")
        except Exception as ex:
            print(f"Изображение №{created} не было создано, произошла ошибка: {ex}")

if __name__ == "__main__":
    main()