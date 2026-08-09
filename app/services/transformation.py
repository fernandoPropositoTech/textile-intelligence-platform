import pandas as pd


class DataTransformationService:

    def normalize_text_columns(
        self,
        df: pd.DataFrame,
        columns: list[str]
    ) -> pd.DataFrame:

        df = df.copy()

        for column in columns:
            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

        return df

    def convert_installation_date(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df = df.copy()

        df["installation_date"] = pd.to_datetime(
            df["installation_date"],
            errors="raise"
        )

        return df

    def convert_hourly_capacity(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        df = df.copy()

        df["hourly_capacity"] = pd.to_numeric(
            df["hourly_capacity"],
            errors="raise"
        )

        return df