#program motivasi

#deklarasi nilai
Nilai = 10
#cetak nilai
print("Nilai : ",Nilai)

if (Nilai>=90):
    print("Pertahankan")
elif ((Nilai>=80) and (Nilai<90)):
    print("Harus lebih baik lagi")
elif ((Nilai>=60) and (Nilai<80)):
    print("Perbanyak belajar")
elif ((Nilai>=40) and (Nilai<60)):
    print("Jangan keseringan main")
elif (Nilai<40):
    print("Kebanyakan bolos")
else:
    print("Maaf, format nilai tidak sesuai")