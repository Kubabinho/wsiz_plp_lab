def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

while True:
    try:
        user_input = input("daj liste do mnozenia")
        numbers = list(map(float, user_input.split()))
        squared_numbers = square_numbers(numbers)
        print("wynik", squared_numbers)
        break
    except ValueError:
        print("nie podales liczb")
