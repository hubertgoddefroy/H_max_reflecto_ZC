import matplotlib.pyplot as plt
import numpy as np
from fonction_reflectance_ZS import couple_reflectance_ZS

# paramètres de calcul de réflectance
n4 = 1.51
n7 =  1.50
incidence = 0

# bornes de recherche en nanomètres
h_min = 0
h_max = 100
pas_de_recherche_lambda = 0.1

# imprécision sur la mesure de réflectance : par exemple, 2,5% signifie +/- 2,5%, i.e. sur une réflectance mesurée à
# 0,8 on prend un interval de [0,78 ; 0,82]
precision = 0.5

ecart_minimal_nano = 20

antecedents = [] # liste qui va stocker toutes les épaisseurs ainsi que les bornes des intervals des intensités mesurées +/- la précision de mesure sur l'intensité
nb_points = int(1 + (h_max - h_min)/pas_de_recherche_lambda)
abscisses = np.linspace(h_min, h_max, nb_points) # array qui représente les abscisses : toutes les épaisseurs calculées de h_min à h_max

for abscisse in range(len(abscisses)):
    reflectance_normalisee_455, reflectance_normalisee_730 = couple_reflectance_ZS(abscisses[abscisse], n4, n7, incidence)
    antecedents.append([abscisses[abscisse], reflectance_normalisee_455, reflectance_normalisee_730, reflectance_normalisee_455*(1-precision), reflectance_normalisee_455*(1+precision), reflectance_normalisee_730*(1-precision), reflectance_normalisee_730*(1+precision), 0])
    for i in range(len(antecedents)):
        # comprises dans les intervals d'un autre point. "-1" pour s'arrêter juste avant le point courant sinon on le compare
        # à lui-même est il va trouver que les 2 points sont confondus donc il va s'arrêter
        if (((antecedents[abscisse][3] >= antecedents[i][3]) and (antecedents[abscisse][3] <= antecedents[i][4])) or ((antecedents[abscisse][4] >= antecedents[i][3]) and (antecedents[abscisse][4] <= antecedents[i][4]))) and (((antecedents[abscisse][5] >= antecedents[i][5]) and (antecedents[abscisse][5] <= antecedents[i][6])) or ((antecedents[abscisse][6] >= antecedents[i][5]) and (antecedents[abscisse][6] <= antecedents[i][6]))) and (antecedents[abscisse][0] != antecedents[i][0]) and (abs(antecedents[abscisse][0] - antecedents[i][0]) >= ecart_minimal_nano):
            # print('les épaisseurs ' + str(abscisses[abscisse]) + 'nm et ' + str(antecedents[i][0]) + 'nm ont les mêmes antécédents avec une précision sur la mesure de la réflectance de +/-' + str(precision*100) + '%')
            antecedents[abscisse][7] = 1 # pour repérer les épaisseurs qui ne sont pas bijective

antecedents = np.asarray(antecedents)

compt = 0
premier_incide_non_bijectif = -1
while(compt < len(antecedents)):
    if antecedents[compt,7] == 1:
        premier_incide_non_bijectif = compt
        compt = len(antecedents) + 1
    else:
        compt += 1

if premier_incide_non_bijectif != -1:
    print('la mesure est bijective sur tout l\'interval testé : [' + str(h_min) + ';' + str(h_max) + 'nm] avec une précision de ' + str(precision*100) + '%')
else :
    print('la mesure est bijective jusqu\'à ' + str(antecedents[premier_incide_non_bijectif,0]) + 'nm')

plt.plot(abscisses, antecedents[:,1], color='blue', label='455')
plt.plot(abscisses, antecedents[:,2], color='red', label='730')
plt.legend()
plt.xlabel('épaisseurs (nm)')
plt.ylabel('reflectance normalisée')
plt.title('Réflectances en 455 et 730')
plt.show()