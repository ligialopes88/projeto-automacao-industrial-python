"""
==========================================================
        PROJETO: AUTOMAÇÃO INDUSTRIAL - PYTHON
==========================================================
Desenvolvido por: Lígia Lopes
Foco: Qualidade e Gestão de Armazenamento
==========================================================
"""

# Você foi convidado por uma empresa do setor industrial para prototipar uma solução de
# automação digital que auxilie no controle de produção e qualidade das peças fabricadas
# em sua linha de montagem. Atualmente, o processo de inspeção é feito manualmente, o
# que gera atrasos, falhas de conferência e aumento no custo de operação.
# Sua missão é desenvolver em Python um sistema lógico capaz de:
# - Receber os dados de cada peça produzida (id, peso, cor e comprimento).
# - Avaliar automaticamente se a peça está aprovada ou reprovada, de acordo com
# critérios de qualidade pré-definidos:
# - Peso entre 95g e 105g
# - Cor azul ou verde
# - Comprimento entre 10cm e 20cm
# - Armazenar as peças aprovadas em caixas de capacidade limitada (10 peças por
# caixa).
# - Fechar a caixa quando atingir a capacidade máxima e iniciar uma nova.
# - Gerar relatórios consolidados com:
# - Total de peças aprovadas
# - Total de peças reprovadas e o motivo da reprovação
# - Quantidade de caixas utilizadas

# --- VARIÁVEIS DE CONTROLE ---
pecas_aprovadas = []  # Lista para armazenar dicionários das peças boas
pecas_reprovadas = [] # Lista para armazenar o ID e o motivo do erro
caixa_atual = []      # Lista temporária para as peças que estão na "esteira"
total_caixas = 0      # Contador de caixas fechadas

