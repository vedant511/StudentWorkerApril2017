#!/usr/bin/env python
import json
import random


names = [
    'Macy Leitz',
    'Gwen Hyre',
    'Jenelle Fearn',
    'Alex Warden',
    'Connie Gideon',
    'Deonna Ferrill',
    'Gerard Marceau',
    'Melissa Dancy',
    'Fern Ariola',
    'Ardelle Palomino',
    'Quentin Didonna',
    'Jenny Lenihan',
    'Ta Lavergne',
    'Rosanne Beadle',
    'Lorri Ashburn',
    'Loree Couvillion',
    'Geoffrey Flecha',
    'Pablo Fahy',
    'Elinor Peet',
    'Towanda Gobeil',
    'Artie Ramsay',
    'Sharmaine Bufford',
    'Cherie Salsman',
    'Gregorio Paquet',
    'Jim Hyatt',
    'Fermin Ransom',
    'Loretta Kibler',
    'Liberty Janousek',
    'Bernadine Draheim',
    'Sidney Vallecillo',
    'Dorian Levinson',
    'Necole Toomey',
    'Maurice Sasso',
    'Lonna Grisham',
    'Arie Dennett',
    'Tomiko Lamkin',
    'Alissa Coldren',
    'Luana Ivy',
    'Otto Rebelo',
    'Vickey Joye',
    'Roderick Birchfield',
    'Pat Villanova',
    'Kaitlyn Finnen',
    'Hedy East',
    'Levi Stead',
    'Chelsie Fiorini',
    'Leisa Borgen',
    'Duncan Mulholland',
    'Stacia Monzon',
    'Salvador Cheeks'
]


def gen_bank_account():
    name = random.choice(names).split(' ')
    return {
        'name': {
            'first': name[0],
            'last': name[1]
        },
        'type': random.choice(['checking', 'savings']),
        'balance': random.randint(-10000, 100000)
    }


accounts = [gen_bank_account() for i in range(20)]

with open('accounts.json', 'w') as jsonfile:
    json.dump(accounts, jsonfile, indent=4)
