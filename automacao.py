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


def cadastrar_peca():
    global total_caixas, caixa_atual
    
    print("\n>>> INICIANDO CADASTRO DE PEÇA <<<")
    id_peca = input("ID da peça: ")
    peso = float(input("Peso (g): "))
    cor = input("Cor (azul/verde): ").strip().lower()
    comprimento = float(input("Comprimento (cm): "))

    # 1. Avaliação Automática de Qualidade [cite: 10, 11, 13, 14]
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append(f"Peso fora do padrão ({peso}g)")
    if cor not in ['azul', 'verde']:
        motivos.append(f"Cor inválida ({cor})")
    if not (10 <= comprimento <= 20):
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm)")

    # 2. Processamento do Resultado 
    if not motivos:
        # Se aprovada, entra no estoque e na caixa
        peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)
        print(f"✅ Peça {id_peca} APROVADA!")

        # 3. Automação do Armazenamento (Limite de 10 peças) 
        if len(caixa_atual) == 10:
            total_caixas += 1
            caixa_atual = [] # Esvazia a caixa atual para iniciar uma nova
            print(f"📦 CAIXA FECHADA! Total de caixas: {total_caixas}")
    else:
        # Se reprovada, registra o motivo para o relatório [cite: 20]
        motivo_str = " | ".join(motivos)
        pecas_reprovadas.append({"id": id_peca, "motivo": motivo_str})
        print(f"❌ Peça REPROVADA. Motivo: {motivo_str}")


        def listar_pecas():
    """Opção 2: Mostra todas as peças processadas até o momento"""
    print("\n" + "="*20)
    print("PEÇAS APROVADAS")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada.")
    for p in pecas_aprovadas:
        print(f"ID: {p['id']} | {p['peso']}g | {p['cor']} | {p['comprimento']}cm")

    print("\nPEÇAS REPROVADAS")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada.")
    for p in pecas_reprovadas:
        print(f"ID: {p['id']} | Motivo: {p['motivo']}")
    print("="*20)

def remover_peca():
    """Opção 3: Permite excluir uma peça do sistema pelo ID"""
    id_remover = input("\nDigite o ID da peça que deseja remover: ")
    
    # Busca na lista de aprovadas
    for p in pecas_aprovadas:
        if p['id'] == id_remover:
            pecas_aprovadas.remove(p)
            if p in caixa_atual:
                caixa_atual.remove(p)
            print(f"✅ Peça {id_remover} removida com sucesso!")
            return

    # Busca na lista de reprovadas
    for p in pecas_reprovadas:
        if p['id'] == id_remover:
            pecas_reprovadas.remove(p)
            print(f"✅ Peça {id_remover} removida com sucesso!")
            return
            
    print("⚠️ ID não encontrado.")