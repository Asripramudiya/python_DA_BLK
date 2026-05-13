a = 100
b = 10**2
c = 101

ab = a==b # Sama dengan
ac = a==c # Sama dengan
ac2 = a!=c # Tidak Sama dengan
ac3 = a>c # Lebih besar
ac4 = a<c # Lebih kecil
ab2 = a>=b # Lebih besar sama dengan
ab3 = a<=b # Lebih kecil sama dengan

print(f"Apakah {a} sama dengan {b} =", ab)
print(f"Apakah {a} sama dengan {c} =", ac)
print(f"Apakah {a} tidak sama dengan {c} =", ac2)
print(f"Apakah {a} lebih besar dari {c} =", ac3)
print(f"Apakah {a} lebih kecil dari {c} =", ac4)
print(f"Apakah {a} lebih besar sama dengan {b} =", ab2)
print(f"Apakah {a} lebih kecil sama dengan {b} =", ab3)