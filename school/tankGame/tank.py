class Tank(object):
    def __init__(self,name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def str(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        if self.ammo>=1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
            return
        else:
            return "insufficient ammo"

    def hit(self):
        self.armor -= 20
        print(self.name, "is hit!")
        if self.armor < 0:
            self.explode()

    def explode(self):
        self.alive = False
        return self.name, "explodes!"