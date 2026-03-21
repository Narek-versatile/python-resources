
# 5. Ստեղծել min_args(n) դեկորատոր, որը պահանջում է առնվազն n արգումենտ։ 
# Հակառակ դեպքում վերադարձնել "Not enough arguments"։


# def min_args(n):
    
#     def decorator(func):
#         def inner(*args, **kwargs):
#             if (len(args) + len(kwargs))<n:
#                 raise ValueError('not enough args')
#             x = func(*args, **kwargs)
#             return x
#         return inner
#     return decorator


# @min_args(2)
# def printer(*args):
#     print(sum(args))


# printer(1)


# 6.  Տրված է employees.txt ֆայլը հետևյալ ձևաչափով ID,Employee name, Position, Salary
# Տպել բոլոր աշխատողներին որոնց salary >= 200000
# Փոխել 3 id ունեցող աշխատողի աշխատավարձը 500000 և գրել ֆայլում

# with open("employees.txt", "r+") as fff:
#     lines = fff.readlines()
#     fff.seek(0)

#     for i in lines:
#         temp = i.strip().split(",")
#         if int(temp[3]) > 200000:
#             print(temp)

#         if temp[0] == "3":
#             temp[3] = "500000"

#         fff.write(",".join(temp) + "\n")



# Ավելացնել    {"id": 4, "model": "Chevrolet", "year": 2019} մեքենան
# Ջնջել Kia մեքենային ֆայլից

# import json

# with open("cars.json", "r+") as fff:
#     data = json.load(fff)
#     data["cars"].append({"id": 4, "model": "Chevrolet", "year": 2019})
#     new = []
#     for i in data["cars"]:
#         if i["model"] == "Kia":
#             continue
#         new.append(i)

#     data["cars"] = new
#     fff.seek(0)
#     json.dump(data, fff, indent=2)
#     fff.truncate()


        

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h

#     def area(self):
#         return self.w * self.h

# r = Rectangle(4, 4)
# print(r.area())

        

class Student:
    def __init__(self, grade):
        self.__grade=grade
    
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if not 0<=grade<=100:
            raise ValueError("Invalid grade")

        self.__grade = grade
    
slave1 = Student(100)
print(slave1.grade)
slave1.grade = 10
print(slave1.grade)
