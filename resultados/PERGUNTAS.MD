1. O que é o agente e qual estado ele recebe do ambiente?

O agente é o jogador. O estado que ele recebe do jogo não é a imagem da tela, e sim a memória interna do Atari, que vem empacotada em uma lista com 128 números. Esses números guardam coisas como a posição da bolinha e das raquetes naquele exato segundo.

2. Qual a diferença entre ação, recompensa e fitness?

Ação: O botão que o agente aperta no jogo naquele instante (subir, descer, ficar parado).
Recompensa: O ponto imediato que o jogo devolve a cada jogada
Fitness: A pontuação final da partida inteira.


3. Como indivíduo, população e geração aparecem no código?

Indivíduo: É um único jogador criado, com a sua própria rede neural e seus próprios pesos.

População: É a lista com todos os 20 jogadores daquela rodada.

Geração: É cada rodada completa do ciclo onde os 20 jogam

4. Como a seleção foi implementada e por que esse critério foi escolhido?

Seleção por Torneio
O código sorteia 3 indivíduos aleatórios da população e pega o que tiver a maior pontuação entre eles para ser o "pai".
Isso dá chance para os melhores passarem seus genes adiante mas sem os mesmos de sempre vencerem. 

5. O que aconteceria se não existisse elitismo?

Sem elitismo, o melhor jogador da rodada poderia sofrer uma mutação ruim ao gerar a próxima turma e perder tudo o que aprendeu.

6. Como taxa e intensidade de mutação afetam os descendentes?

Taxa de mutação: É a chance de um número do cérebro dele mudar. Se for muito alta, ele muda quase tudo e vira uma bagunça; se for muito baixa, o filho sai idêntico ao pai e não aprende nada novo.
Intensidade: Diz se o número vai mudar só um pouquinho ou sofrer uma alteração brusca.

7. Onde ocorre exploração no algoritmo?

A exploração acontece em dois momentos: no início, quando os 20 primeiros agentes nascem com números totalmente aleatórios na cabeça, e a cada geração nova, quando a função de mutação dá pequenas mexidas nos números dos filhos.

8. Os resultados indicam convergência? Qual evidência sustenta a resposta?

Não, os resultados indicam que o algoritmo ainda não convergiu.
Para convergir, a linha verde (melhor) e a linha azul (média) deveriam subir de forma contínua e se estabilizar juntas.
9. O melhor agente superou o agente aleatório? Qual evidência mostra isso?

Sim, o melhor agente superou o agente aleatório na grande maioria das gerações.
O agente aleatório tem pontuação média de -20.6 (linha vermelha pontilhada). No Pong, quanto mais perto de zero, melhor (pois -21 significa que ele perdeu de 21 a 0 sem rebater nada).

10. Qual mudança vocês fariam para tentar melhorar o resultado?

Daria para colocar crossover, fazer o filho herdar metade das características de dois pais diferentes, em vez de ser cópia de um só. 