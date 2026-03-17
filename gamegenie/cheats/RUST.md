# Rust Introductory Cheatsheet

- [Rust Introductory Cheatsheet](#rust-introductory-cheatsheet)
  - [1. Basic Syntax](#1-basic-syntax)
    - [Variables \& Constants](#variables--constants)
    - [Data Types](#data-types)
    - [Functions](#functions)
    - [Control Flow](#control-flow)
  - [2. Ownership \& Borrowing](#2-ownership--borrowing)
    - [Ownership Rules](#ownership-rules)
  - [3. Collections](#3-collections)
  - [4. Structs \& Enums](#4-structs--enums)
    - [Structs](#structs)
    - [Enums](#enums)
  - [5. Traits \& Implementations](#5-traits--implementations)
  - [6. Modules \& Imports](#6-modules--imports)
  - [7. Error Handling](#7-error-handling)
  - [8. Coding Conventions](#8-coding-conventions)
  - [Notes](#notes)


## 1. Basic Syntax

### Variables & Constants

```rust
let x = 5;              // immutable variable
let mut y = 10;         // mutable variable
const MAX_POINTS: u32 = 100_000;  // constant (always immutable)
```

### Data Types

```rust
let a: i32 = 42;        // integer
let b: f64 = 3.14;      // floating-point
let c: bool = true;     // boolean
let d: char = 'Z';      // character
let s: &str = "Hello";  // string slice
```

### Functions

```rust
fn main() {
    greet("Rust");
}

fn greet(name: &str) {
    println!("Hello, {}!", name);
}
```

### Control Flow

```rust
if x < 5 {
    println!("small");
} else if x == 5 {
    println!("equal");
} else {
    println!("large");
}

// loop
let mut counter = 0;
loop {
    counter += 1;
    if counter == 3 { break; }
}

// while
while counter < 5 {
    counter += 1;
}

// for
for i in 0..5 {
    println!("{}", i);
}
```

## 2. Ownership & Borrowing

### Ownership Rules

1. Each value has a single owner.
2. When the owner goes out of scope, the value is dropped.
3. You can borrow references with `&`.

```rust
let s = String::from("Hello");
let r1 = &s;           // immutable borrow
let r2 = &s;           // multiple immutable borrows allowed
println!("{} and {}", r1, r2);

let mut s2 = String::from("Hi");
let r3 = &mut s2;      // mutable borrow
r3.push_str(" there!");
```

## 3. Collections

```rust
// Vectors
let mut v = vec![1, 2, 3];
v.push(4);
for i in &v { println!("{}", i); }

// Strings
let mut s = String::from("hello");
s.push_str(" world");

// HashMap
use std::collections::HashMap;
let mut scores = HashMap::new();
scores.insert("Alice", 10);
scores.insert("Bob", 20);
```

## 4. Structs & Enums

### Structs

```rust
struct User {
    username: String,
    active: bool,
}

let user1 = User {
    username: String::from("logan"),
    active: true,
};

println!("{} is active: {}", user1.username, user1.active);
```

### Enums

```rust
enum Direction {
    North,
    South,
    East,
    West,
}

let dir = Direction::North;
match dir {
    Direction::North => println!("Going up"),
    Direction::South => println!("Going down"),
    _ => println!("Sideways"),
}
```

## 5. Traits & Implementations

A trait in Rust is basically a collection of methods that define shared behavior—kind of like an interface / abstract class in other languages.

_“Any type that implements this trait must provide these methods.”_

```rust
trait Speak {
    fn talk(&self);
}

struct Dog;

impl Speak for Dog {
    fn talk(&self) {
        println!("woof");
    }
}

let d = Dog;
d.talk();
```

## 6. Modules & Imports

```rust
mod greetings {
    pub fn hello() {
        println!("Hello from module!");
    }
}

fn main() {
    greetings::hello();
}
```

## 7. Error Handling

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division by zero"))
    } else {
        Ok(a / b)
    }
}

match divide(10.0, 0.0) {
    Ok(result) => println!("Result: {}", result),
    Err(e) => println!("Error: {}", e),
}
```

## 8. Coding Conventions

* Use `snake_case` for variables and functions.
* Use `PascalCase` for structs, enums, and traits.
* Avoid unnecessary clones; prefer borrowing.
* Always include a `main` function for executables.
* Use `Result<T, E>` instead of panicking (`unwrap`) in production.
* Group imports logically (std, external crates, local modules).
* Prefer explicit type annotations when code clarity benefits.

---

**Quick Reference:**

* `cargo new project_name` → create new project
* `cargo run` → build and run
* `cargo build --release` → optimized build
* `rustfmt` → format code
* `clippy` → lint for idiomatic Rust

## Notes

__Double Colon (`::`)__ == `/` or `.` to separate namespaces and access a "class's" function

