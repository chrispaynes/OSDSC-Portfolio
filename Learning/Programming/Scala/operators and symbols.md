# :+
==In Scala, `:+` is an operator used to append an element to a collection, such as a `List`, `Array`, or `Vector`. It is specifically used for adding an element to the end of the collection, effectively extending its size.==

Here's how you can use `:+` to append an element to a collection:

```scala
val numbers = List(1, 2, 3)
val newNumbers = numbers :+ 4

// newNumbers is now List(1, 2, 3, 4)
```

In the example above, `numbers :+ 4` creates a new list `newNumbers` that is a copy of the original list `numbers` with the element `4` appended to the end.

==Note that `:+` is not a method but a special operator, and it is available for several collection types in Scala to perform the append operation efficiently.==

Here's an example using `:+` with an `Array`:

```scala
val fruits = Array("apple", "banana")
val newFruits = fruits :+ "cherry"

// newFruits is now Array("apple", "banana", "cherry")
```

In this case, the `:+" operator appends "cherry" to the end of the `fruits` array, creating a new array `newFruits`.

==Keep in mind that while `:+` is convenient for appending elements to collections, it creates a new collection with the added element, as collections in Scala are typically immutable. If you need to perform many append operations, consider using a mutable collection like `ListBuffer`, `ArrayBuffer`, or `StringBuilder` for more efficient modifications.==

# _
In Scala, the underscore (`_`) is a versatile symbol that can be used in various contexts and has different meanings depending on how it is used. Here are some of the common uses of the underscore in Scala:

1. ==**Placeholder for Unused Parameters**: Underscore can be used as a placeholder for unused parameters in functions or lambdas when you don't need to refer to those parameters within the function body. This is often used to make code more concise.==

   ```scala
   val addOne: Int => Int = _ + 1
   ```

2. ==**Wildcard Import**: In import statements, the underscore can be used as a wildcard to import all members of a package or object.==

   ```scala
   import scala.collection._ // Import all members of the scala.collection package
   ```

3. ==**Wildcard in Pattern Matching**: In pattern matching, underscore can be used as a wildcard to match any value, effectively ignoring that part of the pattern.==

   ```scala
   val list = List(1, 2, 3)
   list match {
     case _ :: rest => println(rest) // Matches any non-empty list and binds the tail to "rest"
     case _ => println("Empty list")
   }
   ```

4. ==**Anonymous Functions**: Underscore can be used as a placeholder for parameters in anonymous functions (lambdas). It represents each parameter in turn.==

   ```scala
   val multiply: (Int, Int) => Int = _ * _
   ```

5. ==**Partially Applied Functions**: Underscore can be used in partially applied functions to indicate that some arguments are not provided yet.==

   ```scala
   def add(a: Int, b: Int): Int = a + b
   val add2: Int => Int = add(_, 2) // Partially apply "add" with the second argument fixed to 2
   ```

6. ==**Discarding Values**: Underscore can be used to discard values that you don't need when calling a function or method.==

   ```scala
   val myList = List(1, 2, 3)
   myList.foreach(_ => println("Hello")) // Discards each element and just prints "Hello"
   ```

7. ==**Lambda Placeholder**: In lambda expressions, the underscore can be used as a placeholder for parameters when defining anonymous functions.==

   ```scala
   val square: Int => Int = _ * _
   ```

8. ==**Wildcard in Case Classes**: In case classes, the underscore can be used as a wildcard to indicate that a field should not be explicitly named in the constructor. This allows the field to be inferred from the order of fields.==

   ```scala
   case class Point(x: Double, y: Double, _: String)
   val p = Point(1.0, 2.0, "Unused") // The third field is inferred without a name
   ```

The meaning of the underscore in Scala depends on the context in which it is used. It's a flexible and powerful feature that allows you to write more concise and expressive code.

# ::  aka "cons"
==In Scala, the `::` symbol is used to construct a new list by prepending an element to an existing list. It is pronounced "cons" and represents a fundamental operation for building and manipulating lists in a functional and recursive manner.==

Here's the syntax for using `::` to prepend an element to a list:

```scala
element :: list
```

- ==`element` is the element you want to add to the beginning of the list.==
- ==`list` is the existing list to which you want to prepend the element.==

Here's an example of using `::` to build a list:

```scala
val list1 = 1 :: 2 :: 3 :: Nil
// list1: List[Int] = List(1, 2, 3)
```

In the example above, `::` is used to construct a list by repeatedly adding elements to the front. The `Nil` at the end indicates an empty list, and it serves as the base case for list construction.

==You can also use `::` in pattern matching to destructure a list:==

```scala
val myList = List(1, 2, 3)

myList match {
  case head :: tail => println(s"Head: $head, Tail: $tail")
  case Nil => println("Empty list")
}
```

==In this pattern match, `head` captures the first element of the list, and `tail` captures the rest of the list.==

The `::` operator is a fundamental building block for working with lists in Scala and is often used in functional programming when constructing lists or pattern matching against them.

# <: aka "upper type bound operator"
In Scala, the `<:` symbol is used to ==denote an upper type bound in type parameter declarations and type annotations. It specifies that a type parameter or type should be a subtype of the specified upper bound type. This means that the type parameter or type must be a class or trait that extends or implements the upper bound type.==

Here's the basic syntax of an upper type bound in Scala:

```scala
[A <: UpperBoundType]
```

- `[A]` is the type parameter.
- `<:` is the upper type bound operator.
- ==`UpperBoundType` is the type to which `[A]` must be a subtype.==

For example, consider a generic function that operates on elements of a collection and returns a new collection of the same type. You can use an upper type bound to ensure that the returned collection is a subtype of the input collection's type:

```scala
def doubleElements[A <: Iterable[Int]](input: A): A = {
  input.map(_ * 2).asInstanceOf[A]
}

val list = List(1, 2, 3)
val set = Set(4, 5, 6)

val doubledList = doubleElements(list) // Returns List(2, 4, 6)
val doubledSet = doubleElements(set)   // Returns Set(8, 10, 12)
```

In the `doubleElements` function, `[A <: Iterable[Int]]` is an upper type bound that ensures that `A` is a subtype of `Iterable[Int]`. This allows you to call `map` on the `input` collection, which is a method provided by `Iterable`, and then cast the result back to type `A`.

==The `<:` symbol is a way to express constraints on type parameters and ensure type safety in generic code. It allows you to specify that a type must be a subtype of another type, which can be helpful for designing generic functions and classes that work with a wide range of types while maintaining type safety.==