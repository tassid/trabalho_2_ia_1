import random
from deap import base, creator, tools, algorithms

NUM_PERIODOS = 4 

# Definindo o problema
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Função para gerar informações de disciplinas e professores
def generate_data():
  disciplinas = [
    {"id": 1, "nome": "CC1AED1", "carga_horaria": 90, "professor": "Evandro Da Silva Dos Santos", "periodo": 1, "dia": 2, "mes_ano_ingresso": "Ago/2022"},
    {"id": 2, "nome": "CC1ICC", "carga_horaria": 45, "professor": "Claudio Jose Biazus", "periodo": 1, "dia": 3, "mes_ano_ingresso": "Set/2016"},
    {"id": 3, "nome": "CC1MBD", "carga_horaria": 60, "professor": "Giani Carla Ito", "periodo": 1, "dia": 4, "mes_ano_ingresso": "Mar/2017"},
    {"id": 4, "nome": "HU1LA", "carga_horaria": 45, "professor": "Vera Lucia Vasilevski Dos Santos Araujo", "periodo": 1, "dia": 5, "mes_ano_ingresso": "Jun/2014"},
    {"id": 5, "nome": "MA1FM", "carga_horaria": 60, "professor": "Diego Venancio Thomaz", "periodo": 1, "dia": 6, "mes_ano_ingresso": "Abr/2013"},
    {"id": 6, "nome": "MA1LM", "carga_horaria": 45, "professor": "Evandro Alves Nakajima", "periodo": 1, "dia": 2, "mes_ano_ingresso": "Jun/2014"},
    {"id": 7, "nome": "CC2AED2", "carga_horaria": 60, "professor": "Leiliane Pereira De Rezende", "periodo": 2, "dia": 3, "mes_ano_ingresso": "Set/2019"},
    {"id": 8, "nome": "CC2CLD", "carga_horaria": 60, "professor": "Gloria Patricia Lopez Sepulveda", "periodo": 2, "dia": 4, "mes_ano_ingresso": "Jul/2022"},
    {"id": 9, "nome": "CC2ER", "carga_horaria": 60, "professor": "Luana Menezes Monguilod", "periodo": 2, "dia": 5, "mes_ano_ingresso": "Ago/2023"},
    {"id": 10, "nome": "CC2POO", "carga_horaria": 60, "professor": "Giuvane Conti", "periodo": 2, "dia": 6, "mes_ano_ingresso": "Fev/2016"},
    {"id": 11, "nome": "MA2MA", "carga_horaria": 60, "professor": "Evandro Alves Nakajima", "periodo": 2, "dia": 2, "mes_ano_ingresso": "Jun/2014"},
    {"id": 13, "nome": "OPHE", "carga_horaria": 30, "professor": "Claudio Jose Biazus", "periodo": 2, "dia": 3, "mes_ano_ingresso": "Set/2016"},
    {"id": 14, "nome": "OPHHCA", "carga_horaria": 30, "professor": "Dejane Santos Alves", "periodo": 2, "dia": 4, "mes_ano_ingresso": "Set/2016"},
    {"id": 15, "nome": "OPHIT1", "carga_horaria": 30, "professor": "Vera Lucia Vasilevski Dos Santos Araujo", "periodo": 2, "dia": 5, "mes_ano_ingresso": "Jun/2014"},
    {"id": 18, "nome": "OPHMP", "carga_horaria": 30, "professor": "Vera Lucia Vasilevski Dos Santos Araujo", "periodo": 2, "dia": 6, "mes_ano_ingresso": "Jun/2014"},
    {"id": 20, "nome": "CC3AED3", "carga_horaria": 60, "professor": "Thiago Franca Naves", "periodo": 3, "dia": 2, "mes_ano_ingresso": "Fev/2016"},
    {"id": 21, "nome": "CC3AOC", "carga_horaria": 90, "professor": "Claudio Jose Biazus", "periodo": 3, "dia": 3, "mes_ano_ingresso": "Set/2016"},
    {"id": 27, "nome": "CC4LBD", "carga_horaria": 60, "professor": "Leiliane Pereira De Rezende", "periodo": 4, "dia": 3, "mes_ano_ingresso": "Set/2019"},
    {"id": 28, "nome": "CC4PO", "carga_horaria": 60, "professor": "Gloria Patricia Lopez Sepulveda", "periodo": 4, "dia": 4, "mes_ano_ingresso": "Jul/2022"},
    {"id": 29, "nome": "CC4RC", "carga_horaria": 60, "professor": "Agnaldo Da Costa", "periodo": 4, "dia": 5, "mes_ano_ingresso": "Jun/2014"},
    {"id": 30, "nome": "CC4SO", "carga_horaria": 60, "professor": "Hamilton Pereira Da Silva", "periodo": 4, "dia": 6, "mes_ano_ingresso": "Jul/2013"},
    {"id": 31, "nome": "MA4PE", "carga_horaria": 60, "professor": "Diego Venancio Thomaz", "periodo": 4, "dia": 2, "mes_ano_ingresso": "Abr/2013"},
  ]

  professores = [
    {"nome": "Evandro Da Silva Dos Santos", "disponibilidade": ["Ago/2022"]},
    {"nome": "Claudio Jose Biazus", "disponibilidade": ["Set/2016"]},
    {"nome": "Giani Carla Ito", "disponibilidade": ["Mar/2017"]},
    {"nome": "Vera Lucia Vasilevski Dos Santos Araujo", "disponibilidade": ["Jun/2014"]},
    {"nome": "Diego Venancio Thomaz", "disponibilidade": ["Abr/2013"]},
    {"nome": "Evandro Alves Nakajima", "disponibilidade": ["Jun/2014"]},
    {"nome": "Leiliane Pereira De Rezende", "disponibilidade": ["Set/2019"]},
    {"nome": "Gloria Patricia Lopez Sepulveda", "disponibilidade": ["Jul/2022"]},
    {"nome": "Luana Menezes Monguilod", "disponibilidade": ["Ago/2023"]},
    {"nome": "Giuvane Conti", "disponibilidade": ["Fev/2016"]},
    {"nome": "Thiago Franca Naves", "disponibilidade": ["Fev/2016"]},
    {"nome": "Agnaldo Da Costa", "disponibilidade": ["Jun/2014"]},
    {"nome": "Hamilton Pereira Da Silva", "disponibilidade": ["Jul/2013"]},
  ]

  return disciplinas, professores



# Obtendo dados de disciplinas e professores
disciplinas, professores = generate_data()

# Função de inicialização de um cromossomo (indivíduo)
def init_individual():
    return [(random.choice(disciplinas), random.choice(professores)["nome"]) for _ in disciplinas]

# Função de avaliação (fitness)
def evaluate(individual):
    # Inicialize um dicionário para rastrear a carga horária de cada professor em cada período
    professor_horarios = {professor["nome"]: {f"periodo_{i+1}": 0 for i in range(NUM_PERIODOS)} for professor in professores}

    # Inicialize variáveis para rastrear conflitos e carga horária total
    conflitos = 0
    carga_horaria_total = 0

    # Percorra as disciplinas do indivíduo
    for (disciplina, professor_nome) in individual:
        periodo = disciplina["periodo"]
        carga_horaria = disciplina["carga_horaria"]

        # Obtenha o objeto do professor usando o nome
        professor = next(p for p in professores if p["nome"] == professor_nome)

        # Verifique se o professor está disponível no período
        if periodo in professor["disponibilidade"]:
            # Verifique se há conflito de horário para o professor
            if carga_horaria + professor_horarios[professor["nome"]][f"periodo_{periodo}"] <= 180:
                # Atualize a carga horária do professor no período
                professor_horarios[professor["nome"]][f"periodo_{periodo}"] += carga_horaria
                carga_horaria_total += carga_horaria
            else:
                conflitos += 1
        else:
            conflitos += 1

    # Quanto menor o número de conflitos e maior a carga horária total, melhor é o indivíduo
    fitness_value = conflitos + (1/carga_horaria_total if carga_horaria_total > 0 else 0)

    return (fitness_value,)



# Definindo operadores genéticos
toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, init_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Parâmetros do algoritmo genético
population_size = 100
num_generations = 500

# Criando a população inicial
population = toolbox.population(n=population_size)

# Executando o algoritmo genético
algorithms.eaMuPlusLambda(population, toolbox, mu=population_size, lambda_=2*population_size,
                          cxpb=0.7, mutpb=0.2, ngen=num_generations, stats=None, halloffame=None, verbose=True)

# Obtendo o melhor indivíduo
best_individual = tools.selBest(population, k=1)[0]

# Imprimindo o melhor horário encontrado
print("Melhor Horário Encontrado:", best_individual)

# Obtendo o melhor indivíduo
best_individual = tools.selBest(population, k=1)[0]

# Criando uma tabela vazia
horario_table = [["Horário", "Segunda [2]", "Terça [3]", "Quarta [4]", "Quinta [5]", "Sexta [6]"]]

# Preenchendo a tabela com as disciplinas e professores
for periodo in range(1, NUM_PERIODOS + 1):
    row = [f"P{periodo}"]
    for dia in range(2, 7):
        # Encontrando a disciplina atribuída ao período e dia específico
        disciplina = next((disc for disc, prof in best_individual if disc["periodo"] == periodo and disc["dia"] == dia), None)
        
        if disciplina:
            # Obtendo informações da disciplina e professor
            nome_disciplina = disciplina["nome"]
            nome_professor = next(prof["nome"] for prof in professores if prof["nome"] == prof["nome"])
            
            # Construindo a string para a célula da tabela
            cell_content = f"{nome_disciplina}\n({nome_professor})"
        else:
            cell_content = ""
        
        row.append(cell_content)
    
    # Adicionando a linha à tabela
    horario_table.append(row)



# Imprimindo a tabela
for row in horario_table:
    print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*row))



# Criando uma tabela vazia
horario_table = [["Horário", "Segunda [2]", "Terça [3]", "Quarta [4]", "Quinta [5]", "Sexta [6]"]]

# Preenchendo a tabela com as disciplinas e professores
for periodo in range(1, NUM_PERIODOS + 1):
    row = [f"P{periodo}"]
    for dia in range(2, 7):
        # Encontrando a disciplina atribuída ao período e dia específico
        assignment = next(((disc, prof) for disc, prof in best_individual if disc["periodo"] == periodo and disc["dia"] == dia), None)
        
        if assignment:
            # Obtendo informações da disciplina e professor
            disciplina, nome_professor = assignment
            nome_disciplina = disciplina["nome"]
            
            # Construindo a string para a célula da tabela
            cell_content = f"{nome_disciplina}\n({nome_professor})"
        else:
            cell_content = ""
        
        row.append(cell_content)
    
    # Adicionando a linha à tabela
    horario_table.append(row)

# Imprimindo a tabela
for row in horario_table:
    print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*row))

def format_schedule(result):
    formatted_schedule = {}
    for entry in result:
        discipline_info, student = entry
        discipline_name = discipline_info['nome']
        if discipline_name not in formatted_schedule:
            formatted_schedule[discipline_name] = {}
        day = discipline_info['dia']
        period = discipline_info['periodo']
        professor = discipline_info['professor'] if discipline_info['professor'] else "N/A"
        
        formatted_schedule[discipline_name][(day, period)] = f"{professor} ({student})"
    
    return formatted_schedule

def print_schedule(schedule):
    days_of_week = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    periods = ["P1", "P2", "P3", "P4"]

    print("{: <16}".format("Horário"), end="")
    for day in days_of_week:
        print("{: <24}".format(day), end="")
    print()

    for period in periods:
        print("{: <16}".format(period), end="")
        for day in range(2, 7):
            if (day, periods.index(period) + 1) in schedule:
                print("{: <24}".format(schedule[(day, periods.index(period) + 1)]), end="")
            else:
                print("{: <24}".format(""), end="")
        print()

result = [({'id': 29, 'nome': 'CC4RC', 'carga_horaria': 60, 'professor': 'Agnaldo Da Costa', 'periodo': 4, 'dia': 5, 'mes_ano_ingresso': 'Jun/2014'}, 'Giuvane Conti'), 
          # Adicione outras entradas conforme necessário
         ]

formatted_schedule = format_schedule(result)
print_schedule(formatted_schedule)

