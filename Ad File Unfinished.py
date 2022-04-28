#Jhair Garthoff Añez
#class: Ad


#Para la clase Ad, en el proyecto, se llamarán datos de
#otras clases, como los datos del cliente.

#Para este ejercicio, simplemente los definiremos
#en variables diferentes para utilizarlas en el archivo.

client_name    = "Juan Pérez"
client_age     = "25"
client_address = "4to Anillo - UPSA"
client_phnumber= "77777444"

ad_title = input("Escriba el título de la publicación...\n")
ad_cat   = input("Escriba la categoría del trabajo...\n")
ad_desc  = input("Escriba la descripción del trabajo a solicitar...\n")


FILE_NAME = 'ad.txt'

ad = open(FILE_NAME, 'w')
#Client Profile

ad.write(client_name)
ad.write("\t")

ad.write(client_age)
ad.write("\t")

ad.write(client_phnumber)
ad.write("\t")
ad.write("\n")
#Double line here

#Job details
ad.write("=== Detalles ===\n")
ad.write(ad_title)
ad.write("\n")

ad.write(ad_cat)
ad.write("\n")

ad.write(ad_desc)
ad.write("\n")
ad.write("\n")
#Double line here

#Client Address
ad.write("=== Dirección ===\n")
ad.write(client_address)
ad.write("\n")

ad.close()


