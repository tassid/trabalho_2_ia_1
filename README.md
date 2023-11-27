# Trabalho 2 - Algoritmo Genético
Tassiane Anzolin

https://colab.research.google.com/drive/1oHMZD3Gg8DpSzRq-drTTQ9mtD55RvAYV?usp=sharing

## Escopo
O trabalho consiste em implementar um algoritmo genético para montar a grade horários do curso de Ciência da Computação do campus Santa Helena do 1º ao 4º período. O algoritmo deve gerar uma distribuição de disciplinas onde não existam conflitos entre os horários de disciplinas que são pré-requisito e suas correspondentes e nem de horários dos professores, onde um professor não pode ministrar diferentes disciplinas no mesmo dia e horário. As disciplinas do curso podem ser obtidas no site da UTFPR Santa Helena, abaixo seguem links de trabalhos que explicam como modelar o problema. Deve ser feito um relatório explicando cada estratégia adotada na montagem do algoritmo genético, desde a codificação dos cromossomos até a escolha da condição para finalizar o algoritmo.

## Requisitos do Trabalho:

- Codificar o algoritmo genético ou utilizar algum framework/biblioteca
- Desenvolver estratégias para cada etapa do algoritmo
- Executar pelo menos 500 iterações do ciclo do algoritmo genético.
- Gerar um relatório final com os melhores resultados encontrados
# Relatório
## Definição do Problema
- O código aborda o problema de agendar horários acadêmicos para um conjunto de disciplinas ao longo de vários períodos, levando em consideração restrições como disponibilidade de professores, carga horária das disciplinas e evitar conflitos de horários.

- O problema de agendamento é abordado usando um Algoritmo Genético implementado com a biblioteca DEAP. Componentes-chave incluem:

- Representação do Cromossomo: Cada indivíduo na população representa um possível horário, consistindo de pares de disciplinas e professores atribuídos.

- Avaliação de Aptidão (Fitness): A função de aptidão visa minimizar conflitos e maximizar a distribuição total de carga horária entre os professores.

- Operadores Genéticos: Crossover de dois pontos e mutação de embaralhamento são usados para criar diversidade genética.

- População e Gerações: Uma população de indivíduos é evoluída ao longo de um número especificado de gerações usando a função eaMuPlusLambda.

## Dados de Entrada
Os dados incluem informações sobre disciplinas e professores, incluindo disponibilidade e carga horária. Disciplinas são atribuídas a períodos específicos, dias e meses.

## Saída
O algoritmo gera o melhor horário encontrado após o número especificado de gerações. Isso inclui a atribuição de disciplinas a períodos, dias e professores específicos.

## Melhor Horário
O melhor horário é impresso, exibindo as disciplinas e professores atribuídos para cada período e dia da semana.

## Melhor Horário
O melhor horário é impresso, exibindo as disciplinas e professores atribuídos para cada período e dia da semana.

# Conclusão
O algoritmo genético gera com sucesso um horário acadêmico otimizado, considerando diversas restrições. A abordagem demonstra a flexibilidade e eficiência de algoritmos genéticos na resolução de problemas complexos de agendamento.

## DEAP e Python
Este projeto se beneficia da implementação eficiente de algoritmos genéticos proporcionada pela biblioteca DEAP (Distributed Evolutionary Algorithms in Python). A biblioteca DEAP oferece uma ampla gama de funcionalidades para a implementação de algoritmos genéticos e algoritmos evolutivos distribuídos em Python. Sua flexibilidade e desempenho tornam-na uma escolha robusta para lidar com problemas complexos, como o desafiador agendamento acadêmico abordado neste projeto. A utilização do DEAP neste projeto ilustra como a colaboração e a disponibilidade de recursos open source são fundamentais para impulsionar o progresso na resolução de problemas complexos por meio de algoritmos evolutivos.


O DEAP é um inovador framework de computação evolutiva projetado para o rápido prototipagem e teste de ideias. Seu objetivo é tornar os algoritmos explícitos e as estruturas de dados transparentes, proporcionando uma abordagem flexível e eficiente para a implementação de algoritmos evolutivos. O DEAP destaca-se pela harmonia perfeita com mecanismos de paralelização, como multiprocessing e SCOOP, facilitando a escalabilidade e a execução eficiente em ambientes distribuídos. A documentação abrangente apresenta conceitos-chave e diversas funcionalidades, oferecendo aos desenvolvedores as ferramentas necessárias para construir suas próprias evoluções e explorar o potencial da computação evolutiva.
