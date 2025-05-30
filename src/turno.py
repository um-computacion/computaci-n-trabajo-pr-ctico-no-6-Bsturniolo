from paciente import Paciente
from medico import Medico
from datetime import datetime
class Turno:
    def __init__(self, paciente: 'Paciente', medico: 'Medico', fecha_hora: datetime):
        self._paciente = paciente
        self._medico = medico
        self._fecha_hora = fecha_hora

    def obtener_fecha_hora(self) -> datetime:
        return self._fecha_hora

    def __str__(self) -> str:
        return (
            f"Turno:\n"
            f"  Fecha y hora: {self._fecha_hora.strftime('%Y-%m-%d %H:%M')}\n"
            f"  {str(self._paciente)}\n"
            f"  {str(self._medico)}"
        )