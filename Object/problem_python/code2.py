# getAgeをjsのコードと違う方法で書いています。jsでは今の年-誕生年で完結していますが、pythonでは今の月が誕生月を超えていない場合の処理も加えて書いています。

# ライブラリの取得
import datetime

class User:
    def __init__(self,username,firstName,lastName,email,passwordHashed,birthMonth,birthYear,biographyDescription,favoriteHikingLocation):
        # インスタンス変数
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwordHashed = HelperFunction.hashPassword(passwordHashed)
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.biographyDescription = biographyDescription
        self.favoriteHikingLocation = favoriteHikingLocation

    # 名前をフルネームで返す関数
    def getFullName(self):
        return self.firstName + " " + self.lastName

    # 年齢を返す関数
    def getAge(self):
        date = datetime.datetime.now()
        age = date.year - self.birthYear
        # まだ誕生月になっていなかったら年齢を1引く
        if self.birthMonth > date.month:
            return age - 1
        else:
            return age

    # 誕生月まで何ヶ月あるか計算する
    def birthdayCalculator(self):
        dateMonth = datetime.datetime.now().month
        if self.birthMonth > dateMonth:
            return self.birthMonth - dateMonth
        else:
            return 12 - (dateMonth - self.birthMonth)

    # ユーザーのプロフィールを返す
    def showProfile(self):
        return self.username + "\n" + str(self.getAge()) + " year old\n" + self.biographyDescription + "\nfavorite place to hike: " + self.favoriteHikingLocation

    # 指定したpasswordStringが保存したpasswordHashedと一致しているか確認
    def confirmPassword(self, passwordString):
        if self.passwordHashed == HelperFunction.hashPassword(passwordString):
            return True
        else:
            return False

class HelperFunction:
      # staticメソッドはインスタンス無しでも使うことができるという意味です。
      # 状態を持たないので名前空間として使用することができます。
      @staticmethod
      # ハッシュ関数
      def hashPassword(s):
            hash = 5381
            for x in s:
                  hash = (( hash << 5) + hash) + ord(x)
            return str(hash & 0xFFFFFFFF)



claireS = User("claireS", "Claire", "Simmmons", "clairesimmons@gmail.com", "lmnlmn", 9, 2007, "Passionate gamer. Evil internet aficionado. Student. Friendly tv specialist. Introvert.", "Hollywood Sign Hike")

print(claireS.getFullName())
print(claireS.getAge())
print(claireS.birthdayCalculator())
print(claireS.showProfile())
print(claireS.confirmPassword("lmnlmn"))