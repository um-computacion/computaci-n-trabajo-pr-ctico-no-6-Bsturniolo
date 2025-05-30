from datetime import datetime
from paciente import Paciente
from turno import Turno
from receta  import Receta 
from HistoriaClinica import HistoriaClinica
from medico import Medico

class Clinica:
    def __init__(self):
        self._pacientes = {}  # DNI -> Paciente
        self._medicos = {}    # Matrícula -> Medico
        self._turnos = []     # Lista de Turno
        self._historias_clinicas = {}  # DNI -> HistoriaClinica

    def agregar_paciente(self, paciente: 'Paciente'):
        dni = paciente.obtener_dni()
        if dni not in self._pacientes:
            self._pacientes[dni] = paciente
            self._historias_clinicas[dni] = HistoriaClinica(paciente)
        else:
            print(f"Paciente con DNI {dni} ya está registrado.")

    def agregar_medico(self, medico: 'Medico'):
        matricula = medico.obtener_matricula()
        if matricula not in self._medicos:
            self._medicos[matricula] = medico
        else:
            print(f"Médico con matrícula {matricula} ya está registrado.")

    def agendar_turno(self, dni: str, matricula: str, fecha_hora: datetime):
        paciente = self._pacientes.get(dni)
        medico = self._medicos.get(matricula)

        if paciente and medico:
            turno = Turno(paciente, medico, fecha_hora)
            self._turnos.append(turno)
            self._historias_clinicas[dni].agregar_turno(turno)
        else:
            print("No se puede agendar el turno: paciente o médico no encontrado.")

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        paciente = self._pacientes.get(dni)
        medico = self._medicos.get(matricula)

        if paciente and medico:
            receta = Receta(paciente, medico, medicamentos, datetime.now())
            self._historias_clinicas[dni].agregar_receta(receta)
        else:
            print("No se puede emitir la receta: paciente o médico no encontrado.")

    def obtener_historia_clinica(self, dni: str) -> 'HistoriaClinica':
        return self._historias_clinicas.get(dni, None)

    def obtener_turnos(self) -> list['Turno']:
        return self._turnos

def agendar_turno(self, dni: str, matricula: str, fecha_hora: datetime):
    paciente = self._pacientes.get(dni)
    medico = self._medicos.get(matricula)

    # Validación 1: el paciente y el médico deben de existir
    if not paciente:
        print(f"No se encontró el paciente con DNI {dni}.")
        return
    if not medico:
        print(f"No se encontró el médico con matrícula {matricula}.")
        return

    # Validación 2: evitar doble turno con el mismo médico en el mismo horario
    for turno in self._turnos:
        if (turno._medico.obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
            print(f"Ya existe un turno con el médico {medico.obtener_matricula()} en esa fecha y hora.")
            return

    # Validación 3: no permitir turnos en el pasado, no se puede viajar en el tiempo
    if fecha_hora < datetime.now():
        print("No se puede agendar un turno en el pasado.")
        return

    # Si pasa todas las validaciones, crear y registrar el turno. listo
    turno = Turno(paciente, medico, fecha_hora)
    self._turnos.append(turno)
    self._historias_clinicas[dni].agregar_turno(turno)
    print(f"Turno agendado exitosamente para {paciente.nombre} con el Dr/a. {medico._nombre}.")

