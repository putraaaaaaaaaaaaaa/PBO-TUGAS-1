# Program menggunakan while loop dan if-else untuk memeriksa bilangan bulat atau tidak
numbers = [3.5, 7, 2.8, 10.0, 5]
index = 0

while index < len(numbers):
    num = numbers[index]
    if num.is_integer():
        print(f"{num} adalah bilangan bulat.")
    else:
        print(f"{num} adalah bilangan tidak bulat.")
    
    index += 1