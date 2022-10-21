# input nilai variabel
a=input("Masukkan nilai a:")
b=input("Masukkan nilai b:")

# cetak nilai variabel
print("variabel a=",a)
print("variabel b=",b)

# cetak hasil operasi kedua variabel dengan string format
print("Hasil penggabungan {1}&{0}=%d".format(a,b) %(68))

# konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
