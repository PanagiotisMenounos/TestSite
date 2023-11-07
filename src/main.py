# main.py

def greet(name: str) -> str:
    """
    Greets a person with the provided name.

    This function takes a `name` string as an argument and returns a greeting string.

    Arguments:
        name: A string representing the person's name.

    Returns:
        A greeting string.

    Examples:
        >>> greet("Alice")
        'Hello, Alice!'

    Note:
        This function does not validate the name, it simply returns a greeting.

    """
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    This function takes two integer values and returns their sum.

    Arguments:
        a: An integer to be added.
        b: Another integer to be added.

    Returns:
        The sum of `a` and `b`.

    Examples:
        >>> add(1, 2)
        3

    """
    return a + b

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Given two integers, this function returns their product.

    Arguments:
        a: An integer multiplier.
        b: An integer multiplicand.

    Returns:
        The product of `a` and `b`.

    Examples:
        >>> multiply(6, 7)
        42

    """
    return a * b

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))

    print("Let's do some math!")
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}.")
    print(f"The product of {num1} and {num2} is {multiply(num1, num2)}.")
