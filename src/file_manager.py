import json
import os
from src.hhru import FileManager as FileManagerABC
from src.vacancies_hh import Vacancies
from typing import List

class JsonFile(FileManagerABC):
    def __init__(self, filename: str = "data.json"):
        self.__filename = filename

    def add_vacancy(self, vacancy: Vacancies):
        vacancies = []
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                try:
                    vacancies = json.load(file)
                except json.JSONDecodeError:
                    vacancies = []
        except FileNotFoundError:
            vacancies = []

        vacancies.append({
            'name': vacancy.name,
            'url': vacancy.url,
            'payment': vacancy.payment,
            'description': vacancy.description
        })

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, indent=4)

    def get_vacancy(self) -> List[Vacancies]:
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        vacancies_list = []
        for item in data:
            vacancies_list.append(Vacancies(
                item['name'],
                item['url'],
                item['payment'],
                item['description']
            ))
        return vacancies_list

    def delete_vacancy(self, vacancy: Vacancies):
        try:
            with open(self.__filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data = [v for v in data if not (v['name'] == vacancy.name and v['url'] == vacancy.url)]

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
