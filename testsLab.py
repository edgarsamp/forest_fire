import mesa
import pandas as pd
import numpy as np
from forest_fire.model import ForestFire
from datetime import datetime

# Experimentos estatisticos
# planejamento do experimento
# hipotese 1 - A variacao da biomassa na floresta influencia diretamente na area de queimada
controles_e_seus_niveis = {
    "width": 100,
    "height": 100,
    "density": 0.65,
    "biomass": 5, 
    #"variation": 1,
}
variaveis_independentes_e_seus_niveis = {
    "variation": [*range(0, 4, 1)]
}

lista_de_fatores = variaveis_independentes_e_seus_niveis.keys()
print("Lista de Fatores: "+str(lista_de_fatores))
lista_de_niveis_por_fator = variaveis_independentes_e_seus_niveis.values()
print("Lista de tratamentos ou niveis por fator: "+str(lista_de_niveis_por_fator))
qtd_de_tratamentos_por_fator = [len(f) for f in lista_de_niveis_por_fator]
print("Quantidade de tratamentos ou niveis por fator: "+str(qtd_de_tratamentos_por_fator))
qtd_total_tratamentos = np.prod([len(f) for f in variaveis_independentes_e_seus_niveis.values()])
print("Quantidade total de tratamentos a serem aplicados: "+str(qtd_total_tratamentos))

# soma os dois dicionarios 
experimental_design_of_independent_plus_control_variables = controles_e_seus_niveis.copy()
experimental_design_of_independent_plus_control_variables.update(variaveis_independentes_e_seus_niveis)

replicacoes=2 # no desenho experimental, esse parametro e chamado de replicacao, e indica a quantidade de replicacoes de cada tratamento 
print("Quantidade de replicacoes para cada tratamento:"+str(replicacoes))
print("Quantidade total de simulacoes independentes a serem realizadas:"+str(replicacoes*qtd_total_tratamentos))
print("Uma vez que cada simulacao e um sujeito novo, completamente definido por variaveis aleatorias, estaremos fazendo um 'Between Subject Factorial Design'")

qtd_maxima_passos_para_estabilizar = 100 # qtd de interacoes necessarias para o fenomeno e estabilizar
inicio_experimento = datetime.now()

qtd_processadores = 8

results = mesa.batch_run(
    ForestFire,
    parameters=experimental_design_of_independent_plus_control_variables,
    iterations=replicacoes,
    max_steps=qtd_maxima_passos_para_estabilizar,
    number_processes=qtd_processadores, # usar todos os processadores disponiveis em um arranjo multithread
    data_collection_period=-1,
    display_progress=True,
)

# gera uma string com data e hora
fim_experimento = datetime.now()
duracao_experimento = fim_experimento - inicio_experimento
fim_experimento_str = str ( fim_experimento )

file_name_suffix = (
    "_fatores[" +str(lista_de_fatores).replace("[","").replace("]","").replace("(","").replace(")","").replace("-","").replace("dict_keys","")+"]"
    "_tratam[" + str(qtd_total_tratamentos) +"]" +
    "_replic[" + str (replicacoes) +"]"+
    "_passos["+ str (qtd_maxima_passos_para_estabilizar)+"]"+
    "_process["+ str (qtd_processadores)+ "]"+
    "_segs["+ str(duracao_experimento.seconds) + "]"+
    "_final["+ fim_experimento_str +"]"
). replace ( ":" , "-" ). replace ( " " , "-" )
# define um prefixo para o nome para o arquivo de dados
model_name_preffix = "Exp.Tot.Cruzados_BetweenSubject_SchellingPolarizado"
# define o nome do arquivo
file_name = model_name_preffix + file_name_suffix + ".csv"
print(file_name)

results_df = pd.DataFrame(results)
results_df.to_csv("data/"+file_name)