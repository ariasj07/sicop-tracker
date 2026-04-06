import sqlite3

def crear_db():
    conn = sqlite3.connect('LICITACIONES.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS ENTIDADES (
        ID_Entidad INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS LICITACIONES (
        ID_Licitacion INTEGER PRIMARY KEY,
        Descripcion TEXT NOT NULL,
        Monto_crc REAL NOT NULL,
        N_Ofertas INTEGER NOT NULL,
        Fecha_Apertura TEXT NOT NULL,
        Fecha_Cierre TEXT NOT NULL,
        Created_AT TEXT NOT NULL,
        ID_Entidad INTEGER,
        FOREIGN KEY (ID_Entidad) REFERENCES ENTIDADES(ID_Entidad)
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS ANALISIS (
        ID_Analisis INTEGER PRIMARY KEY AUTOINCREMENT,
        Indice_Irregularidad REAL NOT NULL,
        Resumen_IA TEXT NOT NULL,
        ID_Licitacion INTEGER NOT NULL,
        FOREIGN KEY (ID_Licitacion) 
            REFERENCES LICITACIONES(ID_Licitacion)
            ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()





def INSERTAR_ENTIDAD(Nombre):
    conn = sqlite3.connect('LICITACIONES.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        INSERT INTO ENTIDADES (Nombre)
        VALUES (?)
    """, (Nombre,))
    conn.commit()
    conn.close()
    id_insertado = c.lastrowid 
    conn.close()
    return id_insertado






def INSERTAR_LICITACIONES(Descripcion, Monto_crc, N_Ofertas, Fecha_Apertura, Fecha_Cierre, ID_Entidad):
    conn = sqlite3.connect('LICITACIONES.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        INSERT INTO LICITACIONES 
        (ID_Licitacion, Descripcion, Monto_crc, N_Ofertas, Fecha_Apertura, Fecha_Cierre, ID_Entidad, Created_AT)
        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (ID_Licitacion, Descripcion, Monto_crc, N_Ofertas, Fecha_Apertura, Fecha_Cierre, ID_Entidad))

    conn.commit()
    conn.close()





def INSERTAR_ANALISIS(Indice_irregularidad, Resumen_IA, ID_Licitacion):
    conn = sqlite3.connect("LICITACIONES.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        INSERT INTO ANALISIS (Indice_Irregularidad, Resumen_IA, ID_Licitacion)
        VALUES (?, ?, ?)
    """, (Indice_irregularidad, Resumen_IA, ID_Licitacion))

    conn.commit()
    conn.close()





def OBTENER_LICITACIONES():
    conn = sqlite3.connect("LICITACIONES.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        SELECT l.ID_Licitacion, e.Nombre, l.Monto_crc
        FROM LICITACIONES l
        JOIN ENTIDADES e ON l.ID_Entidad = e.ID_Entidad
    """)

    datos = c.fetchall()
    conn.close()

    return datos




def ELIMINAR_LICITACION(id_licitacion):
    conn = sqlite3.connect("LICITACIONES.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        DELETE FROM LICITACIONES
        WHERE ID_Licitacion = ?
    """, (id_licitacion,))

    conn.commit()
    conn.close()


def ACTUALIZAR_ANALISIS(ID_Licitacion, nuevo_indice, nuevo_resumen):
    conn = sqlite3.connect("LICITACIONES.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    c.execute("""
        UPDATE ANALISIS
        SET Indice_Irregularidad = ?, 
            Resumen_IA = ?
        WHERE ID_Licitacion = ?
    """, (nuevo_indice, nuevo_resumen, ID_Licitacion))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_db()









