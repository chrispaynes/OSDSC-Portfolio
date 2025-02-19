The Gang of Four (GoF) design patterns refer to a set of 23 classical software design patterns introduced in the book "Design Patterns: Elements of Reusable Object-Oriented Software," written by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides. These patterns are categorized into three groups: creational, structural, and behavioral. Here's a brief description of each category along with examples in Python:

### 1. Creational Design Patterns:

**a. Singleton Pattern:**
   - Ensures a class has only one instance and provides a global point of access to it.
   - Commonly used for logging, driver objects, caching, thread pools, and database connections.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
singleton_instance_1 = Singleton()
singleton_instance_2 = Singleton()
print(singleton_instance_1 is singleton_instance_2)  # True
```

**b. Factory Method Pattern:**
   - Defines an interface for creating an object but leaves the choice of its type to the subclasses.
   - Allows a class to delegate the instantiation to its subclasses.

```python
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        return "Product A"

class ConcreteProductB(Product):
    def create(self):
        return "Product B"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        product = self.factory_method()
        return product.create()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage
creator_a = ConcreteCreatorA()
print(creator_a.create_product())  # Product A

creator_b = ConcreteCreatorB()
print(creator_b.create_product())  # Product B
```

**c. Abstract Factory Pattern:**
   - Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
   - Useful when a system needs to be independent of how its objects are created, composed, and represented.

```python
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return "Product A1"

    def create_product_b(self):
        return "Product B1"

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return "Product A2"

    def create_product_b(self):
        return "Product B2"

# Usage
factory_1 = ConcreteFactory1()
product_a_1 = factory_1.create_product_a()
product_b_1 = factory_1.create_product_b()

factory_2 = ConcreteFactory2()
product_a_2 = factory_2.create_product_a()
product_b_2 = factory_2.create_product_b()
```

**d. Builder Pattern:**
   - Separates the construction of a complex object from its representation.
   - Allows the same construction process to create different representations.

```python
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_result(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def get_result(self):
        return self.product

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

# Usage
director = Director(ConcreteBuilder())
director.construct()
product = director.get_product()
```

**e. Prototype Pattern:**
   - Creates new objects by copying an existing object, known as the prototype.
   - Reduces the need for subclassing when creating new objects.

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

# Usage
prototype = ConcretePrototype(1)
clone = prototype.clone()
```

---
### 2. Structural Design Patterns:

Certainly! Here are the structural design patterns from the Gang of Four (GoF) with brief descriptions:

### 1. Adapter Pattern:

**Description:**
   - Allows the interface of an existing class to be used as another interface.
   - Often used to make existing classes work with others without modifying their source code.

**Example in Python:**
```python
class Adaptee:
    def specific_request(self):
        return "Adaptee request"

class Target:
    def request(self):
        return "Target request"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter using {self.adaptee.specific_request()}"

# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
result = adapter.request()
```

### 2. Bridge Pattern:

**Description:**
   - Separates abstraction from implementation so that the two can vary independently.
   - Allows a class to have its own implementation.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Implementor(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorA operation"

class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        return "ConcreteImplementorB operation"

class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        return f"Abstraction using {self.implementor.operation_implementation()}"

# Usage
implementor_a = ConcreteImplementorA()
implementor_b = ConcreteImplementorB()

abstraction_1 = Abstraction(implementor_a)
result_1 = abstraction_1.operation()

abstraction_2 = Abstraction(implementor_b)
result_2 = abstraction_2.operation()
```

### 3. Composite Pattern:

**Description:**
   - Composes objects into tree structures to represent part-whole hierarchies.
   - Clients can treat individual objects and compositions of objects uniformly.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf operation"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite operation with: {', '.join(results)}"

# Usage
leaf_1 = Leaf()
leaf_2 = Leaf()

composite = Composite()
composite.add(leaf_1)
composite.add(leaf_2)

result = composite.operation()
```

### 4. Decorator Pattern:

**Description:**
   - Attaches additional responsibilities to an object dynamically.
   - Provides a flexible alternative to subclassing for extending functionality.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent operation"

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return f"Decorator operation using {self.component.operation()}"

class ConcreteDecoratorA(Decorator):
    def added_operation(self):
        return "ConcreteDecoratorA added operation"

    def operation(self):
        return f"{super().operation()} with {self.added_operation()}"

# Usage
concrete_component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(concrete_component)
result = decorator_a.operation()
```

### 5. Facade Pattern:

**Description:**
   - Provides a unified interface to a set of interfaces in a subsystem.
   - Defines a higher-level interface that makes the subsystem easier to use.

**Example in Python:**
```python
class SubsystemA:
    def operation_a(self):
        return "SubsystemA operation"

class SubsystemB:
    def operation_b(self):
        return "SubsystemB operation"

class Facade:
    def __init__(self, subsystem_a, subsystem_b):
        self.subsystem_a = subsystem_a
        self.subsystem_b = subsystem_b

    def operation(self):
        result_a = self.subsystem_a.operation_a()
        result_b = self.subsystem_b.operation_b()
        return f"Facade operation with: {result_a}, {result_b}"

# Usage
subsystem_a = SubsystemA()
subsystem_b = SubsystemB()

facade = Facade(subsystem_a, subsystem_b)
result = facade.operation()
```

### 6. Flyweight Pattern:

**Description:**
   - Minimizes memory usage or computational expenses by sharing as much as possible with related objects.
   - Externalizes the state of shared objects, making them lightweight.

**Example in Python:**
```python
class Flyweight:
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        return f"ConcreteFlyweight operation with {extrinsic_state}"

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyweight()
        return self.flyweights[key]

# Usage
factory = FlyweightFactory()

flyweight_1 = factory.get_flyweight("key_1")
result_1 = flyweight_1.operation("state_1")

flyweight_2 = factory.get_flyweight("key_1")  # Reusing existing flyweight
result_2 = flyweight_2.operation("state_2")
```

### 7. Proxy Pattern:

**Description:**
   - Provides a surrogate or placeholder for another object to control access to it.
   - Can be used for various purposes such as lazy loading, access control, logging, etc.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject request"

class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        # Additional operations can be added before or after delegating to the real subject
        return f"Proxy request using {self.real_subject.request()}"

# Usage
real_subject = RealSubject()
proxy = Proxy(real_subject)
result = proxy.request()
```

These are some of the structural design patterns from the Gang of Four (GoF) book. Each pattern addresses specific problems and provides a solution that promotes flexibility, maintainability, and reusability in software design.

---

Certainly! Let's continue with the Behavioral Design Patterns from the Gang of Four (GoF) book:

### 8. Chain of Responsibility Pattern:

**Description:**
   - Passes a request along a chain of handlers.
   - Each handler decides either to process the request or to pass it to the next handler in the chain.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return f"ConcreteHandlerA handles {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return f"No handler can process {request}"

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return f"ConcreteHandlerB handles {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return f"No handler can process {request}"

# Usage
handler_chain = ConcreteHandlerA(ConcreteHandlerB())
result_a = handler_chain.handle_request("A")
result_c = handler_chain.handle_request("C")
```

### 9. Command Pattern:

**Description:**
   - Encapsulates a request as an object, allowing for parameterization of clients with different requests.
   - Decouples the sender of a request from its receiver.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        return self.receiver.action()

class Receiver:
    def action(self):
        return "Receiver action"

class Invoker:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        return self.command.execute()

# Usage
receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker(command)
result = invoker.invoke()
```

### 10. Interpreter Pattern:

**Description:**
   - Defines a grammar for interpreting the sentences in a language.
   - Provides an interpreter to interpret sentences of the language.

**Example in Python:**
```python
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class TerminalExpression(Expression):
    def __init__(self, data):
        self.data = data

    def interpret(self):
        return f"TerminalExpression interprets {self.data}"

class NonTerminalExpression(Expression):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self):
        return f"NonTerminalExpression interprets {self.expression1.interpret()} and {self.expression2.interpret()}"

# Usage
expression = NonTerminalExpression(TerminalExpression("A"), TerminalExpression("B"))
result = expression.interpret()
```

These behavioral design patterns focus on defining how objects interact and communicate with each other. They provide solutions to common challenges related to managing the flow of control and responsibilities in a system.