import os
import copy
import csv
import gymnasium as gym
import ale_py
import numpy as np
import matplotlib.pyplot as plt

gym.register_envs(ale_py)


ENV_ID = "ALE/Pong-v5"
TAMANHO_POPULACAO = 20
NUM_GERACOES = 30
NUM_ENTRADAS = 128      
NUM_OCULTOS = 16
NUM_ACOES = 6          
NUM_ELITE = 2


TAXA_MUTACAO = 0.10
INTENSIDADE_MUTACAO = 0.20

os.makedirs("resultados", exist_ok=True)


def criar_ambiente(render_mode=None):
    return gym.make(
        ENV_ID,
        obs_type="ram",
        render_mode=render_mode
    )


class Agente:
    def __init__(self):
        
        self.W1 = np.random.randn(NUM_ENTRADAS, NUM_OCULTOS) * np.sqrt(2.0 / NUM_ENTRADAS)
        self.b1 = np.zeros(NUM_OCULTOS)
        self.W2 = np.random.randn(NUM_OCULTOS, NUM_ACOES) * np.sqrt(2.0 / NUM_OCULTOS)
        self.b2 = np.zeros(NUM_ACOES)
        self.fitness = 0.0

    def agir(self, estado):
        
        estado = estado.astype(np.float32) / 255.0
        oculto = np.tanh(estado @ self.W1 + self.b1)
        saida = oculto @ self.W2 + self.b2
        return int(np.argmax(saida))




def avaliar(agente, max_passos=3000):
    
    env = criar_ambiente()
    estado, info = env.reset()
    total_recompensa = 0.0
    passos = 0

    while True:
        acao = agente.agir(estado)
        estado, reward, terminated, truncated, info = env.step(acao)
        total_recompensa += reward
        passos += 1

        if terminated or truncated or passos >= max_passos:
            break

    env.close()
    return total_recompensa


def criar_populacao():
    return [Agente() for _ in range(TAMANHO_POPULACAO)]


def selecionar_torneio(populacao, k=3):
    
    candidatos = np.random.choice(populacao, size=k, replace=False)
    melhor = max(candidatos, key=lambda ind: ind.fitness)
    return melhor


def mutar(agente, taxa=TAXA_MUTACAO, intensidade=INTENSIDADE_MUTACAO):
  
    for param in [agente.W1, agente.b1, agente.W2, agente.b2]:
        mascara = np.random.rand(*param.shape) < taxa
        ruido = np.random.randn(*param.shape) * intensidade
        param += mascara * ruido


def nova_geracao(populacao, taxa=TAXA_MUTACAO, intensidade=INTENSIDADE_MUTACAO):
    
    populacao_ordenada = sorted(populacao, key=lambda ind: ind.fitness, reverse=True)

    nova_pop = []

    
    for i in range(NUM_ELITE):
        elite_clone = copy.deepcopy(populacao_ordenada[i])
        nova_pop.append(elite_clone)

    
    while len(nova_pop) < TAMANHO_POPULACAO:
        pai = selecionar_torneio(populacao_ordenada, k=3)
        filho = copy.deepcopy(pai)
        mutar(filho, taxa, intensidade)
        nova_pop.append(filho)

    return nova_pop


def avaliar_aleatorio(episodios=5):
    
    env = criar_ambiente()
    recompensas = []
    for _ in range(episodios):
        _, _ = env.reset()
        total = 0.0
        while True:
            acao = env.action_space.sample()
            _, reward, term, trunc, _ = env.step(acao)
            total += reward
            if term or trunc:
                break
        recompensas.append(total)
    env.close()
    return float(np.mean(recompensas))





if __name__ == "__main__":
    print(f"--- Iniciando Treinamento no {ENV_ID} ---")
    baseline = avaliar_aleatorio()
    print(f"Baseline (Agente Aleatório Médio): {baseline:.2f}\n")

    populacao = criar_populacao()
    historico = []

    for geracao in range(NUM_GERACOES):
        for agente in populacao:
            agente.fitness = avaliar(agente)

        valores = [agente.fitness for agente in populacao]
        melhor = max(valores)
        media = float(np.mean(valores))
        pior = min(valores)

        historico.append({
            "geracao": geracao,
            "melhor": melhor,
            "media": media,
            "pior": pior,
        })

        print(
            f"Geração {geracao:03d} | "
            f"Melhor: {melhor:.2f} | "
            f"Média: {media:.2f} | "
            f"Pior: {pior:.2f}"
        )

        if geracao < NUM_GERACOES - 1:
            populacao = nova_geracao(populacao)

    
    with open("resultados/fitness.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["geracao", "melhor", "media", "pior"])
        writer.writeheader()
        writer.writerows(historico)

    
    geracoes = [h["geracao"] for h in historico]
    melhores = [h["melhor"] for h in historico]
    medias = [h["media"] for h in historico]

    plt.figure(figsize=(10, 5))
    plt.plot(geracoes, melhores, label="Melhor Fitness", color="green", linewidth=2)
    plt.plot(geracoes, medias, label="Fitness Médio", color="blue", linestyle="--")
    plt.axhline(y=baseline, color="red", linestyle=":", label=f"Baseline Aleatório ({baseline:.1f})")
    plt.title(f"Evolução no {ENV_ID}")
    plt.xlabel("Geração")
    plt.ylabel("Fitness (Recompensa)")
    plt.legend()
    plt.grid(True)
    plt.savefig("resultados/fitness.png")
    print("\nResultados salvos em 'resultados/fitness.csv' e 'resultados/fitness.png'.")