
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, __model: str,  __color: str, __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power


    def get_model(self):
        pass

    def get_horsepower(self):
        pass

    def get_color(self):
        pass



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, *args):
        super().__init__(self)



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

print(vehicle1)

