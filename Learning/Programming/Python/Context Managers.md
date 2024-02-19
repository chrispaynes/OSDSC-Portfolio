In Python, a context manager is an object that is used to set up a resource before a block of code is executed and ensure that the resource is properly cleaned up after the code block finishes, regardless of whether the block succeeds or raises an exception. Context managers are typically used with the `with` statement.

In Python, context managers are implemented using two methods: `__enter__` and `__exit__`.

Here's a brief overview:

1. **`__enter__` method:**
   The `__enter__` method is called when the `with` block is entered. It performs the setup or resource allocation. The result returned from `__enter__` can be assigned to a variable using the `as` keyword.

2. **`__exit__` method:**
   The `__exit__` method is called when the `with` block is exited. It is responsible for cleaning up resources. If an exception occurs within the `with` block, the exception information is passed to the `__exit__` method, allowing it to handle exceptions.

Here's an example using a file as a context manager:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # The value returned by __enter__ and assigned to the variable after 'as'

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Cleanup code goes here

# Using the context manager with the 'with' statement
with MyContextManager() as cm:
    print("Inside the context")

# Output:
# Entering the context
# Inside the context
# Exiting the context
```

In Python, there is also a built-in `contextlib` module that provides a decorator `contextmanager` for creating simple context managers using generator functions.

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    yield  # The value yielded is returned to the variable after 'as' if used
    print("Exiting the context")

# Using the context manager with the 'with' statement
with my_context_manager():
    print("Inside the context")

# Output:
# Entering the context
# Inside the context
# Exiting the context
```

Context managers are commonly used for tasks like file handling (`open`), database connections, acquiring and releasing locks, and more. They help manage resources efficiently and ensure proper cleanup.