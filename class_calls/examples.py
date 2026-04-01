"""
MUST KNOW
class attributes
object attributes
**all the theory related to these
examples
getters
setters
open/protected/private
abstraction
encapsulation
polymorphism
inheritance
class decorators
__slots__
__new__
__call__
__init__
__iter__
super()

init
constructor __new__(cls)
destructor
mutator/accessor (@property and @x.setter)
__del__
__repr__ and __str__

*********
Constructor	__new__(cls)	Allocates memory for the instance.
Initializer	__init__(self)	Sets up object attributes.
Destructor	__del__(self)	Performs cleanup (rarely needed).
Getter	@property	Defines a getter method.
Setter	@<name>.setter	Defines a setter (mutator) method.
*********

del vs __del__
__new__ vs __init__


1. Essential Advanced Topics
Method Resolution Order (MRO): How Python searches for methods in multiple inheritance using the C3 Linearization algorithm.
Abstract Base Classes (ABCs): Using the abc module to define "interfaces" that enforce specific method implementations in subclasses.
Composition over Inheritance: The principle that it is often better to build complex objects by combining simpler ones rather than creating deep inheritance trees.
Metaclasses: "Classes that create classes." They allow you to intercept and modify class creation itself (e.g., to auto-register classes or enforce rules).
Descriptors: The low-level mechanism behind @property, classmethod, and staticmethod that defines how attributes are accessed.
The __slots__ Attribute: A way to explicitly define allowed attributes, which saves memory by preventing the creation of an instance __dict__





2. Tricky Interview Questions & "Gotchas"
The Question 	The "Tricky" Answer / Why it's asked
What's the difference between __getattr__ and __getattribute__?	__getattribute__ is called for every attribute access, while __getattr__ is only a fallback for missing attributes.
Why are mutable default arguments dangerous in methods?	Because a default list (e.g., def add(self, x=[])) is created once at definition time and shared across all instances, leading to data leaking between objects.
How do you solve the "Diamond Problem" in Python?	Python uses MRO (visible via ClassName.mro()) to linearize the hierarchy, ensuring each parent is visited exactly once in a predictable order.
What happens if you forget super().__init__() in a child class?	The parent's __init__ won't run, meaning parent attributes won't be initialized, often leading to AttributeError when those parent methods are called later.
Can you implement a Singleton pattern in Python?	Yes, typically by overriding __new__ to return the same instance every time or using a decorator/metaclass.
Is is the same as == for objects?	No. == checks if values are equal; is checks if they are the same object in memory (identity).





3. Actual "Live" Coding Challenges
Design a File System: You might be asked to design File and Folder classes where a Folder can contain both files and other folders (demonstrating Composition).
Restrict Attribute Creation: "Write a class where users cannot add new attributes after it's initialized" (hint: use __setattr__ or __slots__).
Custom Iterator: Implement a class that can be used in a for loop by defining __iter__ and __next__.



inheritance in python

1. Master These Core Advanced Pillars
Asynchronous Programming (asyncio): In 2025/2026, this is mandatory for high-performance web APIs (FastAPI) and web scraping.
Memory Management & Garbage Collection: Understand how Python uses Reference Counting and the Generational Garbage Collector to prevent memory leaks.
Functional Programming Tools: Master itertools (for memory-efficient loops), functools (for decorators like @lru_cache), and closures.
Metaprogramming: Beyond simple decorators, learn how Metaclasses and Descriptors (the tech behind @property) control class and attribute creation.
Advanced Type Hinting: Using Pydantic or Mypy to enforce strict typing, including Protocols (static duck typing) and Generics.





2. Tricky Interview Questions (General Python)
The Question 	The "Tricky" Answer / Why it's asked
How does the GIL affect Multithreading?	The Global Interpreter Lock prevents multiple threads from executing Python bytecode at once. This means threading is great for I/O-bound tasks (waiting) but useless for CPU-bound tasks (calculating).
What is the difference between deeply copying and shallow copying?	A shallow copy creates a new object but references the original elements (problematic for nested lists). A deep copy recursively copies everything, creating a completely independent object.
Why use a Generator instead of a List?	Generators use Lazy Evaluation; they yield one item at a time instead of storing the whole list in RAM, which is essential for processing massive datasets.
What is "Interning" in Python?	For performance, Python "interns" small integers (typically -5 to 256) and some strings so they reuse the same memory address. This is why a = 10; b = 10; a is b is True.
How does asyncio handle context switching differently than Threads?	asyncio uses Cooperative Multitasking, where the task itself gives up control (via await). Threads use Preemptive Multitasking, where the OS forces switches, which can lead to race conditions.






3. Actual "Modern Python" Topics (3.12 - 3.14)
If you want to sound current in an interview, mention these features:
Free-threaded CPython (Experimental 3.13): The first step toward a GIL-less Python.
Structural Pattern Matching (match/case): Much more powerful than a "switch" statement; it allows for complex data deconstruction.
Typing Improvements: Using the | operator for Unions (e.g., int | str) instead of Union[int, str].
Performance JIT (3.13): An experimental Just-In-Time compiler that aims to significantly speed up certain workloads. 




"""













