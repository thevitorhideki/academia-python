def nota_final(media_quiz,nota_AI,nota_AF,nota_EP1,nota_EP2,nota_PF):
    if media_quiz<0 or media_quiz>10 or nota_AI<0 or nota_AI>10 or nota_AF<0 or nota_AF>10 or nota_EP1<0 or nota_EP1>10 or nota_EP2<0 or nota_EP2>10 or nota_PF<0 or nota_PF>10:
        return 0
    else:
        NI=0.4*nota_AI+0.5*nota_AF+0.1*media_quiz
        NG=0.1*nota_EP1+0.2*nota_EP2+0.7*nota_PF



        if NI>=5 and NG>=5:
            NF=(NI+NG)/2
            return NF
        elif NI<5 or NG<5:
            NF=min(NI,NG)
            return NF
        else:
            return 0

print(nota_final(8,5,5,2,4,4))