from datetime import datetime

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: datetime):
        self._dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self._dni

    def obtener_fecha_hora(self) -> datetime:
        return datetime.now()

    def __str__(self) -> str:
        return f"Paciente: {self.nombre}, DNI: {self._dni}, Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}"
