lietotajs_skaitlis = int(input("Ievadiet skaitli: "))

if lietotajs_skaitlis % 3 == 0 and lietotajs_skaitlis % 7 == 0:
    print(lietotajs_skaitlis, "dalās gan ar 3, gan ar 7.")
else:
    print(lietotajs_skaitlis, "nedalās ne ar 3, ne ar 7.")