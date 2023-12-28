class Buckets:
    temp = None
    child = []
    parent = None

    def __init__(self, bucket, parent):
        self.temp = bucket
        self.parent = parent

    def v8Tov5(self):
        if self.temp[1] == 5:
            return False

        else:
            self.temp[1] += (5 - self.temp[1])
            self.temp[0] -= (5 - self.temp[1])
            return self.temp

    def v8Tov3(self):
        if self.temp[2] == 3:
            return False

        else:
            self.temp[2] += (3 - self.temp[2])
            self.temp[0] -= (3 - self.temp[2])
            return self.temp

    def v5Tov8(self):
        if self.temp[0] == 8:
            return False

        else:
            self.temp[0] += self.temp[1]
            self.temp[1] = 0
            return self.temp

    def v5Tov3(self):
        if self.temp[2] == 3:
            return False

        else:
            self.temp[2] += (3 - self.temp[2])
            self.temp[1] -= (3 - self.temp[2])
            return self.temp

    def v3Tov8(self):
        if self.temp[0] == 8:
            return False

        else:
            self.temp[0] += self.temp[2]
            self.temp[2] = 0
            return self.temp

    def v3Tov5(self):
        if self.temp[1] == 5:
            return False

        else:
            self.temp[1] += (5 - self.temp[1])
            self.temp[2] -= (5 - self.temp[1])
            return self.temp

    def addChild(self, children):
        self.child = children

    def copy(self, temp):
        return temp


initial = Buckets([8, 0, 0], None)
temp = initial
stack = []



