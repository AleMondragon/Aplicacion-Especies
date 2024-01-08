from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

# Conexión
mysql = MySQL(app)

#METODOS GET PARA LA VISUALIZACION DE DATOS

# Consulta para visualizar toda la información de la base de datos
@app.route('/Especies', methods=['GET'])
def listar_toda_informacion():
    try:
        cursor = mysql.connection.cursor()

        # Consulta para obtener toda la información de los estados
        sql_estados = "SELECT * FROM Estado"
        cursor.execute(sql_estados)
        datos_estados = cursor.fetchall()

        estados = []
        for estado in datos_estados:
            info_estado = {
                'id_estado': estado[0],
                'nombre_estado': estado[1],
                'numero_alcaldias': estado[2],
            }
            estados.append(info_estado)
        
        # Consulta para obtener toda la información de las alcaldías
        sql_alcaldias = "SELECT * FROM Alcaldia"
        cursor.execute(sql_alcaldias)
        datos_alcaldias = cursor.fetchall()

        alcaldias = []
        for alcaldia in datos_alcaldias:
            info_alcaldia = {
                'id_alcaldia': alcaldia[0],
                'nombre_alcaldia': alcaldia[1],
            }
            alcaldias.append(info_alcaldia)

        # Consulta para obtener toda la información común
        sql_informacion_comun = "SELECT * FROM InformacionComun"
        cursor.execute(sql_informacion_comun)
        datos_informacion_comun = cursor.fetchall()

        informacion_comun = []
        for fila in datos_informacion_comun:
            info_comun = {
                'id_informacion_comun': fila[0],
                'entidad_tipo': fila[1],
                'id_geo': fila[2],
                'grupoSNIB': fila[3],
                'Familia': fila[4],
                'Especie_DOF': fila[5],
                'Especie_mapa_conabio': fila[6],
                'Categoria_NOM_059': fila[7],
                'Nombre_comun_principal': fila[8],
                'Nombres_comunes': fila[9],
                'Fuente': fila[10],
                'id_alcaldia': fila[11],
                'id_estado': fila[12]
            }
            informacion_comun.append(info_comun)

        return jsonify({
            'estados': estados,
            'alcaldias': alcaldias,
            'informacion_comun': informacion_comun,
            'mensaje': 'Toda la información de la base de datos listada.'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Consulta información de todos los estados
@app.route('/Especies/Estados', methods=['GET'])
def listar_estados():
    try:
        cursorEstados = mysql.connection.cursor()
        sql = "SELECT * FROM Estado"
        cursorEstados.execute(sql)
        datos = cursorEstados.fetchall()

        estados = []
        for estado in datos:
            info_estado = {
                'id_estado': estado[0],
                'nombre_estado': estado[1],
                'numero_alcaldias': estado[2]
            }
            estados.append(info_estado)

        return jsonify({'estados': estados, 'mensaje': 'Información de todos los estados listada.'})

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

# Consulta información específica de un estado
@app.route('/Especies/Estados/<id_estado>', methods=['GET'])
def leer_informacion_estado(id_estado):
    try:
        cursorEstado = mysql.connection.cursor()
        estado_sql = f"SELECT * FROM Estado WHERE id_estado = {id_estado}"
        cursorEstado.execute(estado_sql)
        datos = cursorEstado.fetchone()

        if datos:
            info_estado = {
                'id_estado': datos[0],
                'nombre_estado': datos[1],
                'numero_alcaldias': datos[2]
            }

            return jsonify({'informacionEstado': info_estado, 'mensaje': 'Información encontrada.'})
        else:
            return jsonify({'Mensaje': 'Información no encontrada'})

    except Exception as ex:
        return jsonify({'Mensaje': 'Error'})


# Consulta información de todas las alcaldías
@app.route('/Especies/Alcaldias', methods=['GET'])
def listar_alcaldias():
    try:
        cursorAlcaldias = mysql.connection.cursor()
        sql = "SELECT * FROM Alcaldia"
        cursorAlcaldias.execute(sql)
        datos = cursorAlcaldias.fetchall()

        alcaldias = []
        for alcaldia in datos:
            info_alcaldia = {
                'id_alcaldia': alcaldia[0],
                'nombre_alcaldia': alcaldia[1]
            }
            alcaldias.append(info_alcaldia)

        return jsonify({'alcaldias': alcaldias, 'mensaje': 'Información de todas las alcaldías listada.'})

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Consulta información específica de una alcaldía
@app.route('/Especies/Alcaldias/<id_alcaldia>', methods=['GET'])
def leer_informacion_alcaldia(id_alcaldia):
    try:
        cursorAlcaldia = mysql.connection.cursor()
        alcaldia_sql = f"SELECT * FROM Alcaldia WHERE id_alcaldia = {id_alcaldia}"
        cursorAlcaldia.execute(alcaldia_sql)
        datos = cursorAlcaldia.fetchone()

        if datos:
            info_alcaldia = {
                'id_alcaldia': datos[0],
                'nombre_alcaldia': datos[1]
            }

            return jsonify({'informacionAlcaldia': info_alcaldia, 'mensaje': 'Información encontrada.'})
        else:
            return jsonify({'Mensaje': 'Información no encontrada'})

    except Exception as ex:
        return jsonify({'Mensaje': 'Error'})

# Consulta para visualizar toda la información común
@app.route('/Especies/InformacionComun', methods=['GET'])
def listar_informacion_comun():
    try:
        with mysql.connection.cursor() as cursor:
            sql = "SELECT * FROM InformacionComun"
            cursor.execute(sql)
            datos = cursor.fetchall()
            informacion = []

            for fila in datos:
                info = {
                    'id_informacion_comun': fila[0],
                    'entidad_tipo': fila[1],
                    'id_geo': fila[2],
                    'grupoSNIB': fila[3],
                    'Familia': fila[4],
                    'Especie_DOF': fila[5],
                    'Especie_mapa_conabio': fila[6],
                    'Categoria_NOM_059': fila[7],
                    'Nombre_comun_principal': fila[8],
                    'Nombres_comunes': fila[9],
                    'Fuente': fila[10],
                    'id_alcaldia': fila[11],
                    'id_estado': fila[12]
                }
                informacion.append(info)

            return jsonify({'informacion_comun': informacion, 'mensaje': 'Información almacenada y listada.'})

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Consulta para visualizar información común específica
@app.route('/Especies/InformacionComun/<id_informacion_comun>', methods=['GET'])
def leer_informacion_comun(id_informacion_comun):
    try:
        cursorInformacionComun = mysql.connection.cursor()
        sql = f"SELECT * FROM InformacionComun WHERE id_informacion_comun = {id_informacion_comun}"
        cursorInformacionComun.execute(sql)
        datos = cursorInformacionComun.fetchone()

        if datos:
            info_comun = {
                'id_informacion_comun': datos[0],
                'entidad_tipo': datos[1],
                'id_geo': datos[2],
                'grupoSNIB': datos[3],
                'Familia': datos[4],
                'Especie_DOF': datos[5],
                'Especie_mapa_conabio': datos[6],
                'Categoria_NOM_059': datos[7],
                'Nombre_comun_principal': datos[8],
                'Nombres_comunes': datos[9],
                'Fuente': datos[10],
                'id_alcaldia': datos[10],
                'id_estado': datos[11]
            }

            return jsonify({'informacion_comun': info_comun, 'mensaje': 'Información común encontrada.'})
        else:
            return jsonify({'Mensaje': 'Información común no encontrada'})

    except Exception as ex:
        return jsonify({'Mensaje': 'Error'})




# METODOS POST PARA INSETAR DATOS A LA BASE DE DATOS

# Método POST para agregar Estados
@app.route('/Especies/Estados', methods=['POST'])
def agregar_estado():
    try:
        cursorEstados = mysql.connection.cursor()
        estado_id = request.json['id_estado']
        
        # Verifica si ya existe un estado con la misma clave primaria
        cursorEstados.execute(f"SELECT * FROM Estado WHERE id_estado = {estado_id}")
        existing_estado = cursorEstados.fetchone()

        if existing_estado:
            return jsonify({'mensaje': 'Error, la clave primaria ya existe.'})

        # Si no existe, realiza la inserción
        sql = """INSERT INTO Estado (id_estado, nombre_estado, numero_alcaldias)
        VALUES ({0}, '{1}', {2})""".format(
            estado_id,
            request.json['nombre_estado'],
            request.json['numero_alcaldias']
        )
        cursorEstados.execute(sql)
        mysql.connection.commit()  # Confirma la acción de inserción
        return jsonify({'mensaje': "Informacion registrada"})

    except Exception as ex:
        print("Error:", ex)  # Agrega esta línea para imprimir el error
        return jsonify({'mensaje': "Error"})

# Método POST para agregar Alcaldias
@app.route('/Especies/Alcaldias', methods=['POST'])
def agregar_alcaldia():
    try:
        cursorAlcaldias = mysql.connection.cursor()
        alcaldia_id = request.json['id_alcaldia']

        # Verifica si ya existe una alcaldía con la misma clave primaria
        cursorAlcaldias.execute(f"SELECT * FROM Alcaldia WHERE id_alcaldia = {alcaldia_id}")
        existing_alcaldia = cursorAlcaldias.fetchone()

        if existing_alcaldia:
            return jsonify({'mensaje': 'Error, la clave primaria ya existe.'})

        # Si no existe, realiza la inserción
        sql = """INSERT INTO Alcaldia (id_alcaldia, nombre_alcaldia)
        VALUES ({0}, '{1}')""".format(
            alcaldia_id,
            request.json['nombre_alcaldia']
        )
        cursorAlcaldias.execute(sql)
        mysql.connection.commit()  # Confirma la acción de inserción
        return jsonify({'mensaje': "Informacion registrada"})

    except Exception as ex:
        print("Error:", ex)  # Agrega esta línea para imprimir el error
        return jsonify({'mensaje': "Error"})

# Método POST para agregar información Común
@app.route('/Especies/InformacionComun', methods=['POST'])
def agregar_informacion_comun():
    try:
        cursorInfoComun = mysql.connection.cursor()

        # No necesitas obtener el id_informacion_comun de la solicitud

        sql = """INSERT INTO InformacionComun (
            entidad_tipo,
            id_geo,
            grupoSNIB,
            Familia,
            Especie_DOF,
            Especie_mapa_conabio,
            Categoria_NOM_059,
            Nombre_comun_principal,
            Nombres_comunes,
            Fuente,
            id_alcaldia,
            id_estado
        ) VALUES ('{0}', {1}, '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', {10}, {11})""".format(
            request.json['entidad_tipo'],
            request.json['id_geo'],
            request.json['grupoSNIB'],
            request.json['Familia'],
            request.json['Especie_DOF'],
            request.json['Especie_mapa_conabio'],
            request.json['Categoria_NOM_059'],
            request.json['Nombre_comun_principal'],
            request.json['Nombres_comunes'],
            request.json['Fuente'],
            request.json['id_alcaldia'],
            request.json['id_estado']
        )
        cursorInfoComun.execute(sql)
        mysql.connection.commit()  # Confirma la acción de inserción
        return jsonify({'mensaje': "Informacion registrada"})

    except Exception as ex:
        print("Error:", ex)  # Agrega esta línea para imprimir el error
        return jsonify({'mensaje': "Error"})


#METODO DELETE PARA ELIMINAR DATOS DE LA BASE DE DATOS

# Método DELETE para eliminar Estados
@app.route('/Especies/Estados/<id_estado>', methods=['DELETE'])
def eliminar_estado(id_estado):
    try:
        cursorEstados = mysql.connection.cursor()

        # Verifica si el estado existe antes de intentar eliminarlo
        cursorEstados.execute(f"SELECT * FROM Estado WHERE id_estado = {id_estado}")
        existing_estado = cursorEstados.fetchone()

        if not existing_estado:
            return jsonify({'mensaje': 'Error, el estado no existe.'})

        # Si el estado existe, realiza la eliminación
        cursorEstados.execute(f"DELETE FROM Estado WHERE id_estado = {id_estado}")
        mysql.connection.commit()

        return jsonify({'mensaje': f"Estado con id {id_estado} eliminado correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar eliminar el estado"})

# Método DELETE para eliminar Alcaldías
@app.route('/Especies/Alcaldias/<id_alcaldia>', methods=['DELETE'])
def eliminar_alcaldia(id_alcaldia):
    try:
        cursorAlcaldias = mysql.connection.cursor()

        # Verifica si la alcaldía existe antes de intentar eliminarla
        cursorAlcaldias.execute(f"SELECT * FROM Alcaldia WHERE id_alcaldia = {id_alcaldia}")
        existing_alcaldia = cursorAlcaldias.fetchone()

        if not existing_alcaldia:
            return jsonify({'mensaje': 'Error, la alcaldía no existe.'})

        # Si la alcaldía existe, realiza la eliminación
        cursorAlcaldias.execute(f"DELETE FROM Alcaldia WHERE id_alcaldia = {id_alcaldia}")
        mysql.connection.commit()

        return jsonify({'mensaje': f"Alcaldía con id {id_alcaldia} eliminada correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar eliminar la alcaldía"})

# Método DELETE para eliminar Información Común
@app.route('/Especies/InformacionComun/<id_informacion_comun>', methods=['DELETE'])
def eliminar_informacion_comun(id_informacion_comun):
    try:
        cursorInfoComun = mysql.connection.cursor()

        # Verifica si la información común existe antes de intentar eliminarla
        cursorInfoComun.execute(f"SELECT * FROM InformacionComun WHERE id_informacion_comun = {id_informacion_comun}")
        existing_informacion_comun = cursorInfoComun.fetchone()

        if not existing_informacion_comun:
            return jsonify({'mensaje': 'Error, la información común no existe.'})

        # Si la información común existe, realiza la eliminación
        cursorInfoComun.execute(f"DELETE FROM InformacionComun WHERE id_informacion_comun = {id_informacion_comun}")
        mysql.connection.commit()

        return jsonify({'mensaje': f"Información común con id {id_informacion_comun} eliminada correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar eliminar la información común"})

#METODO PUT PARA ACTUALIZAR LA BASE DE DATOS

# Método PUT para actualizar Estados
@app.route('/Especies/Estados/<id_estado>', methods=['PUT'])
def actualizar_estado(id_estado):
    try:
        cursorEstados = mysql.connection.cursor()

        # Verifica si el estado existe antes de intentar actualizarlo
        cursorEstados.execute(f"SELECT * FROM Estado WHERE id_estado = {id_estado}")
        existing_estado = cursorEstados.fetchone()

        if not existing_estado:
            return jsonify({'mensaje': 'Error, el estado no existe.'})

        # Actualiza el estado con los nuevos datos
        sql = """UPDATE Estado SET
                 nombre_estado = '{0}',
                 numero_alcaldias = {1}
                 WHERE id_estado = {2}""".format(
            request.json['nombre_estado'],
            request.json['numero_alcaldias'],
            id_estado
        )
        cursorEstados.execute(sql)
        mysql.connection.commit()

        return jsonify({'mensaje': f"Estado con id {id_estado} actualizado correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar actualizar el estado"})

# Método PUT para actualizar Alcaldías
@app.route('/Especies/Alcaldias/<id_alcaldia>', methods=['PUT'])
def actualizar_alcaldia(id_alcaldia):
    try:
        cursorAlcaldias = mysql.connection.cursor()

        # Verifica si la alcaldía existe antes de intentar actualizarla
        cursorAlcaldias.execute(f"SELECT * FROM Alcaldia WHERE id_alcaldia = {id_alcaldia}")
        existing_alcaldia = cursorAlcaldias.fetchone()

        if not existing_alcaldia:
            return jsonify({'mensaje': 'Error, la alcaldía no existe.'})

        # Actualiza la alcaldía con los nuevos datos
        sql = """UPDATE Alcaldia SET
                 nombre_alcaldia = '{0}'
                 WHERE id_alcaldia = {1}""".format(
            request.json['nombre_alcaldia'],
            id_alcaldia
        )
        cursorAlcaldias.execute(sql)
        mysql.connection.commit()

        return jsonify({'mensaje': f"Alcaldía con id {id_alcaldia} actualizada correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar actualizar la alcaldía"})

# Método PUT para actualizar Información Común
@app.route('/Especies/InformacionComun/<id_informacion_comun>', methods=['PUT'])
def actualizar_informacion_comun(id_informacion_comun):
    try:
        cursorInfoComun = mysql.connection.cursor()

        # Verifica si la información común existe antes de intentar actualizarla
        cursorInfoComun.execute(f"SELECT * FROM InformacionComun WHERE id_informacion_comun = {id_informacion_comun}")
        existing_informacion_comun = cursorInfoComun.fetchone()

        if not existing_informacion_comun:
            return jsonify({'mensaje': 'Error, la información común no existe.'})

        # Actualiza la información común con los nuevos datos
        sql = """UPDATE InformacionComun SET
                 entidad_tipo = '{0}',
                 id_geo = {1},
                 grupoSNIB = '{2}',
                 Familia = '{3}',
                 Especie_DOF = '{4}',
                 Especie_mapa_conabio = '{5}',
                 Categoria_NOM_059 = '{6}',
                 Nombre_comun_principal = '{7}',
                 Nombres_comunes = '{8}',
                 Fuente = '{9}',
                 id_alcaldia = {10},
                 id_estado = {11}
                 WHERE id_informacion_comun = {12}""".format(
            request.json['entidad_tipo'],
            request.json['id_geo'],
            request.json['grupoSNIB'],
            request.json['Familia'],
            request.json['Especie_DOF'],
            request.json['Especie_mapa_conabio'],
            request.json['Categoria_NOM_059'],
            request.json['Nombre_comun_principal'],
            request.json['Nombres_comunes'],
            request.json['Fuente'],
            request.json['id_alcaldia'],
            request.json['id_estado'],
            id_informacion_comun
        )
        cursorInfoComun.execute(sql)
        mysql.connection.commit()

        return jsonify({'mensaje': f"Información común con id {id_informacion_comun} actualizada correctamente"})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error al intentar actualizar la información común"})




#SECCION DE REGISTO DE USUARIO

# Método POST para registrar un nuevo usuario
@app.route('/Especies/Usuarios', methods=['POST'])
def registrar_usuario():
    try:
        cursor = mysql.connection.cursor()

        # Verifica si el correo ya está registrado
        correo = request.json['correo']
        cursor.execute(f"SELECT * FROM Usuario WHERE correo = '{correo}'")
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({'mensaje': 'Error, el correo ya está registrado.'})

        # Inserta un nuevo usuario
        sql = """INSERT INTO Usuario (correo, contrasena)
                 VALUES ('{0}', '{1}')""".format(
            request.json['correo'],
            request.json['contrasena']
        )
        cursor.execute(sql)
        mysql.connection.commit()

        return jsonify({'mensaje': 'Usuario registrado correctamente.'})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': 'Error al intentar registrar el usuario.'})

# Método GET para obtener información de todos los usuarios
@app.route('/Especies/Usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()

        lista_usuarios = []
        for usuario in usuarios:
            info_usuario = {
                'id_usuario': usuario[0],
                'correo': usuario[1],
                'contrasena': usuario[2]
            }
            lista_usuarios.append(info_usuario)

        return jsonify({'usuarios': lista_usuarios, 'mensaje': 'Información de usuarios obtenida correctamente.'})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': 'Error al intentar obtener la información de usuarios.'})

# Método GET para obtener información de un usuario específico por correo
@app.route('/Especies/Usuarios/<correo>', methods=['GET'])
def obtener_usuario_por_correo(correo):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM Usuario WHERE correo = '{correo}'")
        usuario = cursor.fetchone()

        if usuario:
            info_usuario = {
                'id_usuario': usuario[0],
                'correo': usuario[1],
                'contrasena': usuario[2]
            }
            return jsonify({'usuario': info_usuario, 'mensaje': 'Información de usuario obtenida correctamente.'})
        else:
            return jsonify({'mensaje': 'Usuario no encontrado.'})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': 'Error al intentar obtener la información del usuario.'})

# Método PUT para actualizar información de un usuario por correo
@app.route('/Especies/Usuarios/<correo>', methods=['PUT'])
def actualizar_usuario(correo):
    try:
        cursor = mysql.connection.cursor()

        # Verifica si el usuario existe antes de intentar actualizarlo
        cursor.execute(f"SELECT * FROM Usuario WHERE correo = '{correo}'")
        existing_user = cursor.fetchone()

        if not existing_user:
            return jsonify({'mensaje': 'Error, el usuario no existe.'})

        # Actualiza la información del usuario con los nuevos datos
        sql = """UPDATE Usuario SET
                 contrasena = '{0}'
                 WHERE correo = '{1}'""".format(
            request.json['contrasena'],
            correo
        )
        cursor.execute(sql)
        mysql.connection.commit()

        return jsonify({'mensaje': f"Información del usuario {correo} actualizada correctamente."})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': 'Error al intentar actualizar la información del usuario.'})

# Método DELETE para eliminar un usuario por correo
@app.route('/Especies/Usuarios/<correo>', methods=['DELETE'])
def eliminar_usuario(correo):
    try:
        cursor = mysql.connection.cursor()

        # Verifica si el usuario existe antes de intentar eliminarlo
        cursor.execute(f"SELECT * FROM Usuario WHERE correo = '{correo}'")
        existing_user = cursor.fetchone()

        if not existing_user:
            return jsonify({'mensaje': 'Error, el usuario no existe.'})

        # Elimina al usuario
        cursor.execute(f"DELETE FROM Usuario WHERE correo = '{correo}'")
        mysql.connection.commit()

        return jsonify({'mensaje': f"Usuario {correo} eliminado correctamente."})

    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': 'Error al intentar eliminar el usuario.'})






# Página no encontrada
def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>", 404

#MAIN
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)


#Debug true es el modo de desarrollo para que actualice automaticamente
