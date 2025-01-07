#sprawdza czy jest palindromem
def is_palindrome(lst):
    #porownuje listę z jej odwrotnością
    return lst == lst[::-1]

#pobieranie listy od użytkownika
user_input = input("podaj liste do sprawdzenia czy to palindrom")

#zmiana tego co podal user na liste
user_list = user_input.split()

if is_palindrome(user_list):
    print("jest")
else:
    print("nie jest")
