def calcula_porcentagens(results: dict):
    all_errors = 0

    for v in results.values():
        all_errors += v

    for k, v in results.items():
        results[k] = 100 * (v / all_errors)

    return results
