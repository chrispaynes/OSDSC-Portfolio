In Rust, structs and enums are two fundamental constructs used for defining custom data types. They allow you to create complex data structures that suit the needs of your application.

### Structs:

A struct, short for "structure," is a way to bundle different data types together under a single name. You can think of a struct as a record or object in other languages. Here's an example of defining and using a struct:

```rust
// Define a struct named `Person`
struct Person {
    name: String,
    age: u32,
    is_student: bool,
}

fn main() {
    // Create an instance of the `Person` struct
    let alice = Person {
        name: String::from("Alice"),
        age: 25,
        is_student: true,
    };

    // Access fields of the struct
    println!("Name: {}, Age: {}, Student: {}", alice.name, alice.age, alice.is_student);
}
```

In this example:

- The `Person` struct has three fields: `name` (a `String`), `age` (an unsigned 32-bit integer), and `is_student` (a boolean).
- An instance of the `Person` struct, `alice`, is created with specific values for each field.
- The values of the fields can be accessed using dot notation (`alice.name`, `alice.age`, `alice.is_student`).

### Enums:

Enums, short for "enumerations," allow you to define a type that can have different variants. Each variant can have its own data associated with it. Enums are useful for representing a fixed set of possibilities. Here's an example:

```rust
// Define an enum named `Shape`
enum Shape {
    Circle(f64),   // Variant with a single field (radius)
    Rectangle(f64, f64),  // Variant with two fields (width, height)
}

fn main() {
    // Create instances of the `Shape` enum
    let circle = Shape::Circle(5.0);
    let rectangle = Shape::Rectangle(4.0, 6.0);

    // Match on the enum variants to perform different actions
    match circle {
        Shape::Circle(radius) => {
            println!("Circle with radius: {}", radius);
        }
        Shape::Rectangle(width, height) => {
            println!("Rectangle with width: {}, height: {}", width, height);
        }
    }
}
```

In this example:

- The `Shape` enum has two variants: `Circle` and `Rectangle`.
- Each variant can carry associated data; for example, the `Circle` variant carries a single `f64` (radius), and the `Rectangle` variant carries two `f64` values (width and height).
- Instances of the `Shape` enum can be created using the defined variants, and the associated data can be accessed when matching on the enum.

Both structs and enums play a crucial role in Rust's ownership and borrowing system, making it a memory-safe language. They are essential for defining custom data structures and modeling complex scenarios in Rust programs.