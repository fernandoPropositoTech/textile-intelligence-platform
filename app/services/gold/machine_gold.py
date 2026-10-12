import pandas as pd


class MachineGoldService:

    def create_sector_summary(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        gold_df = (
            df.groupby("sector")
            .agg(
                total_machines=("machine_code", "count"),
                running_machines=("status", lambda x: (x == "Running").sum()),
                maintenance_machines=("status", lambda x: (x == "Maintenance").sum()),
                stopped_machines=("status", lambda x: (x == "Stopped").sum()),
                total_hourly_capacity=("hourly_capacity", "sum"),
                avg_hourly_capacity=("hourly_capacity", "mean"),
            )
            .reset_index()
        )

        return gold_df