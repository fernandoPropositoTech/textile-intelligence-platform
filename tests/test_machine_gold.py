import pandas as pd

from app.services.gold.machine_gold import MachineGoldService


def test_create_sector_summary():

    # 1. Dados de entrada simulando a Silver
    df = pd.DataFrame({
        "machine_code": ["SHM-001", "SHM-002", "STL-001"],
        "sector": ["Knitting", "Knitting", "Seamless"],
        "status": ["Running", "Maintenance", "Running"],
        "hourly_capacity": [120, 80, 150]
    })

    # 2. Executa a transformação Gold
    service = MachineGoldService()
    gold_df = service.create_sector_summary(df)

    # 3. Verifica os indicadores do setor Knitting
    knitting = gold_df.set_index("sector").loc["Knitting"]

    assert knitting["total_machines"] == 2
    assert knitting["running_machines"] == 1
    assert knitting["maintenance_machines"] == 1
    assert knitting["stopped_machines"] == 0
    assert knitting["total_hourly_capacity"] == 200
    assert knitting["avg_hourly_capacity"] == 100


def test_stopped_machines():

    df = pd.DataFrame({
        "machine_code": ["LON-001", "LON-002"],
        "sector": ["Socks", "Socks"],
        "status": ["Stopped", "Running"],
        "hourly_capacity": [140, 160]
    })

    service = MachineGoldService()
    gold_df = service.create_sector_summary(df)

    socks = gold_df.set_index("sector").loc["Socks"]

    assert socks["total_machines"] == 2
    assert socks["running_machines"] == 1
    assert socks["stopped_machines"] == 1
    assert socks["total_hourly_capacity"] == 300
    assert socks["avg_hourly_capacity"] == 150    