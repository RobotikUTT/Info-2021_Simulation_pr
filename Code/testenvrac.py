"""
Ce fichier convertit en fichier .c les intructions du fichier 'pyS.txt'.
Ce fichier sera lu par la carte arduino.
"""
number = 3
# Constantes pour l'écriture du fichier.c
# nom du fichier : instructionList.h
COMMENTSTRING = (
    "/*\n * \\ file instructionList.h\n * \\created by the simulation\n*/"
)
HEADSTRING = "#ifndef INSTRUCTIONLIST_H\n#define INSTRUCTIONLIST_H"
FOOTSTRING = "#endif // INSTRUCTIONLIST_H"
declare1 = "int nbrGoto = "
declare2 = "int golist = ["

with open('instructionList.h', 'w') as isC:
    # Ecrit la tête du fichier
    isC.write(COMMENTSTRING + "\n\n\n" + HEADSTRING + "\n\n" + declare2)
    """
    with open("pySim.txt", "r") as pyS:
        for i in range(number*2-1):
            x = pyS.readline()
            isC.write(x.removesuffix('\n'))
            isC.write(", ")

        # Ecrit la fin du fichier
        x = pyS.readline()
        isC.write(
            x.removesuffix('\n') + "];\n" + declare1 + str(number*2) +
            ";\n\n" + FOOTSTRING
        )
    """
    # Lit l'ensemble du fichier dans un tableau pour chaque ligne
    pyS = open('pySim.txt', 'r')
    coord = pyS.readlines()
    pyS.close()
    # Retire les '\n' de chaque ligne et transforme en int
    for i in range(len(coord)):
        coord[i] = int(coord[i].removesuffix('\n'))
    coord = tuple(coord)

    for xy in coord[:-1]:
        isC.write(str(xy) + ", ")
    isC.write(
        str(coord[-1]) + "];\n" + declare1 + str(number*2) +
        ";\n\n" + FOOTSTRING
    )
