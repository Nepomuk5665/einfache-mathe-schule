import time
import random
import os

# Signatur
os.system('cls' if os.name == 'nt' else 'clear')

name = """

███╗░░██╗███████╗░██████╗░█████╗░███████╗████████╗░██████╗
████╗░██║██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██╔██╗██║█████╗░░╚█████╗░██║░░██║█████╗░░░░░██║░░░╚█████╗░
██║╚████║██╔══╝░░░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░░╚═══██╗
██║░╚███║███████╗██████╔╝╚█████╔╝██║░░░░░░░░██║░░░██████╔╝
╚═╝░░╚══╝╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═════╝░

"""

name_lines = name.split("\n")

name_placeholder = [[' ']*len(line) for line in name_lines]

characters_in_name = [char for char in name if char != ' ' and char != '\n']
total_characters = len(characters_in_name)

initial_pause = 0.2
final_pause = 0.000000000000001
pause_step = (initial_pause - final_pause) / (total_characters * 2)

current_pause = initial_pause

while characters_in_name:
    for i, line in enumerate(name_lines):
        for j, char in enumerate(line):

            if char != ' ' and name_placeholder[i][j] == ' ' and random.random() < 0.05 + 0.95 * (1 - len(characters_in_name) / total_characters):
                name_placeholder[i][j] = char
                characters_in_name.remove(char)

    print('\033[H')
    print('\n'.join([''.join(line) for line in name_placeholder]))
    time.sleep(current_pause)
    current_pause = max(final_pause, current_pause - pause_step)

def typing_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()


typing_animation("created by Nepomuk Crhonek\n")


def print_big_title(text):
    # Create a big title using the input text
    big_title = ''
    for char in text:
        big_title += char.upper() + ' '

    # Print the big title
    print(big_title)


print_big_title("Rechnen mit einem Kreis\n")

# program start

# zuerst kann man auswählen ob man den radius oder den durchmesser hat

print("Was hast du? ")
print("1. Radius")
print("2. Durchmesser")
print("3. Fläche")
print("4. Umfang")

print()

def area(radius):
    return radius * radius * 3.1415926535897932384626433832795


def circumference(radius):
    return 2 * radius * 3.1415926535897932384626433832795


choice = int(input("Deine Wahl: "))
print()

if choice == 1:
    radius = float(input("Was ist der Radius von deinem Kreis? "))
    print()
elif choice == 2:
    durchmesser = float(input("Was ist der Durchmesser von deinem Kreis? "))
    print()
elif choice == 3:
    fläche = float(input("Was ist die Fläche von deinem Kreis? "))
    print()
elif choice == 4:
    umfang = float(input("Was ist der Umfang von deinem Kreis? "))
    print()

# rechne es aus wenn es der durchmesser ist 2 oder wenn es der radius ist 1

if choice == 1:
    durchmesser = radius * 2
    print("Der Durchmesser ist: ", round(durchmesser, 2), "wenn der Radius", radius, "ist")
    # rechne die fläche, den umfang und den durchmesser aus
    print("Die Fläche ist: ", round(area(radius), 2), "wenn der Radius", radius, "ist")
    print("Der Umfang ist: ", round(circumference(radius), 2), "wenn der Radius", radius, "ist")
    print("Der Durchmesser ist: ", round(durchmesser, 2), "wenn der Radius", radius, "ist")



    print()
elif choice == 2:
    radius = durchmesser / 2
    print("Der Radius ist: ", round(radius, 2), "wenn der Durchmesser", durchmesser, "ist")
    print("Die Fläche ist: ", round(area(radius), 2), "wenn der Radius", radius, "ist")
    print("Der Umfang ist: ", round(circumference(radius), 2), "wenn der Radius", radius, "ist")
    print("Der Durchmesser ist: ", round(radius * 2, 2), "wenn der Radius", radius, "ist")
    print()
    # mach mir das gleiche für das gleiche wie oben für fläche und umfang


elif choice == 3:


    print()
    radius = (fläche / 3.1415926535897932384626433832795) ** 0.5
    print("Der Radius ist: ", round(radius, 2), "wenn die Fläche", fläche, "ist")
    print("Der Umfang ist: ", round(circumference(radius), 2), "wenn die Fläche", fläche, "ist")
    print("Der Durchmesser ist: ", round(radius * 2, 2), "wenn die Fläche", fläche, "ist")
    print()

elif choice == 4:


    print()
    radius = umfang / (2 * 3.1415926535897932384626433832795)
    print("Der Radius ist: ", round(radius, 2), "wenn der Umfang", umfang, "ist")
    print("Die Fläche ist: ", round(area(radius), 2), "wenn der Umfang", umfang, "ist")
    print("Der Durchmesser ist: ", round(radius * 2, 2), "wenn der Umfang", umfang, "ist")
    print()


else:
    print("Falsche Eingabe!")
    exit()



print()




# program end