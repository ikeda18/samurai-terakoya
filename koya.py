#学習したことを組み合わせてコードを書こう
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
           print(f"{self.name}さんは大人です")
        else:
           print(f"{self.name}さんは大人ではありません")

humans = [Human("田中", 25),Human("吉田", 15),Human("佐藤", 22) ]

for human in humans:
    human.check_adult()
