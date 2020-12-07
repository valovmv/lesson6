class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начинает джижение'
    def stop(self):
        return f'{self.name} останавливается'
    def turn_right(self):
        return f'{self.name} поворачивает направо'
    def turn_left(self):
        return f'{self.name} поворачивает налево'
    def show_speed(self):
        return f'Текущая скорость {self.name} {self.speed} км/ч'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name} {self.speed} км/ч - превышение скорости'
        else:
            return f'Скорость {self.name} {self.speed} км/ч - движение по правилам'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name} {self.speed} км/ч - превышение скорости'
        else:
            return f'Скорость {self.name} {self.speed} км/ч - движение по правилам'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



leo_car = TownCar(70, 'Белый', 'Городской автомобиль', False)
curt_car = SportCar(150, 'Желтый', 'Спортивный автомобиль', False)
dora_car = WorkCar(50, 'Черный', 'Служебный автомобиль', False)
sam_car = PoliceCar(80, 'Бело-синий',  'Полиция', True)
print(leo_car.turn_left())
print(f'Когда {leo_car.turn_right()}, {curt_car.stop()}')
print(f'{dora_car.go()} со скоростью {dora_car.show_speed()}')
print(f'{dora_car.name} is {dora_car.color}')
print(f'{curt_car.name} это Полиция? {curt_car.is_police}')
print(f'{dora_car.name} это Полиция? {dora_car.is_police}')
print(curt_car.show_speed())
print(leo_car.show_speed())
print(sam_car.show_speed())