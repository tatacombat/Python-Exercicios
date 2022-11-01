def voto(x=0):
    from datetime import date
    atual = date.today()
    resp = 'none'
    if x == 0:
        resp = 'Idade Inválida'
    elif atual.year - x < 16:
        resp = f'Com {atual.year-x} anos: NÃO VOTA'
    elif atual.year - x >= 18:
        resp = f'Com {atual.year - x} anos: VOTO OBRIGATÓRIO.'
    elif atual.year - x > 65 or 16 <= atual.year - x < 18:
        resp = f'Com {atual.year - x} anos: VOTO OPCIONAL.'
    return resp


print(('-=' * 20))
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

#def voto(ano):
#    from datetime import date
#    atual = date.today().year
#    idade = atual - ano
#    if idade < 16:
#        return f'Com {atual.year-x} anos: NÃO VOTA'
#    elif 16 <= idade < 18 or idade > 65:
#        return f'Com {atual.year - x} anos: VOTO OPCIONAL.'
#    else:
#        return f'Com {atual.year - x} anos: VOTO OBRIGATÓRIO.'


#print(('-=' * 20))
#nasc = int(input('Em que ano você nasceu? '))
#print(voto(nasc))