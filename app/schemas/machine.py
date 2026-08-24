from datetime import date

from pydantic import BaseModel, ConfigDict


class MachineResponse(BaseModel):

    id: int
    machine_code: str
    machine_name: str
    manufacturer: str
    sector: str
    installation_date: date
    status: str
    hourly_capacity: int

    model_config = ConfigDict(
        from_attributes=True
    )