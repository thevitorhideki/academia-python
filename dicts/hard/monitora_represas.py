def monitora_represas(initial_state: dict, variations: dict) -> dict:
    final_state = {}

    for dam in initial_state:
        initial_state[dam]['volume'] *= initial_state[dam]['capacidade'] / 100

        for k, v in variations.items():
            for variation in v.values():
                if k == dam:
                    initial_state[k]['volume'] += variation[0] - variation[1]

        relative_volume = initial_state[dam]['volume'] / \
            initial_state[dam]['capacidade'] * 100

        if relative_volume < 20:
            final_state.setdefault('emergencia', []).append(dam)
        elif relative_volume < 50:
            final_state.setdefault('critico', []).append(dam)
        elif relative_volume < 70:
            final_state.setdefault('atencao', []).append(dam)
        elif relative_volume < 100:
            final_state.setdefault('normal', []).append(dam)
        else:
            final_state.setdefault('escoar', []).append(dam)

    return final_state


print(monitora_represas(
    {
        'cantareira': {
            'capacidade': 982000,
            'volume': 25
        },
        'guarapiranga': {
            'capacidade': 171000,
            'volume': 95
        },
        'alto tiete': {
            'capacidade': 540000,
            'volume': 55
        }
    },
    {
        'cantareira': {
            '01': [5000, 30000],
            '02': [10000, 35000],
            '03': [0, 29000],
            '04': [31000, 28000],
            '05': [0, 29000]
        },
        'guarapiranga': {
            '01': [6000, 10000],
            '02': [38000, 12000],
            '03': [35000, 14000],
            '04': [0, 13000],
            '05': [15000, 12000]
        },
        'alto tiete': {
            '01': [18000, 30000],
            '02': [15000, 25000],
            '03': [17700, 24000],
            '04': [41000, 28000],
            '05': [13000, 24000]
        }
    }
))
