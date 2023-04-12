
#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division



SeuilI = { 'Cr1': 0, 'Cr2': 50, 'Cr3': 10.67, 'Cr4': 0, 'Cr5': 15, 'Cr6': 0, 'Cr7': 0}

SeuilP = { 'Cr1': 3, 'Cr2': 3, 'Cr3': 2, 'Cr4': 3, 'Cr5': 3, 'Cr6': 2, 'Cr7': 2, 'Cr8': 1 }

Criteres = [ 'Cr1', 'Cr2', 'Cr3', 'Cr4', 'Cr5', 'Cr6', 'Cr7']

Poids = { 'Cr1':4, 'Cr2':2, 'Cr3':3, 'Cr4':0, 'Cr5':3, 'Cr6':1, 'Cr7':4}

Actions = [ 'P1', 'P2', 'P3', 'P4', 'P5', 'P6' ]

Performances = {
    'P1': { 'Cr1':100, 'Cr2':  50, 'Cr3':100, 'Cr4': 75, 'Cr5':65, 'Cr6':100, 'Cr7':100},
    'P2': { 'Cr1': 100, 'Cr2':100, 'Cr3':33.09, 'Cr4':  100, 'Cr5': 10, 'Cr6': 0, 'Cr7': 100},
    'P3': { 'Cr1': 0, 'Cr2': 25, 'Cr3': 0.35, 'Cr4': 0, 'Cr5' : 70, 'Cr6': 100, 'Cr7': 0},
    'P4': { 'Cr1': 50, 'Cr2': 100, 'Cr3': 20.28, 'Cr4': 50, 'Cr5': 85, 'Cr6': 100, 'Cr7': 0},
    'P5': { 'Cr1': 50, 'Cr2': 0, 'Cr3': 55.87, 'Cr4': 50, 'Cr5':   100, 'Cr6': 0, 'Cr7':100},
    'P6': { 'Cr1': 100, 'Cr2':   72.50, 'Cr3':0, 'Cr4': 50, 'Cr5': 0, 'Cr6': 0, 'Cr7': 0},
}


Delta = 0.0
for a1 in Actions:
    p1 = Performances[a1]
    for a2 in Actions:
        p2 = Performances[a2]
        for critere in Criteres:
            g1 = p1[critere]
            g2 = p2[critere]
            Delta = max(Delta, abs(g1-g2))
print('Delta : ',Delta)

def Concordance(a1, a2):
    p1 = Performances[a1]
    p2 = Performances[a2]
    num = 0.0
    den = 0.0
    for critere in Criteres:
        g1 = p1[critere]
        g2 = p2[critere]
        poids = Poids[critere]
        if (g2 - g1) <= SeuilI[critere]:
            num += poids
        den += poids
    return num/den

def Discordance(a1, a2):
    p1 = Performances[a1]
    p2 = Performances[a2]
    num = 0.0
    for critere in Criteres:
        g1 = p1[critere]
        g2 = p2[critere]
        if (g2 - g1) > SeuilI[critere]:
            num = max(g2 - g1, num)
    return num/100

print('Matrice de concordance :')
for a1 in Actions:
    print('\t', a1, end='')
print()
for a1 in Actions:
    print(a1, end='')
    for a2 in Actions:
        if a1 != a2:
            print('\t%.2f' % Concordance(a1, a2), end='')
        else:
            print('\t--', end='')
    print()

print('Matrice de discordance :')
for a1 in Actions:
    print('\t', a1, end='')
print()
for a1 in Actions:
    print(a1, end='')
    for a2 in Actions:
        if a1 != a2:
            print('\t%.2f' % Discordance(a1, a2), end='')
        else:
            print('\t--', end='')
    print()


# Initialisation des données
c = 0.6
couples = []

# Calcul des concordances et stockage des couples qui dépassent le seuil
for a1 in Actions:
    for a2 in Actions:
        if a1 != a2:
            conc = Concordance(a1, a2)
            if conc >= c:
                couples.append((a1, a2))

# Affichage des couples
print(f"Couples dont la concordance dépasse {c} :")
for couple in couples:
    print(couple[0], "-", couple[1])




# biblio https://engees.unistra.fr/fileadmin/user_upload/pdf/gsp/Cours_MCDA_AN.pdf
