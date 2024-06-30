from prettytable import PrettyTable

from api_clients.hh_client import HHAPIClient


def main():
    list_company = ['сбер', 'альфа', 'VK']
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

if __name__ == '__main__':
    main()
