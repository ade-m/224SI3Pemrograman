diskon = 0
membership =""

nama = input("Masukkan Nama : ")
totalBelanjaan = int(input("Masukkan Total Belanjaan : "))

if(totalBelanjaan>=10000000):
    membership="Platinum"
    diskon = 0.2*totalBelanjaan
elif(totalBelanjaan>=5000000):
    membership="Gold"
    diskon = 0.1*totalBelanjaan
elif(totalBelanjaan>=500000):
    membership="Silver"
    diskon = 0.05*totalBelanjaan
else:
    membership="Bukan Member"
    diskon = 0

totalBayar = totalBelanjaan-diskon
print("Nama Pelanggan : ",nama)
print("Membership : ",membership)
print("Total yang harus dibayar : ",totalBayar)
