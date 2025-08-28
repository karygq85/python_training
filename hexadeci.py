# Python code​​​​​​‌‌​​​‌‌​​​​​​​​​‌‌‌​‌‌‌‌​ below
hexNumbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = input("Type a hexnumber to decimal:")
    for char in hexNum:
        if char not in hexNumbers:
            print("No hexanumber, type again")
            return None
        else:
            print(f"{char} OK")
    num = 0
    n = len(hexNum) - 1
    for char in hexNum:
        # print(n)
        num = num + (hexNumbers[char] * (16**n))
        n = n - 1
    print(num)
    return num


hexToDec(hexNumbers)
