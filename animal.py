class Animal:
    def __init__(self, name, color, legs=2, tail=True, ears=2, eyes=2):
        self.__name = name
        self.__color = color
        self.__legs = legs
        self.__tail = tail
        self.__ears = ears
        self.__eyes = eyes

    def talk(self):
        print(f"{self.__name} says Hello!")


class Cat(Animal):
    def __init__(self, name, color, legs=4, tail=True, ears=2, eyes=2):
        super().__init__(name, color, legs, tail, ears, eyes)

    def talk(self):
        print(f"{self.__name} says Meow!")
