from pathlib import Path

import pandas as pd


class DataIngestionService:

    def read_csv(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {file_path}"
            )

        return pd.read_csv(path)