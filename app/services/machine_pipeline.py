import pandas as pd

from app.services.ingestion import DataIngestionService
from app.services.quality import DataQualityService
from app.services.transformation import DataTransformationService
from app.services.machine_repository import MachineRepository
from app.services.lake_storage import LakeStorageService
from app.services.gold.machine_gold import MachineGoldService


class MachinePipeline:

    def __init__(self):
        self.ingestion = DataIngestionService()
        self.quality = DataQualityService()
        self.transformation = DataTransformationService()
        self.repository = MachineRepository()
        self.lake_storage = LakeStorageService()
        self.gold = MachineGoldService()

    def run(self, file_path: str) -> pd.DataFrame:

        # 1. Ingestion
        df = self.ingestion.read_csv(file_path)

        required_columns = [
            "machine_code",
            "machine_name",
            "manufacturer",
            "sector",
            "installation_date",
            "status",
            "hourly_capacity"
        ]

        # 2. Data Quality
        self.quality.validate_required_columns(
            df,
            required_columns
        )

        self.quality.validate_null_values(
            df,
            required_columns
        )

        self.quality.validate_machine_code_duplicates(df)
        self.quality.validate_status(df)
        self.quality.validate_hourly_capacity(df)

        # 3. Transformation
        text_columns = [
            "machine_code",
            "machine_name",
            "manufacturer",
            "sector",
            "status"
        ]

        df = self.transformation.normalize_text_columns(
            df,
            text_columns
        )

        df = self.transformation.convert_installation_date(df)

        df = self.transformation.convert_hourly_capacity(df)

        # 4. Silver Layer
        silver_path = self.lake_storage.save_silver(
            df,
            "machines.csv"
        )

        print(f"Silver salva em: {silver_path}")

        # 5. Load / Persistence
        result = self.repository.save_dataframe(df)

        print(
            f"Registros inseridos: {result['inserted']}"
        )

        print(
            f"Registros atualizados: {result['updated']}"
        )

        # 6. Gold Layer
        gold_df = self.gold.create_sector_summary(df)

        gold_path = self.lake_storage.save_gold(
            gold_df,
            "machine_sector_summary.csv"
        )

        print(f"Gold salva em: {gold_path}")

        return df