from paciente import Paciente
from datetime import datetime
from medico import Medico
class Receta:
    def __init__(self, paciente: 'Paciente', medico: 'Medico', medicamentos: list[str], fecha: datetime):
        self._paciente = paciente
        self._medico = medico
        self._medicamentos = medicamentos
        self._fecha = fecha

    def __str__(self) -> str:
        medicamentos_str = '\n    - '.join(self._medicamentos)
        return (
            f"Receta:\n"
            f"  Fecha: {self._fecha.strftime('%Y-%m-%d')}\n"
            f"  {str(self._paciente)}\n"
            f"  {str(self._medico)}\n"
            f"  Medicamentos:\n    - {medicamentos_str}"
        )
