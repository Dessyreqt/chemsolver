from chempy import balance_stoichiometry

def create_dict_from_side(side):
    dct = {}
    for r in side.split('+'):
        split_r = r.split(None, 1)
        if len(split_r) == 2:
            coeff, name = split_r
            dct[name.strip()] = int(coeff.strip())
        elif len(split_r) == 1:
            dct[split_r[0].strip()] = 1
    return dct

eq = input("Enter the chemical equation to balance (Sample format: 12 C4H9Cl + O2 -> CO2 + H2O + Cl2): ")

reactants, products = eq.split('->')
reactant_dict = create_dict_from_side(reactants)
product_dict = create_dict_from_side(products)

reactants, products = balance_stoichiometry(reactant_dict, product_dict)

print('Balanced equation:')
reactants_str = ' + '.join([f'{coeff}{r}' if coeff != 1 else r for r, coeff in reactants.items()])
products_str = ' + '.join([f'{coeff}{p}' if coeff != 1 else p for p, coeff in products.items()])
print(f'{reactants_str} -> {products_str}')
