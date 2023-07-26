a = input("Noutbuk nomi: ")
b = int(input("SSD hajmi(512/1024): "))
c = int(input("DDR hajmi(8/16): "))
d = input("Protsessor turi(Ryzon/Core): ")
e = int(input("Protsessor o'chami(5/7/9): "))
f = input("Rangi(black/grey/gold): ")

def laptop(a,b,c,d,e,f):
    lap_library={
        "msi": 30,
        "macbook": 100,
        "asus": 40,
        "lenovo": 30,
        "acer": 30,
        "hp": 15,
        "windows": 25
    }
    if b==512 and c==8:
        bP=200
    else:
        bP=400
    

        
    if d == 'Ryzon' and e == 5 and f == "black" :
       if a in lap_library:
           print(lap_library[a]+1000+bP) 
    elif b == 512 and c == 8 and d == 'Ryzon' and e == 5 and f == "black" :
       if a in lap_library:
           print(lap_library[a]+1000) 
           
laptop(a,b,c,d,e,f)
    