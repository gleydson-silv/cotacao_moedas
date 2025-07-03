from services.cotacao_service import buscar_cotacoes, salvar_cotacoes

def menu():
    while True:
        print("\n=== COTAÇÃO DE MOEDAS ===")
        print("1 - Buscar e salvar cotações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dados = buscar_cotacoes()
            salvar_cotacoes(dados)
            print("Cotações salvas com sucesso.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
