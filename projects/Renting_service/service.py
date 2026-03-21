# 🎯 Նպատակ
# Ստեղծել մեքենաների վարձակալության համակարգ, որտեղ հաճախորդները կարող են վարձակալել մեքենաներ։
# Պետք է օգտագործել․
# ինկապսուլացիա (private attributes)
# @property

# 1️⃣ Car Class
# Ներկայացնում է մեկ մեքենա։
# 📌 Ատրիբուտներ
# brand
# Տիպ՝ string
# Մեքենայի ապրանքանիշը (օր․ "Toyota")
# year
# Տիպ՝ int
# Թողարկման տարեթիվը
# __price_per_day
# Տիպ՝ float կամ int
# Մեքենայի մեկ օրվա վարձակալության գինը
# Private է (օգտագործվում է ինկապսուլացիա ապահովելու համար)
# __is_available
# Տիպ՝ bool
# Ցույց է տալիս՝ մեքենան հասանելի է վարձակալման համար, թե ոչ
# Սկզբնական արժեքը → True

# 📌 Property-ներ
# price_per_day
# Getter → վերադարձնում է գինը
# Setter →
# Չպետք է թույլ տա ≤ 0 արժեք
# Սխալի դեպքում raise ValueError
# is_available
# Read-only property
# Վերադարձնում է մեքենայի հասանելիության վիճակը
# Setter չպետք է ունենա

# 📌 Մեթոդներ
# rent()
# Ստուգում է՝ մեքենան հասանելի՞ է
# Եթե հասանելի է →
# _is_available = False
# Եթե ոչ → raise Exception

# return_car()
# Փոխում է _is_available = True

# calculate_rent(days)
# days → վարձակալության օրերի քանակ
# Վերադարձնում է days * price_per_day
# Եթե days ≤ 0 → error

# 2️⃣ Customer Class
# Ներկայացնում է հաճախորդ։

# 📌 Ատրիբուտներ
# __name
# Հաճախորդի անուն
# __driver_license_number
# Վարորդական իրավունքի համար
# rented_cars
# List
# Պահում է տվյալ հաճախորդի վարձակալած մեքենաները



# 📌 Property-ներ
# name
# Getter → վերադարձնում է անունը
# Setter →
# Պետք է թույլ տա միայն տողեր
# Սխալի դեպքում raise ValueError
# Պետք է դատարկ տող չլինի
# driver_license_number
# Getter → վերադարձնում է վարորդական վկայականի համարը
# Setter →
# Պետք է թույլ տա միայն տողեր
# Սխալի դեպքում raise ValueError
# Պետք է դատարկ տող չլինի և պետք է լինի հետևյալ ձևաչափով
# Սկզբում 2 տառ, ապա հաջորդի 6 թվանշան

# 📌 Մեթոդներ
# add_car(car)
# Ավելացնում է մեքենան rented_cars ցուցակում

# return_car(car)
# Հանում է մեքենան ցուցակից
# Կանչում է car.return_car()

# 3️⃣ RentalService Class
# Կառավարում է ամբողջ համակարգը։

# 📌 Ատրիբուտներ
# cars
# List
# Պահում է բոլոր մեքենաները

# 📌 Մեթոդներ
# add_car(car)
# Ավելացնում է մեքենա համակարգում

# show_available_cars()
# Տպում է բոլոր մեքենաները, որոնց is_available == True

# rent_car(customer, car, days)
# Գործողությունների հերթականություն․
# Ստուգել՝ մեքենան հասանելի՞ է
# Կանչել car.rent()
# Ավելացնել մեքենան հաճախորդի ցուցակում
# Հաշվել գումարը → car.calculate_rent(days)
# Վերադարձնել ընդհանուր գումարը

# 📌 Պարտադիր Դեմո Սցենար
# Ստեղծել 3 մեքենա
# Ստեղծել 1 հաճախորդ
# Ստեղծել RentalService
# Ավելացնել մեքենաները համակարգում
# Վարձակալել մեքենա 3 օրով
# Տպել վճարման գումարը
# Վերադարձնել մեքենան

class Car:
    def __init__(self, brand, year, price_per_day, is_available = True):
        self.brand = brand
        self.year = year
        self.price_per_day = price_per_day
        self.__is_available = is_available
    
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if not isinstance(brand, str):
            raise ValueError('put str')
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise ValueError('put int or float')
        self.__year = year

    @property
    def price_per_day(self):
        return self.__price_per_day

    @price_per_day.setter
    def price_per_day(self, price_per_day):
        if not (isinstance(price_per_day, float) or isinstance(price_per_day, int)):
            raise ValueError
        if price_per_day<=0:
            raise ValueError('cant set to negative')
        self.__price_per_day = price_per_day

    @property
    def is_available(self):
        return self.__is_available

    # @is_available.setter
    # def is_available(self, is_available):
    #     if not isinstance(is_available, bool):
    #         raise ValueError('')
    #     self.__is_available = is_available


    def rent(self):
        if not (self.is_available):
            raise Exception('unavailable')
        self.__is_available = False
    
    def return_car(self):
        self.__is_available = True

    def calculate_rent(self, days):
        if days<=0:
            raise ValueError('no negative days')
        return days * self.__price_per_day

# car1 = Car("Toyota", 1999, 100, True)
# print(car1.calculate_rent(10))
# car1.rent()
# print(car1.is_available)
# car1.return_car()
# print(car1.is_available)


class Customer:
    def __init__(self, name, driver_license_number, rented_cars):
        self.name = name
        self.driver_license_number = driver_license_number
        self.rented_cars = rented_cars
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if (len(name)<1 or not isinstance(name, str)):
            raise ValueError('put str')
        self.__name = name

    @property
    def driver_license_number(self):
        return self.__driver_license_number

    @driver_license_number.setter
    def driver_license_number(self, driver_license_number):
        if not isinstance(driver_license_number, (str, int)):
            raise ValueError('put str or int')
        self.__driver_license_number = driver_license_number

    @property
    def rented_cars(self):
        return self.__rented_cars

    @rented_cars.setter
    def rented_cars(self, rented_cars):
        if not isinstance(rented_cars, list):
            raise ValueError('put list')
        self.__rented_cars = rented_cars

    def add_car(self, car):
        self.__rented_cars.append(car)

    def return_car(self, car):
        car.return_car()
        self.rented_cars.pop(self.__rented_cars.index(car))
    



# 3️⃣ RentalService Class
# Կառավարում է ամբողջ համակարգը։

# 📌 Ատրիբուտներ
# cars
# List
# Պահում է բոլոր մեքենաները

# 📌 Մեթոդներ
# add_car(car)
# Ավելացնում է մեքենա համակարգում

# show_available_cars()
# Տպում է բոլոր մեքենաները, որոնց is_available == True

# rent_car(customer, car, days)
# Գործողությունների հերթականություն․
# Ստուգել՝ մեքենան հասանելի՞ է
# Կանչել car.rent()
# Ավելացնել մեքենան հաճախորդի ցուցակում
# Հաշվել գումարը → car.calculate_rent(days)
# Վերադարձնել ընդհանուր գումարը

# 📌 Պարտադիր Դեմո Սցենար
# Ստեղծել 3 մեքենա
# Ստեղծել 1 հաճախորդ
# Ստեղծել RentalService
# Ավելացնել մեքենաները համակարգում
# Վարձակալել մեքենա 3 օրով
# Տպել վճարման գումարը
# Վերադարձնել մեքենան




class RentalService:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_available_cars(self):
        for car in self.cars:
            if car.is_available:
                print(car)

    def rent_car(self, customer, car, days):
        if car.is_available:
            car.rent()
            customer.rented_cars.append(car)
            total_price = car.calculate_rent(days)
            return total_price

    def return_car(self, customer, car):
        car.return_car()



car11 = Car("Mercedes-Benz", 2022, 120, True)
car22 = Car("BMW X5", 2021, 100, True)
car33 = Car("Audi A6", 2023, 110, True)

customer1 = Customer("Negr", "A1234567", [])

rental_service = RentalService()
rental_service.add_car(car11)
rental_service.add_car(car22)
rental_service.add_car(car33)

payment_amount = rental_service.rent_car(customer1, car22, 3)
print(payment_amount)

customer1.return_car(car22)

    