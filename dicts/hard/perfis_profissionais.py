def perfis_profissionais(censo: dict):
    jobs = {desc['ramo']: {'média salarial': [], 'tempo médio de serviço': [
    ], 'servidores': []} for desc in censo.values()}

    for desc in censo.values():
        for censo_v in desc.values():
            for jobs_k, jobs_v in jobs.items():
                if censo_v == jobs_k:
                    jobs_v['média salarial'].append(desc['salário'])
                    jobs_v['tempo médio de serviço'].append(
                        desc['anos de serviço'])
                    if desc['e-mail'][desc['e-mail'].index('@') + 1:desc['e-mail'].index('.com')] not in jobs_v['servidores']:
                        jobs_v['servidores'].append(
                            desc['e-mail'][desc['e-mail'].index('@') + 1:desc['e-mail'].index('.com')])

    for infos in jobs.values():
        for k, v in infos.items():
            if k == 'média salarial':
                infos[k] = sum(v) / len(v)
            elif k == 'tempo médio de serviço':
                infos[k] = sum(v) / len(v)

    return jobs
