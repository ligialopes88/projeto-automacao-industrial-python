"""
# ==========================================================
#        PROJETO: AUTOMAÇÃO INDUSTRIAL - PYTHON
# ==========================================================
# Desenvolvido por: Lígia Lopes
# Foco: Qualidade e Gestão de Armazenamento
# ==========================================================
"""

# --- VARIÁVEIS DE CONTROLO ---
# Listas para armazenar os dados durante a execução
pecas_aprovadas = []  # Armazena dicionários das peças que passaram na qualidade
pecas_reprovadas = [] # Armazena o ID e o motivo da reprovação
caixa_atual = []      # Controla as peças que estão a entrar na caixa agora
total_caixas = 0      # Contador de caixas enviadas para o armazém

def cadastrar_peca():
    """Opção 1: Recebe dados, valida a qualidade e gere o armazenamento"""
    global total_caixas, caixa_atual
    
    print("\n>>> INICIANDO CADASTRO DE PEÇA <<<")
    try:
        id_peca = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor (azul/verde): ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))

        # 1. Avaliação Automática de Qualidade
        motivos = []
        if not (95 <= peso <= 105):
            motivos.append(f"Peso fora do padrão ({peso}g)")
        if cor not in ['azul', 'verde']:
            motivos.append(f"Cor inválida ({cor})")
        if not (10 <= comprimento <= 20):
            motivos.append(f"Comprimento fora do padrão ({comprimento}cm)")

        # 2. Processamento do Resultado
        if not motivos:
            # Se aprovada, entra no sistema e na caixa logística
            peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
            pecas_aprovadas.append(peca)
            caixa_atual.append(peca)
            print(f"✅ Peça {id_peca} APROVADA!")

            # 3. Automação do Armazenamento (Máximo 10 peças por caixa)
            if len(caixa_atual) == 10:
                total_caixas += 1
                caixa_atual = [] # Reinicia a contagem para a próxima caixa
                print(f"📦 CAIXA FECHADA! Total de caixas prontas: {total_caixas}")
        else:
            # Se reprovada, regista o erro para o relatório industrial
            motivo_str = " | ".join(motivos)
            pecas_reprovadas.append({"id": id_peca, "motivo": motivo_str})
            print(f"❌ Peça REPROVADA. Motivo: {motivo_str}")
            
    except ValueError:
        print("⚠️ Erro: Insira valores numéricos válidos para peso e comprimento.")

def listar_pecas():
    """Opção 2: Lista o estado atual de toda a produção"""
    print("\n" + "="*30)
    print("      ESTADO DA PRODUÇÃO")
    print("="*30)
    
    print("\n[PEÇAS APROVADAS]")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada em stock.")
    for p in pecas_aprovadas:
        print(f"ID: {p['id']} | {p['peso']}g | Cor: {p['cor']} | {p['comprimento']}cm")

    print("\n[PEÇAS REPROVADAS]")
    if not pecas_reprovadas:
        print("Nenhuma falha de qualidade registada.")
    for p in pecas_reprovadas:
        print(f"ID: {p['id']} | Falha: {p['motivo']}")
    print("="*30)

def remover_peca():
    """Opção 3: Permite remover um registo incorreto pelo ID"""
    id_remover = input("\nDigite o ID da peça que deseja remover: ")
    
    # Procura na lista de aprovadas
    for p in pecas_aprovadas:
        if p['id'] == id_remover:
            pecas_aprovadas.remove(p)
            if p in caixa_atual:
                caixa_atual.remove(p)
            print(f"✅ Registo da peça {id_remover} removido.")
            return

    # Procura na lista de reprovadas
    for p in pecas_reprovadas:
        if p['id'] == id_remover:
            pecas_reprovadas.remove(p)
            print(f"✅ Registo da peça {id_remover} removido.")
            return
            
    # Se chegar aqui, o ID não existe (Esta linha deve estar indentada!)
    print("⚠️ ID não encontrado no sistema.")

def mostrar_status_caixas():
    """Opção 4: Mostra a situação logística atual das caixas"""
    print(f"\n📦 Caixas prontas para expedição: {total_caixas}")
    print(f"📦 Peças na esteira/caixa atual: {len(caixa_atual)}/10")

def gerar_relatorio_final():
    """Opção 5: Exibe o balanço final antes do encerramento"""
    print("\n" + "█"*40)
    print("       RELATÓRIO FINAL DE EFICIÊNCIA")
    print("█"*40)
    print(f"TOTAL DE PEÇAS APROVADAS:   {len(pecas_aprovadas)}")
    print(f"TOTAL DE PEÇAS REPROVADAS:  {len(pecas_reprovadas)}")
    print(f"TOTAL DE CAIXAS UTILIZADAS: {total_caixas}")
    
    if pecas_reprovadas:
        print("\nDETALHE DAS REPROVAÇÕES:")
        for r in pecas_reprovadas:
            print(f"- Peça {r['id']}: {r['motivo']}")
    print("█"*40)

def main():
    """Ciclo principal do programa com menu interativo"""
    while True:
        print("\n" + "═"*35)
        print("   GESTÃO DE QUALIDADE INDUSTRIAL")
        print("═"*35)
        print("1. Registar nova peça")
        print("2. Listar produção completa")
        print("3. Remover peça por ID")
        print("4. Verificar status das caixas")
        print("5. Gerar relatório e Encerrar")
        
        opcao = input("\nSelecione uma operação (1-5): ")

        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            mostrar_status_caixas()
        elif opcao == '5':
            gerar_relatorio_final()
            print("\nSistema encerrado com sucesso. Bom trabalho!")
            break
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()