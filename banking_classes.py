from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime



AGENCIA = '0001'

#-------------------------------------------------------------------------------------------------------

class PessoaFisica:
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime ):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return ", ".join(f"{k}:{v}" for k, v in self.__dict__.items())

#-------------------------------------------------------------------------------------------------------

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: datetime, endereco: str):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


    def __str__(self):
        return ", ".join(f"{k}:{v}" for k, v in self.__dict__.items())

#-------------------------------------------------------------------------------------------------------

class Conta:
    def __init__(self, numero:int, cliente:Cliente ):
        self._saldo = 0
        self._numero = numero
        self._agencia = AGENCIA
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        if valor <= 0:
            input("""
    =========================================
        VALOR INVÁLIDO - TENTE NOVAMENTE
    =========================================""")
            return False
        elif self.saldo < valor:
            input("""
    =========================================
        SALDO INSUFICIENTE PARA O SAQUE
    =========================================""")
            return False
        elif self._saldo >= valor:
            self._saldo -= valor
            input("""
    =========================================
        SAQUE REALIZADO COM SUCESSO
    =========================================""")
        return True
    
    def depositar(self, valor):
        status = False
        if valor <= 0:
            input("""
    =========================================
        VALOR INVÁLIDO - TENTE NOVAMENTE
    =========================================""")
            return False
        else:
            self._saldo += valor
            input("""
    =========================================
        DEPÓSITO REALIZADO COM SUCESSO
    =========================================""")
        return True

#-------------------------------------------------------------------------------------------------------

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        saques_realizados = Historico.qtd_saques
        if saques_realizados >= self.limite_saques:
            input("""
    =========================================
        OPERAÇÃO DE SAQUE INDISPONÍVEL
        NUMERO DE SAQUES EXCEDIDO.
    =========================================""")
            return False
        elif valor > self.limite:
            input("""
    =========================================
        OPERAÇÃO DE SAQUE INDISPONÍVEL
            VALOR ACIMA DO LIMITE
    =========================================""")
            return False
        else:
            super().sacar(valor)

    def __str__(self):
        return f"""
                Agência: {self.agencia}
                C/C:     {self.numero}
                Titular: {self.cliente.nome}"""

#-------------------------------------------------------------------------------------------------------

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    @property
    def qtde_saques(self):
        saques = [ transacao for i,transacao in self.transacoes if transacao['tipo']=='Saque' ]
        return len(saques)

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor
            }
        )


#-------------------------------------------------------------------------------------------------------

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

#-------------------------------------------------------------------------------------------------------

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

#-------------------------------------------------------------------------------------------------------

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

