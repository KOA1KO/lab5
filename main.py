import requests

print(requests.get("https://vk.com/feed"))

TOKEN = '3e07177a15fb85ca66b09ddfddfb9250'
city_name = input('Введите название города:')


def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'

    try:
        response = requests.get(url).json()

        weather = f'''
            Температура: {response["main"]["temp"]} °C
            Ощущается как: {response["main"]["feels_like"]} °C
            Влажность: {response["main"]["humidity"]} %
            Давление: {response["main"]["pressure"]} мм рт.ст.
        
            В целом - {response["weather"][0]["description"]}
            '''

        print(weather)

    except:

        print('\nК сожалению, такого города нет.')


if __name__ == '__main__':
    get_weather(TOKEN, city_name)
