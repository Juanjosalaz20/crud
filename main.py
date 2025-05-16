from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

usuarios = []

id_contador = 1

@app.route('/', methods=['GET', 'POST'])
def crud():
    global id_contador

    if request.method == 'POST': # Para evitar que al recargar la pagina se agrguem usuarios vacio por el get (si accedemos a la ruta con datos en el formulario)
        nombre = request.form.get('nombre')
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


if __name__ == '__name__':
    app.run(debug=True)