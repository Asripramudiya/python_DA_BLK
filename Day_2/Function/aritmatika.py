def add(a, b):
    total = a + b
    return total


# jumlah = add(10, 5)
# print(f"Jumlah dari 10 + 5 = {jumlah}")


# def add2(a, b, c, d):
#     total2 = a + b * c / d
#     return total2


# jumlah2 = add2(10, 10, 2, 5)
# print(f"Jumlahnya adalah = {jumlah2}")


# def add3(a=None, b=None):
#     if a == None or b == None:
#         print(f"Parameter tidak lengkap")
#         return
#     total3 = a + b
#     return total3


# Pengurangan
def subsstract(a=None, b=None):
    if a == None or b == None:
        print(f"Parameter tidak lengkap")
        return
    total4 = a - b
    return total4


# BMI Check
def bmi(berat=None, tinggi=None):
    if berat == None or tinggi == None:
        print("Parameter tidak lengkap")
        return
    totalbmi = berat / (tinggi**2)
    return totalbmi


def bmi_check(bmi):
    if bmi < 18.5:
        print("Dalam Kategori Kurus")
    elif 18.5 <= bmi < 24.9:
        print("Dalam Kategori Normal")
    elif 25 <= bmi < 29.9:
        print("Dalam Kategori Overweight")
    elif 30 <= bmi < 50:
        print("Dalam Kategori Obesitas")
    else:
        print("ERROR")


# print("Kamu termasuk kategory:", bmi)
