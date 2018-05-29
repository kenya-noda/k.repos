#簡単な戦闘シミュレーション

import random
from time import sleep
import sys

#クラス、コンストラクタにステータスを設定
class Person:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)

#基本情報の表示
    def info(self):
        print(self.name, "HP:",self.hp, "Attack:",self.attack, "Defense:",self.defense)

#Person classを継承
class Item(Person):
    def __init__(self, name, hp, attack, defense):
        Person.__init__(self, name, hp, attack, defense)

#attackとdefenseにボーナスをつける
    def equip(self, Person):
        Person.attack += self.attack
        Person.defense += self.defense

class Enemy(Person):
    def __init__(self, name, hp, attack, defense):
        Person.__init__(self, name, hp, attack, defense)

#クラス関数の定義（randomでもクラスで一つ）
    drop = random.random()


def battle(Person, Enemy):
#どちらかのhpが0以下になるまで
    while (Person.hp > 0 and Enemy.hp >0):
#攻撃する側のattackからされる側のdefenseを引いた値がダメージになる
        if (Person.attack - Enemy.defense) > 0:
            Enemy.hp -= (Person.attack - Enemy.defense)
        else:
            Enemy.hp -= 1
        print(Person.name, "'s Attack!")
        sleep(1)

        if (Enemy.attack - Person.defense) > 0:
            Person.hp -= (Enemy.attack - Person.defense)
        else:
            Person.hp -= 1
        print(Enemy.name, "'s Attack!")
        sleep(1)
        Person.info()
        Enemy.info()

#whileを抜けた時点で主人公のhpが残っていればenemy.hpは0以下
    if Person.hp > 0:
        print("You Win!")
    
    else:
        print("You Died...")
        sys.exit()

    return


#主人公情報
print("Input Hero's name")
hero = Person(input(">>  "), 30, 15, 15)
hero.info()
sleep(2)
#敵情報
enemy1 = Enemy("Slime", 20, 10, 5)
print("Slime Appears!")
enemy1.info()
sword = Item("Sword", 0, 20*enemy1.drop, 0)

sleep(2)
battle(hero, enemy1)
sword.equip(hero)

#2回戦
hero.info()
sleep(2)

enemy2 = Enemy("Golem", 20, 18, 20)
print("Golem Appears!")
enemy2.info()
shield = Item("Shield", 0, 0, 20*enemy2.drop)

sleep(2)
battle(hero, enemy2)
shield.equip(hero)


#3回戦
hero.info()
sleep(2)

enemy3 = Enemy("Dragon", 30, 30, 25)
print("Dragon Appears!")
enemy3.info()

sleep(2)
battle(hero, enemy3)


#終了
print("Game Cleared!!")
