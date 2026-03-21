# �
# �
# Vehicle Management System 
# �
# �
# Նպատակ 
# Ստեղծել տրանսպորտային միջոցների կառավարման համակարգ, որտեղ կարող ենք 
# ստեղծել տարբեր տիպի մեքենաներ և կառավարել դրանք մեկ ընդհանուր համակարգում։ 
# Պետք է օգտագործել․ 
# ● ժառանգում (inheritance) 
# ● մեթոդների վերասահմանում (method overriding) 
# 1⃣ Vehicle Class 
# Ներկայացնում է ցանկացած տրանսպորտային միջոց։ 
# �
# �
# Ատրիբուտներ 
# ● make 
# Տիպ՝ string 
# Արտադրող (օր․ "Toyota") 
# ● model 
# Տիպ՝ string 
# Մոդել 
# ● year 
# Տիպ՝ int 
# Թողարկման տարեթիվ 
# �
# �
# Մեթոդներ 
# description() 
# Վերադարձնում է մեքենայի ամբողջական նկարագրությունը (string) 
# age(current_year) 
# Հաշվում է մեքենայի տարիքը 
# Վերադարձնում է → current_year - year
# 📌
# Validation 
# ● make, model → չեն կարող լինել դատարկ 
# ● year → չի կարող լինել ապագայում 
# Սխալի դեպքում → raise ValueError 

import datetime

class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.make} model {self.model} was made on {self.year}")

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new):
        if not isinstance(new, str):
            raise TypeError("hop")
        if not str:
            raise ValueError("hop")

        self.__make = new

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new):
        if not isinstance(new, str):
            raise TypeError("hop")
        if not str:
            raise ValueError("hop")

        self.__model = new

    @property
    def year(self):
        return self.__year


    @year.setter
    def year(self, new):
        if not isinstance(new, int):
            raise TypeError("hop")
        if new > datetime.datetime.now().year:
            raise ValueError("hop")

        self.__year = new

def vehtest():
    veh1 = Vehicle("toy", "911", 1945)
    veh1.description()
# vehtest()


# 2⃣ Car Class (Vehicle-ից ժառանգված) 
# �
# �
# Լրացուցիչ ատրիբուտ 
# ● number_of_doors (int) 
# �
# �
# Մեթոդներ 
# description() 
# Վերասահմանել base class-ի մեթոդը և ավելացնել դռների քանակը 
# �
# �
# Validation 
# ● Դռների քանակը պետք է լինի > 0 

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def description(self):
        print(f"Car {self.make} model {self.model} was made on {self.year} and has {self.number_of_doors} doors")

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @number_of_doors.setter
    def number_of_doors(self, new):
        if not isinstance(new, int):
            raise TypeError("hop")
        if new<1:
            raise ValueError("hop")

        self.__number_of_doors = new

def cartest():
    car1 = Car("toyot", "919", 1900, 10)
    car1.description()
# cartest()



# 3⃣ Truck Class (Vehicle-ից ժառանգված) 
# �
# �
# Լրացուցիչ ատրիբուտ 
# ● cargo_capacity (float, տոննա) 
# �
# �
# Մեթոդներ 
# description() 
# Ներառել բեռնատարողությունը
# 📌
# Validation 
# ● cargo_capacity > 0 


class Truck(Vehicle):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
    
    def description(self):
        print(f"Truck {self.make} model {self.model} was made on {self.year} and has cargo capacity of {self.cargo_capacity} tons")

    @property
    def cargo_capacity(self):
        return self.__cargo_capacity

    @cargo_capacity.setter
    def cargo_capacity(self, new):
        if not isinstance(new, float):
            raise TypeError("hop")
        if new <= 0:
            raise ValueError("hop")

        self.__cargo_capacity = new


def trktest():
    trk1 = Truck("toyot", "9191", 1809, 10.0)
    trk1.description()
# trktest()



# 4⃣ Motorcycle Class (Vehicle-ից ժառանգված) 
# �
# �
# Լրացուցիչ ատրիբուտ 
# ● has_sidecar (bool) 
# �
# �
# Մեթոդներ 
# description() 
# Նշել՝ ունի կողային կցորդ, թե ոչ 



class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def description(self):
        print(f"Motorcycle {self.make} model {self.model} was made on {self.year} and has sidecar status of {self.has_sidecar}")

    @property
    def has_sidecar(self):
        return self.__has_sidecar

    @has_sidecar.setter
    def has_sidecar(self, new):
        if not isinstance(new, bool):
            raise TypeError
        
        self.__has_sidecar = new

def mtctest():
    mtc1 = Motorcycle("toyot", "456d", 1944, True)
    mtc1.description()
# mtctest()


# 5⃣ Fleet Class 
# Կառավարում է բոլոր մեքենաները 
# �
# �
# Ատրիբուտ 
# ● vehicles → list 
# �
# �
# Մեթոդներ 
# add_vehicle(vehicle) 
# Ավելացնում է մեքենան ցուցակում 
# remove_vehicle(index) 
# Հեռացնում է մեքենան ըստ ինդեքսի 
# list_vehicles() 
# Տպում է բոլոր մեքենաների description()-ները 
# filter_by_type(vehicle_type) 
# Վերադարձնում է տվյալ տիպի մեքենաները 
# (օր․ միայն Car) 
# total_cargo_capacity() 
# Հաշվում է բոլոր Truck-ների ընդհանուր բեռնատարողությունը 

class Fleet:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, *args):
        for i in args:
            if not isinstance(i, Vehicle):
                raise TypeError("hop")
            self.vehicles.append(i)
    
    def remove_vehicle(self, ind):
        if len(self.vehicles) <= ind or ind<0:
            raise ValueError("hop")
        self.vehicles.pop(ind)
    
    def list_vehicles(self):
        for i in self.vehicles:
            i.description()
            print("===================================")

    def filter_by_type(self, vehicle_type: str):
        ls = []
        if vehicle_type == "Car":
            for i in self.vehicles:
                if isinstance(i, Car):
                    ls.append(i)
        elif vehicle_type == "Truck":
            for i in self.vehicles:
                if isinstance(i, Truck):
                    ls.append(i)
        elif vehicle_type == "Motorcycle":
            for i in self.vehicles:
                if isinstance(i, Motorcycle):
                    ls.append(i)
        else:
            raise TypeError("hop")
        return ls

    def total_cargo_capacity(self):
        sum = 0
        for i in self.filter_by_type("Truck"):
            sum += i.cargo_capacity
        print(sum)
        

# Պարտադիր Դեմո Սցենար 
# ● Ստեղծել՝ 
# ○ 2 Car 
car1 = Car("porcho", "19dfi", 1520, 2)
car2 = Car("ferdari", "kaynando", 1969, 1)
# ○ 1 Truck 
truck1 = Truck("Lambrgmbr", "Traktarist", 2010, 5.5)
# ○ 1 Motorcycle 
motorcycle1 = Motorcycle("kawasake", "pegasusik", 1910, True)
# ● Ստեղծել Fleet 
fleet1 = Fleet()
# ● Ավելացնել բոլոր մեքենաները 
fleet1.add_vehicle(car1, car2, truck1, motorcycle1)
# ● Տպել բոլոր մեքենաները 
fleet1.list_vehicles()
# ● Տպել միայն Truck-երը
for i in fleet1.filter_by_type("Truck"):
    i.description()
# ● Հաշվել ընդհանուր բեռնատարողությունը 
fleet1.total_cargo_capacity()