# class Rectangle():
#     def __init__(self,w,h):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
# class Square(Rectangle):
#     def __init__(self,s):
#         super(Square,self).__init__(s,s)
#         self.s = s
#
# s = Square(4)
# print(s.area())
# ...............................................................................
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;MONKEY PATCHING;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# class A:
#     def __init__(self,num):
#         self.num = num

#
#     def add(self,num2):
#         print(self.num + num2)
#
#
# def get_num(self):
#     return self.num
#
# # Monkey Patching
# A.get_num = get_num
#
# foo = A(42)
# A.get_num = get_num
# print(foo.get_num())
# bar = A(2)
# print(bar.get_num())

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# .................................................................................................
# .................................................................................................
# ............................polymorphism.................................................
# l=[1,2,3,4,5]
# print(l[0::2]+l[1::2])
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;POLYMORPHISM PROPERTIES;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# POLYMORPHISM
# class Duck:
#     def quark(self):
#         print('Quaaaaaaaaaaaaaaaa')
#
#     def feathers(self):
#         print('the duck has white feathers')
#
#
# class Person:
#     def quark(self):
#         print('the person can imitate duck')
#
#     def feathers(self):
#         print('the person takes a feathers from ground aand takes it')
#
#     def name(self):
#         print('matt henry')
#
#
# def in_the_forest(obj):
#     obj.quark()
#     obj.feathers()
#
# donald = Duck()
# matt = Person()
#
# in_the_forest(donald)
# in_the_forest(matt)
#

# ................Properties
class Character(object):
    def __init__(self,name,max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp


    @property
    def hp(self):
        return self._hp

    @property
    def name(self):
        return self._name

    def take_damage(self,damage):
        self._hp -=damage
        self._hp = 0 if self._hp < 0 else self._hp

    @property
    def is_alive(self):
        return self._hp != 0

    @property
    def is_wounded(self):
        return self._hp < self._max_hp if self._hp > 0 else False


bill = Character("Bill",100)
print(bill.is_alive)
print(bill.is_wounded)




























































































