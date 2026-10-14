# Neuroevolução em Jogos Atari — ALE/Pong-v5

Trabalho prático desenvolvido para a unidade curricular de **Fundamentos de Inteligência Artificial**.



---

## 1. Configurações do Experimento

* **Ambiente Utilizado:** `ALE/Pong-v5` (via Gymnasium / ALE)
* **Forma de Observação:** RAM do Atari (vetor com 128 bytes, normalizados no intervalo $[0.0, 1.0]$)
* **Espaço de Ações:** 6 ações discretas disponíveis no ambiente (`NOOP`, `FIRE`, `RIGHT`, `LEFT`, `RIGHTFIRE`, `LEFTFIRE`)
* **Arquitetura da Rede Neural:** 128 entradas $\rightarrow$ 16 neurônios ocultos (ativação $\tanh$) $\rightarrow$ 6 saídas lineares ($\text{argmax}$)
* **Tamanho da População:** 20 indivíduos por geração
* **Número de Gerações:** 30 gerações
* **Estratégia de Seleção:** Seleção por Torneio ($k = 3$)
* **Elitismo:** 2 indivíduos preservados diretamente (os melhores da geração são clonados sem mutação)
* **Taxa de Mutação Padrão:** 10% (0.10)
* **Intensidade de Mutação Padrão:** 0.20 (desvio padrão da perturbação gaussiana)

---

## 2. Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior instalado.

### Passo a Passo

1. Clone ou baixe este repositório e navegue até a pasta do projeto no terminal:
   ```bash
   cd caminho/para/o/projeto

   Instale as dependências necessárias:

Bash
pip install "gymnasium[atari]" ale-py autorom[accept-rom-license] numpy matplotlib
Baixe as ROMs oficiais do Atari:

Bash
AutoROM --accept-license
Execute o treinamento principal:

Bash
python main.py
Ao final das 30 gerações, a execução será finalizada automaticamente e os seguintes arquivos serão criados dentro do diretório resultados/:

resultados/fitness.csv: Tabela com o histórico do melhor, médio e pior fitness de cada geração.

resultados/fitness.png: Gráfico comparativo da evolução ao longo das gerações.

