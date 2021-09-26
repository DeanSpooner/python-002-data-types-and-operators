# Python 002 - Data Types, Operators

## Data Types

Just like in JavaScript, Python has several different primitive data types, including

    "Dean"- string
    40 - integer
    0.5 - float
    True - boolean

## Data Type Conversion

Data types can be converted easily using methods such as str(), int(), float().

For example:

    number = "408"
    int(number)
    print(number)

    408

If a float is passed into int(), **it rounds down to the floor amount**:

    print(int(40.68))

    40

It does **not** round the float!

## round(float, dp)

The round() function allows us to round a float. The first parameter it takes is the float variable, the second is the number of decimal places you want to round the float to - if left blank, it will round to 0 decimal places i.e. to the nearest **whole number**.

For example:

    print(round(40.62))

Will print:

    41

As it went straight to the nearest whole number, 41. Meanwhile:

    print(round(40.62, 1)

Will print:

    40.6

## Operators

Similarly to JavaScript, Python uses different mathematical operators.

- +: plus
- -: minus
- \*: times
- /: divide (**this will always result in a float data type, even if it is a clean division**)
- \*\*: exponent or power
- //: divides and floors to the integer, e.g. **8 // 2** and **9 // 2** will both result in the **integer** 4.
- +=: add an amount to the variable's current value
- -=: subtract an amount from the variable's current value
- \*=: multiply an amount with the variable's current value
- /=: divide the variable's current value by an amount

## f-Strings

f-Strings allow for much easier mixing of data types in strings, very similar to how _\`${string literals} were used like this in ${JavaScript}\`._

In Python, we simply use the character **f** immediately before the string, then included non-string variables with **{curly braces}**.

For example:

    age = 31
    name = "Dean"
    print(f"My name is {name} and I am {age} years old.")

Will print:

    My name is Dean and I am 31 years old.

## Subscripting

This is a way of extracting the character in a string at a particular index location. It comes immediately after a string in **[square brackets]**.

For example:

    print("Manchester"[6])

Will print the character in the 6th **indexed** position, or the **7th** character:

    s
