import periodictable

#calculate the molar mass of the input material
def calc_molarmass(material):
    elements = periodictable.formula(material)
    molar_mass = sum(element.mass * count for element, count in elements.atoms.items())
    return molar_mass

def mole(mass, molar_mass):
    n = mass/molar_mass
    return n

def conc(n,V):
        c = n/V
        return c
'''
molar_mass = calc_molarmass("H2O")
n = mole(4,molar_mass)
c = conc(n,4)
print(n, c)'''



        
