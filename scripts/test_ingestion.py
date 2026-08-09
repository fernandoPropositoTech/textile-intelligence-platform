from app.services.ingestion import DataIngestionService


service = DataIngestionService()

df = service.read_csv("data/raw/machines.csv")

print(df)
print()
print(f"Registros: {len(df)}")
print(f"Colunas: {list(df.columns)}")