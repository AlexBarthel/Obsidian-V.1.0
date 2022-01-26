# Obsidian V.1.0

## Table of Contents

1. Language Summary
2. Syntax
3. Contributors
4. Files
5. Modules
6. TODO List

---

### Language Summary
Obsidian+ has numerous features and functions which come from a mix of C#, Java, and Python. Obsidian+ was created as a way to experience all of the great features from some of the most popular languages, in a relatively simple way. Obsidian+ (obs+ for short) has many benefits including easy-to-learn, easy-to-read, high portability, and OOP. Obsidian+ is a unique and easy-to-learn programming language for programmers of all skill levels.

---

### Syntax
| Token | Description | Example |
|--|--|--|
|`int`|Any number of decimal digits.|`12` `22` `37`|
|`String`|Any number of characters in between two double/single quotes.|`"hello"` `'world'`|
|`Symbol`|Any character that isn't alphanumeric.|`*` `+` `%`|
|`Newline`|A line break character.|`\n`|
|`Comment`|An asterisk `*` followed by any alphanumeric or symbol combination.|`* Test`<br>`* Hello`|
|`(` `)`|Left `(` or right `)` parentheses. Delimeter.|`(` `)`|
|`[` `]`|Left `[` or right `]` square brackets. Delimeter.|`[` `]`|
|`{` `}`|Left `{` or right `}` curly braces. Delimeter.|`int {}`|

1. Indentation in obs+ doesn't matter. Since obs+ uses curly braces to enclose certain scopes of code, indentation isn't important.
2. Writing a data type before a variable is extremely important to the parser so that it knows what type of variable your variable is. And if your variable value does not match the type, then it will throw an error.
3. Variables are case sensitive, and cannot start with a number.
4. Variables can only have a number at the end of it's name.
5. Symbols can be used anywhere withing a variable name eg: `int my_new_var: 5;`.
---

### Contributors
> Replit(@msgaalex) Github(@AlexBarthel) - Leader of Replit(@ObsidianDevelopers)<br>
> Replit(@jasonkirchner) - Co-Founder, Syntax Designer<br>
> Replit(@matthillial) - Lead Programmer, Bug Fixer

---

### Files
| File | Description |
|--|--|
|`.replit`|Customizes the behavior of the repl to run Obsidian.|
|`run.sh`|Runs Obsidian once the run button is pressed.|
|`LICENSE`|GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007|
|`README.md`|The file you are currently in.|

---

### Modules
| Module | Description |
|--|--|
|`example`|A folder of example Obsidian programs.|
|`Modules`|All of the different modules that you can import into your Obsidian program.|
|`Parser`|The Obsidian Language Parser.|
|`std`|Standard files you can import into your Obsidian program.|
|`utils`|Utilities the Obsidian Language Parser uses.|

---
### To Do List
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