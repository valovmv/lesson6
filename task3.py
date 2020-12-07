class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())


good_worker = Position('Leo', 'Goodman', 'Best man', 135000, 15000)
print(good_worker._income)
print(good_worker.get_full_name())
print(f'Total income: {good_worker.get_total_income()}')
print(good_worker.position)