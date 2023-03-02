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
