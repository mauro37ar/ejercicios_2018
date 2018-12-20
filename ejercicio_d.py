#Cree un diccionario llamado servicios y asigne en cada clave el nombre del servicio y en cada valor su puerto número de puerto correspondiente (ej: {‘ssh’: 22 } ).
#Imprima en pantalla sólo las claves del diccionario.
#Imprima en pantalla cada ítem del diccionario pero en una lista de tuplas clave valor.
#Imprima en pantalla si existe la clave ‘ftp’ en el diccionario y si existe imprima su valor.
#Imprima en pantalla para cada elemento del diccionario la siguiente frase: “[+] Found vulnerabilities with NOMBRE_SERVICIO on port NOMBRE_PUERTO ”
servicio={"ssh":22,"FTP":21,"HTTP":80, "SMTP":25, "HTTPS":443, "Shoutcast":8080,"TCP":8100}
if 'FTP' in servicio != False:
	print("""el diccionario tiene la clave "FTP" y su valor es {}""".format(servicio['FTP']))
print(sorted(servicio.keys()))
print(servicio.items())
for key in servicio:
	print("[+] Found vulnerabilities with {} on port {}".format(key, servicio[key]))