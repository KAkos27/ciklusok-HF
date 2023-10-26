import ciklusok

print("Teszteset 1 - páros szám, ami 3-mal is osztható:")
print()
print("1, BAM, BUMM, BAM,")
ciklusok.feladat4(4)
print("Teszteset 1 - 6-tal osztható:")
print()
print("1, BAM, BUMM, BAM, 5, BUMMBAM,")
ciklusok.feladat4(6)
print("Teszteset 1 - 3-mal osztható, de kettővel nem:")
print()
print("1, BAM, BUMM, BAM, 5, BUMMBAM, 7, BAM, BUMM,")

ciklusok.feladat4(9)


print("Teszteset 1 - negatív szám esetén:")
print("Várt eredmény: hiba")
ciklusok.feladat4(-7)

print("Teszteset 2 - 0 a paraméter:")
print("Várt eredmény: hiba")
ciklusok.feladat4(0)

print("Teszteset 3 tört szám:")
ciklusok.feladat4(6.4)


