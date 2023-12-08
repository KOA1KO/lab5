import requests


def get_deaths(date):
    try:
        url = f"https://api.covidtracking.com/v1/us/{date}.json"
        response = requests.get(url)
        data = response.json()
        deaths = data.get("death")
        negative = data.get("negative")
        positive = data.get("positive")
        return deaths, negative, positive
    except:
        print("Ошибка при получении данных")
        return None


date = input('Чтобы узнать данные о COVID-19 введите дату '
             'в формате "YYYY.MM.DD" с 2020.01.13 по 2021.03.07: ')
right_date = date.replace('.', '')

deaths, negative, positive = get_deaths(right_date)

if __name__ == '__main__':
    print(f"""
    Положение на {date}, начиная с 5 апреля 2020 года 
    Общее количество смертельных случаев: {deaths}
    Общее количество отрицательных ПЦР: {negative}
    Общее количество положительных ПЦР: {positive}

     """)
