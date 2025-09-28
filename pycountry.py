import turtle
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pycountry  # pip install pycountry

# функция для показа флага
def show_flag(country_code):
    url = f"https://flagcdn.com/w320/{country_code.lower()}.png"
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))

        screen = turtle.Screen()
        screen.title(f"Флаг {country_code.upper()}")
        screen.bgcolor("#303030")
        screen.setup(width=img.width + 50, height=img.height + 50)

        flag_img = ImageTk.PhotoImage(img)
        canvas = turtle.getcanvas()
        canvas.img = flag_img  # сохраняем ссылку
        canvas.create_image(0, 0, anchor='nw', image=flag_img)

        turtle.done()
    except requests.RequestException:
        print(f"Не удалось загрузить флаг для страны {country_code.upper()}")

# --- интерактивный выбор ---
screen = turtle.Screen()
screen.title("Флаги мира")

# получаем список всех стран через pycountry
country_list = {country.alpha_2.lower(): country.name for country in pycountry.countries}

# формируем текст для подсказки (первые 20 стран, чтобы не перегружать)
sample_list = "\n".join([f"{code.upper()}: {name}" for code, name in list(country_list.items())[:20]])
country_code = screen.textinput("Выбор страны", f"Введите код страны (например, US, KG, FR):\nПримеры:\n{sample_list}")

if country_code and country_code.lower() in country_list:
    show_flag(country_code.lower())
else:
    print("Страна не найдена!")

