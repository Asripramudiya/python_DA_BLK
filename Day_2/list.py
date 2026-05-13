nama = ["kim","v","tae"]
nilai = [80,90,100]

nama_slice = nama[0:3]
nilai_slice = nilai[0:3]

print(nama_slice)
print(nilai_slice)

nama_slice[1] = "kthv"
nilai_slice[1] = 99
print("\n")
print(nama_slice)
print(nilai_slice)

# INSERT 
nama_slice.insert(1, "tan")
nilai_slice.insert(1, 80)
print("\n")
print(nama_slice)
print(nilai_slice)

# APPEND
nama_slice.append("jung")
nilai_slice.append(100)
print("\n")
print(nama_slice)
print(nilai_slice)

# SORT
nama_slice.sort()
print("\nSORT")
print(nama_slice)
print(nilai_slice)

# POP
nama_slice.pop()
nilai_slice.pop()
print("\nPOP")
print(nama_slice)
print(nilai_slice)

# print (f"indeks -1 adalah {nama[-1]}")
# #print(f"panjang data dari nama{len(nama)}")

# for z in range (len(nama)):
#     print(z)
#     print(f"nama{nama[1]} mendapatkan nilai {nilai[1]}")