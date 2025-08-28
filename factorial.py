def get_number():
    prompt = "Number, please: "
    num = int(input(prompt))
    if type(num) != int:  # noqa: E721
        print("type an integer, please")
        return None
    if num < 0:
        print("type an integer positive, please")
        return None
    else:
        print("num OK")
        return num


def factorial(num):
    # Your code goes here.
    if num is None:
        return None
    else:
        i = num
        fact = 1

        while i > 0:
            fact = fact * i
            i = i - 1

        print(f"{num} ! = {fact}")
        return fact


num = get_number()
factorial(num)
