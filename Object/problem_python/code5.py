import random
import math

class BankAccount:
      maxWidthdrawRate = 0.2

      def __init__(self,bankName,ownerName,savings,interestPerDay):
            self.bankName = bankName
            self.ownerName = ownerName
            self.savings = savings
            self.interestPerDay = interestPerDay

      # ユーザーの情報を返す
      def showInfo(self):
            return "bank: " + self.bankName + "\nowner name: " + self.ownerName + "\nbank account number: " + str(HelperFunction.getRandomInteger())

      # 貯蓄額を増やす
      def depositMoney(self, depositAmount):
            if self.savings <= 20000:
                  self.savings -= 100
            self.savings += depositAmount
            return self.savings

      # 貯蓄から引きおろす
      def withdrawMoney(self,withdrawAmount):
            if withdrawAmount <= self.savings * self.maxWidthdrawRate:
                  self.savings -= withdrawAmount
            else:
                  self.savings -= self.savings * self.maxWidthdrawRate
            return self.savings

      # 利息をつける
      def pastime(self,days):
            return math.floor(self.savings * (1 + self.interestPerDay) ** days)

class HelperFunction:
      @staticmethod
      # ランダムに整数を取得する関数
      def getRandomInteger():
            return random.randint(1,10**8)

user1 = BankAccount("Chase", "Claire Simmmons", 30000, 0.010001)
        
print(user1.showInfo())
print(user1.depositMoney(1000))
print(user1.withdrawMoney(10000))
print(user1.pastime(200))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000, 0.010001)

print(user2.showInfo())
print(user2.depositMoney(5000))
print(user2.withdrawMoney(12000))
print(user2.pastime(500))