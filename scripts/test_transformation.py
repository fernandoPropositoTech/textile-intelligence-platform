from app.services.ingestion import DataIngestionService
from app.services.transformation import DataTransformationService


ingestion = DataIngestionService()
transformation = DataTransformationService()

df = ingestion.read_csv("data/raw/machines.csv")

text_columns = [
    "machine_code",
    "machine_name",
    "manufacturer",
    "sector",
    "status"
]

df = transformation.normalize_text_columns(
    df,
    text_columns
)

df = transformation.convert_installation_date(df)

df = transformation.convert_hourly_capacity(df)

print(df)

print()
print(df.dtypes)