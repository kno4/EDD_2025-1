import csv

# Abrir el archivo CSV
with open('Presencia_Redes_Sociales.csv', newline='', encoding='iso-8859-1') as redes_sociales:
    lector_csv = csv.DictReader(redes_sociales)
    
    # Convertir el lector CSV a una lista para acceder a la fila por índice
    filas = list(lector_csv)
    
    fila = filas[7]
    dif= str(int(fila['ENERO'])-int(fila['JUNIO']))
    print("LA DIFERENCIA DE FOLLOWERS EN TWITTER " + dif)
    print('---------------------------------------') #Para diferenciar un calculo y otro
    print('CALCULO DE LA DIFERENCIA DE VIEWS ENTRE UN MES DADO Y OTRO')
    mes1= input("Ingrese el mes del que quiere obtener la diferencia de visualizaciones en Youtube EN MAYUSCULAS (ENERO a JUNIO)")
    mes2= input("Seleccione el segundo mes(ENERO a JUNIO)")
    fila=filas[15]
    dif = str(int(fila[mes1])-int(fila[mes2]))
    print("La diferencia de views en Youtube de ", mes1, " a ", mes2, " es de: " + dif)
    print('---------------------------------------') #Para diferenciar un calculo y otro
    fila = filas[1]
    sum = int(fila['ENERO'])+int(fila['FEBRERO'])+int(fila['MARZO'])+int(fila['ABRIL'])+int(fila['MAYO'])+int(fila['JUNIO'])
    prom = str(sum /6)
    print("EL PROMEDIO DE CRECIMINETO DE FOLLOWERS DE ENERO A JUNIO EN FACEBOOK ES DE " +prom)
    fila = filas[8]
    sum = int(fila['ENERO'])+int(fila['FEBRERO'])+int(fila['MARZO'])+int(fila['ABRIL'])+int(fila['MAYO'])+int(fila['JUNIO'])
    prom = str(sum /6)
    print("EL PROMEDIO DE CRECIMINETO DE FOLLOWERS DE ENERO A JUNIO EN TWITTER ES DE " +prom)
    print('---------------------------------------') #Para diferenciar un calculo y otro
    fila= filas[4]
    sum = int(fila['ENERO'])+int(fila['FEBRERO'])+int(fila['MARZO'])+int(fila['ABRIL'])+int(fila['MAYO'])+int(fila['JUNIO'])
    prom = str(sum /6)
    print("EL PROMEDIO DE LIKES EN FACEBOOK DE ENERO A JUNIO ES DE: "+ prom)
    fila= filas[12]
    sum = int(fila['ENERO'])+int(fila['FEBRERO'])+int(fila['MARZO'])+int(fila['ABRIL'])+int(fila['MAYO'])+int(fila['JUNIO'])
    prom = str(sum /6)
    print("EL PROMEDIO DE LIKES EN TWITTER DE ENERO A JUNIO ES DE: "+ prom)
    fila= filas[17]
    sum = int(fila['ENERO'])+int(fila['FEBRERO'])+int(fila['MARZO'])+int(fila['ABRIL'])+int(fila['MAYO'])+int(fila['JUNIO'])
    prom = str(sum /6)
    print("EL PROMEDIO DE LIKES EN YOUTUBE DE ENERO A JUNIO ES DE: "+ prom)