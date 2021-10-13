import cirpy
with open("names.txt") as file:
    data = file.readlines()
for molecule in data:
    try:
        name = molecule.rstrip("\n\r")
        SMILES = cirpy.resolve(name, 'smiles')
        formula = cirpy.resolve(SMILES, 'formula')
        Mw = cirpy.resolve(SMILES, 'Mw')
        print(name, ";", SMILES, ";", formula, ";", Mw)
        
        except:
        print("none")