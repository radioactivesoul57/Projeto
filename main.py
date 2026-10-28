from datetime import date, time
from utilizadores import UtilizadorNormal
from espacos import CampoFutebol
from reservas import Reserva


def main():
    # Teste simples de criação de objetos
    user = UtilizadorNormal("U01", "João Silva", "joao@email.com", "123456")
    campo = CampoFutebol("E01", "Campo Principal", "Zona A", 22, "Relva Sintética")

    reserva = Reserva("R01", user, campo, date(2026, 11, 10), time(18, 0), time(19, 0))

    print(f"Utilizador: {user._nome}")
    print(f"Espaço Reservado: {campo._nome}")
    print(f"Estado da Reserva: {reserva._estado.value}")


if __name__ == "__main__":
    main()