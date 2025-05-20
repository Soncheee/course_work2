from hh_api import HH_API
from file_manager import JsonFile
from vacancies_hh import Vacancies


def user_interaction():
    """Основная программа где происходят почти все действия с классами и функциями"""
    hh_api = HH_API()
    file_worker = JsonFile('data/vacancies.json')

    keyword = input("Введите поисковый запрос для вакансий: ")

    vacancies_data = hh_api.load_vacancies(keyword)

    vacancies_list = []
    for data in vacancies_data:
        salary_info = data.get('salary')

        salary_from = salary_info.get('from') if salary_info and salary_info.get('from') else 0

        description_snippet = ''

        snippet_data = data.get('snippet')

        if snippet_data and snippet_data.get('requirement'):
            description_snippet = snippet_data.get('requirement')

        vacancy_obj = Vacancies(
            name=data.get('name'),
            url=data.get('alternate_url'),
            payment=salary_from,
            description=description_snippet
        )

        file_worker.add_vacancy(vacancy_obj)

        vacancies_list.append(vacancy_obj)

    n_top_strs = int(input("Введите количество топ вакансий по зарплате: "))

    top_vacancies = sorted(vacancies_list, key=lambda v: v.payment, reverse=True)[:n_top_strs]

    print("\nТоп вакансий по зарплате:")
    for vac in top_vacancies:
        print(f"Title: {vac.name}, Salary: {vac.payment}, URL: {vac.url}")

    keyword_in_description = input("Введите ключевое слово для поиска в описании: ")

    filtered_by_desc = [v for v in vacancies_list if v.description and keyword_in_description in v.description]

    print(f"\nВакансии с ключевым словом '{keyword_in_description}':")

    for v in filtered_by_desc:
        print(f"Title: {v.name}, Description: {v.description}, URL: {v.url}")


if __name__ == "__main__":
    user_interaction()