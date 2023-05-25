## Pizza Py
Perhaps the most popular place for pizza in **Harvard Squarehttps://en.wikipedia.org/wiki/Harvard_Square** [is Pinocchio’s](https://www.pinocchiospizza.net/) Pizza & Subs, aka Noch’s, known for its [Sicilian pizza](https://www.pinocchiospizza.net/sicilian_vs_regular.html), which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its [menu](https://www.pinocchiospizza.net/menu.html) too, per this CSV file of [Sicilian pizzas](https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv), sicilian.csv, below:

    Sicilian Pizza,Small,Large
    Cheese,$25.50,$39.95
    1 item,$27.50,$41.95
    2 items,$29.50,$43.95
    3 items,$31.50,$45.95
    Special,$33.50,$47.95
    
See r[egular.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv) for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as [ASCII art](https://en.wikipedia.org/wiki/ASCII_art), like this one:  


| Sicilian Pizza   | Small   | Large   |
|------------------|---------|---------|
| Cheese           | $25.50  | $39.95  |
| 1 item           | $27.50  | $41.95  |
| 2 items          | $29.50  | $43.95  |
| 3 items          | $31.50  | $45.95  |
| Special          | $33.50  | $47.95  |

**In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.**

### Hints
- Recall that the csv module comes with quite a few methods, per https://docs.python.org/3/library/csv.html, among which are reader, per https://docs.python.org/3/library/csv.html#csv.reader, and DictReader, per https://docs.python.org/3/library/csv.html#csv.DictReader.
- Note that open can raise a FileNotFoundError, per https://docs.python.org/3/library/exceptions.html#FileNotFoundError.
- Note that the tabulate package comes with just one function, per https://pypi.org/project/tabulate. You can install the package with:
     pip install tabulate

### How to Test
**Here’s how to test your code manually:**

- Run your program with python pizza.py. Your program should exit using sys.exit and provide an error message:

    Too few command-line arguments
    
- Be sure to download regular.csv and sicilian.csv, placing them in the same folder as pizza.py. Run your program with python pizza.py regular.csv sicilian.csv. Your 
program should output:
    
    Too many command-line arguments

 - Run your program with python pizza.py invalid_file.csv. Assuming invalid_file.csv doesn’t exist, your program should exit using sys.exit and provide an error message:
    
    File does not exist
 
- Create a file named sicilian.txt. Run your program with python pizza.py sicilian.txt. Your program should exit using sys.exit and provide an error message:

    Not a CSV file
    
- Run your program with python pizza.py regular.csv. Assuming you’ve downloaded regular.csv, your program should print a table like the below:
-

| Regular Pizza   | Small   | Large   |
|-----------------|---------|---------|
| Cheese          | $13.50  | $18.95  |
| 1 topping       | $14.75  | $20.95  |
| 2 toppings      | $15.95  | $22.95  |
| 3 toppings      | $16.95  | $24.95  |
| Special         | $18.50  | $26.95  |

