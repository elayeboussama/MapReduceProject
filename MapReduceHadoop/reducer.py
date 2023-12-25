#!/usr/bin/env python

import sys

current_company = None
total_closing_price = 0.0
count = 0

# Lit l'entrée à partir de la saisie standard
for line in sys.stdin:
    # Divise la ligne d'entrée en clé et valeur
    company, closing_price = line.strip().split("\t")
    closing_price = float(closing_price)

    # Vérifie si l'entreprise a changé
    if current_company != company:
        # Résultat de sortie pour l'entreprise précédente
        if current_company:
            average_closing_price = total_closing_price / count
            print("{}\t{}".format(current_company, average_closing_price))

        # Réinitialise les variables pour la nouvelle entreprise
        current_company = company
        total_closing_price = closing_price
        count = 1
    else:
        # Met à jour les variables pour l'entreprise en cours
        total_closing_price += closing_price
        count += 1

# Résultat de sortie pour la dernière entreprise
if current_company:
    average_closing_price = total_closing_price / count
    print("{}\t{}".format(current_company, average_closing_price))
