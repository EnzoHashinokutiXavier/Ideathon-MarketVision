refrii = 30
cervejai = 50
macai = 5
painel = 0
refrip = 5
cervejap = 6
macap = 36
refriv = 0
cervejav = 0
macav = 0
refric = 2
cervejac = 3
macac = 15
perigo = 0
perigoa = 0
perigob = 0
refriat = 0
cervejaat = 0
macaat = 0
refritt = 0
cervejatt = 0
macatt = 0
print('_'*60)
print('\033[33mBem vindo ao painel de controle de estoque da MarketVision !')
for c in range(0, 50):
    opcao = int(input('\033[m[1]Ver produtos em estoque  \n[2]Atualizar quantia em estoque  \n[3]Adicionar ao estoque  \
    \n[4]Retirar do estoque  \n[5]Acessar o caixa  \n[6]Análise de dados\n'))
    #produtos em estoque
    if opcao == 1:
        print('\033[32mHá {} refrigerantes, {} cervejas e {}kg de maçã no estoque'.format(refrii, cervejai, macai))
    #atualizaçao de estoque
    elif opcao == 2:
        refrif = int(input('Quantos refrigerantes há no estoque?'))
        cervejaf = int(input('Quantas cervejas há no estoque ?'))
        macaf = float(input('Qauntos kilos de maçã há no estoque ?'))
        if refrii > refrif:
            print('\033[31mHouve a perda de {} refrigerantes.'.format(refrii - refrif))
            perigo = 1
            perigob = 1
        if refrif > refrii:
            print('\033[32mHá {} refrigerantes amais em relação aos dados anteriores'.format(refrif - refrii))
        if refrii == refrif:
            print('\033[32mNão ocorreram alterações no número de refrigerantes !')
        if cervejai > cervejaf:
            print('\033[31mHouve a perda de {} cervejas.'.format(cervejai - cervejaf))
            perigo = 1
            perigob = 1
        if cervejaf > cervejai:
            print('\033[32mHá {} cervejas amais em relação aos dados anteriores'.format(cervejaf - cervejai))
        if cervejai == cervejaf:
            print('\033[32mNão ocorreram alterações no número de cervejas !')
        if macai > macaf:
            print('\033[31mHouve a perda de {}kg de maçã'.format(macai - macaf))
            perigo = 1
            perigoa = 1
        if macaf > macai:
            print('\033[32mHá {}kg de maçã amais em relação aos dados anteriores'.format(macaf - macai))
        if macai == macaf:
            print('\033[32mNão ocorreram alterações na quantia de maçãns !')
        refrii = int(refrif)
        cervejai = int(cervejaf)
        macai = float(macaf)
        if perigo == 1:
            print('\033[31mVerifique as cameras em suspeita de furto !')
    #adicionar ao estoque
    elif opcao == 3:
        refria = int(input('Quantos refrigerantes deseja adicionar ?'))
        refriat += refria
        refrii = refrii + refria
        cervejaa = int(input('Quantas cervejas deseja adicionar ?'))
        cervejaat += cervejaa
        cervejai = cervejai + cervejaa
        macaa = float(input('Quantos Kilogramas de maçã deseja adicionar ?'))
        macaat += macaa
        macai = macai + macaa
        print('\033[36mHá {} refrigerantes, {} cervejas e {}kg de maçã no estoque'.format(refrii, cervejai, macai))
    #retirar do estoque
    elif opcao == 4:
        refria = int(input('Quantos refrigerantes deseja retirar ?'))
        refritt += refria
        refrii = refrii - refria
        cervejaa = int(input('Quantas cervejas deseja retirar ?'))
        cervejatt += cervejaa
        cervejai = cervejai - cervejaa
        macaa = float(input('Quantos Kilogramas de maçã deseja retirar ?'))
        macatt += macaa
        macai = macai - macaa
        print('\033[36mHá {} refrigerantes, {} cervejas e {}kg de maçã no estoque'.format(refrii, cervejai, macai))
    #caixa de vendas
    elif opcao == 5:
        print('\033[m' '_' * 60)
        print('\033[36mBem vindo ao painel de venda da MarketVision !')
        for n in range(0, 50):
            #caixa aberto
            if painel == 0:
                opcx = int(input('\033[m[1]Ver preços \n[2]Atualizar preços \n[3]Vender produtos \n[4]Histórico de vend\
a\n[5]Fechar o caixa\n'))
                #ver preços
                if opcx == 1:
                    print('\033[36mTabela de Preços : \nRefrigerante R${:.2f}/unidad\nCerveja      R${:.2f}/unidad\nMaç\
ã         R${:.2f}/kg'.format(refrip, cervejap, macap))
                    print('\033[m' '_' * 60)
                #atualizar preços
                elif opcx == 2:
                    refrip = float(input('Novo preço da unidade de refrigerante :'))
                    cervejap = float(input('Novo preço da unidade de cerveja :'))
                    macap = float(input('Novo preço do kg de maçã :'))
                    print('\033[m' '_' * 60)
                #vender produtos
                elif opcx == 3:
                    refriq = int(input('Quantia de refrigerantes :'))
                    cervejaq = int(input('Quantia de cervejas :'))
                    macaq = float(input('Quantia de maçã (kg) :'))
                    total = (refriq * refrip) + (cervejaq * cervejap) + (macaq * macap)
                    print('\033[32mTotal : R${:.2f}'.format(total))
                    pg = int(input('\033[mQual a forma de pagamento ?\n[1]Dinheiro (\033[32m-6%\033[m)\n[2]Débito\n[3]C\
rédito (\033[31m+5% x (número de parcelas -1)\033[m)\n[4]Cancelar\n'))
                    pagamento = 0
                    if pg == 1:
                        print('\033[32mValor a ser cobrado : R${:.2f}'.format(total * 0.94))
                    elif pg == 2:
                        print('\033[32mValor a ser cobrado : R${:.2f}'.format(total))
                    elif pg == 3:
                        parcelas = int(input('Será pago em quantas parcelas ?'))
                        if parcelas == 1:
                            print('\033[32mValor a ser cobrado : R${:.2f}'.format(total))
                        else:
                            print('\033[32mValor a ser cobrado : R${:.2f} por parcela'
                                  .format((total * (1+(0.05 * parcelas)))/parcelas))
                    elif pg == 4:
                        print('\033[31mPagamento cancelado.')
                        pagamento = 1
                    else:
                        print('\033[31mErro, compra cancelada !')
                        pagamento = 1
                    if pagamento == 0:
                        refrii = refrii - refriq
                        cervejai = cervejai - cervejaq
                        macai = macai - macaq
                        refriv += refriq
                        cervejav += cervejaq
                        macav += macaq
                    print('\033[m' '_' * 60)
                #historico de venda
                elif opcx == 4:
                    print('\033[32mForam vendidos :\n{} Refrigerantes\n{} Cervejas\n{}kg de Maçã '.format(refriv,
                                                                                                          cervejav,
                                                                                                          macav))
                    print('\033[m' '_' * 60)
                #fechar o caixa
                elif opcx == 5:
                    painel = 1
                #erro
                else:
                    print('\033[31mERRO')
                    print('\033[m' '_' * 60)
            #caixa fechado
            if painel == 1:
                continue
    #Analise de dados
    elif opcao == 6:
        print('\033[m' '_' * 60)
        print('\033[35mBem vindo ao painel de analise de dados da MarketVision !')
        for y in range(0, 50):
            #painel aberto
            if painel == 0:
                opcy = int(input('\033[m[1]Análise de vendas\n[2]Análise de segurança\n[3]Analise de estoque\n[4]Fechar\
 o painel\n'))
                #analise de vendas
                if opcy == 1:
                    print('\033[35m|Produto        |Quantia        |Total          |Lucro')
                    print('|Refrigerante   |{:<15}|R${:<13}|R${:<13}'.format(refriv, (refriv * refrip),
                                                                             (refrip - refric)*refriv))
                    print('|Cerveja        |{:<15}|R${:<13}|R${:<13}'.format(cervejav, (cervejav * cervejap),
                                                                             (cervejap - cervejac)*cervejav))
                    print('|Maçã           |Kg{:<13}|R${:<13}|R${:<13}'.format(macav, (macav * macap),
                                                                                     (macap - macac) * macav))
                    print('\033[m' '_' * 60)
                #analise de segurança
                elif opcy == 2:
                    if perigo == 0:
                        print('\033[35mNão foram encontradas irregularidades no sistema !')
                    if perigo == 1:
                        if perigoa == 1 and perigob == 0:
                            print('\033[31mOcorreram irregularidades no setor de alimentos !\nRevise a vigilância do se\
tor !')
                        if perigoa == 0 and perigob == 1:
                            print('\033[31mOcorreram irregularidades no setor de bebidas !\nRevise a vigilância do se\
tor !')
                        if perigoa == 1 and perigob == 1:
                            print('\033[31mOcorreram irregularidades nos setores de alimentos e de bebidas !\nRevise a \
vigilância dos setores !')
                    print('\033[m' '_' * 60)
                #analise de estoque
                elif opcy == 3:
                    print('\033[35mForam adicionados ao estoque :\n{} unidades de refrigerante\n{} unidades de cerveja\
\n{} kg de Maçã'.format(refriat, cervejaat, macaat))
                    print('\033[35mForam retirados do estoque :\n{} unidades de refrigerante\n{} unidades de cerveja\n\
{} kg de Maçã'.format(refritt, cervejatt, macatt))
                    print('\033[m' '_' * 60)
                #fechar painel
                elif opcy == 4:
                    painel = 1
                else:
                    print('\033[31mERRO')
            #painel fechado
            if painel == 1:
                continue

    #erro
    else:
        print('\033[31mERRO')
    print('\033[m' '_' * 60)
    if painel == 1:
        print('\033[33mBem vindo ao painel de controle de estoque da MarketVision !')
    painel = 0
