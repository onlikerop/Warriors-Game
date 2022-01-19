gl_number_of_warriors = 0


class Warrior:
    id = int()
    hp = int()
    damage = 20
    name = str()
    status = 1

    def __init__(self, name):
        global gl_number_of_warriors
        gl_number_of_warriors += 1
        self.id = gl_number_of_warriors
        self.hp = 100
        self.set_name(name)

    def set_name(self, name):
        self.name = str(name)

    def attack(self, whom):
        if self.get_status():
            whom.get_damage(self)

    def get_damage(self, attacker):
        if self.hp - attacker.damage <= 0:
            self.hp = 0
            print("Воин " + attacker.name + " атаковал воина " + self.name + " и нанёс ему " + str(
                attacker.damage) + " урона.\nУ воина " + self.name + " осталось " + str(self.hp) + " очков здоровья")
            print("Воин " + self.name + " пал от рук " + attacker.name)
            self.status = 0
        else:
            self.hp -= attacker.damage
            print("Воин " + attacker.name + " атаковал воина " + self.name + " и нанёс ему " + str(
                attacker.damage) + " урона.\nУ воина " + self.name + " осталось " + str(self.hp) + " очков здоровья")

    def get_status(self) -> int:
        return self.status


warr1 = Warrior("The Metal Guardian")
warr2 = Warrior("Dark Pigeon")

while warr1.get_status() and warr2.get_status():
    warr1.attack(warr2)
    warr2.attack(warr1)

print("Бой окончен!\nПобедил воин " + warr1.name if warr1.get_status() else warr2.name)
