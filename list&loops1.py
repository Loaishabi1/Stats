
import random
Mobland = ["harry", "conrad", "Paul", "Edward", "maeve",
              "freddie", "kat", "jan", "seraphina", "michel"]


random.shuffle(Mobland)


sentence = ""

for i in range(len(Mobland)):

    if i == 0:
        sentence = f"{Mobland[i]}"

    elif i == len(Mobland) - 1:
        sentence += f" and {Mobland[i]}"

    else:
        sentence += f", {Mobland[i]}"


sentence += "."

print(sentence)
