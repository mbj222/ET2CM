import re


filename = "ydke.txt"
with open(filename) as file:
    lines = [line.rstrip() for line in file]

if "Main Deck:" in lines:
    lines.remove("Main Deck:")
if "Extra Deck:" in lines:
    lines.remove("Extra Deck:")
if "Side Deck:" in lines:
    lines.remove("Side Deck:")

lines = list(filter(None, lines))

linesC = list()

for line in lines:
    linesC.append(line[-1] + " " + line[:-3])

with open("output.txt", "w") as txt_file:
    for line in linesC:
        txt_file.write("".join(line) + "\n")
