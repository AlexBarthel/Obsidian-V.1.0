# Obsidian+
## Table of Contents

1. [Project Structure](#Modules)

2. [Language Summary](#)

3. [Syntax](#)

4. [Contributors](#)

5. [Files](#)

6. [TODO List](#)

---

### Language Summary
Obsidian+ has numerous features and functions which come from a mix of C#, Java, and Python. Obsidian+ was created as a way to experience all of the great features from some of the most popular languages, in a relatively simple way. Obsidian+ (obs+ for short) has many benefits including easy-to-learn, easy-to-read, high portability, and OOP. Obsidian+ is a unique and easy-to-learn programming language for programmers of all skill levels.

---

### Syntax
| ‎Token | Description | Example |
|--|--|--|
|`int`|Any number of decimal digits.|`12` `22` `37`|
|`String`|Any number of characters inbetween two double/single quotes.|`"hello"` `'world'`|
|`Symbol`|Any character that isn't alphanumeric.|`*` `+` `%`|
|`Newline`|A line break character.|`\n`|
|`Comment`|An asterisk `*` followed by any alphanumeric or symbol combination.|`* This is a comment`|
|`(` `)`|Left `(` or right `)` parentheses. Delimeter.|`(` `)`|
|`[` `]`|Left `[` or right `]` square brackets. Delimeter.|`[` `]`|
|`{` `}`|Left `{` or right `}` curly braces. Delimeter.|`int {}`|

1. Indentation in obs+ doesn't matter. Since obs+ uses curly braces to enclose certain scopes of code, indentation isn't important.
2. Writing a data type before a variable is extremely important to the parser so that it knows what type of variable your variable is. And if your variable value does not match the type, then it will throw an error.

---

### Contributors
> @msgaalex - Lead Programmer, Syntax Designer, Bug Fixer<br>
@matthillial - Lead Programmer, Bug Fixer<br>
@kristenkirchner - Programmer, Syntax Designer

## TODO :
- [x] Create a Lexer
  - [ ] Lex Escape Sequences
- [x] Create a Tokenizer
- [x] Arrange Tokens to Evaluate Syntax
- [ ] Parse from Tokens
  - [x] Variables
  - [ ] Functions
  - [ ] Lambda Functions
  - [ ] for() and while() loops
  - [ ] display() statements
- [ ] Variable Stacking
- [ ] Create a pseudo-random number generator (PRNG)
- [ ] Create a Github page for obs+
- [ ] Tokenizing all the [] and , and elements separately,  this won't catch any errors inside the array eg: ArrayList a: ["[test]", "2", "[noerror"]
- [ ] Beta Test