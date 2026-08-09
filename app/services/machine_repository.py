import pandas as pd

from app.database.session import SessionLocal
from app.models.machine import Machine


class MachineRepository:

    def save_dataframe(
        self,
        df: pd.DataFrame
    ) -> dict:

        session = SessionLocal()

        inserted = 0
        updated = 0

        try:
            for _, row in df.iterrows():

                machine = (
                    session.query(Machine)
                    .filter(
                        Machine.machine_code
                        == row["machine_code"]
                    )
                    .first()
                )

                if machine:
                    machine.machine_name = row["machine_name"]
                    machine.manufacturer = row["manufacturer"]
                    machine.sector = row["sector"]
                    machine.installation_date = (
                        row["installation_date"].date()
                    )
                    machine.status = row["status"]
                    machine.hourly_capacity = int(
                        row["hourly_capacity"]
                    )

                    updated += 1

                else:
                    machine = Machine(
                        machine_code=row["machine_code"],
                        machine_name=row["machine_name"],
                        manufacturer=row["manufacturer"],
                        sector=row["sector"],
                        installation_date=(
                            row["installation_date"].date()
                        ),
                        status=row["status"],
                        hourly_capacity=int(
                            row["hourly_capacity"]
                        )
                    )

                    session.add(machine)

                    inserted += 1

            session.commit()

            return {
                "inserted": inserted,
                "updated": updated
            }

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()