from dataclasses import dataclass


@dataclass
class Employer:
    """
    Класс для работы с работодателями
    """
    id: int
    name: str
    url: str
    open_vacancies: int
