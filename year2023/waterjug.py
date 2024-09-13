class Buckets:
    temp = None
    child = []
    parent = None

    def __init__(self, bucket, parent):
        self.temp = bucket
        self.parent = parent

    def addChild(self, children):
        self.child.append(children)

    def output(self):
        print(self)
        print(self.child)

    def __str__(self):
        return str(self.temp)


def v8Tov5(temp):
    if temp[1] == 5:
        return False
    else:
        a = (5 - temp[1])
        temp[1] += a
        temp[0] -= a
        return temp


def v8Tov3(temp):
    if temp[2] == 3 or temp[0] == 0:
        return False

    else:
        temp[0] -= (3 - temp[2])
        temp[2] += (3 - temp[2])
        return temp


def v5Tov8(temp):
    if temp[0] == 8 or temp[0] == 0:
        return False

    else:
        temp[0] += temp[1]
        temp[1] = 0
        return temp


def v5Tov3(temp):
    if temp[2] == 3 or temp[1] == 0:
        return False

    else:
        temp[1] -= (3 - temp[2])
        temp[2] += (3 - temp[2])
        return temp


def v3Tov8(temp):
    if temp[0] == 8 or temp[2] == 0:
        return False

    else:
        temp[0] += temp[2]
        temp[2] = 0
        return temp


def v3Tov5(temp):
    if temp[1] == 5 or temp[2] == 0:
        return False

    else:
        temp[1] += (5 - temp[1])
        temp[2] -= (5 - temp[1])
        return temp


