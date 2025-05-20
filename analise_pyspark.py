from pyspark.sql import SparkSession

# Inicializa Spark
spark = SparkSession.builder \
    .appName("AnaliseClientesPsicologa") \
    .getOrCreate()

# Lê CSV gerado
df = spark.read.csv("clientes_para_powerbi.csv", header=True, inferSchema=True)

# Mostra dados
df.show()

# Agrupamento por grau de atendimento
df.groupBy("Grau_Atendimento").count().show()

# Salvar versão transformada (opcional)
df.write.csv("clientes_agrupado_spark.csv", header=True, mode="overwrite")
print("✅ Exportado clientes_agrupado_spark.csv")