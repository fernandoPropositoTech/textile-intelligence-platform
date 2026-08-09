from app.services.machine_pipeline import MachinePipeline


pipeline = MachinePipeline()

df = pipeline.run(
    "data/raw/machines.csv"
)

print(df)

print()
print("Pipeline executado com sucesso.")
print(f"Registros processados: {len(df)}")

print()
print(df.dtypes)