# errores.py

class PacienteNoExisteError(Exception):
    """Se lanza cuando el paciente no está registrado en el sistema."""
    pass

class MedicoNoExisteError(Exception):
    """Se lanza cuando el médico no está registrado en el sistema."""
    pass

class TurnoDuplicadoError(Exception):
    """Se lanza cuando se intenta registrar un turno ya existente."""
    pass

# gestor_turnos.py

from errores import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError
from src import paciente
from datetime import datetime

class GestorTurnos:
    def __init__(self):
        self.pacientes = {}   # DNI: Paciente
        self.medicos = set()  # nombres de médicos
        self.turnos = set()   # (dni, medico, fecha)

    def registrar_paciente(self, paciente: paciente):
        self.pacientes[paciente.obtener_dni()] = paciente

    def registrar_medico(self, nombre: str):
        self.medicos.add(nombre)

    def asignar_turno(self, dni: str, medico: str, fecha: datetime):
        if dni not in self.pacientes:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe.")
        if medico not in self.medicos:
            raise MedicoNoExisteError(f"Médico '{medico}' no está registrado.")
        clave = (dni, medico, fecha)
        if clave in self.turnos:
            raise TurnoDuplicadoError("El turno ya está registrado.")
        self.turnos.add(clave)

# test_gestor_turnos.py

import unittest
from datetime import datetime
from src import GestorTurnos
from src import paciente
from errores import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class TestErroresGestorTurnos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTurnos()
        self.fecha = datetime(2025, 6, 15, 10, 0)

    def test_error_paciente_no_existe(self):
        self.gestor.registrar_medico("Dra. García")
        with self.assertRaises(PacienteNoExisteError):
            self.gestor.asignar_turno("11111111", "Dra. García", self.fecha)

    def test_error_medico_no_existe(self):
        paciente = paciente("22222222", "Luis Romero", datetime(1980, 3, 10))
        self.gestor.registrar_paciente(paciente)
        with self.assertRaises(MedicoNoExisteError):
            self.gestor.asignar_turno("22222222", "Dr. Inexistente", self.fecha)

    def test_error_turno_duplicado(self):
        paciente = paciente("33333333", "Marta Díaz", datetime(1995, 7, 22))
        self.gestor.registrar_paciente(paciente)
        self.gestor.registrar_medico("Dr. López")
        self.gestor.asignar_turno("33333333", "Dr. López", self.fecha)
        with self.assertRaises(TurnoDuplicadoError):
            self.gestor.asignar_turno("33333333", "Dr. López", self.fecha)

if __name__ == "__main__":
    unittest.main()
