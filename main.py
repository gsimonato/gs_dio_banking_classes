from banking_classes import *
from banking_functions import menu, clear_screen
from banking_functions import depositar, sacar, extrato, criar_conta, listar_contas, cria_usuario

if __name__ == "__main__":
    # ==================    PICKLE PERSISTANCE  ==========================
    import pickle
    try:
        with open("dados.pkl", "rb") as f:
            data = pickle.load(f)
            contas = data["contas"]
            clientes = data["clientes"]
    except:
        contas = []
        clientes = []
    # ====================================================================

    while True:
        clear_screen()
        VALID = [ 'd', 's', 'e', 'nc', 'lc', 'nu', 'x' , 'ADMIN']
        option = menu()
        if option not in VALID:
            input('*** Opção inválida ***')
            continue

        if option == 'd':
            depositar(clientes)
        elif option == 's':
            sacar(clientes)
        
        elif option == 'e':
            extrato(clientes)
        
        elif option == 'nc':
            nova_conta = len(contas) + 1
            criar_conta(nova_conta, clientes, contas)
        
        elif option == 'lc':
            listar_contas(clientes)
        
        elif option == 'nu':
            cria_usuario(clientes)

        elif option == 'x':
            input('Obrigado por utilizar o banco xxxxxxx')
            clear_screen()
            break

        elif option == 'ADMIN':
            """
                menu para visualização dos dados de clientes, contas
                e saldos em árvore simples
            """
            from banking_functions import admin_admin
            print(f'CONTAS> {contas}')
            print(f'CLIENTES> {[ cl.nome for cl in clientes]}')
            admin_admin(clientes)


    # ====================================================================
    with open("dados.pkl", "wb") as f:
        pickle.dump({"contas": contas, "clientes": clientes}, f)
    # ====================================================================