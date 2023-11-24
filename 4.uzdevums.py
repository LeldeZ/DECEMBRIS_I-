lietotajs_skaitlis = int(input("Ievadiet skaitli: "))
faktorials = 1

for i in range(1, lietotajs_skaitlis + 1):
    faktorials *= i

print("Faktoriāls no", lietotajs_skaitlis, "ir:", faktorials)