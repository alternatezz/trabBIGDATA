import pandas as pd
from faker import Faker
import random
from sqlalchemy import create_engine

# Configurações do banco MySQL
usuario = 'root'
senha = '1234'
host = 'localhost'
porta = '3306'
banco = 'psicologia'

# Conexão com o banco MySQL
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}")

# Inicializa Faker
fake = Faker('pt_BR')

# Gera 30 pacientes fictícios
def gerar_clientes(n=30):
    dados = []
    for _ in range(n):
        nome = fake.name()
        idade = random.randint(12, 70)
        sexo = random.choice(['Masculino', 'Feminino', 'Outro'])

        # Define o grau de atendimento
        if idade < 18 or idade > 60:
            grau = 3  # Alta prioridade
        elif 18 <= idade <= 30:
            grau = 2  # Média
        else:
            grau = 1  # Baixa

        dados.append({
            'Nome': nome,
            'Idade': idade,
            'Sexo': sexo,
            'Grau_Atendimento': grau
        })
    return pd.DataFrame(dados)

# Cria DataFrame e exporta
df = gerar_clientes()
df.to_csv('clientes_para_powerbi.csv', index=False)
print("✅ Arquivo CSV gerado!")

# Insere no banco MySQL
df.to_sql('clientes', con=engine, if_exists='replace', index=False)
print("✅ Dados inseridos no MySQL!")