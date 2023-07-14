a = int(input("boyi=> "))
b = int(input("eni=> "))
c = float(input("qalinligi=> "))
d = input("material turi=> ")


def darv(a, b, c, d):
    m_turi = {
        "temir": 25000,
        "oltin": 30000,
        "plastmassa": 10000
    }
    if d in m_turi:
        print(int(a*b*c*m_turi[d]))
    else:
        print("bunday metal turi yoq")


darv(a, b, c, d)
