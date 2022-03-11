import instaloader
import requests
import sys

print("Пробую подключиться к Инстаграму... ", end="")

url = "https://instagram.com"
response = requests.get(url)
if response.status_code == 200:
    print("Подключение успешно!\n")
else:
    print("Не удалось подключиться. Проверьте подключение к интернету")
    input("Нажмите ENTER для выхода")
    sys.exit()

il = instaloader.Instaloader()

username = input("Введите имя профиля: ")
password = input("Введите пароль: ")
print("Пробую войти в профиль... ", end="")

try:
    il.login(username, password)
    print("Успешный вход!")
except:
    print("Неверное имя пользователя или пароль!")
    input("Нажмите ENTER для выхода")
    sys.exit()


il.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
il.quiet = True
il.download_geotags = False
il.save_metadata = False
il.save_metadata_json = False
il.download_comments = False
il.post_metadata_txt_pattern = ""

print("\nСкачиваю фото, пожалуйста, подождите...")
il.download_profile(username)

print(f"\n\nГотово! Фотографии профиля сохранены в папку {username}")
input("Нажмите ENTER для выхода")