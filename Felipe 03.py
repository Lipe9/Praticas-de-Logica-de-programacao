print('''
1 - Desenvolvimento de Sistema
2 - Edifiçãoes
3 - Multiídias
''')

curso = int(input("Insira seu curso: "))

print(f'''
 2 para Segunda-Feira
 3 para Terça-Feira
 4 para Quarta-Feira
 5 para Quinta-Feira
 6 para Sexta-Feira
''')

dia_da_semana = int(input(f"Insira o dia da Semana: "))

if curso == 1:
    if dia_da_semana == 2:
        print(f'''
     Formação Cidadania
     História
     Mundo do Trabalho
     Empreendedorismo
     Aprof, em Língua Portuguesa
     Aprof, em Matemática
     Filosofia
     ''')   
    elif dia_da_semana == 3:
        print('''
     Geografia - Roberta
     Matemática - Elizangela
     Química - Rosiane
     Biologia - Jhefferson
     ''')
    elif dia_da_semana == 4:
        print('''
     Lógica de programação - Evaldo
     Projeto de Vida- Daniele
     Arte - Madson
     Língua Inglesa - Madson
     Sociologia - Fernanda
     Educação Física - Pedro
     ''')
    elif dia_da_semana == 5:
        print('''
     Projeto de Vida- Daniele
     Planejamento de Carreira - Evaldo
     Arquiteturae Man. de Computadores - Evaldo
     Língua Espanhol- Daniele
     Lógica de programação - Evaldo
     Horário de Estudo I - Madson
     ''')
    elif dia_da_semana == 6:
        print('''
     Hor. De Estudo II - Fernando
     Planejamento de Carreira-Evaldo
     Física- Fernando
     Arquiteturae Man. de Computadores
     Língua Portuguesa - Tarcisia
     Aprof. em História - Fernanda
     ''')    
elif curso == 2:
    if dia_da_semana == 2:
         print('''
     Form. para a cidadania - Roberta
     Física - Fernando
     Matemática - Elizangela
     ''')
    elif dia_da_semana == 3:
         print('''
     História - Fernanda
     Mundo do Trabalho - Jhefferson
     Int. ao Curso e Ética Profissional
     ''')
    elif dia_da_semana == 4:
         print('''
     Língua Portuguesa - Tarcisia
     Informática Básica - Cleilda
     Int. ao Curso e Ética Profissional
     ''')
    elif dia_da_semana == 5:
         print('''
     Desenho Técnico
     Mecânica de Solos
     Língua Espanhol- Daniele
     ''')
    elif dia_da_semana == 6:
         print('''
     Projeto de Vida- Daniele
     Aprof. em Matemática - Elizangela
     Empreendedorismo - Pedro
     ''')
elif curso == 3:
    if dia_da_semana == 2:
         print('''
     Form. para a cidadania - Daniele
     Arte - Madson
     Física - Fernando
     ''')
    elif dia_da_semana == 3:
         print('''
     Biologia - Jhefferson
     Proj. Interdisciplinares I - Rosiane
     Aprof. em História - Fernanda
     ''')
    elif dia_da_semana == 4:
         print('''
     Língua Inglesa - Madson
     Aprof. em Língua Portuguesa - Tarcisia
     Projeto de Vida- Daniele
     ''')
    elif dia_da_semana == 5:
         print('''
     Matemática - Elizangela
     Língua Espanhol- Daniele
     Hor. de Estudo I - Pedro
     ''')
    elif dia_da_semana == 6:
         print('''
     História - Fernanda
     Informática Básica - Cleilda
     Projeto de Vida- Daniele
     ''')
else:
    print('''Curso ivalido''')
