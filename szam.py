import random
def elso():
    velsz = random.randint(1, 50)
    print("I/A:\n \t A generált szám: {}".format(velsz))
    if velsz % 5 == 0 and velsz % 3 == 0:
        print("I/B: \n \t A szám öttel és hárommal is osztható!")
    elif velsz % 5 == 0:
        print("I/B: \n \t A szám öttel osztható!")
    elif velsz % 3 == 0:
        print("I/B: \n \t A szám hárommal osztható!")

