In Rust, you can make and handle HTTP requests using external crates. One popular crate for this purpose is `reqwest`. Below is a simple example demonstrating how to use `reqwest` to make a basic HTTP GET request:

1. Add the `reqwest` crate to your `Cargo.toml` file:

   ```toml
   [dependencies]
   reqwest = "0.11"
   ```

   Make sure to check for the latest version on [crates.io](https://crates.io/crates/reqwest).

2. Use the `reqwest` crate in your Rust code:

   ```rust
   use reqwest;

   fn main() -> Result<(), reqwest::Error> {
       // Make a GET request to a URL
       let response = reqwest::blocking::get("https://www.example.com")?;

       // Check if the request was successful (status code 2xx)
       if response.status().is_success() {
           // Print the body of the response
           println!("{}", response.text()?);
       } else {
           // Print the status code and reason phrase for unsuccessful requests
           println!("Request failed with status code: {}", response.status());
       }

       Ok(())
   }
   ```

   In this example:

   - We use `reqwest::blocking::get` to make a synchronous GET request to the specified URL.
   - We check if the response status is successful using `response.status().is_success()`.
   - If successful, we print the body of the response using `response.text()?`. Note the use of `?` for error propagation.

To run this example, make sure to include the `reqwest` crate in your project by running `cargo build` or `cargo run`.

Additionally, `reqwest` provides features for more advanced use cases, such as handling request headers, handling response headers, sending JSON payloads, and handling timeouts. You can refer to the official documentation of `reqwest` for more details: [reqwest documentation](https://docs.rs/reqwest).