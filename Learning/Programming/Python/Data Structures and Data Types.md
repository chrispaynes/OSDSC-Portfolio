Python supports a variety of built-in data structures and data types. Here's an overview of some of the key ones:

1. **Numeric Types:**
   - `int`: Integer data type (e.g., 5, -10).
   - `float`: Floating-point data type (e.g., 3.14, -2.0).

2. **Sequence Types:**
   - `str`: String data type (e.g., 'hello', "world").
   - `list`: Ordered and mutable collection (e.g., [1, 2, 3]).
   - `tuple`: Ordered and immutable collection (e.g., (1, 2, 3)).

3. **Set Types:**
   - `set`: Unordered collection of unique elements (e.g., {1, 2, 3}).

4. **Mapping Type:**
   - `dict`: Unordered collection of key-value pairs (e.g., {'key': 'value'}).

5. **Boolean Type:**
   - `bool`: Represents boolean values, either True or False.

6. **None Type:**
   - `None`: Represents the absence of a value or a null-like value.

7. **Collections Module:**
   - `collections`: Module provides additional data structures like `deque`, `Counter`, `namedtuple`, etc.

8. **Other Built-in Types:**
   - `complex`: Represents complex numbers (e.g., 2 + 3j).
   - `bytes` and `bytearray`: Represent sequences of bytes.
   - `range`: Represents a sequence of numbers.

These data structures and types form the foundation for building more complex data structures and handling various types of data in Python.

---

In Python, you can access, slice, and reverse lists using various techniques. Here are some examples:

1. **Accessing Elements:**
   - You can access elements in a list using their index. Indexing starts from 0.
   ```python
   my_list = [10, 20, 30, 40, 50]
   first_element = my_list[0]  # Access the first element
   second_element = my_list[1]  # Access the second element
   last_element = my_list[-1]  # Access the last element
   ```

2. **Slicing Lists:**
   - Slicing allows you to create a new list from a subset of the original list.
   ```python
   my_list = [10, 20, 30, 40, 50]
   sliced_list = my_list[1:4]  # Creates a new list with elements from index 1 to 3
   ```
   - You can omit start or end to slice from the beginning or until the end, respectively.
   ```python
   partial_list = my_list[:3]   # Elements from the beginning to index 2
   tail_list = my_list[2:]      # Elements from index 2 to the end
   ```

3. **Reversing a List:**
   - You can reverse a list using the `reverse()` method.
   ```python
   my_list = [10, 20, 30, 40, 50]
   my_list.reverse()
   print(my_list)  # Output: [50, 40, 30, 20, 10]
   ```
   - Alternatively, you can use slicing to reverse a list.
   ```python
   reversed_list = my_list[::-1]
   ```

These methods provide flexibility in manipulating and extracting information from lists in Python.