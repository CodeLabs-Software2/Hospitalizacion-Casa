import psycopg2

conexion = psycopg2.connect(
    host="localhost",
    database="HospitalizacionenCasa",
    user="postgres",
    password="05092001"
)


def GuardarConexion(data):
    cur = conexion.cursor()
    cur.execute(data)
    conexion.commit()

GuardarConexion("CREATE TABLE SignosVitales (id SERIAL PRIMARY KEY, Nombre_signo VARCHAR(50), Unidad VARCHAR(10))")
GuardarConexion("CREATE TABLE Diagnostico (id SERIAL PRIMARY KEY, Nombre_diagnostico VARCHAR(100), Descripcion VARCHAR(200))")
GuardarConexion("CREATE TABLE Usuario (id SERIAL PRIMARY KEY, Nombre VARCHAR(100), Apellido VARCHAR(200), Cedula INT, Edad INT, Telefono VARCHAR(10), Email VARCHAR(100), Password VARCHAR(50), Direccion VARCHAR(100))")
GuardarConexion("CREATE TABLE FamiliarDesignado (id SERIAL PRIMARY KEY, usuario_id INT,telefono_alterno VARCHAR(11), CONSTRAINT fkUsuarioFamiliar FOREIGN KEY (usuario_id) REFERENCES Usuario(id))")
GuardarConexion("CREATE TABLE Paciente (id SERIAL PRIMARY KEY, usuario_id INT, Familiar_id INT, CONSTRAINT fkUsuarioPaciente FOREIGN KEY (usuario_id) REFERENCES Usuario(id), CONSTRAINT fkFamiliarPaciente FOREIGN KEY (Familiar_id) REFERENCES FamiliarDesignado(id))")
GuardarConexion("CREATE TABLE Auxiliar (id SERIAL PRIMARY KEY, usuario_id INT, CONSTRAINT fkUsuarioAuxiliar FOREIGN KEY (usuario_id) REFERENCES Usuario(id))")
GuardarConexion("CREATE TABLE personalMedico (id SERIAL PRIMARY KEY, usuario_id INT, Tarjeta_profesional VARCHAR(30), Especialidad VARCHAR(50), Tipo_personal CHAR, CONSTRAINT fkUsuarioMedico FOREIGN KEY (usuario_id) REFERENCES Usuario(id))")
GuardarConexion("CREATE TABLE HistorialDiagnostico (id SERIAL PRIMARY KEY, medico_id INT, Fecha TIMESTAMP, Paciente_id INT, Diagnostico_id INT, CONSTRAINT fkMedicoHDiagnostico FOREIGN KEY (medico_id) REFERENCES PersonalMedico(id), CONSTRAINT fkPacienteHDiagnostico FOREIGN KEY (paciente_id) REFERENCES Paciente(id), CONSTRAINT fkDiagHDiagnostico FOREIGN KEY (diagnostico_id) REFERENCES Diagnostico(id))")
GuardarConexion("CREATE TABLE HistorialCuidados (id SERIAL PRIMARY KEY, Fecha_Inicial TIMESTAMP, Fecha_Final TIMESTAMP, Cuidado VARCHAR(100),  medico_id INT, Paciente_id INT, Descripcion VARCHAR(1000), CONSTRAINT fkHCuidadosPaciente FOREIGN KEY (paciente_id) REFERENCES Paciente(id), CONSTRAINT fkHCuidadosMedico FOREIGN KEY (medico_id) REFERENCES PersonalMedico(id))")
GuardarConexion("CREATE TABLE HistorialSignoVital (id SERIAL PRIMARY KEY, Fecha TIMESTAMP, Valor FLOAT, signo_id INT, Paciente_id INT, CONSTRAINT fkHSignoPaciente FOREIGN KEY (paciente_id) REFERENCES Paciente(id), CONSTRAINT fkHSignosSigno FOREIGN KEY (signo_id) REFERENCES SignosVitales(id))")