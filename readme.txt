executar: python3 city_plan.py [ficheiro de input]

navegação: inicialmente, é calculada a solução inicial de onde se partirá nos algoritmos de optmização (excepto do genético, este precisa de 
calcular duas soluções adicionais). Depois, é escolher os algortimos e inserir os valores consoante cada algoritmo. Os algortimos escolhidos
são deixados numa queue que depois são resolvidos de forma consecutiva. Isto permite que se deixe o programa a processar vários algoritmos
com diferentes pârametros sem que tenha que se ir ao computador fazer verificações periodicamente.
