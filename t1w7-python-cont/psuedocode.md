# Pseudocode
- Plain language description of the steps in an algorithm or program.
- Bridge between the program's logic and the actual code.

## Importance of Psuedocode
- Helps to understand and plan the program logic, so its easier to code.
- Improves collaberation in team projects.
- Helps with troubleshooting
- Identify the core areas of the programming that needs to be done.

## Characteristics of Psuedocode
- Plain language: simple and understandable.
- Structured: Follows a proper logic sequence.
- Abstracted: Focuses on logic more than the syntax.
- Detailed: Thorough walkthrough that helps explain the logic.

## Basic Constructs:

- Sequencial:
```
    Step 1: Do this
    Step 2: Do that
```
- Conditional:
```
    IF condition THEN
        Do something
    ELSE
        Do something else
```

- Loops:
```
    WHILE condition meets
        DO something
    END WHILE
```

- For Loops:
```
    FOR EACH item in collection
        Do something
    END FOR
```

### Practical Examples:
[Examples Code](pseudocode_to_code.py)

- Example 1: Calculating the sum of a list of numbers
```
    Initialise sum to 0
    FOR each number in the list
        ADD the number to sum
    END FOR
    Print sum
```

- Example 2: Finding the maximum number in a list
```
    Initialise max to the first number of the list
    FOR each number in the list
        IF number is greater than max THEN
            Set max to number
        END IF
    END FOR
    Print max 
```