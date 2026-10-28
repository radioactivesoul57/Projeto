from datetime import date, time
from enums import EstadoReserva
from utilizadores import Utilizador
from espacos import EspacoDesportivo


class Reserva:
    def __init__(self, id_reserva: str, utilizador: Utilizador, espaco: EspacoDesportivo, data: date, hora_inicio: time, hora_fim: time):
        self._id = id_reserva
        self._utilizador = utilizador
        self._espaco = espaco
        self._data = data
        self._hora_inicio = hora_inicio
        self._hora_fim = hora_fim
        self._estado = EstadoReserva.PENDENTE

    def confirmar(self) -> None:
        self._estado = EstadoReserva.CONFIRMADA

    def cancelar(self) -> None:
        self._estado = EstadoReserva.CANCELADA

    def concluir(self) -> None:
        self._estado = EstadoReserva.CONCLUIDA

    def expirar(self) -> None:
        self._estado = EstadoReserva.EXPIRADA