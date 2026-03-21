# Ստեղծել BankAccount class․ 
# Ատրիբուտ 
# ● private __balance 
# Property 
# ● balance → միայն getter (read-only) 
# Մեթոդներ 
# ● deposit(amount) 
# ○ amount պետք է լինի > 0 
# ○ հակառակ դեպքում → տպել "Invalid amount" 
# ● withdraw(amount) 
# ○ amount > 0 
# ○ եթե գումարը բավարար չէ → "Insufficient funds"

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     @property
#     def balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if not amount>0:
#             raise ValueError('Invalid value')
        
#         self.__balance+=amount
#         return "done"

#     def withdraw(self, amount):
#         if not amount>0:
#             raise ValueError('Invalid Value')
#         if amount>self.__balance:
#             raise ValueError('Insufficient funds')

#         self.__balance-=amount

#         return "done"

# account1 = BankAccount(1000)
# print(account1.balance)
# account1.deposit(100)
# account1.withdraw(50)
# print(account1.balance)
        
        

# Ստեղծել Student class․ 
# Ատրիբուտ 
# ● private __grade 
# Property 
# ● grade 
# ○ getter 
# ○ setter → արժեքը պետք է լինի 0 <= value <= 100 
# ○ եթե սխալ արժեք է → տպել "Invalid grade" և չփոխել grade-ը 

# class Student:
#     def __init__(self, grade):
#         self.__grade = grade

#     @property
#     def grade(self):
#         return self.__grade

#     @grade.setter
#     def grade(self, grade):
#         if grade<0 or grade>100:
#             raise ValueError('invalid grade')
        
#         self.__grade = grade

# student1 = Student(10)
# print(student1.grade)
# student1.grade = 100
# print(student1.grade)



# Ստեղծել Temperature class․ 
# Ատրիբուտ 
# ● private __celsius 
# Property 
# ● celsius 
# ○ setter → արժեքը չպետք է լինի < -273 
# ○ եթե սխալ է → "Temperature below absolute zero" 
# ○ getter 
# Մեթոդ 
# ● to_fahrenheit() → վերադարձնի Fahrenheit արժեքը


# class Temperature:
#     def __init__(self, celsius):
#         self.__celsius = celsius
    
#     @property
#     def celsius(self):
#         return self.__celsius

#     @celsius.setter
#     def celsius(self, temp):
#         if temp<-273:
#             raise ValueError('Temperature below absolute zero')
        
#         self.__celsius = temp

#     def to_fahrenheit(self):
#         return (self.celsius * 1.8 + 32)


# temp1  = Temperature(100)
# print(temp1.celsius)
# print(temp1.to_fahrenheit())
# temp1.celsius = 1000
# print(temp1.celsius)
# print(temp1.to_fahrenheit())




# Ստեղծել PasswordManager class․ 
# Ատրիբուտ 
# ● private __password 
# Property 
# ● password →  getter չպետք է լինի  
# ● password setter → 
# ○ նոր password ≥ 6 սիմվոլ 
# ○ հակառակ դեպքում → "Password too short" 
# Մեթոդներ 
# ● verify(input_password) → վերադարձնի True / False 
# ● change_password(old, new) 
# ○ old պետք է ճիշտ լինի 
# ○ new ≥ 6 

# class PasswordManager:
#     def __init__(self, password):
#         self.__password = password
    
#     @property
#     def password(self):
#         raise Exception('ahahhahaha')

#     @password.setter
#     def password(self, password):
#         if len(password)<6:
#             raise ValueError('Password too short')

#         self.__password = password
    

#     def verify(self, password):
#         if self.__password == password:
#             return True

#         return False

#     def change_password(self, old, new):
#         if not old == self.__password:
#             raise ValueError('Incorrect Password')

#         self.__password = new


# password1 = PasswordManager("1234")
# # print(password1.password)
# password1.password = "123456"
# print(password1.verify("1234"))
# print(password1.verify("123456"))
# password1.change_password("123456", "1234")
# print(password1.verify("1234"))



# Ստեղծել Rectangle class․ 
# Ատրիբուտներ 
# ● private __width 
# ● private __height 
# Properties 
# ● width 
# ○ setter → value > 0 
# ● height 
# ○ setter → value > 0 
# Եթե ≤ 0 → "Invalid dimension" 
# Մեթոդներ 
# ● area() 
# ● perimeter() 

# class Rectangle:
#     def __init__(self, width, height):
#         self.__height = height
#         self.__width = width
    
#     @property
#     def width(self):
#         return self.__width

#     @property
#     def height(self):
#         return self.__height

#     @width.setter
#     def width(self, width):
#         if width<=0:
#             raise ValueError('invalid dimension')
#         self.__width = width

#     @height.setter
#     def height(self, height):
#         if height<=0:
#             raise ValueError('invalid dimension')
#         self.__height = height

#     def area(self):
#         return self.__height * self.__width

#     def perimeter(self):
#         return (self.__height + self.__width) *2


# rect1 = Rectangle(10, 10)
# rect1.height = 100
# rect1.width = 100

# print(rect1.area())
# print(rect1.perimeter())

#can't use @width.setter without first defining @property



# Ստեղծել Car class․ 
# Ատրիբուտ 
# ● private __fuel 
# Property 
# ● fuel → getter միայն (read-only) 
# Մեթոդներ 
# ● drive(km) 
# ○ 1km = 1 liter 
# ○ եթե fuel < km → "Not enough fuel" 
# ● refuel(amount) 
# ○ amount > 0 
# fuel-ը դրսից փոխել հնարավոր չպետք է լինի։ 

# class Car:
#     def __init__(self, fuel):
#         self.__fuel = fuel

#     @property
#     def fuel(self):
#         return self.__fuel

#     def drive(self, km):
#         if(km > self.__fuel):
#             raise ValueError('low fuel')
#         self.__fuel -= km
    
#     def refuel(self, km):
#         if km<=0:
#             raise ValueError('wrong value')
#         self.__fuel+=km



#     Mihael = Car(100)
#     Mihael.refuel(1000)
#     Mihael.drive(1000)
#     Mihael.drive(10000)
# Mihael.refuel(500)



# Ստեղծել Book class․ 
# Ատրիբուտ 
# ● private __is_available 
# Property 
# ● is_available → getter only 
# Մեթոդներ 
# ● borrow() 
# ○ եթե արդեն վերցված է → "Book is already borrowed" 
# ● return_book() 
# ○ եթե արդեն վերադարձված է → "Book is already available" 

# class Book:
#     def __init__(self, is_available):
#         self.__is_available = is_available
#     @property
#     def is_available(self):
#         return self.__is_available

#     def borrow(self):
#         if not self.is_available:
#             raise ValueError('Book is already available')
#         self.__is_available = False

#     def return_book(self):
#         if self.__is_available:
#             raise ValueError('Book is already available')
        
#         self.__is_available = True

# book1 = Book(True)
# print(book1.is_available)
# book1.borrow()
# print(book1.is_available)
# book1.return_book()
# print(book1.is_available)


# Ստեղծել Thermostat class․ 
# Ատրիբուտ 
# ● private __temperature 
# Property 
# ● temperature 
# ○ setter → թույլատրելի միջակայք 16 <= value <= 30 
# ○ եթե դուրս է միջակայքից → "Temperature out of range" 
# ○ getter


# class Thermostat:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#     @property
#     def temperature(self):
#         return self.__temperature
    
#     @temperature.setter
#     def temperature(self, temp):
#         if temp<16 or temp>30:
#             raise ValueError('Temperature out of range')
#         self.__temperature = temp


# therm1 = Thermostat(100)
# print(therm1.temperature)
# therm1.temperature = 16
# print(therm1.temperature)