from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

usuarios = []

id_contador = 1

@app.route('/', methods=['GET', 'POST'])
def crud():
    global id_contador

    if request.method == 'POST': # Para evitar que al recargar la pagina se agrguem usuarios vacio por el get (si accedemos a la ruta con datos en el formulario)
        nombre = request.form.get('nombre') #guarda en una variable de python lo que el usuario entrega al formulario
        email = request.form.get('email')
        usuarios.append({'id': id_contador, 'username': nombre, 'email': email})
        id_contador += 1
        return redirect(url_for('crud'))

    id_eliminar = request.args.get('borrar')
    if id_eliminar:
        #TODO: Eliminar el usuario con el id del parametro de la lista
        for item in usuarios:
            if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for('crud')) # Llamar el nombre de la función


    return render_template('registro.html', usuarios=usuarios)

#Ruta de actualizacion de datos del usuario
@app.route('/update/<int:id>', methods=['GET','POST']) #Ruta con parametros
def update(id):
    print(usuarios) #Esta es la lista global
    estudiante_a_editar=''
    #TODO: identificar el diccionario del usuario con el id a entregar
    for diccionario in usuarios:
        if diccionario['id']==id:
            estudiante_a_editar=diccionario
            print('el estudiante a editar es: ', estudiante_a_editar)
            break

    if request.method=='POST':
        #TODO: actualizar el diccioario del estudiante con los datos del formulario
        estudiante_a_editar['username']=request.form.get('nombre')
        estudiante_a_editar['email']=request.form.get('email')

        return redirect(url_for('crud')) # Llamar el nombre de la función


    # Si despues de recorrer toda la lista, no encontramos el id entregado
    if estudiante_a_editar=='':
        return f'no existe el usuario con el id: {id}' #salgo de la funcion

    return render_template('editar.html', estudiante_a_editar=estudiante_a_editar)

if __name__ == '__name__':
    app.run(debug=True)