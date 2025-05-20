from abc import ABC, abstractmethod
from typing import List

class HH_API_ABC(ABC):

    @abstractmethod
    def __connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str):
        pass

class FileManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self) -> List:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
