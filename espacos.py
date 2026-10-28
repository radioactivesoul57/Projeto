from abc import ABC
from typing import List
from enums import EstadoEspaco
from equipamentos import Equipamento


class EspacoDesportivo(ABC):
    def __init__(self, id_espaco: str, nome: str, tipo_espaco: str, localizacao: str, capacidade: int):
        self._id = id_espaco
        self._nome = nome
        self._tipo_espaco = tipo_espaco
        self._localizacao = localizacao
        self._capacidade_maxima = capacidade
        self._estado = EstadoEspaco.DISPONIVEL
        self._equipamentos: List[Equipamento] = []

    def is_disponivel(self) -> bool:
        return self._estado == EstadoEspaco.DISPONIVEL

    def alterar_estado(self, novo_estado: EstadoEspaco) -> None:
        self._estado = novo_estado


class CampoFutebol(EspacoDesportivo):
    def __init__(self, id_espaco: str, nome: str, localizacao: str, capacidade: int, tipo_piso: str):
        super().__init__(id_espaco, nome, "Campo de Futebol", localizacao, capacidade)
        self._tipo_piso = tipo_piso


class CourtTenis(EspacoDesportivo):
    def __init__(self, id_espaco: str, nome: str, localizacao: str, capacidade: int, superficie: str):
        super().__init__(id_espaco, nome, "Court de Ténis", localizacao, capacidade)
        self._superficie = superficie


class Pavilhao(EspacoDesportivo):
    def __init__(self, id_espaco: str, nome: str, localizacao: str, capacidade: int, tem_bancada: bool):
        super().__init__(id_espaco, nome, "Pavilhão", localizacao, capacidade)
        self._tem_bancada = tem_bancada


class SalaFitness(EspacoDesportivo):
    def __init__(self, id_espaco: str, nome: str, localizacao: str, capacidade: int, tem_espelhos: bool):
        super().__init__(id_espaco, nome, "Sala de Fitness", localizacao, capacidade)
        self._tem_espelhos = tem_espelhos