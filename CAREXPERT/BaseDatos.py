import sqlite3

# Crear la base de datos SQLite
conn = sqlite3.connect("CarExpert.db")
cursor = conn.cursor()

# Crear tablas para la base de datos
cursor.execute("""
CREATE TABLE IF NOT EXISTS tipos_falla (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sintomas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_falla_id INTEGER,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (tipo_falla_id) REFERENCES tipos_falla (id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS causas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_falla_id INTEGER,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (tipo_falla_id) REFERENCES tipos_falla (id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS soluciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_falla_id INTEGER,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (tipo_falla_id) REFERENCES tipos_falla (id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sugerencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_falla_id INTEGER,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (tipo_falla_id) REFERENCES tipos_falla (id)
);
""")

# Insertar datos en las tablas
tipos_falla = [("Combustión",), ("Lubricación",), ("Refrigeración",)]
cursor.executemany("INSERT INTO tipos_falla (nombre) VALUES (?)", tipos_falla)

sintomas = [
    (1, "Check Engine, Humo negro, Petardeo, Aceleración irregular, Pérdida de potencia, Olor a combustible, Marcha mínima inestable, Dificultad para arrancar, consumo de combustible elevado, explosiones en el escape, fallo en la emisión de gases."),
    (2, "Testigo del aceite encendido, Humo azul, Pérdida de aceite, Olor a aceite quemado, Vibraciones, Fugas de aceite, Ruidos al acelerar, Emisiones altas."),
    (3, "Aumento de temperatura, Pérdida de refrigerante, Humo o vapor, Ruidos extraños, Fugas en el radiador, Refrigerante en el aceite, Calefacción inconsistente.")
]
cursor.executemany("INSERT INTO sintomas (tipo_falla_id, descripcion) VALUES (?, ?)", sintomas)

causas = [
    (1, "Bujías desgastadas, Bobinas defectuosas, Inyectores obstruidos, Bomba de combustible defectuosa, Filtro de combustible obstruido, Mezcla aire-combustible incorrecta, Sensor MAF defectuoso, Filtro de aire sucio o bloqueado, Fugas de aire en la admisión, Catalizador obstruido, Sensor de oxígeno o sonda lambda defectuoso, Baja compresión en los cilindros, Sincronización incorrecta del motor, Problemas en la válvula EGR (Recirculación de Gases de Escape), Combustible de baja calidad o contaminado, Uso de combustible incorrecto, Falta de mantenimiento.."),
    (2, "Fugas, Aceite de baja calidad, Filtro obstruido, Desgaste en la bomba de aceite, Obstrucciones en las líneas de lubricación, Calor extremo, Sobrecarga del motor, Sellos defectuosos, drenaje incompleto, contaminación interna, cojinetes desgastados, bomba de vació defectuosa, cedazo tapado."),
    (3, "Fugas en el sistema, Radiador obstruido, Bomba defectuosa, Termostato atascado, Ventilador en mal estado, Junta de culata dañada, Refrigerante incorrecto, Mezcla con agua de mala calidad, Fisuras en el motor, Uso de refrigerante incorrecto, Refrigerante viejo, Mezcla con agua de baja calidad, Fugas en la válvula de la tapa del radiador, Clima extremo, Remolque excesivo.")
]
cursor.executemany("INSERT INTO causas (tipo_falla_id, descripcion) VALUES (?, ?)", causas)

soluciones = [
    (1, "Escanear el carro, revisar códigos de error, verificar compresión de los cilindros, inspeccionar cables y bujías, revisar pulsos de los inyectores. Si todo está en orden, considerar reemplazar la computadora del vehículo."),
    (2, "Revisión visual para detectar fugas, verificar que la bomba de aceite funcione correctamente, reemplazar aceite y filtro si no son adecuados, revisar que el cedazo no esté obstruido. En caso extremo, cambiar componentes principales como cojinetes o la bomba de vacío."),
    (3, "Inspección visual de fugas, revisar funcionamiento del ventilador, apretar tornillos de tapas o reemplazar empaques dañados, verificar termostato y bomba de agua. En caso de problemas graves, reemplazar la junta de culata.")
]
cursor.executemany("INSERT INTO soluciones (tipo_falla_id, descripcion) VALUES (?, ?)", soluciones)

sugerencias = [
    (1, "Usar combustible de calidad, verificar compresión regularmente, evitar estrés excesivo al motor, realizar mantenimiento periódico, monitorear testigos del tablero y actuar rápidamente ante síntomas como pérdida de potencia o consumo excesivo de combustible."),
    (2, "Revisar el nivel de aceite periódicamente, usar aceite de calidad con la viscosidad adecuada, cambiar aceite y filtro según las recomendaciones, evitar sobrecargar el motor y realizar mantenimiento regular."),
    (3, "Mantener el nivel de refrigerante adecuado, cambiar el refrigerante regularmente, inspeccionar el radiador para evitar obstrucciones, revisar y mantener la bomba de agua, inspeccionar mangueras y conexiones, evitar sobrecargar el motor en climas extremos.")
]
cursor.executemany("INSERT INTO sugerencias (tipo_falla_id, descripcion) VALUES (?, ?)", sugerencias)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos creada y cargada exitosamente.")
