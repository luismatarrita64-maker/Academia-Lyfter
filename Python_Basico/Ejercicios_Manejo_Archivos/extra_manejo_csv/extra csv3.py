import csv
from collections import Counter

counter = Counter()

with open("games1.csv", newline="", encoding="utf-8") as file:
    lector = csv.DictReader(file)
    for fila in lector:
        counter[fila["gender"]] += 1

print("\n",counter,"\n")
