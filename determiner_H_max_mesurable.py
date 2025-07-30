import matplotlib.pyplot as plt
import numpy as np

n4 = 1.51
n7 =  1.50
# bornes de recherche en nanomètres
h_min = 0
h_max = 1000
pas_de_recherche_lambda = 0.1

antecedents = [] # liste qui va stocker toutes les épaisseurs ainsi que les bornes des intervals des intensités mesurées +/- la précision de mesure sur l'intensité
nb_points = 1 + (h_max - h_min)/pas_de_recherche_lambda
abscisses = np.linspace(h_min, h_max, nb_points) # array qui représente les abscisses : toutes les épaisseurs calculées de h_min à h_max

for abscisse in abscisses:

