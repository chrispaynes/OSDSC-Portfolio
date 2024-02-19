Concurrency patterns in Rust leverage the ownership and borrowing system, along with Rust's powerful abstractions, to ensure memory safety and prevent data races. Rust provides several concurrency patterns, and here are some common ones:

1. **Thread-Based Concurrency:**
   Rust supports creating threads for concurrent execution. The `std::thread` module provides functions for spawning threads. The ownership system ensures that data is not shared between threads without proper synchronization.

   Example:
   ```rust
   use std::thread;

   fn main() {
       let handle = thread::spawn(|| {
           // Thread code
       });

       // Do some work in the main thread

       handle.join().unwrap(); // Wait for the spawned thread to finish
   }
   ```

2. **Message Passing:**
   Channels are used for communication between threads. The `std::sync::mpsc` module provides a multiple-producer, single-consumer channel for sending messages between threads.

   Example:
   ```rust
   use std::sync::mpsc;
   use std::thread;

   fn main() {
       let (sender, receiver) = mpsc::channel();

       thread::spawn(move || {
           sender.send("Hello from the thread").unwrap();
       });

       let message = receiver.recv().unwrap();
       println!("{}", message);
   }
   ```

3. **Mutexes and Locks:**
   Mutexes (Mutual Exclusion) and locks are used to synchronize access to shared data between threads. The `std::sync` module provides `Mutex` and `RwLock` for exclusive and shared access, respectively.

   Example with Mutex:
   ```rust
   use std::sync::{Mutex, Arc};
   use std::thread;

   fn main() {
       let counter = Arc::new(Mutex::new(0));
       let mut handles = vec![];

       for _ in 0..10 {
           let counter = Arc::clone(&counter);
           let handle = thread::spawn(move || {
               let mut num = counter.lock().unwrap();
               *num += 1;
           });
           handles.push(handle);
       }

       for handle in handles {
           handle.join().unwrap();
       }

       println!("Result: {}", *counter.lock().unwrap());
   }
   ```

4. **Atomic Operations:**
   The `std::sync::atomic` module provides atomic operations for shared memory. These operations are suitable for simple operations where data races can be avoided without using locks.

   Example:
   ```rust
   use std::sync::atomic::{AtomicBool, Ordering};
   use std::thread;

   fn main() {
       let flag = AtomicBool::new(true);

       let handle = thread::spawn(move || {
           flag.store(false, Ordering::SeqCst);
       });

       // Do some work in the main thread

       handle.join().unwrap();

       println!("Flag: {}", flag.load(Ordering::SeqCst));
   }
   ```

5. **Futures and Async/Await:**
   Rust's asynchronous programming model uses futures and async/await syntax. The `async` and `await` keywords, along with the `tokio` or `async-std` runtime, enable writing asynchronous, non-blocking code.

   Example:
   ```rust
   use tokio::time::sleep;
   use std::time::Duration;

   async fn async_example() {
       println!("Start");
       sleep(Duration::from_secs(2)).await;
       println!("End");
   }

   #[tokio::main]
   async fn main() {
       async_example().await;
   }
   ```

These concurrency patterns in Rust provide developers with flexibility and control over concurrent execution while maintaining safety. The ownership system and type system help prevent common concurrency issues such as data races and deadlocks. Developers can choose the concurrency model that best fits the requirements of their application.