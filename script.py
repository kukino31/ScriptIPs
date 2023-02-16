contador = 10
archivo = open("IP_Fijas_19102022.txt",mode="r")
for dispositivo in archivo:

	#print(dispositivo)
	#dispositivo = "Smart Things-d0:52:a8:00:67:5e-Wired";
	dispositivo_coma = dispositivo.replace('----------',';')
	elementos = dispositivo_coma.split(';')

	nombre_dispositivo= elementos[0].replace(' ','_')

	print ("host" , nombre_dispositivo , "{" )
	print ("#asignacion estatica")
	print ("hardware ethernet",elementos[1],"; #direccion MAC del host")
	#print ("hardware ethernet" , elementos[1] , ";#direccion MAC del host")
	print ('fixed-addreess 192.168.0.%d'%contador , "; #IP a asignar al host")

	print ("}")
	
	contador=contador+1
