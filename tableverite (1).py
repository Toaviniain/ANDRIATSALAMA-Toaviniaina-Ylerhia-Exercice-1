from itertools import product

def table_verite(f, v):
    # Générer les en-têtes de la table de vérité
    en_tetes = v + [f]
    print(" | ".join(en_tetes))

    # Calculer et afficher les lignes de la table de vérité
    for i in product([0, 1], repeat=len(v)):
        valeurs = list(i)
        k=int(eval(f, dict(zip(v,i))))
        if k >1:
        	k=1
        	valeurs.append(k)
        else:
        	valeurs.append(k)
        print(" | ".join(map(str, valeurs)))

def premiere_forme_canonique(variables, table_verite):
    formule = []
    for ligne in table_verite:
        if ligne[-1] == 1:
            terme = []
            for i in range(len(variables)):
                if ligne[i] == 0:
                    terme.append(variables[i])
                else:
                    terme.append(f"not {variables[i]}")
            formule.append("(" + " & ".join(terme) + ")")
    return " | ".join(formule)

# Fonction logique à tester 
fonction_logique = input("Entrez la fonction logique : ")

# Variables de la fonction logique
variables = [v.strip() for v in input("Entrez les noms des variables séparés par des espaces : ").split()]

# Affichage de la table de vérité
print("\nTable de vérité :")
table_verite(fonction_logique, variables)

# Calcul et affichage des formes canoniques
table = []
for ligne in product([0, 1], repeat=len(variables)):
    valeurs = list(ligne)
    valeurs.append(int(eval(fonction_logique, dict(zip(variables, ligne)))))
    table.append(valeurs)

print("\nPremière forme canonique :")
print(premiere_forme_canonique(variables, table))