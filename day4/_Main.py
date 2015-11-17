#coding:utf-8

import sys,time

class MyBasic:

    def __init__(self,name,age,job,salary,race,nation,gender,specialty):

        self.name = name
        self.age = age
        self.job = job
        self.salary = salary
        self.race = race
        self.nation = nation
        self.gender = gender
        self.specialty = specialty

    def __del__(self):
        print('Game over')
    def __call__(self):
        return('This is my basic class')

class Liz(MyBasic):
    def __init__(self):
        super(Liz,self).__init__('Liz',18,'IT',100,'Yellow Race','China','M','1')
    def __str__(self):
        return('Bad Gril')
    def __del__(self):
        print('Liz is Game over')
class Peter(MyBasic):
    pass
class JohnBerry(MyBasic):
    pass


if __name__ == '__main__':
    _Liz=Liz()
    print(_Liz())
    print(_Liz)