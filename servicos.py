from datetime import date, time
from typing import List
from espacos import EspacoDesportivo


class GestorReservas:
    @staticmethod
    def verificar_sobreposicao(espaco: EspacoDesportivo, data: date, inicio: time, fim: time) -> bool:
        return False

    @staticmethod
    def processar_reservas_expiradas() -> None:
        pass


class RelatorioService:
    @staticmethod
    def total_reservas() -> int:
        return 0

    @staticmethod
    def reservas_por_espaco(espaco_id: str) -> int:
        return 0

    @staticmethod
    def taxa_ocupacao(espaco_id: str, periodo: str) -> float:
        return 0.0

    @staticmethod
    def obter_espacos_mais_utilizados() -> List[EspacoDesportivo]:
        return []