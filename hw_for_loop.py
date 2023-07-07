s = input(">>> ")
unli=[]
undosh=[]

for harf in s:
    if harf.lower() in 'aeuio':
        unli.append(harf)
    elif harf.lower() in 'qwrtypsdfghjklzxcvbnm':
        undosh.append(harf)
    

print("unli harflar: ", set(unli))
print("undosh harflar: ", set(undosh))