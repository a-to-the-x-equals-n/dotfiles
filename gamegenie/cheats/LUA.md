# Lua Introductory Cheat Sheet

---

## Basics

```lua
-- single-line comment
--[[ multi-line
comment ]]--

print("hello world")

-- variables (dynamically typed)
x = 10
name = "Logan"
is_ready = true
```

---

## Data Types

| Type     | Example            |
| -------- | ------------------ |
| number   | `x = 3.14`         |
| string   | `s = "hello"`      |
| boolean  | `b = true`         |
| table    | `t = {1, 2, 3}`    |
| function | `function f() end` |
| nil      | `n = nil`          |

---

## Tables (lists, dicts, objects all-in-one)

```lua
-- list
fruits = {"apple", "banana", "cherry"}
print(fruits[1]) -- 1-based indexing!

-- dictionary
person = {name = "Logan", age = 25}
print(person.name)
print(person["age"])

-- adding new fields
person.job = "developer"

-- iterate
for key, value in pairs(person) do
  print(key, value)
end
```

---

## Functions

```lua
function greet(name)
  return "Hello, " .. name
end

print(greet("world"))

-- anonymous / inline
say = function(msg) print(msg) end
say("hi")

-- multiple returns
function divide(a, b)
  return a // b, a % b
end
q, r = divide(10, 3)
```

---

## Loops

```lua
-- numeric for
for i = 1, 5 do
  print(i)
end

-- generic for (over tables)
for key, value in pairs(person) do
  print(key, value)
end

-- while
i = 1
while i <= 5 do
  print(i)
  i = i + 1
end

-- repeat-until
repeat
  print("looping")
  i = i - 1
until i == 0
```

---

## Conditionals

```lua
if x > 0 then
  print("positive")
elseif x == 0 then
  print("zero")
else
  print("negative")
end
```

---

## Strings

```lua
s = "hello"
print(#s)              -- length
print(string.upper(s)) -- HELLO
print(string.sub(s, 2, 4)) -- "ell"
print("hi " .. "there")    -- concatenation
```

---

## Tables as Objects (OOP-style)

```lua
Dog = {}
Dog.__index = Dog

function Dog:new(name)
  local self = setmetatable({}, Dog)
  self.name = name
  return self
end

function Dog:bark()
  print(self.name .. " says woof!")
end

fido = Dog:new("Fido")
fido:bark()
```

---

## Miscellaneous

```lua
-- nil removes a variable
x = nil

-- local variables
local y = 5

-- require loads modules
math = require("math")
print(math.sqrt(9))
```

---

## Common Gotchas

* Arrays start at **1**, not 0
* `nil` deletes keys in tables
* Strings are **immutable**
* `..` is the string concatenation operator
* `and`, `or`, `not` are logical operators
