from abc import ABC
from datetime import date, time
from enums import PerfilUtilizador


class Utilizador(ABC):
    def __init__(self, id_utilizador: str, nome: str, email: str, password: str, perfil: PerfilUtilizador):
        self._id = id_utilizador
        self._nome = nome
        self._email = email
        self._password = password
        self._perfil = perfil

    def autenticar(self, password: str) -> bool:
        return self._password == password

    def get_perfil(self) -> PerfilUtilizador:
        return self._perfil


class UtilizadorNormal(Utilizador):
    def __init__(self, id_utilizador: str, nome: str, email: str, password: str):
        super().__init__(id_utilizador, nome, email, password, PerfilUtilizador.NORMAL)

    def criar_reserva(self, espaco, data: date, hora_inicio: time, hora_fim: time):
        pass

    def cancelar_reserva(self, reserva) -> bool:
        pass


class Administrador(Utilizador):
    def __init__(self, id_utilizador: str, nome: str, email: str, password: str):
        super().__init__(id_utilizador, nome, email, password, PerfilUtilizador.ADMINISTRADOR)

    def aprovar_reserva(self, reserva) -> None:
        reserva.confirmar()

    def gerir_espaco(self, espaco) -> None:
        pass

    def gerar_relatorios(self) -> None:
        pass