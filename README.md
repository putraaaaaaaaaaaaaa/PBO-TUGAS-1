# *Tugas 1 Pemrograman Perbasis Objek*
## Nama : Dwi saputra
## NPM  : G1F022069

## 1. Buatlah perulangan hingga 100 menggunakan Python dengan output sebagai berikut:(https://github.com/randiijulian/randiijulian/assets/81604461/e32b6d92-7e3a-4323-a0e3-711009112c8e)
- **Source Code** :  
```
for i in range(1, 101):
    if i % 10 == 0:
        print("Dwi saputra\nDwi saputra\nDwi saputra")
    else:
        print(i)

```
 - **Output :** 
![alt text](/image/loop100pbo.png)

 - **Penjelasan :** 

1. ```for i in range(1, 101):```: Ini adalah loop for yang akan melakukan for pada variabel i dari 1 hingga 100 .

2. ```if i % 10 == 0:```: ini adalah kondisi if yang memeriksa apakah nilai i adalah kelipatan 10.

3. Jika kondisi di atas benar (yaitu i adalah kelipatan 10), maka program akan mencetak "Dwi saputra" sebanyak tiga kali. Tanda \n digunakan untuk membuat baris baru. ```print("Dwi saputra\nDwi saputra\nDwi saputra")```

4. ```else```: Bagian ini akan dieksekusi jika kondisi di atas tidak terpenuhi. dan di dalam else terdapat ```print(i)```: Jika i bukan kelipatan 10, program akan mencetak nilai i.

## 2 Buatlah program bebas, dengan menerapkan if else pada: a. For Loops b. While Loops
***a. For Loops***

 - **Source Code :** 
```
# Program menggunakan for loop dan if-else untuk memeriksa bilangan bulat atau tidak
for bilangan in [3.5, 7, 2.8, 10.0, 5]:
    if bilangan.is_integer():
        print(f"{bilangan} adalah bilangan bulat.")
    else:
        print(f"{bilangan} adalah bilangan tidak bulat.")
```

 - **Output :**

 ![alt text](/image/Forpbo.png?raw=true)

 - **Penjelasan :**
1. ```for bilangan in [3.5, 7, 2.8, 10.0, 5]:``` : Ini adalah perulangan for yang mengiterasi melalui setiap elemen dalam list [3.5, 7, 2.8, 10.0, 5]

2. ```if bilangan.is_integer():``` : kondisi if  memeriksa apakah nilai bilangan adalah bilangan bulat. Method is_integer() digunakan untuk memeriksa apakah nilai tersebut tidak memiliki pecahan

3. ```print(f"{bilangan} adalah bilangan bulat.")```: jika kondisi di atas terpenuhi, program akan mencetak bahwa nilai bilangan adalah bilangan bulat.

4. ```print(f"{bilangan} adalah bilangan tidak bulat.")```:Jika kondisi if tidak terpenuhi, program akan mencetak bahwa nilai bilangan adalah bilangan tidak bulat.


***b. while Loops***

- **Source Code :**
```
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
```

- **Output :**

![alt text](/image/whilepbo.png?raw=true)

- **Penjelasan :**

1. ```numbers = [3.5, 7, 2.8, 10.0, 5] ``` : Ini adalah list yang berisi beberapa bilangan. ```index = 0```: ni adalah inisialisasi variabel index yang akan digunakan untuk melacak posisi saat ini dalam list numbers.

2. ``` while index < len(numbers): ```  perulangan while yang akan terus berjalan selama nilai index kurang dari panjang (jumlah elemen) dari list numbers. ```num = numbers[index]``` Variabel num mengambil nilai dari list numbers pada posisi index saat ini. 

3. ```if num.is_integer():``` : kondisi if yang memeriksa apakah nilai num adalah bilangan bulat menggunakan method is_integer(). 

4. ```print(f"{num} adalah bilangan bulat.")``` :Jika kondisi di atas terpenuhi, program akan mencetak bahwa nilai num adalah bilangan bulat. ```print(f"{num} adalah bilangan tidak bulat.")``` jika kondisi if tidak terpenuhi, program akan mencetak bahwa nilai num adalah bilangan tidak bulat.

## 3. Buatlah sebuah variabel dengan tipe data array, kemudian tampilkan semua nilai dalam variabel tersebut menggunakan perulangan for

- **Source Code :**
```
# Membuat variabel dengan tipe data array (list) dari rentang nilai 21 hingga 30
nilai_array = list(range(21, 31))

# Menampilkan semua nilai dalam variabel menggunakan perulangan for
for element in nilai_array:
    print(element)
```

- **Output :**

![alt text](/image/arraypbo.png?raw=true)

- **Penjelasan :**

1.```nilai_array = list(range(21, 31))```: baris yang membuat variabel nilai_array dengan tipe data array (list) menggunakan fungsi range(21, 31),berisi bilangan 21 sampai 30

2. ```for element in nilai_array```: perulangan for yang mengiterasi melalui setiap elemen dalam list nilai_array. Variabel element akan mengambil nilai dari setiap elemen dalam setiap iterasi.

3. ```print(element)```: mencetak nilai dari element ke layar. mencetak semua nilai dalam list satu per satu.
