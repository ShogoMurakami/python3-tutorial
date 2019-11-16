# coding: utf-8

class Ninja:
    def run(self):
        print("Narutoは走る")
    def attack(self, enemy):
        print("Narutoは" + enemy + "を攻撃した")

ninja1 = Ninja()

ninja1.run()
ninja1.attack("大蛇丸")
