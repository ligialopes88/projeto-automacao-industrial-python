def mostrar_status_caixas():
    """Opção 4: Mostra a situação logística atual"""
    # IMPORTANTE: Estas linhas precisam de 1 TAB de distância da margem
    print(f"\n📦 Caixas prontas: {total_caixas}")
    print(f"📦 Peças na caixa atual: {len(caixa_atual)}/3") # Mudei para 3 para testar rápido!

def gerar_relatorio_final():
    """Opção 5: Exibe o balanço final"""
    print("\n" + "█"*40)
    print("       RELATÓRIO FINAL")
    print("█"*40)
    print(f"APROVADAS: {len(pecas_aprovadas)} | REPROVADAS: {len(pecas_reprovadas)}")
    print(f"CAIXAS: {total_caixas}")
    print("█"*40)

def main():
    while True:
        print("\n1. Novo | 2. Listar | 3. Remover | 4. Status Caixas | 5. Sair")
        opcao = input("Selecione: ")

        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            mostrar_status_caixas() # Verifique se esta linha está alinhada com as outras
        elif opcao == '5':
            gerar_relatorio_final()
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()