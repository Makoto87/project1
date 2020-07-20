class Animal:
    # クラス変数。どれほど動物が活発的か表す数字
    activityMultiplier = 1.2

    def __init__ (self, name, species, description, weightKg, heightM, isPredator, speedKph, urlPic, registerDate):
        # インスタンス変数
        self.name = name
        self.species = species
        self.description = description
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
        self.urlPic = urlPic
        self.registerDate = registerDate

    # 動物の情報を返す関数
    def getStateString(self):
        # isPredatorによって返す言葉を変える
        predatorInfo = "Not Predator"
        if self.isPredator == True:
            predatorInfo = "Predetor"

        return "name: " + self.name + "\nspecies: " + self.species + "\ndescription: " + self.description + "\nweightKg: " + str(self.weightKg) + "kg" + "\nheightM: " + str(self.heightM) + "m\n" + predatorInfo + "\nspeedKph: " + str(self.speedKph) + "kph" + "\nurlPic: " + self.urlPic + "\n" + self.registerDate

    # BMIを計算して返す変数
    def getBmi(self):
        return self.weightKg / (self.heightM ** 2)

    # 消費する必要があるカロリーを計算し、返す関数
    def getDailyCalories(self):
        return 70 * (self.weightKg ** 0.75) * self.activityMultiplier

    # 動物か危険か判断し、返す関数
    def isDangerous(self):
        if self.isPredator == True or self.heightM >= 1.7 or self.speedKph >= 35:
            return True
        else:
            return False

    # 他の動物オブジェクトが与えられ、どちらが速いか判断する関数
    def isFaster(self, animal):
        if self.speedKph > animal.speedKph:
            return True
        else:
            return False

rabbit = Animal("rabbit", "leporidae", "Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika).", 10, 0.3, False, 20, "img1", "2020/04/03")
elephant = Animal("elephant", "Elephantidae", "Elephants are mammals of the family Elephantidae and the largest existing land animals.", 300, 3, False, 5, "img2", "2020/5/26")

# rabbitの情報
print(rabbit.getStateString())
print(rabbit.getBmi())
print(rabbit.getDailyCalories())
print(rabbit.isDangerous())
print("\n")
# elephantの情報
print(elephant.getStateString())
print(elephant.getBmi())
print(elephant.getDailyCalories())
print(elephant.isDangerous())

# rabbitがelephtantより速いか調べる
print(rabbit.isFaster(elephant))