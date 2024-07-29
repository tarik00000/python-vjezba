'''Napiši program koji ispisuje zadani rječnik, s tim da sve vrijednosti manje od 14 trebaju biti uduplane.
R = {"A": 7, "B": 15, "C": 28, "D": 9,"E": 3, "F": 23}.
'''
R = {"A": 7, "B": 15, "C": 28, "D": 9,"E": 3, "F": 23}
for i in R:
    if R[i] < 14:
        R[i]*=2
print(R)