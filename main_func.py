from api_clients.hh_client import HHAPIClient
from db_pack.config import config
from db_pack.db_create import create_databases, create_schema, save_emp_to_database, save_vac_to_database


def first_step_function():
    params = config()

    create_databases('hh_api', params)
    create_schema('hh_api', params)

    list_company = ['ixora', 'позитив', 'VK', 'Хекслет', 'софтлайн', 'точка', 'skypro', 'додо', 'айтеко',
                    'авито']

    hh_client = HHAPIClient()

    for company in list_company:
        employers = hh_client.search_employers(company)
        #выбирается только тот id компании, у которого больше всего вакансий
        max_zn = max([emp.open_vacancies for emp in employers])
        for emp in employers:
            if emp.open_vacancies == max_zn:
                #сохраняется информация о работодателе
                save_emp_to_database(emp, 'hh_api', params)
                print(emp)
                #сохраняются вакансии текущего работодателя
                vacancies = hh_client.search_vacancies(emp.id)
                save_vac_to_database(vacancies, 'hh_api', params)
                break
