# --- VARIÁVEIS DE CONTROLE ---
pecas_aprovadas = []
pecas_reprovadas = []
caixa_atual = []
total_caixas = 0

def cadastrar_peca():
    global total_caixas, caixa_atual
    print("\n>>> CADASTRANDO PEÇA <<<")
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
            pecas_aprovadas.append(id_peca)
            caixa_atual.append(id_peca)
            print(f"✅ Peça {id_peca} APROVADA!")
            
            # --- LOGÍSTICA: FECHAMENTO DE CAIXA EM 10 UNIDADES ---
            if len(caixa_atual) == 10:
                total_caixas += 1
                caixa_atual = []
                print(f"\n📦 [ALERTA] CAIXA FECHADA! Total: {total_caixas}")
        else:
            pecas_reprovadas.append({"id": id_peca, "motivo": ", ".join(motivos)})
            print(f"❌ REPROVADA: {motivos}")
    except:
        print("⚠️ Use apenas números.")

def listar_pecas():
    print(f"\nAprovadas: {pecas_aprovadas}")
    print(f"Reprovadas: {pecas_reprovadas}")

def mostrar_status_caixas():
    print(f"\nCaixas Prontas: {total_caixas}")
    print(f"Peças na caixa atual: {len(caixa_atual)}/10")

def gerar_relatorio_final():
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Aprovadas: {len(pecas_aprovadas)} | Reprovadas: {len(pecas_reprovadas)} | Caixas: {total_caixas}")

def main():
    while True:
        print("\n1. Cadastrar | 2. Listar | 4. Status Caixas | 5. Sair")
        op = input("Opção: ")
        if op == '1': cadastrar_peca()
        elif op == '2': listar_pecas()
        elif op == '4': mostrar_status_caixas()
        elif op == '5':
            gerar_relatorio_final()
            break

if __name__ == "__main__":
    main()