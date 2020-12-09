import random

class Character:
        def __init__(self, name, **kwargs):
            self.name = name
            for key, value in kwargs.items():
                setattr(self, key, value)

class Thief(Character):
    sneaky = True

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickPocket(self):
        if self.sneaky:
            return self.sneaky and bool(random.randint(0, 1))
        else:
            return False

    def hide(self, lightLevel):
        return self.sneaky and lightLevel < 10

Marcus = Thief('Marcus', scar = None, favoriteWeapon = 'shortgun')
print(Marcus.pickPocket())
print(Marcus.hide(8))
print(f'{Marcus.favoriteWeapon}')