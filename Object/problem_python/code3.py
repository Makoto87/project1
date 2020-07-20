# kgやm/sなどの単位の把握に気をつけましょう
class Planet:
    # クラス変数
    constantOfGravitation = 6.67438 * (10 ** (-11))   # 万有引力定数
    speedOfLight = 2.99792458 * (10 ** 8)   # 光速(m/s)
    massOfSun = 1.989 * (10 ** 30)  # 太陽の質量(kg)
    radiusOfSun = 6.96 * (10 ** 5)  # 太陽の半径(km)
    oneYear = 31556926  # 1年間の秒数(sec)

    def __init__(self,name,massKg,meanRadiusKm,distanceToStarLs):
        # インスタンス変数
        self.name = name
        self.massKg = massKg    # 惑星の質量
        self.meanRadiusKm = meanRadiusKm    # 惑星の半径
        self.distanceToStarLs = distanceToStarLs    #惑星から恒星まで光が届くのにかかる時間(s)

    # 惑星の体積を返す関数(単位km)
    def getVolume(self):
        return (4 / 3) * 3.14 * (self.meanRadiusKm ** 3)

    # 惑星の表面積を返す(単位km)
    def getSurfaceArea(self):
        return 4 * 3.14 * (self.meanRadiusKm ** 2)

    # 入力から渡される惑星と比較して、惑星の大きさや小ささを表すスカラ値を返す
    def compareToPlanet(self, planet):
        if self.meanRadiusKm > planet.meanRadiusKm:
            return self.getVolume() - planet.getVolume()
        else:
            return planet.getVolume() - self.getVolume()

    # 惑星の重力を返す(単位：m/s)
    def getSurfaceGravity(self):
        return self.massKg * self.constantOfGravitation / (self.meanRadiusKm * 1000) ** 2

    # 公転半径を返す(単位：km)
    def getDistanceToStarKm(self):
        # 光速 * かかる時間 / 1000(単位をkmにするため)
        return self.speedOfLight * self.distanceToStarLs / 1000

    # 公転速度を返す(単位：m/s)
    def getOrbitalSpeed(self):
        # 円運動をしている物体には中心力が働きます（中心力=惑星の質量*公転速度^2/惑星から恒星までの距離）
        # 惑星の場合、万有引力=中心力になります。中心力=惑星の質量*太陽の質量*万有引力定数/惑星から構成までの距離^2
        # 上記2つを整理すると、公転速度=(太陽の質量*万有引力定数/恒星から惑星までの距離(m))^(1/2)
        return (self.massOfSun * self.constantOfGravitation / (self.getDistanceToStarKm() * 1000)) ** 0.5

    # 公転周期を返します
    def getOrbitalPeriodYear(self):
        # 求め方 -> 2*円周率*恒星から惑星までの距離(m)/公転速度(m/s)
        # 距離(km->m)と公転速度(m/s->m/year)の単位直しをします
        return 2 * 3.14 * (self.getDistanceToStarKm() * 1000) / self.getOrbitalSpeed() / self.oneYear


mercury = Planet("Mercury", 3.302e23, 2.4397e3, 1.931e2)
venus = Planet("Venus",4.869e24, 6.0518e3, 3.602e2)
earth = Planet("Earth", 5.974e24, 6.3782e3, 4.990e2)
mars = Planet("Mars", 6.419e23, 3.3972e3, 7.602e2)
jupiter = Planet("Jupiter", 1.899e27, 7.1492e4, 2.596e3)
saturn = Planet("Saturn", 5.6880e26, 6.0268e4, 4.760e3)
uranus = Planet("Uranus", 8.6830e25, 2.5559e4, 9.57e3)
neptune = Planet("Neptune", 1.0240e26, 2.4786e04, 15e3)

print(earth.getVolume())
print(earth.getSurfaceArea())
print(earth.compareToPlanet(mars))
print(earth.getSurfaceGravity())
print(earth.getDistanceToStarKm())
print(earth.getOrbitalSpeed())
print(earth.getOrbitalPeriodYear())
