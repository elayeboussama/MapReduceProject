#!/usr/bin/env python

import sys

# Entrée : Date,Open,High,Low,Close,Volume,Dividends,Stock Splits,Company
for line in sys.stdin:
    # Divise la ligne d'entrée en jetons
    tokens = line.strip().split(",")

    # Vérifie si la ligne a suffisamment de jetons
    if len(tokens) >= 9:
        company = tokens[8]
        closing_price = float(tokens[4])

        # Sortie paire clé-valeur : (company, closing_price)
        print("{}\t{}".format(company, closing_price))
