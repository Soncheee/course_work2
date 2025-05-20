class Vacancies:
    __slots__ = ("__name", "__url", "payment", "description")

    def __init__(self, name: str, url: str, payment: float, description: str):
        self.__name = name
        self.__url = url
        self.payment = self.__validate(payment)
        self.description = description

    @staticmethod
    def __validate(payment: float) -> float:
        return payment if payment is not None else 0

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    def main_data(self):
        return {
            'name': self.__name,
            'url': self.__url,
            'payment': self.payment,
            'description': self.description
        }

    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.payment < other.payment

    def __gt__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.payment > other.payment

    def __eq__(self, other):
        if not isinstance(other, Vacancies):
            return NotImplemented
        return (
            self.payment == other.payment and
            self.name == other.name and
            self.url == other.url and
            self.description == other.description
        )

    def __repr__(self):
        return f"Vacancies(name={self.name}, url={self.url}, payment={self.payment})"