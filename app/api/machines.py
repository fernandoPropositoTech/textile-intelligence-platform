from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.machine import Machine
from app.schemas.machine import MachineResponse


router = APIRouter(
    prefix="/machines",
    tags=["Machines"]
)


@router.get(
    "/",
    response_model=list[MachineResponse]
)
def list_machines(
    db: Session = Depends(get_db)
):
    machines = db.query(Machine).all()

    return machines