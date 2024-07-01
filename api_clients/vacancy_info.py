from dataclasses import dataclass


@dataclass
class Vacancy:
    """
    класс для работы с вакансиями
    """
    id: int
    employer_id: int
    name: str
    url: str
    area: str
    salary_from: int | None
    salary_to: int | None
