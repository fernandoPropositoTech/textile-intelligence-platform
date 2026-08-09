from app.services.ingestion import DataIngestionService
from app.services.quality import DataQualityService


ingestion = DataIngestionService()
quality = DataQualityService()

df = ingestion.read_csv("data/raw/machines.csv")

required_columns = [
    "machine_code",
    "machine_name",
    "manufacturer",
    "sector",
    "installation_date",
    "status",
    "hourly_capacity"
]

quality.validate_required_columns(
    df,
    required_columns
)


quality.validate_null_values(
    df,
    required_columns
)

quality.validate_machine_code_duplicates(df)

quality.validate_status(df)

quality.validate_hourly_capacity(df)


print("Data Quality: OK")