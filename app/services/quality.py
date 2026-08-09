import pandas as pd


class DataQualityService:

    def validate_required_columns(
        self,
        df: pd.DataFrame,
        required_columns: list[str]
    ) -> None:

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Colunas obrigatórias ausentes: {missing_columns}"
            )

    def validate_null_values(
        self,
        df: pd.DataFrame,
        required_columns: list[str]
    ) -> None:

        null_columns = [
            column
            for column in required_columns
            if df[column].isnull().any()
        ]

        if null_columns:
            raise ValueError(
                f"Valores nulos encontrados: {null_columns}"
            )

    def validate_machine_code_duplicates(
        self,
        df: pd.DataFrame
    ) -> None:

        duplicates = df[
            df["machine_code"].duplicated(keep=False)
        ]

        if not duplicates.empty:
            codes = duplicates["machine_code"].unique().tolist()

            raise ValueError(
                f"machine_code duplicado: {codes}"
            )

    def validate_status(
        self,
        df: pd.DataFrame
    ) -> None:

        valid_status = {
            "Running",
            "Maintenance",
            "Stopped"
        }

        invalid_status = set(df["status"]) - valid_status

        if invalid_status:
            raise ValueError(
                f"Status inválido: {list(invalid_status)}"
            )

    def validate_hourly_capacity(
        self,
        df: pd.DataFrame
    ) -> None:

        invalid_rows = df[df["hourly_capacity"] <= 0]

        if not invalid_rows.empty:
            raise ValueError(
                "hourly_capacity deve ser maior que zero"
            )