name = "Sabina"
count_a = 0
count_b = 0
count_c = 0

for letter in name:
    if letter == 'a':
        count_a += 1
    elif letter == 'b':
        count_b += 1
    elif letter == 'c':
        count_c += 1


print(f"Imię: {name}\nLiczba liter 'a' to: {count_a}\nLiczba liter 'b' to: {count_b}\nLiczba liter 'c' to: {count_c}")