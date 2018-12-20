#Logre un error de división por cero.
#Intente escapar al error de división por cero con una excepción general.
#Logre en un sólo programa un error de división por cero, un error por valor  y un error de índice fuera de rango. 
#Intente escapar a los errores anteriores con excepciones general e imprima la excepción generada.
#Intente escapar a los errores anteriores con excepciones específicas para cada error e imprima la excepción generada. Para cada excepción atrapada gestione su solución.
#A partir de éste punto desarrolle sus programas utilizando excepciones según cada caso (de ser necesario).
try:
    logan=12/0
    per='a'/1
    print (logan)
except ZeroDivisionError:
    print("no se puede dividir por Cero")
except ValueError:
    print _("tiene que ser intero")