import requests
from hhru import HH_API_ABC


class HH_API(HH_API_ABC):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def __connect(self):
        try:
            response = requests.get(self.__url, headers=self.headers)
            response.raise_for_status()
            print("Successfully connected to the API.")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to connect to the API: {e}")
            return False

    def load_vacancies(self, keyword: str):

        self.params['text'] = keyword
        self.params['page'] = 0

        all_vacancies = []

        while True:
            if self.params['page'] >= 20:
                break

            response = requests.get(self.__url, headers=self.headers, params=self.params)

            if response.status_code != 200:
                print(f"Ошибка при получении данных: {response.status_code}")
                break

            data = response.json()

            items = data.get('items', [])

            if not items:
                break

            all_vacancies.extend(items)

            self.params['page'] += 1

        return all_vacancies
