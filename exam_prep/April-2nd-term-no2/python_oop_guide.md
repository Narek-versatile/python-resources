# Python OOP — Complete Learning Reference

---

## 1. What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects** — self-contained units that bundle data (attributes) and behavior (methods) together. Instead of writing a sequence of instructions, you model the world as interacting objects.

The four pillars are: **Abstraction, Encapsulation, Inheritance, Polymorphism**.

```python
class Dog:
    def __init__(self, name):
        self.name = name          # data

    def bark(self):               # behavior
        print(f"{self.name} says Woof!")

rex = Dog("Rex")
rex.bark()   # Rex says Woof!
```

---

## 2. What is OOA?

**Object-Oriented Analysis (OOA)** is the process of examining a problem domain (requirements, user stories, real-world scenarios) and identifying the **objects, their attributes, behaviors, and relationships** that should exist in the system.

It answers: *"What exists in this domain?"*

```python
# During OOA for a library system you might identify:
# - Book  → attributes: title, author, isbn | behavior: checkout, return
# - Member → attributes: name, id          | behavior: borrow, return_book
# - Library → manages Books and Members

# OOA output is usually UML diagrams or written descriptions, not code yet.
# But conceptually:

# Entities found:
entities = {
    "Book":    {"attrs": ["title", "author", "isbn"], "behaviors": ["checkout", "return"]},
    "Member":  {"attrs": ["name", "id"],              "behaviors": ["borrow"]},
    "Library": {"attrs": ["name", "address"],         "behaviors": ["add_book", "register_member"]},
}
```

---

## 3. What is OOD?

**Object-Oriented Design (OOD)** takes the results of OOA and decides **how** those objects will be implemented — class hierarchies, interfaces, design patterns, relationships (inheritance vs composition), and responsibilities.

It answers: *"How should we build it?"*

```python
# OOD decision: Book should be abstract; PhysicalBook and EBook are concrete.
# Member borrows books via Library (not directly) → association through Library.

from abc import ABC, abstractmethod

class Book(ABC):                    # OOD decision: make Book abstract
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def checkout(self): ...

class PhysicalBook(Book):           # OOD decision: concrete subclass
    def checkout(self):
        print(f"Physical copy of '{self.title}' checked out.")

class EBook(Book):                  # OOD decision: another concrete subclass
    def checkout(self):
        print(f"E-copy of '{self.title}' downloaded.")
```

---

## 4. Difference Between OOA and OOD

| | OOA | OOD |
|---|---|---|
| **Focus** | Problem domain (what?) | Solution domain (how?) |
| **Question** | What objects exist? | How are they structured? |
| **Output** | Conceptual model, entity list | Class diagrams, design patterns |
| **Tech-aware?** | No | Yes |
| **Example** | "A Library has Books" | "Book is abstract; use Factory pattern" |

---

## 5. What is an Object?

An **object** is a specific **instance** of a class — a concrete entity in memory with its own state (attribute values) and behavior (methods). Every object has:
- **Identity** — unique memory address
- **State** — current attribute values
- **Behavior** — methods it can perform

```python
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} now at {self.speed} km/h")

car1 = Car("Toyota", 0)    # object 1
car2 = Car("BMW", 0)       # object 2 — independent state

car1.accelerate(50)   # Toyota now at 50 km/h
car2.accelerate(80)   # BMW now at 80 km/h

print(car1 is car2)   # False — different identities
```

---

## 6. What is a Class?

A **class** is a **blueprint/template** for creating objects. It defines the structure (attributes) and behavior (methods) that all instances will share. The class itself is also an object in Python (everything is an object).

```python
class BankAccount:
    bank_name = "PyBank"          # class attribute (shared by all)

    def __init__(self, owner, balance=0):
        self.owner = owner        # instance attribute (unique per object)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

acc = BankAccount("Alice", 1000)
print(acc)               # BankAccount(owner='Alice', balance=1000)
print(BankAccount.bank_name)  # PyBank  <- accessed on the class itself
```

---

## 7. What are Object Operations?

Object operations are actions you can perform **on or with** objects:

| Operation | Description |
|---|---|
| **Creation** | Instantiating via `ClassName()` |
| **Attribute access** | `obj.attr` |
| **Method call** | `obj.method()` |
| **Comparison** | `obj1 == obj2` (via `__eq__`) |
| **Destruction** | `del obj` (via `__del__`) |
| **Copying** | `copy.copy()` / `copy.deepcopy()` |

```python
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)           # creation
print(p1.x)                # attribute access -> 1
print(p1)                  # repr -> Point(1, 2)

p2 = copy.copy(p1)         # copy operation
print(p1 == p2)            # comparison -> True
print(p1 is p2)            # identity check -> False

del p1                     # destruction
```

---

## 8. What is an Object Attribute?

An **object (instance) attribute** is a variable that belongs to a **specific instance** of a class. Each object has its own copy, set typically in `__init__`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name    # object attribute
        self.age = age      # object attribute

alice = Person("Alice", 30)
bob   = Person("Bob", 25)

alice.name = "Alice Smith"   # modifying only alice's attribute

print(alice.name)  # Alice Smith
print(bob.name)    # Bob  <- unaffected
```

---

## 9. What is a Class Attribute?

A **class attribute** is a variable defined **on the class itself**, shared by all instances. Changing it on the class affects all instances (unless an instance has shadowed it with its own attribute of the same name).

```python
class Employee:
    company = "OpenCorp"    # class attribute
    headcount = 0

    def __init__(self, name):
        self.name = name            # instance attribute
        Employee.headcount += 1    # modifying class attribute via class name

e1 = Employee("Alice")
e2 = Employee("Bob")

print(Employee.headcount)    # 2
print(e1.company)            # OpenCorp  <- inherited from class
print(e2.company)            # OpenCorp

Employee.company = "NewCorp"
print(e1.company)            # NewCorp  <- both see the change
print(e2.company)            # NewCorp

e1.company = "PrivateCorp"   # shadows class attr on e1 only
print(e1.company)            # PrivateCorp
print(e2.company)            # NewCorp  <- unaffected
```

---

## 10. What is an Instance Attribute?

Same as **object attribute** (Section 8) — a variable that belongs to a specific instance, not the class. Defined inside `__init__` (or any method) via `self.attr = value`.

```python
class Circle:
    pi = 3.14159          # class attribute

    def __init__(self, radius):
        self.radius = radius    # instance attribute — unique per circle

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)   # 5
print(c2.radius)   # 10
print(c1.area())   # 78.53975
```

---

## 11. What is Abstraction?

**Abstraction** means hiding complex implementation details and exposing only what is necessary. You interact with an object through a clean interface without needing to know how it works internally.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...     # interface — no implementation

    @abstractmethod
    def perimeter(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, w, h):
        self._w = w     # hidden detail
        self._h = h

    def area(self):
        return self._w * self._h

    def perimeter(self):
        return 2 * (self._w + self._h)

r = Rectangle(4, 6)
print(r.area())       # 24  — you don't need to know how it's calculated
print(r.perimeter())  # 20

# Shape()  <- TypeError: Can't instantiate abstract class
```

---

## 12. What is Encapsulation?

**Encapsulation** is bundling data and the methods that operate on it together, while **restricting direct access** to internal state. Python uses naming conventions:
- `_attr` -> protected (convention: don't touch from outside)
- `__attr` -> private (name-mangled by Python)

```python
class Thermostat:
    def __init__(self, temp):
        self.__temp = temp           # private

    def get_temp(self):
        return self.__temp

    def set_temp(self, value):
        if 15 <= value <= 30:        # validation logic hidden inside
            self.__temp = value
        else:
            raise ValueError("Temperature out of safe range!")

t = Thermostat(22)
print(t.get_temp())     # 22
t.set_temp(25)          # OK
# t.__temp              # AttributeError — name-mangled to _Thermostat__temp
# t.set_temp(100)       # ValueError

# Python's name mangling:
print(t._Thermostat__temp)  # 25 — accessible but signals "don't do this"
```

---

## 13. What is Polymorphism?

**Polymorphism** means "many forms" — the same interface (method name) works differently depending on the object's type. You can write code that works on objects of different classes as long as they share the expected interface.

```python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

class Duck:
    def speak(self):
        return "Quack"

animals = [Cat(), Dog(), Duck()]

for animal in animals:
    print(animal.speak())   # each calls its own version
# Meow
# Woof
# Quack

def make_it_speak(animal):
    print(animal.speak())   # doesn't care about the type, just the interface

make_it_speak(Dog())   # Woof
make_it_speak(Cat())   # Meow
```

---

## 14. What is Duck Typing?

**Duck Typing** is a form of polymorphism specific to dynamically-typed languages like Python. It means: *"If it walks like a duck and quacks like a duck, it's a duck."* You don't check the type of an object; you just use it. If it has the expected methods/attributes, it works.

```python
class Duck:
    def quack(self): print("Quack!")
    def walk(self):  print("Waddle waddle")

class Person:
    def quack(self): print("I'm quacking like a duck!")
    def walk(self):  print("I'm walking like a duck!")

class RubberDuck:
    def quack(self): print("Squeak!")
    def walk(self):  print("I don't walk, I float!")

def in_the_pond(duck):
    duck.quack()    # no isinstance() check — we just call the method
    duck.walk()

# All three work — no shared base class required
in_the_pond(Duck())
in_the_pond(Person())
in_the_pond(RubberDuck())
```

---

## 15. What is Inheritance?

**Inheritance** allows a class (child/subclass) to **inherit** attributes and methods from another class (parent/superclass), enabling code reuse and the "is-a" relationship.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} breathes")

class Dog(Animal):              # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows!")

d = Dog("Rex")
d.breathe()   # inherited -> Rex breathes
d.bark()      # own method -> Rex barks!

c = Cat("Whiskers")
c.breathe()   # inherited
c.meow()
```

---

## 16. Types of Inheritance

| Type | Description |
|---|---|
| **Single** | One child, one parent |
| **Multi-level** | Chain: A -> B -> C |
| **Multiple** | One child, multiple parents |
| **Hierarchical** | Multiple children, one parent |
| **Hybrid** | Combination of the above |

```python
# Single
class A: pass
class B(A): pass

# Multi-level
class C(B): pass   # C -> B -> A

# Multiple
class D(A, C): pass   # D inherits from both A and C

# Hierarchical
class E(A): pass
class F(A): pass   # Both E and F inherit from A

# Hybrid (combination of multiple + hierarchical)
class G(E, F): pass   # Diamond-like

print(D.__mro__)
print(G.__mro__)
```

---

## 17. What is the Diamond Problem?

The **diamond problem** occurs in multiple inheritance when two parent classes inherit from the same grandparent, and a child inherits from both parents. The question becomes: which version of the grandparent's method should be used?

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):    # D inherits B and C — both inherit from A
    pass

#       A
#      / \
#     B   C
#      \ /
#       D   <- Which greet() does D use?

d = D()
d.greet()    # Hello from B  <- Python's MRO decides this
```

Python solves this with **MRO (Method Resolution Order)** using the **C3 Linearization** algorithm.

---

## 18. What is MRO?

**Method Resolution Order (MRO)** is the order in which Python searches classes when looking up a method or attribute. Python uses **C3 Linearization** to compute a consistent, predictable order. You can inspect it via `ClassName.__mro__` or `ClassName.mro()`.

```python
class A:
    def who(self): print("A")

class B(A):
    def who(self): print("B")

class C(A):
    def who(self): print("C")

class D(B, C):
    pass

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
# D -> B -> C -> A -> object

D().who()    # B  <- first in MRO that defines who()

# super() follows MRO:
class B2(A):
    def who(self):
        print("B2")
        super().who()   # calls next in MRO, which is C2 (not A!)

class C2(A):
    def who(self):
        print("C2")
        super().who()

class D2(B2, C2): pass

D2().who()
# B2
# C2
# A
```

---

## 19. Register and Protocol in Duck Typing Context

**Protocol** (from `typing`) defines an interface structurally — a class satisfies a Protocol if it has the required methods, **without inheriting** from it (structural subtyping / static duck typing).

**register** (from `abc.ABC`) lets you declare that a class implements an ABC **without inheriting** from it — virtual subclassing.

```python
# --- Protocol (structural duck typing for type checkers) ---
from typing import Protocol, runtime_checkable

@runtime_checkable
class Quackable(Protocol):
    def quack(self) -> str: ...

class RealDuck:
    def quack(self): return "Quack!"

class Robot:
    def quack(self): return "Beep-quack!"

class Stone:
    pass

print(isinstance(RealDuck(), Quackable))  # True  — has .quack()
print(isinstance(Robot(),    Quackable))  # True  — has .quack()
print(isinstance(Stone(),    Quackable))  # False — no .quack()


# --- register (virtual subclassing via ABC) ---
from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self): ...

class Airplane:
    def fly(self):
        print("Flying with engines")

Flyable.register(Airplane)    # register without inheriting

print(issubclass(Airplane, Flyable))      # True
print(isinstance(Airplane(), Flyable))    # True

# Note: register does NOT enforce that Airplane actually implements fly()
# It's a declaration of intent — use Protocol for safer structural checks
```

---

## 20. Object and Class Relationships

In OOP, objects and classes can relate to each other in several fundamental ways:

| Relationship | Keyword | Example |
|---|---|---|
| **Inheritance** | "is-a" | Dog is-a Animal |
| **Association** | "uses-a" / "knows-a" | Teacher knows Student |
| **Composition** | "owns-a" (strong) | Car owns Engine |
| **Aggregation** | "has-a" (weak) | Library has Books |

---

## 21. Inheritance (as a Relationship)

**Inheritance** expresses an **"is-a"** relationship. A subclass *is a* specialized version of its superclass.

```python
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Moving at {self.speed} km/h")

class Car(Vehicle):       # Car IS-A Vehicle
    def honk(self):
        print("Beep!")

class Truck(Vehicle):     # Truck IS-A Vehicle
    def load(self, cargo):
        print(f"Loading {cargo}")

c = Car(120)
c.move()    # inherited
c.honk()

print(isinstance(c, Vehicle))   # True — is-a confirmed
```

---

## 22. What is Association?

**Association** is a relationship where one object **uses or knows** another but neither owns the other. Both can exist independently. It's the weakest form of relationship.

```python
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):          # uses a Student, doesn't own it
        print(f"{self.name} is teaching {student.name}")

class Student:
    def __init__(self, name):
        self.name = name

# Both created independently — no ownership
t = Teacher("Mr. Smith")
s = Student("Alice")

t.teach(s)   # association via method parameter
# Mr. Smith is teaching Alice

# s and t live on independently — association is not a "containment"
del t
print(s.name)   # Alice — still alive
```

---

## 23. What is Composition?

**Composition** is a **strong "owns-a"** relationship where one object contains another and the contained object **cannot exist without** the parent. If the parent is destroyed, so are its parts.

```python
class Engine:
    def __init__(self, horsepower):
        self.hp = horsepower

    def start(self):
        print(f"Engine ({self.hp}hp) starting...")

class Car:
    def __init__(self, brand, hp):
        self.brand = brand
        self._engine = Engine(hp)   # Car OWNS the Engine — created internally

    def drive(self):
        self._engine.start()
        print(f"{self.brand} is driving!")

car = Car("Toyota", 150)
car.drive()
# Engine (150hp) starting...
# Toyota is driving!

# Engine is created and destroyed with Car
# You cannot pass an existing Engine to Car — it builds its own
# If car is deleted, its engine ceases to exist meaningfully
```

---

## 24. What is Aggregation?

**Aggregation** is a **weak "has-a"** relationship. The parent contains a reference to a child, but the child **can exist independently**. The child is passed in from outside.

```python
class Student:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.students: list = []   # aggregates students

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for s in self.students:
            print(f"  - {s.name}")

# Students are created independently
alice = Student("Alice")
bob   = Student("Bob")

cs_dept = Department("Computer Science")
cs_dept.add_student(alice)
cs_dept.add_student(bob)
cs_dept.list_students()

# Department can be deleted but students live on
del cs_dept
print(alice.name)   # Alice — still alive (aggregation, not composition)
```

---

## 25. Class Relationships vs Object Relationships

| | Class Relationships | Object Relationships |
|---|---|---|
| **Level** | Design time (blueprint level) | Runtime (instance level) |
| **Defined via** | `class` definitions, inheritance | Object instantiation, passing references |
| **Example** | `class Dog(Animal)` | `my_dog = Dog(); owner.pet = my_dog` |
| **Describes** | How types relate | How specific instances interact |

```python
# Class relationship: defined in code
class Engine: pass
class Car:
    def __init__(self):
        self.engine = Engine()   # class-level composition design

# Object relationship: exists at runtime
car1 = Car()   # car1.engine is a specific Engine instance
car2 = Car()   # car2.engine is a DIFFERENT Engine instance

# Object relationship: association at runtime
garage = [car1, car2]   # garage object holds references to car objects
```

---

## 26. What is a Link?

A **link** is a **runtime instance of an association** — a concrete connection between two specific objects. If Association is the class-level concept, a Link is the object-level reality.

```python
class Person:
    def __init__(self, name):
        self.name = name
        self.friends: list = []    # association defined at class level

    def add_friend(self, other):
        self.friends.append(other)           # LINK created at runtime

alice = Person("Alice")
bob   = Person("Bob")
carol = Person("Carol")

alice.add_friend(bob)     # link: alice <-> bob
alice.add_friend(carol)   # link: alice <-> carol

print([f.name for f in alice.friends])   # ['Bob', 'Carol']
# These links exist at runtime; they're not described in the class definition
```

---

## 27. Composition (revisited — ownership lifecycle)

The key distinction of Composition vs Aggregation is **lifecycle ownership**:

```python
# Composition — part cannot outlive the whole
class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self, address):
        self.address = address
        # Rooms are CREATED inside House — they don't exist without it
        self.rooms = [Room("Living Room"), Room("Bedroom"), Room("Kitchen")]

    def list_rooms(self):
        for r in self.rooms:
            print(f"  {r.name}")

h = House("123 Main St")
h.list_rooms()
# Rooms were born with House and die with House

# Aggregation — part can outlive the whole
class Wheel:
    def __init__(self, size):
        self.size = size

w1, w2, w3, w4 = Wheel(18), Wheel(18), Wheel(18), Wheel(18)

class Car2:
    def __init__(self, wheels):
        self.wheels = wheels   # wheels passed in — exist independently

car = Car2([w1, w2, w3, w4])
del car
print(w1.size)   # 18 — wheels outlived the car
```

---

## 28. What is a Server?

In OOP, a **Server** is an object that **provides services** (exposes methods) to be called by other objects (clients). It waits to serve requests.

```python
class DatabaseServer:
    def __init__(self):
        self._data = {}

    def store(self, key, value):
        self._data[key] = value
        print(f"[Server] Stored {key}={value}")

    def fetch(self, key):
        value = self._data.get(key, None)
        print(f"[Server] Fetched {key}={value}")
        return value

# DatabaseServer is the SERVER — it provides a service
db = DatabaseServer()
db.store("user_1", {"name": "Alice"})
db.fetch("user_1")
```

---

## 29. What is a Proxy?

A **Proxy** is an object that acts as a **substitute/intermediary** for another object (the real subject). It controls access to the real object, adding logic like caching, access control, or logging.

```python
class RealDatabase:
    def query(self, sql):
        print(f"[DB] Executing: {sql}")
        return f"results for '{sql}'"

class DatabaseProxy:
    def __init__(self):
        self._real = RealDatabase()
        self._cache = {}

    def query(self, sql):
        if sql in self._cache:
            print(f"[Proxy] Cache hit for: {sql}")
            return self._cache[sql]

        print(f"[Proxy] Cache miss, forwarding to DB")
        result = self._real.query(sql)
        self._cache[sql] = result
        return result

proxy = DatabaseProxy()
proxy.query("SELECT * FROM users")    # cache miss -> DB called
proxy.query("SELECT * FROM users")    # cache hit -> DB not called
proxy.query("SELECT * FROM orders")   # cache miss -> DB called
```

---

## 30. What is a Client?

A **Client** is an object that **uses** (calls) the services provided by a Server or Proxy. It initiates requests.

```python
class EmailService:                    # Server
    def send(self, to, message):
        print(f"[EmailService] Sending to {to}: {message}")

class UserRegistration:                # Client
    def __init__(self, email_service):
        self._email = email_service    # client holds reference to server

    def register(self, user_email):
        print(f"Registering {user_email}...")
        self._email.send(user_email, "Welcome to our platform!")   # client calls server

service = EmailService()                   # server
registration = UserRegistration(service)   # client
registration.register("alice@example.com")
```

---

## 31. State of an Object

The **state** of an object is the **current set of values of all its attributes** at a given point in time. State can change over the object's lifetime.

```python
class TrafficLight:
    STATES = ["red", "yellow", "green"]

    def __init__(self):
        self._state_index = 0    # initial state

    @property
    def state(self):
        return self.STATES[self._state_index]

    def next(self):
        self._state_index = (self._state_index + 1) % len(self.STATES)
        print(f"Light is now: {self.state}")

light = TrafficLight()
print(light.state)   # red
light.next()         # yellow
light.next()         # green
light.next()         # red — state cycled back
```

---

## 32. Behavior of an Object

The **behavior** of an object is what it **can do** — the set of methods it exposes. Behavior is defined by the class and may interact with or change the object's state.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance   # state

    # behaviors:
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50)          # behavior changes state
acc.withdraw(30)         # behavior changes state
print(acc.get_balance()) # behavior reads state -> 120
```

---

## 33. Identity of an Object

**Identity** is what makes an object **uniquely itself** — its location in memory. In Python, `id(obj)` returns the memory address. Two objects can have the same state but different identities.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = p1           # p3 is an alias — same object

print(p1 == p2)    # True  — same STATE (we defined __eq__)
print(p1 is p2)    # False — different IDENTITY (different objects in memory)
print(p1 is p3)    # True  — same IDENTITY (same object)

print(id(p1))      # e.g. 140234567890
print(id(p2))      # different number
print(id(p3))      # same as p1
```

---

## 34. What is Hierarchy?

**Hierarchy** in OOP refers to the arrangement of classes in parent-child (superclass-subclass) relationships, forming a tree structure. It enables code reuse and specialization.

```python
class LivingThing:
    def breathe(self): print("Breathing...")

class Animal(LivingThing):
    def move(self): print("Moving...")

class Mammal(Animal):
    def nurse_young(self): print("Nursing young...")

class Dog(Mammal):
    def bark(self): print("Woof!")

class GoldenRetriever(Dog):
    def fetch(self): print("Fetching!")

# Hierarchy: LivingThing -> Animal -> Mammal -> Dog -> GoldenRetriever
g = GoldenRetriever()
g.breathe()      # from LivingThing
g.move()         # from Animal
g.nurse_young()  # from Mammal
g.bark()         # from Dog
g.fetch()        # own

print(GoldenRetriever.__mro__)
```

---

## 35. What is Modularity?

**Modularity** means organizing code into **self-contained, interchangeable units** (classes, modules, packages) with clear interfaces. Changes inside one module don't break others.

```python
class PaymentProcessor:
    def charge(self, amount, card_number):
        print(f"Charging ${amount} to card ending {card_number[-4:]}")
        return True

class NotificationService:
    def notify(self, email, message):
        print(f"Emailing {email}: {message}")

class OrderService:
    def __init__(self, payment: PaymentProcessor, notifier: NotificationService):
        self._payment = payment
        self._notifier = notifier

    def place_order(self, customer_email, amount, card):
        success = self._payment.charge(amount, card)
        if success:
            self._notifier.notify(customer_email, f"Order of ${amount} confirmed!")

# Assemble
payment = PaymentProcessor()
notifier = NotificationService()
orders = OrderService(payment, notifier)
orders.place_order("alice@example.com", 99.99, "1234567890123456")
# Each module is independent and replaceable
```

---

## 36. What is a Static Method?

A **static method** belongs to the class conceptually but has **no access to `self` or `cls`**. It's essentially a regular function namespaced inside a class — used for utility logic related to the class.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.add(3, 4))      # 7  — called on class
print(MathUtils.is_even(8))     # True

obj = MathUtils()
print(obj.add(1, 2))            # 3  — can also be called on instance
# No self/cls parameter — no access to instance or class state
```

---

## 37. What is a Class Method?

A **class method** receives the **class itself** (`cls`) as the first argument instead of the instance. It can access and modify class-level state. Often used as alternative constructors.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):      # alternative constructor
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)     # creates an instance using cls

    @classmethod
    def today(cls):
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

    def __repr__(self):
        return f"Date({self.year}-{self.month:02d}-{self.day:02d})"

d1 = Date(2025, 6, 15)
d2 = Date.from_string("2025-06-15")    # class method as factory
d3 = Date.today()

print(d1)   # Date(2025-06-15)
print(d2)   # Date(2025-06-15)
print(d3)   # Date(today's date)
```

---

## 38. What is an Abstract Class?

An **abstract class** is a class that **cannot be instantiated** and is meant to be subclassed. It can define abstract methods (interface requirements) that subclasses *must* implement, as well as concrete methods with default behavior.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self) -> str: ...       # must be implemented

    @abstractmethod
    def move(self) -> str: ...        # must be implemented

    def describe(self):               # concrete method — shared behavior
        print(f"I am {self.name}. I say '{self.speak()}' and I {self.move()}.")

class Dog(Animal):
    def speak(self): return "Woof"
    def move(self):  return "run"

class Fish(Animal):
    def speak(self): return "..."
    def move(self):  return "swim"

# Animal()   <- TypeError: Can't instantiate abstract class Animal
Dog("Rex").describe()     # I am Rex. I say 'Woof' and I run.
Fish("Nemo").describe()   # I am Nemo. I say '...' and I swim.
```

---

## 39. What is an Interface Class?

Python doesn't have a formal `interface` keyword, but the concept is implemented via **abstract classes with only abstract methods** — no concrete implementations. Every method must be overridden. Alternatively, use `Protocol` for structural interfaces.

```python
from abc import ABC, abstractmethod

# Interface-style ABC — purely abstract, no concrete methods
class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> str: ...

    @abstractmethod
    def deserialize(self, data: str) -> None: ...

class JSONUser(Serializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self):
        import json
        return json.dumps({"name": self.name, "age": self.age})

    def deserialize(self, data):
        import json
        d = json.loads(data)
        self.name = d["name"]
        self.age  = d["age"]

u = JSONUser("Alice", 30)
s = u.serialize()
print(s)                  # {"name": "Alice", "age": 30}

u2 = JSONUser("", 0)
u2.deserialize(s)
print(u2.name, u2.age)    # Alice 30
```

---

## 40. What is the ABC Library?

The `abc` (Abstract Base Classes) module provides tools to define abstract classes. Key components:

| Component | Purpose |
|---|---|
| `ABC` | Convenience base class |
| `ABCMeta` | Metaclass behind ABC |
| `@abstractmethod` | Marks a method as abstract |
| `.register()` | Virtual subclassing |

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self): ...

    @property
    @abstractmethod
    def color(self) -> str: ...     # abstract property

class Circle(Drawable):
    def __init__(self):
        self._color = "red"

    def draw(self):
        print(f"Drawing a {self._color} circle")

    @property
    def color(self):
        return self._color

# Register without inheriting
class Triangle:
    def draw(self): print("Drawing a triangle")
    @property
    def color(self): return "blue"

Drawable.register(Triangle)

c = Circle()
c.draw()                                   # Drawing a red circle
print(isinstance(Triangle(), Drawable))    # True — registered
print(Drawable.__abstractmethods__)        # frozenset({'draw', 'color'})
```

---

## 41. What is super()?

`super()` returns a **proxy object** that delegates method calls to the **next class in the MRO** (not necessarily the direct parent). Essential for proper cooperative multiple inheritance.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()   # delegates to A

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()   # delegates to A (or next in MRO)

class D(B, C):            # MRO: D -> B -> C -> A
    def hello(self):
        print("Hello from D")
        super().hello()   # delegates to B (next in MRO)

D().hello()
# Hello from D
# Hello from B
# Hello from C  <- because B's super() is C in D's MRO, not A!
# Hello from A

# super() in __init__
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed

d = Dog("Rex", "Labrador")
print(d.name, d.breed)   # Rex Labrador
```

---

## 42. Dunder Methods: `__slots__`, `__call__`, `__new__`, `__iter__`, `__str__`, `__repr__`

### `__repr__` and `__str__`

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Unambiguous, for developers — used in REPL and repr()
        return f"Vector(x={self.x}, y={self.y})"

    def __str__(self):
        # Human-readable — used by print() and str()
        return f"({self.x}, {self.y})"

v = Vector(3, 4)
print(repr(v))   # Vector(x=3, y=4)
print(str(v))    # (3, 4)
print(v)         # (3, 4)  <- print() uses __str__
```

### `__call__`

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):    # makes the object callable like a function
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))        # 10
print(triple(5))        # 15
print(callable(double)) # True
```

### `__new__`

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):    # called BEFORE __init__
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

s1 = Singleton(10)
s2 = Singleton(99)
print(s1 is s2)     # True — same object
print(s1.value)     # 99  — __init__ ran again on same object
```

### `__iter__` and `__next__`

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):       # makes object iterable
        return self

    def __next__(self):       # called on each iteration
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(5):
    print(n, end=" ")   # 5 4 3 2 1
```

### `__slots__`

```python
class Point:
    __slots__ = ["x", "y"]   # restricts attributes, saves memory

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x)       # 1
# p.z = 3        # AttributeError — z not in __slots__
# p.__dict__     # AttributeError — no __dict__ with __slots__

# Memory benefit: instances without __dict__ are leaner
# Useful when creating millions of small objects
import sys

class WithDict:
    def __init__(self, x, y): self.x = x; self.y = y

class WithSlots:
    __slots__ = ["x", "y"]
    def __init__(self, x, y): self.x = x; self.y = y

print(sys.getsizeof(WithDict(1, 2)))    # larger
print(sys.getsizeof(WithSlots(1, 2)))   # smaller
```

---

## 43. What is the Singleton Pattern?

The **Singleton** pattern ensures a class has **only one instance** throughout the program's lifetime, providing a global access point to it. Common uses: config managers, connection pools, loggers.

```python
# Method 1: Using __new__
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}    # initialized once
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        return self._settings.get(key)

c1 = Config()
c2 = Config()
c1.set("theme", "dark")

print(c1 is c2)           # True — same instance
print(c2.get("theme"))    # dark  — shared state


# Method 2: Using a decorator (cleaner)
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)
        print(f"[LOG] {msg}")

l1 = Logger()
l2 = Logger()
l1.log("App started")
print(l1 is l2)           # True
print(len(l2.logs))       # 1 — shared log list
```

---

*End of Python OOP Complete Reference*
