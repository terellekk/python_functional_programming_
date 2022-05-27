#relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid

def relation_to_luke(name):
    starwars = {
    'Darth Vader' : 'father',
    'Leia'   : 'sister',
    'Han': 'brother in law',
    'R2D2': 'droid'
    }

    return 'Luke, I am your {}.'.format(starwars[name])

relation_to_luke('Darth Vader')

