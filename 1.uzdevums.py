lietotaja_skaitlis = int(input("Ievadiet skaitli: "))
summa = 0

for i in range(1, lietotaja_skaitlis + 1):
    summa += i

print("Summa no 1 līdz", lietotaja_skaitlis, "ir:", summa)