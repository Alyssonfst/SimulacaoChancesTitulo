import random

# Exemplo de probabilidades para um confronto entre time1 e time2
def simulate_game(p_time1_win, p_draw, p_time2_win):
    result = random.random()  # Gera um número aleatório entre 0 e 1
    if result < p_time1_win:
        return 1  # Time 1 vence
    elif result < p_time1_win + p_draw:
        return 0  # Empate
    else:
        return -1  # Time 2 vence

# Número de simulações
num_simulations = 1000000

# Pontuação inicial dos times
times = {
    "America": 10, 
    "Central": 9,
    "Ibis": 7,
    "Afogados": 5,
    "Porto": 5,
    "Salgueiro": 3,
    "Retro": 0,
}

# Tabela de confrontos restantes
confrontos = [
    {"time1": "Central", "time2": "Ibis", "p_time1_win": 0.3524, "p_draw": 0.2734, "p_time2_win": 0.3742},
    {"time1": "Porto", "time2": "Salgueiro", "p_time1_win": 0.4292, "p_draw": 0.3824, "p_time2_win": 0.1883},
    {"time1": "Afogados", "time2": "Retro", "p_time1_win": 0.4918, "p_draw": 0.3786, "p_time2_win": 0.1296},
    {"time1": "Ibis", "time2": "Salgueiro", "p_time1_win": 0.5907, "p_draw": 0.2131, "p_time2_win": 0.1962},
    {"time1": "America", "time2": "Afogados", "p_time1_win": 0.3759, "p_draw": 0.4550, "p_time2_win": 0.1691},
    {"time1": "Porto", "time2": "Retro", "p_time1_win": 0.4918, "p_draw": 0.3786, "p_time2_win": 0.1296},
    {"time1": "America", "time2": "Retro", "p_time1_win": 0.7281, "p_draw": 0.1891, "p_time2_win": 0.0828},
    # Adicione todos os confrontos restantes aqui
]

# Dicionário para armazenar os resultados finais das simulações
vencedores = {team: 0 for team in times.keys()}

# Simular o campeonato
for _ in range(num_simulations):
    # Copiar a pontuação inicial para cada simulação
    pontuacao = times.copy()
    
    # Simular cada confronto
    for confronto in confrontos:
        resultado = simulate_game(confronto["p_time1_win"], confronto["p_draw"], confronto["p_time2_win"])
        if resultado == 1:
            pontuacao[confronto["time1"]] += 3  #"Time 1 vence
        elif resultado == 0:
            pontuacao[confronto["time1"]] += 1  # Empate
            pontuacao[confronto["time2"]] += 1
        else:
            pontuacao[confronto["time2"]] += 3  # Time 2 vence
    
    # Determinar o vencedor desta simulação
    vencedor = max(pontuacao, key=pontuacao.get)
    vencedores[vencedor] += 1

# Exibir o resultado final
for team, wins in vencedores.items():
    print(f"{team}: venceu {wins / num_simulations * 100:.2f}% das simulações")
