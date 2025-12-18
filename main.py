import matplotlib.pyplot as plt      
import pandas as pd
import numpy as np

#transfert des données excel en tableau numpy
tableau= pd.read_excel("huile.xlsx", header=None)
tableau_numpy = tableau.values.tolist()


def valeur(mat):
    valeur = []
    for k in range(len(mat)):
        valeur.append(mat[k][:3])# Récuparation des seules données utiles
    return valeur 

tableau = valeur(tableau_numpy)

def abscurv(mat): # Calcul de l'abscisse curviligne pour le tracé de la régression linéaire
    s=[]
    s.append(np.sqrt((mat[1][0]-mat[0][0])**2 + (mat[1][1]-mat[0][1])**2))
    for k in range(1,len(mat)-7): # Seules les premières valeurs sont interessantes (tant que le modèle est bon)
        s.append(((mat[k+1][0]-mat[k][0])**2 + (mat[k+1][1]-mat[k][1])**2)**(1/2) + s[k-1]) 
        # Calcul de l'abscisse curviligne en cumulé en supposant la trajectoire rectiligne entre chaque pointé
    tableau_abscurv = np.array(s)
    return (tableau_abscurv)


def vitesse(mat): # Calcul du log de la vitesse pour le tracé de la regression linéaire
    v=[]
    v.append(mat[0][2])
    for k in range(1,len(mat)-7):
        v.append(mat[k][2])
    tableau_vitesse=np.array(v)
    return np.log(tableau_vitesse)

a,b = np.array(abscurv(tableau)),np.array(vitesse(tableau))
print(a,b) 


pente, ordonnée = np.polyfit(a,b,1)
# Affectation des valeurs du coefficient directeur et de l'ordonnée à l'origine pour le tracé de la reg linéaire

print(pente) # Valeur permettant de remonter au coefficient de trainé
print(ordonnée)


ud_x = np.sqrt(2)*2E-3
ud_y = np.sqrt(2)*2E-3
def incertitude_abscurv(ud_x,ud_y,mat): # Calculs d'incertitudes sur l'abscisse curviligne 
    l = len(mat)
    ds = 0
    S_u_ds = []
    
    for k in range(l-7):
        
        dx = abs(abs(mat[k+1][0])-abs(mat[k][0])) # Variation d'abscisse entre 2 instants
        dy = abs(abs(mat[k+1][1])-abs(mat[k][1])) # Variation d'ordonnées entre 2 instants
        ds=np.sqrt((mat[k+1][0]-mat[k][0])**2 + (mat[k+1][1]-mat[k][1])**2)
        # Variation d'abscisse curviligne entre 2 instants
        S_u_ds.append(ds*np.sqrt((dx*ud_x/(dx**2 + dy**2))**2 + (dy*ud_y/(dx**2 + dy**2))**2 ))
        # Incertitudes sur l'abscisse curviligne pour chaque pointé
    return S_u_ds

def incertitude_vitesse(ud_x,ud_y,mat): # Calculs d'incertitudes sur le log de la vitesse
    n=len(mat)
    S_u_v = []
    
    for k in range (n-7):
        dx = abs(abs(mat[k+1][0])-abs(mat[k][0])) 
        dy = abs(abs(mat[k+1][1])-abs(mat[k][1]))
        ds=np.sqrt((mat[k+1][0]-mat[k][0])**2 + (mat[k+1][1]-mat[k][1])**2)
        u_ds = ds*np.sqrt((dx*ud_x/(dx**2 + dy**2))**2 + (dy*ud_y/(dx**2 + dy**2))**2 )
        S_u_v.append(u_ds/ds) # Incertitudes sur le log de la vitesse pour chaque pointé
    return S_u_v
        
incer_s = np.array(incertitude_abscurv(ud_x,ud_y,tableau))
incer_v = np.array(incertitude_vitesse(ud_x,ud_y,tableau))



# Définir une nouvelle série de valeurs x pour la droite de régression
abscisse = np.linspace(min(a), max(a), 100)


droite_affine = pente * abscisse + ordonnée

# Tracer les données et la droite de régression
plt.figure(1) # On crée la figure n°1
plt.errorbar(a, b, xerr=incer_s, yerr=incer_v, label="points expérimentaux", fmt="none") # fmt="none" (minuscule) ou 'o'
plt.plot(abscisse, droite_affine, color='red', label="Regression linéaire")

plt.xlabel('abscisse curviligne')
plt.ylabel('logarithme de la vitesse')
plt.title("Régression Linéaire")
plt.legend()


v_ideal = pente * a + ordonnée
    
def z_score(v,v_ideal): # Calcul de z_score pour chaque point
    z =[]
    n = len(v)
    for k in range(n):
        z.append((np.abs(v[k]-v_ideal[k]))/incer_v[k]) 
        # Ecart entre les valeurs expérimentales et les valeurs déterminées par la régression linéaire
    return z

z = z_score(b,v_ideal)

# Tracer du z_score en fonction de l'abscisse curviligne
plt.figure(2) # On crée une NOUVELLE figure (fenêtre) pour ne pas dessiner par dessus la précédente
plt.plot(a, z, color='green', label='z_score')
plt.xlabel('abscisse curviligne')
plt.ylabel('z_score')
plt.title("z_score en fonction de l'abscisse curviligne")
plt.legend()


plt.show()


























    