# Program menggunakan for loop dan if-else untuk memeriksa bilangan bulat atau tidak
for bilangan in [3.5, 7, 2.8, 10.0, 5]:
    if bilangan.is_integer():
        print(f"{bilangan} adalah bilangan bulat.")
    else:
        print(f"{bilangan} adalah bilangan tidak bulat.")