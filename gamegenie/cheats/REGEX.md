# Regex Cheatsheet

## Basics
```
.        - any single character (except newline)
^        - start of a line/string
$        - end of a line/string
*        - 0 or more repetitions of the previous element
+        - 1 or more repetitions of the previous element
?        - 0 or 1 occurrence of the previous element (makes it optional)
{n}      - exactly n repetitions
{n,}     - n or more repetitions
{n,m}    - between n and m repetitions (inclusive)
```

## Classes
```
[...]    - character class; matches any one character inside brackets
[^...]   - negated character class; matches any one character *not* inside brackets
[a-z]    - range; matches any lowercase letter from a to z
[0-9]    - range; matches any digit
```

## Groups
```
( )      - capture group; groups regex parts and captures the match
(?: )    - non-capturing group; groups without capturing
|        - alternation (logical OR)
```

## Escapes
```
\        - escape character (treats the next character literally or gives it special meaning)
\d       - digit (0-9)
\D       - non-digit
\w       - word character (letters, digits, underscore)
\W       - non-word character
\s       - whitespace (space, tab, newline, etc.)
\S       - non-whitespace
```

## Boundaries
```
\b       - word boundary
\B       - non-word boundary
```

## Lookarounds
```
(?=...)  - positive lookahead (asserts that what follows matches ...)
(?!...)  - negative lookahead (asserts that what follows does NOT match ...)
(?<=...) - positive lookbehind (asserts that what precedes matches ...)
(?<!...) - negative lookbehind (asserts that what precedes does NOT match ...)
```

## Literals
```
\\       - matches a literal backslash
\.       - matches a literal dot
\*       - matches a literal asterisk
\+       - matches a literal plus
\?       - matches a literal question mark
\|       - matches a literal pipe
\^       - matches a literal caret
\$       - matches a literal dollar sign
\n       - matches a newline
```
