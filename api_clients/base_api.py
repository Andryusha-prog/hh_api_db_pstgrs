from abc import ABC, abstractmethod

import requests


class APIClient(ABC):
    @property
    @abstractmethod
    def base_url(self) -> str:
        """
        Абстрактный метод для определения базового адреса
        :return:
        """
        pass

    def get(self, url: str, params: dict) -> dict:
        """
        метод получения данных в виде json файла с указанного адреса
        :param url:
        :param params:
        :return:
        """
        full_url = self.base_url + url

        response = requests.get(full_url, params=params, timeout=3)
        response.raise_for_status()
        return response.json()
