Ranks = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

Suits = {
    'd': 1,
    'c': 2,
    'h': 3,
    's': 4
}

Types = {
    'HighCard':      1,
    'OnePair':       2,
    'TwoPairs':      3,
    '3OfAKind':      4,
    'Straight':      5,
    'Flush':         6,
    'FullHouse':     7,
    '4OfAKind':      8,
    'StraightFlush': 9
}

PHASE = {'INIT_DEALING', 'BIDDING', 'SHOWDOWN'}
AGENT_ACTIONS = {'CALL', 'BET5', 'BET10', 'BET25', 'FOLD'}
BETTING_ACTIONS = {'BET5', 'BET10', 'BET25'}

fixed_hands = [(['Tc', '9d', 'Qd', '8h', 'Kh'], ['2s', '8s', '4c', '3s', '4h']),
               (['Js', 'Qc', 'Ac', '5c', '7c'], ['Kd', '7d', '2s', '5h', '2c']),
               (['Ts', 'Ac', 'Ad', 'Qs', '8s'], ['8c', 'As', '6c', '4h', 'Kd']),
               (['Kc', 'Ts', '4d', 'Jh', 'Jc'], ['5s', '9c', 'Qh', '8h', '3s']),
               (['3s', '2c', '6s', '4s', '9s'], ['Ks', '9c', '8c', 'Ts', '6d']),
               (['Kd', '4c', '6h', '4h', '2c'], ['Kc', 'Jc', '2s', '5d', '3s']),
               (['5s', '5d', '8c', 'Tc', '7h'], ['Jd', '5h', 'Kd', 'Ad', '8s']),
               (['Kc', '3s', 'Ts', 'Qh', '8c'], ['As', 'Kd', '9d', '7c', '2d']),
               (['2d', 'Ad', 'Tc', '7s', 'Jd'], ['3d', '5c', 'Ac', 'Td', '9d']),
               (['2c', '5c', 'As', '7s', 'Ac'], ['Ah', 'Tc', 'Jc', '2h', '9c']),
               (['7c', '4c', 'Ts', 'Th', '5c'], ['7d', 'Qc', '8s', '5d', '9s']),
               (['Td', 'Js', 'Ad', 'Th', '6h'], ['8s', 'Tc', '3h', 'Qs', '3d']),
               (['Qd', '7s', 'Qh', '8d', '2h'], ['8s', '5c', '7d', '4c', '6h']),
               (['5s', '4d', '3d', 'Kh', '9h'], ['2s', '9c', '2c', '7h', '8h']),
               (['2d', 'Ad', '3c', 'Tc', 'Qh'], ['4s', 'Js', 'Jd', '2c', '7h']),
               (['Kd', '9d', '4h', 'Th', 'Ac'], ['3h', 'Jd', '3d', 'Tc', 'Qd']),
               (['2h', '3c', 'Jh', '8d', '2s'], ['Td', 'As', 'Ad', 'Jc', 'Th']),
               (['2s', '4s', 'Kd', '5s', 'Qh'], ['Js', 'Kh', '6h', 'As', '7d']),
               (['4d', '8h', '2c', 'Tc', '7d'], ['Jc', '8s', '2d', '6d', '4c']),
               (['Kc', 'Qc', 'Qh', '4s', '4d'], ['5c', 'Ad', '2c', '5h', 'Tc'])]
