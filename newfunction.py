def dragon(heat, damage = 10):
    """
    Creates a mean dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: how hard the dragon bites (1-50)
    :return: the sum of heat and damage
    """
    # here comes the body of the function
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("you must use numbers for the dragon attributes")
        return
    print(f"you are creating a dragon with a fire power of {heat} and bite power of {damage}")
    return heat + damage
    #That's it. The idea is to leave two empty strings

dragon1 = dragon(8,10)
dragon2 = dragon(7,10)
if dragon1 > dragon2:
    print("Dragon 1 is stronger")
else:
    print("Dragon 2 is stronger")
dragon3=dragon(40)