Data Classes in Python are a feature introduced in Python 3.7 (PEP 557) to simplify the creation of classes that primarily store data. They are designed to reduce boilerplate code by automatically generating special methods such as `__init__`, `__repr__`, `__eq__`, and `__hash__` based on the class attributes.

Here's a basic example of a data class:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # Default value for z

# Creating instances of the data class
p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)

# Automatically generated methods
print(p1)  # Output: Point(x=1.0, y=2.0, z=0.0)
print(p1 == p2)  # Output: True
```

In the example above, the `@dataclass` decorator is used to create a `Point` class with attributes `x`, `y`, and an optional default value for `z`. The decorator automatically generates the `__init__`, `__repr__`, `__eq__`, and `__hash__` methods based on the specified attributes.

Key features of data classes include:

1. **Automatic `__init__` method:** The constructor is automatically generated based on the annotated attributes.

2. **Automatic `__repr__` method:** A human-readable string representation of the object is automatically generated.

3. **Automatic `__eq__` method:** An equality method is automatically generated, comparing the attribute values.

4. **Automatic `__hash__` method:** A hash method is automatically generated, allowing instances to be used in hash-based collections like sets and dictionaries.

5. **Default values:** You can provide default values for attributes.

6. **Inheritance:** Data classes support inheritance, and the generated methods take superclass attributes into account.

Data classes simplify the creation and maintenance of classes that are primarily used for holding data, making the code more concise and readable. They are particularly useful in scenarios where you need simple classes to store structured data without a lot of additional logic.