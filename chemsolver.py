from chempy import balance_stoichiometry

# eq = '12 C4H9Cl + O2 -> CO2 + H2O + Cl2'
eq = input("Enter the chemical equation to balance (Sample format: 12 C4H9Cl + O2 -> CO2 + H2O + Cl2): ")
eq = eq.strip() # Strip extra white spaces
print(repr(eq))
reactants, products = eq.split('->')
reactant_dict = {}
for r in reactants.split('+'):
    split_r = r.split(None, 1)
    if len(split_r) == 2:
        coeff, name = split_r
        reactant_dict[name.strip()] = int(coeff.strip())
    else:
        reactant_dict[r.strip()] = 1
product_dict = {}
for p in products.split('+'):
    split_p = p.split(None, 1)
    if len(split_p) == 2:
        coeff, name = split_p
        product_dict[name.strip()] = int(coeff.strip())
    else:
        product_dict[p.strip()] = 1
print(reactant_dict)
print(product_dict)
reactants, products = balance_stoichiometry(reactant_dict, product_dict)
print('Balanced equation:')
reactants_str = ' + '.join([f'{coeff}{r}' if coeff != 1 else r for r, coeff in reactants.items()])
products_str = ' + '.join([f'{coeff}{p}' if coeff != 1 else p for p, coeff in products.items()])
print(f'{reactants_str} -> {products_str}')
