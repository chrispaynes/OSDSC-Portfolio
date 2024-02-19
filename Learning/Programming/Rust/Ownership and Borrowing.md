Ownership and borrowing are fundamental concepts in Rust that play a crucial role in managing memory and ensuring memory safety without the need for garbage collection.

### Ownership:

In Rust, each value has a variable that is its "owner." The owner is responsible for cleaning up the value when it's no longer needed. Ownership rules prevent multiple parts of the code from simultaneously accessing or modifying the same data, preventing data races and memory safety issues.

#### Ownership Transfer:

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;  // Ownership of the string is moved to s2, and s1 is invalidated
    // println!("{}", s1); // This would result in a compilation error
    println!("{}", s2); // This is valid
}
```

In this example, the ownership of the `String` is transferred from `s1` to `s2`. This ensures that there's only one owner for the allocated memory, avoiding double frees and dangling references.

### Borrowing:

Borrowing is the mechanism in Rust that allows code to reference a value without taking ownership of it. Borrowing can be either mutable or immutable.

#### Immutable Borrow:

```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1); // Passing an immutable reference to s1
    println!("Length of '{}' is: {}", s1, len);
}

fn calculate_length(s: &String) -> usize { // s is an immutable reference to a String
    s.len()
}
```

Here, `calculate_length` takes an immutable reference (`&String`) to the `String`, allowing it to access the value without taking ownership. This is useful for passing values around without transferring ownership.

#### Mutable Borrow:

```rust
fn main() {
    let mut s = String::from("hello");
    change_string(&mut s); // Passing a mutable reference to s
    println!("Modified string: {}", s);
}

fn change_string(s: &mut String) { // s is a mutable reference to a String
    s.push_str(", world!");
}
```

In this example, `change_string` takes a mutable reference (`&mut String`) to the `String`, allowing it to modify the value. Mutable borrowing ensures that only one part of the code can modify the data at a time, preventing data races.

Ownership and borrowing contribute to Rust's memory safety by enforcing strict rules on how data can be accessed and modified. These concepts enable concurrent programming without the need for a garbage collector, making Rust suitable for systems programming where performance and safety are critical.