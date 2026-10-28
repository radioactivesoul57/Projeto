from enum import Enum


class PerfilUtilizador(Enum):
    NORMAL = "NORMAL"
    ADMINISTRADOR = "ADMINISTRADOR"


class EstadoEspaco(Enum):
    DISPONIVEL = "DISPONIVEL"
    INDISPONIVEL = "INDISPONIVEL"


class EstadoReserva(Enum):
    PENDENTE = "PENDENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
    CONCLUIDA = "CONCLUIDA"
    EXPIRADA = "EXPIRADA"


class EstadoEquipamento(Enum):
    OPERACIONAL = "OPERACIONAL"
    EM_MANUTENCAO = "EM_MANUTENCAO"
    DANIFICADO = "DANIFICADO"