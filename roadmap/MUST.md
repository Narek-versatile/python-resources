# 1. MUST KNOW: FUNDAMENTALS (EASY)

## OOP Theory
- Abstraction
- Encapsulation
- Polymorphism
- Inheritance
- Access Modifiers: open / protected / private

## Class and Object Basics
- Class Attributes vs Object Attributes
- Getters and Setters: @property, @<name>.setter (mutator/accessor)
- del vs __del__
- __new__ vs __init__
- super()
- Class Decorators

## Magic (Dunder) Methods
- __new__(cls): Constructor. Allocates memory for the instance.
- __init__(self): Initializer. Sets up object attributes.
- __del__(self): Destructor. Performs cleanup.
- __str__ and __repr__: String representation.
- __call__: Object execution.
- __iter__: Object iteration.
- __slots__: Explicitly define allowed attributes, saving memory by preventing instance __dict__.

# 2. CORE PILLARS: INTERMEDIATE TO ADVANCED (MUST)

## Advanced OOP Concepts
- Composition over Inheritance: Building complex objects by combining simpler ones instead of deep inheritance.
- Method Resolution Order (MRO): How Python resolves methods in multiple inheritance (C3 Linearization).
- Abstract Base Classes (ABCs): Using the abc module to enforce method implementations in subclasses.

## Memory and Performance
- Memory Management & Garbage Collection: Reference Counting and Generational Garbage Collector.
- Interning: Reusing memory addresses for small integers (-5 to 256) and strings to boost performance.

## Advanced Language Features
- Functional Programming: itertools (memory-efficient loops), functools (@lru_cache), closures.
- Advanced Type Hinting: Pydantic, Mypy, Protocols (static duck typing), Generics.
- Asynchronous Programming (asyncio): Cooperative multitasking (await) vs threading (preemptive multitasking).

# 3. METAPROGRAMMING (ADVANCED)

- Descriptors: The low-level mechanism behind @property, classmethod, and staticmethod controlling attribute access.
- Metaclasses: Classes that create classes. Intercept and modify class creation (e.g., auto-registration, rule enforcement).

# 4. TRICKY INTERVIEW QUESTIONS & GOTCHAS

- Mutable Default Arguments: Evaluated once at definition time. Leads to shared state (data leaking) across instances.
- Identity vs Equality: 'is' checks memory address (identity); '==' checks value equality.
- __getattr__ vs __getattribute__: __getattribute__ runs on every access; __getattr__ is only a fallback for missing attributes.
- The Diamond Problem: Handled globally by Python's MRO using C3 linearization.
- Missing super().__init__(): Fails to initialize parent attributes, causing AttributeError on parent methods.
- Singleton Pattern in Python: Implemented by overriding __new__ or using a metaclass/decorator.
- Threading & The GIL: The Global Interpreter Lock prevents parallel Python bytecode execution. Useful for I/O-bound tasks, useless for CPU-bound tasks.
- Deep vs Shallow Copy: Shallow copies inner references; deep copy creates fully independent recursive copies.
- Generators vs Lists: Generators use lazy evaluation to yield items sequentially, saving RAM on large datasets.

# 5. LIVE CODING CHALLENGES

- Design a File System: File and Folder classes demonstrating Composition.
- Restrict Attribute Creation: Prevent adding new attributes post-initialization using __setattr__ or __slots__.
- Custom Iterator: Implement __iter__ and __next__ for a custom class.

# 6. MODERN PYTHON TRENDS 3.12+ (OPTIONAL/ADVANCED)

- Structural Pattern Matching: match/case for complex data deconstruction.
- Typing Improvements: The | operator for Unions (e.g., int | str).
- Free-threaded CPython (3.13): Experimental step toward a GIL-less Python.
- Performance JIT (3.13): Experimental Just-In-Time compiler for speed improvements.
