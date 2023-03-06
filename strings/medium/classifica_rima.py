def classifica_rima(syllable1, syllable2, syllable3, syllable4):
    if len(set([syllable1, syllable2, syllable3, syllable4])) == 1:
        return 'outra'
    elif (syllable1, syllable2) == (syllable3, syllable4):
        return 'alternada'
    elif (syllable1, syllable3) == (syllable2, syllable4):
        return 'emparelhada'
    elif (syllable1, syllable2) == (syllable4, syllable3):
        return 'interpolada'
    else:
        return 'outra'
