def fase_grupos(grupos: dict, continentes: dict) -> dict:
    resultado_grupos = {}
    
    for grupo, dados in grupos.items():
        for resultados in dados.values():
            paises_partida = [resultados[0], resultados[-1]]
            gols = [resultados[1], resultados[2]]
            for i, pais in enumerate(paises_partida):
                for continente, paises in continentes.items():
                    pts = 0
                    if gols[i] == gols[i-1]:
                        pts = 1
                    elif gols[i] > gols[i-1]:
                        pts = 3
                    gols_pro = gols[i]
                    gols_contra = gols[i-1]
                    if pais not in resultado_grupos and pais in paises:
                        resultado_grupos[pais] = {
                            'continente': continente,
                            'grupo': grupo,
                            'pontuacao': pts,
                            'gols pro': gols_pro,
                            'gols contra': gols_contra,
                            'saldo de gols': gols_pro - gols_contra
                        }
                        break
                    elif pais in resultado_grupos:
                        resultado_grupos[pais]['pontuacao'] += pts
                        resultado_grupos[pais]['gols pro'] += gols_pro
                        resultado_grupos[pais]['gols contra'] += gols_contra
                        resultado_grupos[pais]['saldo de gols'] += gols_pro - gols_contra
                        break
    
    return resultado_grupos