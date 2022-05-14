m=int(input("Ведите номер месяца: "))
if m == 12 or m == 1 or m == 2:
    print("Это зима")
elif m == 3 or m == 4 or m == 5:
    print("Это весна")
elif m == 6 or m == 7 or m == 8:
    print("Это лето")
elif m == 9 or m == 10 or m == 11:
    print("Это осень")
elif m <= 0 or m > 12:
    print("Нет такого месяца!")
print(m)