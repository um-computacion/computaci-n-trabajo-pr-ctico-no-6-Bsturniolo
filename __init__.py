import unittest
from src import HistoriaClinica
from datetime import datetime, timedelta
from src import paciente  

class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.dni = "12345678"
        self.nombre = "Juan Pérez"
        self.fecha_nacimiento = datetime(1990, 5, 10)
        self.paciente = paciente(self.dni, self.nombre, self.fecha_nacimiento)

    def test_obtener_dni(self):
        self.assertEqual(self.paciente.obtener_dni(), self.dni)

    def test_fecha_hora_actual(self):
        ahora = datetime.now()
        resultado = self.paciente.obtener_fecha_hora()
        diferencia = abs((resultado - ahora).total_seconds())
        self.assertLess(diferencia, 2)  # Tolerancia de 2 segundos

    def test_str(self):
        esperado = f"Paciente: {self.nombre}, DNI: {self.dni}, Nacimiento: {self.fecha_nacimiento.strftime('%Y-%m-%d')}"
        self.assertEqual(str(self.paciente), esperado)

# errores.py
class PacienteNoExisteError(Exception):
    pass

class MedicoNoExisteError(Exception):
    pass

class TurnoDuplicadoError(Exception):
    pass
# gestor_turnos.py

from src import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError
from src import paciente

class GestorTurnos:
    def __init__(self):
        self.pacientes = {}  # clave: dni
        self.medicos = set()
        self.turnos = set()  # (dni, medico, fecha)

    def registrar_paciente(self, paciente: paciente):
        self.pacientes[paciente.obtener_dni()] = paciente

    def registrar_medico(self, nombre: str):
        self.medicos.add(nombre)

    def asignar_turno(self, dni: str, medico: str, fecha: datetime):
        if dni not in self.pacientes:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe.")
        if medico not in self.medicos:
            raise MedicoNoExisteError(f"Médico {medico} no está registrado.")
        clave_turno = (dni, medico, fecha)
        if clave_turno in self.turnos:
            raise TurnoDuplicadoError("El turno ya fue asignado.")
        self.turnos.add(clave_turno)

if __name__ == '__main__':
    unittest.main()

# test_gestor_turnos.py
import unittest
from datetime import datetime
from src import GestorTurnos
from src import paciente
from test import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError

class TestGestorTurnos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTurnos()
        self.fecha = datetime(2025, 6, 15, 10, 0)

    def test_paciente_no_existe_error(self):
        self.gestor.registrar_medico("Dr. Gómez")
        with self.assertRaises(PacienteNoExisteError):
            self.gestor.asignar_turno("12345678", "Dr. Gómez", self.fecha)

    def test_medico_no_existe_error(self):
        paciente = paciente("12345678", "Ana López", datetime(1990, 5, 20))
        self.gestor.registrar_paciente(paciente)
        with self.assertRaises(MedicoNoExisteError):
            self.gestor.asignar_turno("12345678", "Dr. NoExiste", self.fecha)

    def test_turno_duplicado_error(self):
        paciente = paciente("12345678", "Ana López", datetime(1990, 5, 20))
        self.gestor.registrar_paciente(paciente)
        self.gestor.registrar_medico("Dr. Gómez")
        self.gestor.asignar_turno("12345678", "Dr. Gómez", self.fecha)

        with self.assertRaises(TurnoDuplicadoError):
            self.gestor.asignar_turno("12345678", "Dr. Gómez", self.fecha)

if __name__ == '__main__':
    unittest.main()

# Mocks básicos para Paciente, Turno y Receta
class MockPaciente:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self._dni = dni

    def obtener_dni(self):
        return self._dni

class MockTurno:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f"Turno: {self.descripcion}"

class MockReceta:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f"Receta: {self.descripcion}"

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = MockPaciente("Juan Pérez", "12345678")
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_y_obtener_turno(self):
        turno = MockTurno("Consulta general - 01/06/2025")
        self.historia.agregar_turno(turno)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertIs(turnos[0], turno)

    def test_agregar_y_obtener_receta(self):
        receta = MockReceta("Ibuprofeno 600mg")
        self.historia.agregar_receta(receta)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertIs(recetas[0], receta)

    def test_historia_clinica_str_con_datos(self):
        turno = MockTurno("Consulta general - 01/06/2025")
        receta = MockReceta("Ibuprofeno 600mg")
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        resultado = str(self.historia)
        self.assertIn("Historia Clínica de Juan Pérez", resultado)
        self.assertIn("Turno: Consulta general", resultado)
        self.assertIn("Receta: Ibuprofeno", resultado)

    def test_historia_clinica_str_sin_datos(self):
        resultado = str(self.historia)
        self.assertIn("No hay turnos registrados", resultado)
        self.assertIn("No hay recetas registradas", resultado)

if __name__ == '__main__':
    unittest.main()


