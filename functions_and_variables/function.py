# def hello(to="world"):
#     print("hello,", to)

# hello()

# name = input("What's your name? ").strip()

# hello(name)

def main():
    x = int(input("what's x? "))
    print("square of x is", square(x))

def square(n):
    return n * n

main()