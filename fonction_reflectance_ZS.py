import matplotlib.pyplot as plt
import numpy as np

def reflectance_ZS(epaisseur, lambdaa, n1, n2, incidence):
''' Cette fonction prend comme argument :
    - l'épaisseur de la couche mesurée,
    - la longueur d'onde d'intérêt poiur laquelle on calcule la rélfectance,
    - l'indices de réfraction pour la longueur d'onde lambdaa
    - l'angle d'incidence

    Cette fonction retourne :
    - une valeur de réflectance normalisée pour la longueur d'onde correspondante
'''
    n0 = 1
    r01 = (n0 - n1)/(n0 + n1)
    r12 = (n1 - n2)/(n1 + n2)
    phi = 2*np.pi*epaisseur*np.cos(incidence)/lambdaa

    reflectance = ((r01**2) + (r12**2) + 2*r01*r12*np.cos(2*phi))/(1 + (r01**2)*(r12**2)*np.cos(2*phi))

    # Réflectances min et max pour normaliser la réflectance calculée
    Rmin = ((r01 - r12)**2)/(1 + (r01**2)*(r12**2) - 2*r01*r12)
    Rmax = ((r01 + r12)**2)/(1 + (r01**2)*(r12**2) + 2*r01*r12)
    reflectance_normalisee = (reflectance - Rmin)/(Rmax - Rmin)

    return reflectance_normalisee

def couple_reflectance_ZS(epaisseur, n4, n7, incidence):
''' Cette fonction prend comme argument :
    - l'épaisseur de la couche mesurée,
    - les indices de réfraction en 455 et 730
    - l'angle d'incidence

    Cette fonction retourne :
    - un couple de reflectance normalisée [reflectance_normalisée_455, reflectance_normalisée_730]
'''
    n04 = 4.55
    n07 = 3.65

    reflectance_normalisee_455 = reflectance_ZS(epaisseur, 455, n4, n04, incidence)
    reflectance_normalisee_730 = reflectance_ZS(epaisseur, 730, n7, n07, incidence)

    return reflectance_normalisee_455, reflectance_normalisee_730

