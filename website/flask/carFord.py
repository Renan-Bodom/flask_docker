from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração banco
app.config['MYSQL_HOST'] = 'db-carford'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nork'
app.config['MYSQL_DB'] = 'nork'

mysql = MySQL(app)


#--------------------------Funções de interações------------
# Faz leitura por tabela do MySQL
def lerTabelaBanco(tabela):
	cursor = mysql.connection.cursor()
	cursor.execute("SELECT * FROM " + tabela)
	retorno = cursor.fetchall()
	print("Lendo:", cursor.rowcount, " dados")

	return retorno

# Insere morador no banco, e pode ser incrementado por colunas CPF, CNH, etc.
def inserirMoradorBanco(nomeMorador):
	cursor = mysql.connection.cursor()
	cursor.execute("INSERT INTO moradores (name) VALUES (%s);", (nomeMorador,))
	
	print("Dados inserido no banco:", cursor.rowcount)
	mysql.connection.commit()

# Insere carro no banco
def inserirCarBanco(idMorador, modelo, cor):
	cursor = mysql.connection.cursor()
	cursor.execute("INSERT INTO cars (morador_idmoradores, modelo, cor) VALUES (%s, %s, %s);", (idMorador, modelo, cor))
	
	print("Dados inserido no banco:", cursor.rowcount)
	mysql.connection.commit()

# Deleta morador do mando e os carros dele
def deletarDoBanco(idMorador, carrosApagar):
	cursor = mysql.connection.cursor()
	if len(carrosApagar) == 0:
		cursor.execute("DELETE FROM moradores WHERE id=%(param1)s;", {'param1':idMorador})
	else: # Aqui apaga todos os carros dele da tabela carros
		for car in carrosApagar:
			cursor.execute("DELETE FROM cars WHERE id=%(param1)s;", {'param1':car})
		cursor.execute("DELETE FROM moradores WHERE id=%(param1)s;", {'param1':idMorador})

	print("Deletando: ", cursor.rowcount," dado(s)")
	mysql.connection.commit()

# Deleta o carro do banco
def deletarCarBanco(idCar):
	cursor = mysql.connection.cursor()
	cursor.execute("DELETE FROM cars WHERE id=%(param1)s;", {'param1':idCar})
	
	print("Deletando carro: ", cursor.rowcount," dado(s)")
	mysql.connection.commit()


#Lista de carros por dono
def donoCar(morador, listaCars):
	carsMorador = []
	for car in listaCars:
		if morador == car[1]:
			carsMorador.append(car)

	return carsMorador



#-----------------------WebSite------------------
@app.route('/')
def index():
	listaCars = lerTabelaBanco("cars")
	moradores = lerTabelaBanco("moradores")
	moradoresSemCarro = []
	moradoresComCarro = []

	# Identifica os donos e separa moradores sem carro
	for morador in moradores:
		carrosMorador = donoCar(morador[0], listaCars)
		if len(carrosMorador) == 0:
			moradoresSemCarro.append(morador)
		else:
			moradoresComCarro.append([morador[1], carrosMorador])

	return render_template("index.html", moradoresSemCarro=moradoresSemCarro, moradoresComCarro=moradoresComCarro)

@app.route('/addResident', methods=["GET", "POST"])
def cadMorador():
	if request.method == "GET":
		return render_template("cadMorador.html")
	else:
		novoMorador = request.form.get("name")
		print('O novo morador chama:', novoMorador)
		inserirMoradorBanco(novoMorador)
		return redirect('/')

@app.route('/addCar', methods=["GET", "POST"])
def cadCar():
	listaCars = lerTabelaBanco("cars")
	moradores = lerTabelaBanco("moradores")
	moradoresAptosCarro = []
	moradoresNaoAptosCarro = []

	# Identifica quem pode ter mais carros
	for morador in moradores:
		carrosMorador = donoCar(morador[0], listaCars)
		if len(carrosMorador) < 3:
			moradoresAptosCarro.append(morador)
		else:
			moradoresNaoAptosCarro.append(morador)

	if request.method == "GET":
		return render_template("cadCar.html", moradoresAptosCarro=moradoresAptosCarro, moradoresNaoAptosCarro=moradoresNaoAptosCarro)
	else:
		idMorador = request.form.get("idMorador")
		modelo = request.form.get("modelo")
		cor = request.form.get("cor")
		print('O novo carro é: Morador', idMorador, 'Modelo:', modelo, 'Cor:', cor)
		inserirCarBanco(idMorador, modelo, cor)
		return redirect('/')

@app.route('/delResident/<string:idMorador>')
def delMorador(idMorador):
	listaCars = lerTabelaBanco("cars")
	carrosApagar = []
	for car in listaCars:
		if int(idMorador) == car[1]:
			carrosApagar.append(car[0])

	print('Lista de carros', len(carrosApagar))

	deletarDoBanco(idMorador, carrosApagar)
	return redirect('/')

@app.route('/delCar/<string:idCar>')
def delCar(idCar):
	deletarCarBanco(idCar)
	return redirect('/')

@app.route('/<string:pag>')
def error(pag):
	return f'<center>Página ({pag}) não existe</center>'


# Executar flask no Docker
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
