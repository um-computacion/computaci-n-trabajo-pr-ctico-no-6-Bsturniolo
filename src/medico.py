class Medico:
    def __init__(self, matricula: str, nombre: str, especialidad: str):
        self._matricula = matricula
        self._nombre = nombre
        self._especialidad = especialidad

    def obtener_matricula(self) -> str:
        return self._matricula

    def __str__(self) -> str:
        return f"Médico: {self._nombre}, Matrícula: {self._matricula}, Especialidad: {self._especialidad}"
