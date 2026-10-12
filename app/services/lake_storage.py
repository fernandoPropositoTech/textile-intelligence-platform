from pathlib import Path

import pandas as pd


class LakeStorageService:

    def save_silver(
        self,
        df: pd.DataFrame,
        file_name: str
    ) -> Path:

        silver_path = Path("data/lake/silver")
        silver_path.mkdir(parents=True, exist_ok=True)

        output_path = silver_path / file_name

        df.to_csv(
            output_path,
            index=False
        )

        return output_path

    def save_gold(
        self,
        df: pd.DataFrame,
        file_name: str
    ) -> Path:

        gold_path = Path("data/lake/gold")
        gold_path.mkdir(parents=True, exist_ok=True)

        output_path = gold_path / file_name

        df.to_csv(
            output_path,
            index=False
        )

        return output_path