from random import randint

class Dice:
    """
    The class represents playing dice.
    """

    def __init__(self, side_num = 6):
        self.__side_num = side_num

    def __str__(self):
        """
        The __str__ method returns text based message of dice object.
        """
        return str(f"This is the playing dice with {self.__side_num} sides.)

    def __repr__(self):
        """
        The __repl__ method returns code of contructor (as string) for fucntion eval().
        """
        return str(f"This is the playing dice with {self.__side_num} sides.)

    def ret_side_num(self):
        """
        The method returns private attribute number of dice sides.
        """
        return self.__side_num

    def cast(self):
        """
        The method
        """
        return randint(1,self.__side_num)

class Fighter:
    """
    The class represents the fighter in the arena.
    """

    def __init__(self, name, hp, attack, defence, dice):
        """
        name - fighter's name
        hp - the starting fighter's hp
        attack - fighter's attack
        defence - fighter's defence
        dice - dice instance
        """
        self.__name = name
        self.__current_hp = hp
        self.__max_hp = hp
        self.__attack = attack
        self.__defence = defence
        self.__dice = dice

    def __str__(self):
        """
        The __str__ method returns text based message of fighter's name.
        """
        return str(f"The fighter {self.__name}")

    @ property
    def is_alive(self):
        return True if self.__current_hp else False





sex_side_dice = Dice()
print(sex_side_dice.ret_side_num())
print(sex_side_dice.cast())
print(sex_side_dice)