class Enemy:
    # type_of_enemy: str
    # health: int
    # attack_power: int

    def __init__(self, type_of_enemy, health=100, attack_power=10):
        self.__type_of_enemy = type_of_enemy
        self.__health = health
        self.__attack_power = attack_power

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def set_type_of_enemy(self, type_of_enemy):
        self.__type_of_enemy = type_of_enemy
    
    def get_health(self):
        return self.__health
    def set_health(self, health):
        self.__health = health


    def get_attack_power(self):
        return self.__attack_power
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    
    

    def talk(self):
        print(f"Grrr... I am an enemy of type {self.__type_of_enemy}!")