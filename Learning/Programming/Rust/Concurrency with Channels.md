Concurrency with channels in Rust involves using the `std::sync::mpsc` module, which provides a multi-producer, single-consumer channel. This allows communication between different threads, and it is often used for passing messages in concurrent Rust programs.

Here's a simple example demonstrating concurrency with channels in Rust:

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    // Create a channel
    let (tx, rx) = mpsc::channel();

    // Spawn a thread to send messages
    let sender_thread = thread::spawn(move || {
        for i in 0..5 {
            // Send messages through the channel
            tx.send(i).unwrap();
            thread::sleep(std::time::Duration::from_millis(200)); // Simulate some work
        }
    });

    // Main thread receives messages
    for received in rx {
        println!("Received: {}", received);
    }

    // Wait for the sender thread to finish
    sender_thread.join().unwrap();
}
```

In this example, the `mpsc::channel()` function creates a channel with a sender (`tx`) and a receiver (`rx`). The `sender_thread` is spawned to send messages through the channel, and the main thread receives and prints those messages.

Key points:

1. `tx.send(i).unwrap()` sends a message through the channel. The `send` method returns a `Result`, and `unwrap` is used to handle errors in a straightforward manner for this example.

2. The main thread consumes messages from the receiver (`rx`) by iterating over it. The loop will continue until the sender closes the channel.

3. The `thread::sleep` is added to simulate some work in the sender thread between sending messages.

Concurrency with channels is useful for coordinating work between different parts of a program, such as splitting tasks among multiple threads. The channel provides a safe and synchronized way to pass data between threads in a concurrent Rust application.