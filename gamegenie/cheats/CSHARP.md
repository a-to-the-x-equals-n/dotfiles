# C# Introductory Cheat Sheet

- [C# Introductory Cheat Sheet](#c-introductory-cheat-sheet)
  - [1. Types \& Variables](#1-types--variables)
  - [2. Control Flow](#2-control-flow)
  - [3. Classes \& Interfaces](#3-classes--interfaces)
  - [4. Properties \& Auto-Properties](#4-properties--auto-properties)
  - [5. Records](#5-records)
  - [6. Collections](#6-collections)
  - [7. LINQ](#7-linq)
  - [8. Async / Await](#8-async--await)
  - [9. Nullability](#9-nullability)
  - [10. Pattern Matching](#10-pattern-matching)
  - [11. Coding Conventions](#11-coding-conventions)


## 1. Types & Variables

```csharp
int x = 42;
double pi = 3.14;
bool flag = true;
char ch = 'A';
string name = "Logan";

// type inference
var count = 10;
var greeting = "hello";

// constants
const int MaxItems = 100;

// string interpolation
string msg = $"Hello, {name}! Count: {count}";

// verbatim strings (no escape processing)
string path = @"C:\Users\Logan\file.txt";
```

## 2. Control Flow

```csharp
// if / else
if (x > 0)
    Console.WriteLine("positive");
else if (x == 0)
    Console.WriteLine("zero");
else
    Console.WriteLine("negative");

// switch expression (modern)
string label = x switch {
    > 0  => "positive",
    0    => "zero",
    _    => "negative"
};

// for / foreach / while
for (int i = 0; i < 5; i++) { }

foreach (var item in collection) { }

while (flag) { flag = false; }
```

## 3. Classes & Interfaces

```csharp
// class
public class Animal {
    public string Name { get; set; }

    public Animal(string name) {
        Name = name;
    }

    public virtual string Speak() => "...";
}

// inheritance
public class Dog : Animal {
    public Dog(string name) : base(name) { }

    public override string Speak() => "Woof!";
}

// interface
public interface IMovable {
    void Move(int dx, int dy);
}

// implementing multiple interfaces
public class Player : Animal, IMovable {
    public void Move(int dx, int dy) { /* ... */ }
}
```

## 4. Properties & Auto-Properties

```csharp
public class Person {
    // auto-property
    public string Name { get; set; } = "Unknown";

    // read-only
    public int Age { get; }

    // computed
    public string Display => $"{Name} (age {Age})";

    // init-only (set only during construction)
    public string Id { get; init; }
}

var p = new Person { Name = "Logan", Id = "001" };
```

## 5. Records

Records are immutable reference types with value-based equality.

```csharp
// positional record (compact syntax)
public record Point(double X, double Y);

var p1 = new Point(1.0, 2.0);
var p2 = p1 with { Y = 5.0 };  // non-destructive mutation

// full record syntax
public record User {
    public required string Name { get; init; }
    public int Age { get; init; }
}
```

## 6. Collections

```csharp
// List<T>
var list = new List<int> { 1, 2, 3 };
list.Add(4);
list.Remove(2);

// Dictionary<TKey, TValue>
var dict = new Dictionary<string, int> {
    ["alice"] = 10,
    ["bob"] = 20
};
dict.TryGetValue("alice", out int score);

// HashSet<T>
var set = new HashSet<string> { "a", "b", "c" };
set.Add("d");
bool has = set.Contains("a");

// IEnumerable is the base for all collections / LINQ
```

## 7. LINQ

```csharp
using System.Linq;

var numbers = new[] { 1, 2, 3, 4, 5, 6 };

// query syntax
var evens = from n in numbers
            where n % 2 == 0
            select n * 2;

// method syntax (more common)
var result = numbers
    .Where(n => n % 2 == 0)
    .Select(n => n * 2)
    .ToList();

// common operators
numbers.First(n => n > 3);          // first match or exception
numbers.FirstOrDefault(n => n > 9); // first match or default
numbers.Any(n => n > 4);            // true if any match
numbers.All(n => n > 0);            // true if all match
numbers.OrderBy(n => n).ToArray();
numbers.GroupBy(n => n % 2);        // group by even/odd
numbers.Sum();
numbers.Average();
numbers.Min(); numbers.Max();
```

## 8. Async / Await

```csharp
// mark method async and return Task or Task<T>
public async Task<string> FetchDataAsync(string url) {
    using var client = new HttpClient();
    string result = await client.GetStringAsync(url);
    return result;
}

// fire-and-forget (avoid when possible)
_ = DoWorkAsync();

// running multiple tasks in parallel
var t1 = FetchDataAsync(url1);
var t2 = FetchDataAsync(url2);
var results = await Task.WhenAll(t1, t2);

// cancellation
public async Task WorkAsync(CancellationToken ct) {
    await Task.Delay(1000, ct);
}
```

## 9. Nullability

Enable with `<Nullable>enable</Nullable>` in .csproj.

```csharp
string? nullable = null;         // explicitly nullable
string nonNull = "hello";        // compiler warns if assigned null

// null-conditional operator
int? len = nullable?.Length;

// null-coalescing
string display = nullable ?? "default";

// null-coalescing assignment
nullable ??= "assigned if null";

// null-forgiving (use sparingly)
string forced = nullable!;
```

## 10. Pattern Matching

```csharp
object obj = "hello";

// type patterns
if (obj is string s)
    Console.WriteLine(s.ToUpper());

// switch with patterns
string Describe(object o) => o switch {
    int i when i < 0     => "negative int",
    int i                => $"int: {i}",
    string { Length: 0 } => "empty string",
    string s             => $"string: {s}",
    null                 => "null",
    _                    => "something else"
};

// list patterns (C# 11+)
int[] arr = { 1, 2, 3 };
if (arr is [1, .. var rest])
    Console.WriteLine($"starts with 1, rest has {rest.Length} elements");
```

## 11. Coding Conventions

* `PascalCase` for classes, methods, properties, and constants.
* `camelCase` for local variables and parameters.
* `_camelCase` for private fields.
* Interfaces are prefixed with `I` (e.g., `IDisposable`).
* Prefer `var` when the type is obvious from the right-hand side.
* Prefer expression-bodied members (`=>`) for single-line methods/properties.
* Use `async`/`await` throughout; never block with `.Result` or `.Wait()`.
* Prefer records for immutable data, classes for mutable stateful objects.

---

**Quick Reference:**

| Concept | Syntax |
|---|---|
| String interpolation | `$"Hello, {name}"` |
| Null-conditional | `obj?.Property` |
| Null-coalescing | `value ?? fallback` |
| Lambda | `x => x * 2` |
| Expression body | `public int Double(int x) => x * 2;` |
| Primary constructor (C# 12) | `class Foo(int X) { }` |
| Deconstruction | `var (a, b) = point;` |
| Range/index | `arr[1..^1]`, `arr[^1]` |
