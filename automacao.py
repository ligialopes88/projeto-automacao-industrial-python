"""
==========================================================
       PROJETO: AUTOMAÇÃO INDUSTRIAL - PYTHON
==========================================================
Desenvolvido por: Lígia Lopes
Instituição: UniFECAF
Foco: Gestão de Qualidade e Logística Industrial 4.0

DESAFIO:
Prototipar uma solução de automação digital para controle 
de produção e qualidade de peças, substituindo a inspeção 
manual. O sistema deve:
- Validar peso (95g-105g), cor (azul/verde) e comprimento (10-20cm).
- Gerenciar o armazenamento automático em caixas de 10 unidades.
- Permitir a rastreabilidade e remoção de registros.
- Gerar relatórios de eficiência produtiva.

==========================================================
"""

# --- VARIÁVEIS DE CONTROLE ---
pecas_aprovadas = []
pecas_reprovadas = []
caixa_atual = []
total_caixas = 0

# --- FUNÇÕES DO SISTEMA ---

def cadastrar_peca():
    global total_caixas, caixa_atual
    print("\n>>> NOVO CADASTRO <<<")
    try:
        id_peca = input("ID: ")
        peso = float(input("Peso (95-105g): "))
        cor = input("Cor (azul/verde): ").strip().lower()
        comprimento = float(input("Comprimento (10-20cm): "))

        motivos = []
        if not (95 <= peso <= 105): motivos.append("Peso")
        if cor not in ['azul', 'verde']: motivos.append("Cor")
        if not (10 <= comprimento <= 20): motivos.append("Comprimento")

        if not motivos:
            # Criamos um dicionário para a peça ser um objeto único
            peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
            pecas_aprovadas.append(peca)
            caixa_atual.append(peca)
            print(f"✅ Peça {id_peca} APROVADA!")
            
            if len(caixa_atual) == 10:
                total_caixas += 1
                caixa_atual = []
                print(f"📦 CAIXA FECHADA! Total: {total_caixas}")
        else:
            pecas_reprovadas.append({"id": id_peca, "motivo": ", ".join(motivos)})
            print(f"❌ REPROVADA: {motivos}")
    except ValueError:
        print("⚠️ Erro: Use apenas números para peso e comprimento.")

def listar_pecas():
    print("\n--- LISTA DE PRODUÇÃO ---")
    print(f"Aprovadas: {pecas_aprovadas}")
    print(f"Reprovadas: {pecas_reprovadas}")

def mostrar_status_caixas():
    print(f"\nCaixas Prontas: {total_caixas}")
    print(f"Peças na caixa atual: {len(caixa_atual)}/10")

def remover_peca():
    """Remove apenas UMA unidade específica do ID informado"""
    id_rem = input("\nDigite o ID exato para remover: ")
    removido = False
    
    # Busca e remove das aprovadas
    for p in pecas_aprovadas:
        if p['id'] == id_rem:
            pecas_aprovadas.remove(p)
            removido = True
            # Se a peça estiver na caixa atual, remove de lá também
            for p_caixa in caixa_atual:
                if p_caixa['id'] == id_rem:
                    caixa_atual.remove(p_caixa)
                    break 
            break # O break garante que remova apenas UMA peça
            
    # Se não estava em aprovadas, busca em reprovadas
    if not removido:
        for p in pecas_reprovadas:
            if p['id'] == id_rem:
                pecas_reprovadas.remove(p)
                removido = True
                break
            
    if removido:
        print(f"✅ Uma unidade do ID {id_rem} foi removida.")
    else:
        print("⚠️ ID não encontrado.")

def gerar_relatorio_final():
    print("\n" + "="*30)
    print("       RELATÓRIO FINAL")
    print("="*30)
    print(f"Aprovadas:  {len(pecas_aprovadas)}")
    print(f"Reprovadas: {len(pecas_reprovadas)}")
    print(f"Caixas:     {total_caixas}")
    print("="*30)

# --- MENU PRINCIPAL ---

def main():
    while True:
        print("\n1. Cadastrar | 2. Listar | 4. Status Caixas | 5. Remover | 6. Sair")
        op = input("Opção: ")

        if op == '1':
            cadastrar_peca()
        elif op == '2':
            listar_pecas()
        elif op == '4':
            mostrar_status_caixas()
        elif op == '5':
            remover_peca()
        elif op == '6':
            gerar_relatorio_final()
            print("Sistema encerrado. Bom trabalho!")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    main()