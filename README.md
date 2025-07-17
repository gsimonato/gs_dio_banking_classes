# 💰 Sistema Bancário em Python (Terminal)

Projeto de um sistema bancário simples, feito em Python, com interface de texto via terminal. Ideal para fins didáticos ou como projeto introdutório em programação orientada a objetos.

## 📚 Funcionalidades

- Criar cliente (Pessoa Física)
- Criar conta bancária
- Depósito e saque com controle de limite
- Extrato bancário
- Listagem de contas por cliente
- Persistência automática de dados usando `pickle`
- Menu secreto `ADMIN` para depuração

## 🧱 Estrutura do Projeto

```bash
.
├── main.py                  # Arquivo principal do sistema
├── banking_classes.py       # Classes de domínio (Cliente, Conta, Transações, etc.)
├── banking_functions.py     # Funções auxiliares
├── dados.pkl                # Arquivo gerado automaticamente com os dados persistidos
```

## ▶️ Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Execute o script principal:

```bash
python main.py
```

⚠️ Certifique-se de estar usando Python 3.7 ou superior.

## 📝 Exemplo de Uso

```text
=========================================
[d]  Depósito
[s]  Saque
[e]  Extrato
[nc] Nova Conta
[lc] Listar Conta
[nu] Novo Usuário
[x]  Sair
=========================================
Digite a opção desejada: nu
CPF do cliente: 12345678900
Nome completo: João da Silva
Data de nascimento (dd/mm/yyyy): 01/01/1990
Endereço: Rua Exemplo, 123
```

## 🧪 Dados de Teste

* Os dados são salvos e carregados automaticamente via `dados.pkl`.
* Se o arquivo não existir, listas vazias serão criadas.

## 🛠️ Tecnologias

* Python 3
* Programação Orientada a Objetos
* Terminal/CLI
* Persistência com `pickle`
