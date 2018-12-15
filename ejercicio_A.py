#Variables: Cree una variable llamada port y asigne el entero 22, luego cree una variable llamada banner y asigne la cadena “SSH Port”. Imprima en pantalla la siguiente frase: “{+] Checking for VARIABLE_BANNER  on port VARIABLE_PORT-
port = 22
banner="SSH Port"
print("{+] Checking for %s on port %s" % (banner,port))
