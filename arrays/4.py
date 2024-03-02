import numpy as np

even_array = np.array([2, 4, 6, 8])
odd_array = np.array([1, 3, 5, 7])

numbers = input("plz type even or odd: ")

if numbers.lower() == "even":
    print(even_array)
elif numbers.lower() == "odd":
    print(odd_array)
else:
    print("plz type even or odd")
