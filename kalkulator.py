x = int(input("Masukkan bilangan pertama: "))
y = input("Pilih operator matematika (+/-/x/:)")
z = int(input("Masukkan bilangan kedua: "))
if y == "+":
    print("Hasil:", x + z)
elif y == "-":
    print("Hasil:", x - z)
elif y == "x":
    print("Hasil:", x * z)
elif y == ":":
    print("Hasil:", x / z)
else:
    print("Operator tidak dikenal")