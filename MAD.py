import pulp

# Criação do modelo
model = pulp.LpProblem("MAD_Portfolio", pulp.LpMinimize)

# Variáveis de decisão
x_A = pulp.LpVariable('x_A', lowBound=0)
x_B = pulp.LpVariable('x_B', lowBound=0)
x_C = pulp.LpVariable('x_C', lowBound=0)
y_1 = pulp.LpVariable('y_1', lowBound=0)
y_2 = pulp.LpVariable('y_2', lowBound=0)
y_3 = pulp.LpVariable('y_3', lowBound=0)

# Função objetivo
model += (1/3) * (y_1 + y_2 + y_3), "Media dos Desvios Absolutos"

# Restrições
model += x_A + x_B + x_C == 1, "Soma das proporções de investimento"
model += 5.33 * x_A + 2.00 * x_B + 5.00 * x_C >= 4, "Retorno Esperado Mínimo"

# Desvio absoluto para cada período
R_1 = 5 * x_A + 3 * x_B + 4 * x_C
R_2 = 7 * x_A + 2 * x_B + 6 * x_C
R_3 = 4 * x_A + 1 * x_B + 5 * x_C
R_medio = 4.44 

model += y_1 >= R_1 - R_medio
model += y_1 >= R_medio - R_1
model += y_2 >= R_2 - R_medio
model += y_2 >= R_medio - R_2
model += y_3 >= R_3 - R_medio
model += y_3 >= R_medio - R_3

# Resolução do problema
model.solve()

# Resultados
print(f"Proporção investida em A: {x_A.varValue:.4f}")
print(f"Proporção investida em B: {x_B.varValue:.4f}")
print(f"Proporção investida em C: {x_C.varValue:.4f}")
print(f"Desvio absoluto medio: {(pulp.value(y_1) + pulp.value(y_2) + pulp.value(y_3)) / 3:.4f}")