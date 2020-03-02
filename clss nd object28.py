class Enemy:
    life = 3

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("i am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy(5)

enemy1.attack()
enemy1.checklife()
enemy1.get_energy()
