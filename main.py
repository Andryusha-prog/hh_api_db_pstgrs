from db_pack.db_manager import DBManager
from main_func import first_step_function


def main():
    while True:
        input_first_step = input("""Приветствую!!!
        При первом запуске программы необходимо заполнить БД данными:
        Введите любую цифру для заполнения БД данными:
        Для выхода введите цифру 0: \n""")

        if input_first_step.isdigit():
            if int(input_first_step) == 0:
                break
            else:
                first_step_function()

                while True:
                    input_sec_step = input("""Теперь можно работать с выборками данных
                    Выберите нужный пункт:
                    1 - список всех компаний и количество вакансий у каждой компании;
                    2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
                    3 - выводит среднюю зарплату по вакансиям;
                    4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям;
                    5 - писок всех вакансий, в названии которых содержатся переданные в метод слова
                    0 - в предыдущее меню \n""")

                    if int(input_sec_step) == 0:
                        break
                    else:
                        db_man = DBManager('localhost', 'hh_api', 'postgres', 'admin', 5432)
                        try:
                            db_man.connect()
                            if int(input_sec_step) == 1:
                                print(db_man.get_companies_and_vacancies_count())
                            elif int(input_sec_step) == 2:
                                print(db_man.get_all_vacancies())
                            elif int(input_sec_step) == 3:
                                print(db_man.get_avg_salary())
                            elif int(input_sec_step) == 4:
                                print(db_man.get_vacancies_with_higher_salary())
                            elif int(input_sec_step) == 5:
                                input_search_word = input('Введите слово для поиска \n')
                                print(db_man.get_vacancies_with_keyword(input_search_word))
                        finally:
                            db_man.disconnect()
                            #break





        else:
            continue


if __name__ == '__main__':
    main()
