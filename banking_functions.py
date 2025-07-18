from banking_classes import Cliente, Conta, Deposito, Saque, Historico, ContaCorrente, Transacao

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

MENU = """=========================================
[d]  Depósito
[s]  Saque
[e]  Extrato
[nc] Nova Conta
[lc] Listar Conta
[nu] Novo Usuário
[x]  Sair
=========================================
"""

def menu( interface = False):
    if not interface:
        return input(f"{MENU}      Digite a opção desejada: ")
    else:
        print(MENU)
        return False

def pause():
    input(f"\n\n**** Aperte ENTER para a próxima operação ****")

def seleciona_cliente( cpf , clientes):
    cliente = [ cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None

def seleciona_conta( cliente ):
    if not cliente.contas:
        print("*** Cliente não possui conta cadastrada ***")
        return
    else:
        available = [ conta.numero for conta in cliente.contas ]
        print(available)
        qtd = len(available)
        if qtd == 0:
            input("*** Cliente não possui conta cadastrada ***")
            return
        elif qtd == 1:
            conta = next(c for c in cliente.contas)
        else:
            while True:
                clear_screen()
                menu(interface=True)
                listar_contas( [] , cliente_selecionado=cliente)
                escolha = input("Digite o número da conta ou 'c' para cancelar: ").strip()
                if escolha.lower() == 'c':
                    print("Operação cancelada.")
                    break
                try:
                    numero = int(escolha)
                    if numero in available:
                        conta = next(c for c in cliente.contas if c.numero == numero)
                        break
                    else:
                        input("*** Conta inválida. Tente novamente. ***")
                except ValueError:
                    input("*** Entrada inválida. Digite um número. ***")

        if conta:
            clear_screen()
            menu(interface=True)
            input(f"*** Conta selecionada: {conta.numero} ***")
            return conta
        else:
            return

def depositar( clientes ):
    cpf = input("CPF do cliente:")
    cliente = seleciona_cliente( cpf, clientes)
    if not cliente:
        input('*** Cliente não encontrado no sistema ***')
        return
    conta = seleciona_conta(cliente)
    if not conta:
        return
    while True:
        entrada = input("Valor a ser depositado (ou 'c' para cancelar): R$").strip()
        if entrada.lower() == 'c':
            valor = None
            break
        try:
            valor = float(entrada.replace(',', '.'))
            break
        except ValueError:
            print("Valor inválido. Tente novamente.")
    transacao = Deposito(valor)
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("CPF do cliente:")
    cliente = seleciona_cliente( cpf, clientes)
    if not cliente:
        input('*** Cliente não encontrado no sistema ***')
        return
    conta = seleciona_conta(cliente)
    if not conta:
        return
    while True:
        entrada = input("Valor a ser sacado (ou 'c' para cancelar): R$").strip()
        if entrada.lower() == 'c':
            valor = None
            break
        try:
            valor = float(entrada.replace(',', '.'))
            break
        except ValueError:
            print("Valor inválido. Tente novamente.")
    transacao = Saque(valor)
    cliente.realizar_transacao(conta, transacao)

def extrato(clientes):
    cpf = input("CPF do cliente:")
    cliente = seleciona_cliente( cpf, clientes)
    if not cliente:
        input('*** Cliente não encontrado no sistema ***')
        return
    conta = seleciona_conta(cliente)
    if not conta:
        return
    historico = conta.historico.transacoes
    print("\n------------ Extrato ------------")
    if not historico:
        input('*** Sem registro de movimentações ***')
    else:
        extr = ''
        for transacao in historico:
            extr += f'--- {transacao["tipo"]}\tR${transacao["valor"]:.2f}\n'
        extr += f'==== Saldo da conta: R${conta.saldo:.2f} ===='
        print(extr)
        input("\n---------------------------------")

def criar_conta(nova_conta, clientes, contas):
    cpf = input("CPF do cliente:")
    cliente = seleciona_cliente( cpf, clientes)
    if not cliente:
        input('*** Cliente não encontrado no sistema ***')
        return
    cliente.adicionar_conta(Conta(nova_conta, cliente))
    contas.append(nova_conta)
    input(f'*** Conta {nova_conta} criada com sucesso ***')
 

def listar_contas(clientes, cliente_selecionado=False):
    if not cliente_selecionado:
        cpf = input("CPF do cliente:")
        cliente = seleciona_cliente( cpf, clientes)
    else:
        cliente = cliente_selecionado
    if not cliente:
        input('*** Cliente não encontrado no sistema ***')
        return
    if len(cliente.contas) == 0:
        input("*** Cliente não possui conta cadastrada ***")
        return
    else:
        clear_screen()
        menu(interface=True)
        print(f"Contas disponíveis:")
        available = [ conta.numero for conta in cliente.contas ]
        for conta in available:
            print(f"Conta: {conta}")
        if not cliente_selecionado:
            pause()
    return

def cria_usuario(clientes):
    cpf = input("CPF do cliente:")
    cliente = seleciona_cliente( cpf, clientes)
    if cliente:
        input('*** Cliente já cadastrado ***')
    else:
        nome = input("Nome completo:")
        nascimento = input("Data de nascimento (dd/mm/yyyy):")
        endereco = input("Endereço:")
        clientes.append( Cliente( cpf, nome, nascimento, endereco) )
        input(f"*** Cliente cadastrado no sistema [{nome} | {cpf}]")

def admin_admin(clientes):
    for cliente in clientes:
        print(f'--CPF:  {cliente.cpf}')
        for conta in cliente.contas:
            print(f'  |___ Conta: {conta.numero}')
            print(f'          |___Saldo:R${conta.saldo:.2f}')
            transacoes = conta.historico.transacoes
            depositos = [ t['valor'] for t in transacoes if t['tipo'] == 'Deposito' ]
            saques = [ t['valor'] for t in transacoes if t['tipo'] == 'Saque' ]
            if len(depositos) > 0:
                print(f'                |___Depositos')
                for d in depositos:
                    print(f'                    |___R${d:.2f}')
            if len(saques) > 0:
                print(f'                |___Saques')
                for s in saques:
                    print(f'                    |___{s:.2f}')


    pause()