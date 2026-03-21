# 1. Ստեղծել Animal դասը, որն ունի name և age ատրիբուտներ։ 
# 2. Ավելացնել make_sound() մեթոդ, որը տպում է "Some generic sound": 
# 3. Ստեղծել Dog և Cat ժառանգ դասերը։ 
# 4. Վերասահմանել make_sound() մեթոդը յուրաքանչյուր կենդանու համար (օրինակ՝ 
# "Woof" և "Meow")։ 
# 5. Ստեղծել օբյեկտներ և կանչել նույն մեթոդը բոլորի համար։ 

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self. age = age
    
#     def make_sound(self):
#         print("some generic sound")
    
# class Dog(Animal):
#     def make_sound(self):
#         print("haf")


# class Cat(Animal):
#     def make_sound(self):
#         print("myau")

# a = Animal("Qerop", 10)
# b = Dog("Apo", 11)
# c = Cat("Armen", 9)

# a.make_sound()
# b.make_sound()
# c.make_sound()



# 1. Ստեղծել Product դասը՝ name և price դաշտերով։ Ավելացնել display_info() 
# մեթոդ։ 
# 2. Ստեղծել Smartphone և Laptop ժառանգ դասերը։ 
# 3. Յուրաքանչյուր ժառանգ դասի __init__-ում կանչել ծնող դասի կոնստրուկտորը 
# super()-ի միջոցով և ավելացնել նոր հատկանիշներ (օրինակ՝ ram կամ 
# battery_capacity)։ 
# 4. Վերասահմանել display_info() մեթոդը այնպես, որ այն տպի թե՛ ընդհանուր 
# տվյալները, թե՛ տվյալ սարքի առանձնահատկությունները։ 

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
    
#     def display_info(self):
#         print(f"product {self.name} has price of {self.price}")

# class Smartphone(Product):
#     def __init__(self, name, price, ram, battery):
#         super().__init__(name, price)
#         self.ram = ram
#         self.battery = battery

#     def display_info(self):
#         print(f"smartphone {self.name} has has price of {self.price}, ram of {self.ram} and battery capacity of {self.battery}")

    
# class Laptop(Product):
#     def __init__(self, name, price, ram, battery):
#         super().__init__(name, price)
#         self.ram = ram
#         self.battery = battery

#     def display_info(self):
#         print(f"laptop {self.name} has has price of {self.price}, ram of {self.ram} and battery capacity of {self.battery}")

# x = Product("first", 1000)
# y = Smartphone("second", 100, 10, 10000)
# z = Laptop("third", 100000, 100, 100000)

# x.display_info()
# y.display_info()
# z.display_info()




# 1. Ստեղծել Employee բազային դասը, որն ունի name և base_salary։ 
# 2. Ավելացնել calculate_pay() մեթոդ, որը պարզապես վերադարձնում է 
# base_salary-ն։ 
# 3. Ստեղծել երկու ժառանգ դաս․ 
# ○ Manager – որի աշխատավարձին գումարվում է նաև հաստատուն bonus։ 
# ○ CommissionWorker – որի աշխատավարձը հաշվարկվում է որպես 
# base_salary + (sales * 0.1) (վաճառքների 10%-ը)։(sales-ը 
# սահմանվում է այս կլասի մեջ) 
# 4. Ստեղծել տարբեր տիպի աշխատողների ցուցակ (list) և ցիկլի միջոցով տպել 
# յուրաքանչյուրի վերջնական աշխատավարձը։


# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary

#     def calculate_pay(self):
#         print(self.base_salary)

# class Manager(Employee):
#     def __init__(self, name, base_salary, bonus):
#         super().__init__(name, base_salary)
#         self.bonus = bonus
#     def calculate_pay(self):
#         print(self.base_salary + self.bonus)

# class CommissionWorker(Employee):
#     def __init__(self, name, base_salary, sales):
#         super().__init__(name, base_salary)
#         self.sales = sales
#     def calculate_pay(self):
#         print(int(self.base_salary + self.sales/10))


# ls = [Employee("Eduard", 100), Manager("Narek", 100, 1), CommissionWorker("Artak", 100, 20)]

# for i in ls:
#     i.calculate_pay()