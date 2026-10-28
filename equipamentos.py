from enums import EstadoEquipamento


class Equipamento:
    def __init__(self, id_equipamento: str, nome: str, quantidade: int, estado: EstadoEquipamento):
        self._id = id_equipamento
        self._nome = nome
        self._quantidade_disponivel = quantidade
        self._estado = estado

    def atualizar_quantidade(self, qtd: int) -> None:
        self._quantidade_disponivel = qtd