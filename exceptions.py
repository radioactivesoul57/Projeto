class LoginInvalidoException(Exception):
    """Exceção lançada quando as credenciais de login estão incorretas."""
    pass


class ConflitoHorarioException(Exception):
    """Exceção lançada quando existe sobreposição de horários numa reserva."""
    pass


class EspacoInexistenteException(Exception):
    """Exceção lançada quando o espaço não existe ou não está disponível."""
    pass