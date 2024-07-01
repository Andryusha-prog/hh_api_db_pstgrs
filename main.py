from prettytable import PrettyTable

from api_clients.hh_client import HHAPIClient
from db_pack.config import config
from db_pack.db_create import create_databases, create_schema, save_emp_to_database, save_vac_to_database
from db_pack.db_manager import DBManager


def main():
    '''#list_company = ['', 'альфа', 'VK', 'яндекс', 'мегафон', 'точка', '', 'газпром', 'мтс', 'авито']
    list_company = ['ixora', 'альфа', 'VK', 'Хекслет', 'мегафон', 'точка', 'skypro', 'додо', 'мтс', 'авито']
    hh_client = HHAPIClient()
    for company in list_company:
        employers = hh_client.search_employers(company)
        table = PrettyTable(field_names=['ID', 'Название компании', 'Ссылка', 'Кол-во вакансий'])
        table.sortby = 'Кол-во вакансий'
        table.reversesort = True
        for emp in employers:
            table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])


        print(table)

        #vacancies = hh_client.search_vacancies(78638)
'''
    '''table = PrettyTable(field_names=['ID', 'Название компании', 'Ссылка', 'Кол-во вакансий'])
    table.sortby = 'Кол-во вакансий'
    table.reversesort = True
    for emp in employers:
        table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])

    print(table)

    vacancies = hh_client.search_vacancies(78638)
    #for vac in vacancies:
     #   print(vac)
    print(len(vacancies))
'''

    db_man = DBManager('localhost', 'hh_api', 'postgres', 'admin', 5432)
    try:
        db_man.connect()
        resul = db_man.get_companies_and_vacancies_count()
        res2 = db_man.get_all_vacancies()
        res3 = db_man.get_avg_salary()
        res4 = db_man.get_vacancies_with_higher_salary()
        res5 = db_man.get_vacancies_with_keyword('python')
        print('1111111')
        print(resul)
        print(res2)
        print('avg_sal', res3)
        print(res4)
        print(res5)
    finally:
        db_man.disconnect()

    '''params = config()

    create_databases('hh_api', params)
    create_schema('hh_api', params)

    list_company = ['ixora', 'позитив', 'VK', 'Хекслет', 'софтлайн', 'точка', 'skypro', 'додо', 'айтеко', 'авито']
    hh_client = HHAPIClient()
    for company in list_company:
        employers = hh_client.search_employers(company)
        max_zn = max([emp.open_vacancies for emp in employers])
        for emp in employers:
            if emp.open_vacancies == max_zn:
                save_emp_to_database(emp, 'hh_api', params)
                print(emp)
                vacancies = hh_client.search_vacancies(emp.id)
                save_vac_to_database(vacancies, 'hh_api', params)
                break
                '''




if __name__ == '__main__':
    main()
