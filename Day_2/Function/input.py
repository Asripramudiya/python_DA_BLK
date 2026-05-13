import aritmatika as f

# print(aritmatika.add(20, 6))
BB = float(input("Masukkan Berat badan (kg) :"))
TB = float(input("Masukkan Tinggi badan (m) :"))

bmi = f.bmi(BB, TB)
print("BMI kamu adalah", bmi)

f.bmi_check(bmi)
