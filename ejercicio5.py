p_e = 0.01
p_pos_e = 0.95
p_pos_noe = 0.10

resultado = (p_pos_e * p_e) / ((p_pos_e * p_e) + (p_pos_noe * (1 - p_e)))

print("Probabilidad:", resultado)
