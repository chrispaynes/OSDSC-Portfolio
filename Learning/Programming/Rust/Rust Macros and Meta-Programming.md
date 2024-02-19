In Rust, macros are a powerful feature that allows metaprogramming, enabling the definition and generation of code at compile time. Rust macros are a form of compile-time code transformation, allowing you to write code that writes code. There are two main types of macros in Rust: declarative macros (also known as macros by example) and procedural macros.

1. **Declarative Macros (Macros by Example - `macro_rules!`):**
   - Declarative macros are a way to define code patterns using a syntax similar to the one used in the code they will generate.
   - They are created using the `macro_rules!` keyword, followed by the macro definition.
   - Example:

     ```rust
     // Define a simple declarative macro
     macro_rules! say_hello {
         () => {
             println!("Hello, World!");
         };
     }

     fn main() {
         // Use the macro
         say_hello!();
     }
     ```

2. **Procedural Macros:**
   - Procedural macros allow for more advanced code generation by defining functions that are executed at compile time.
   - They are more flexible than declarative macros but also more complex to write.
   - Procedural macros are often used for tasks like deriving implementations of traits (`#[derive]`), custom attribute macros, and more.
   - Example (an overly simplified procedural macro):

     ```rust
     use proc_macro::TokenStream;
     use quote::quote;
     use syn::{parse_macro_input, ItemFn};

     #[proc_macro]
     pub fn my_procedural_macro(input: TokenStream) -> TokenStream {
         // Parse the input tokens into a syntax tree
         let input = parse_macro_input!(input as ItemFn);

         // Generate new code using the quote crate
         let expanded = quote! {
             #input
             fn my_generated_function() {
                 println!("Generated code!");
             }
         };

         // Convert the generated code back into a TokenStream
         TokenStream::from(expanded)
     }
     ```

Rust's macros are hygienic, meaning they operate in their own namespace, preventing unintentional name conflicts. This design choice contributes to Rust's focus on safety and predictability.

To enhance the capabilities of procedural macros, external crates like `syn` (for parsing) and `quote` (for code generation) are commonly used. These crates make it easier to work with the abstract syntax tree (AST) and generate code in a readable way.

Metaprogramming in Rust, using both declarative and procedural macros, enables developers to write more concise and expressive code by automating repetitive tasks and code generation.