"Listcomprehension"

linhas_e_colunas1 = []
for x in range(1, 4):
    for y in range(1, 4):
        lc = linhas_e_colunas1.append(x, y)
print(lc)

linhas_e_colunas = [ (x, y) if y != 2 else (x, y * 1000) for x in range (1, 4) for y in range(1, 4) if x != 2]

print(linhas_e_colunas)
