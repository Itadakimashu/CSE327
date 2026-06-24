def add_numbers(a, b):
    # Intentional bug: using subtraction instead of addition
    return a - b

def main():
    numbers = [1, 2, 3, 4, 5]
    total = 0

    # Bug: wrong variable name 'numbr' instead of 'number'
    for numbr in numbers:
        total = add_numbers(total, numbr)

    # Bug: print statement missing parentheses (Python 3)
    print "The sum is:", total

if __name__ == "__main__":
    main()
