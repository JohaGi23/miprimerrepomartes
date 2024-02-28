userBD="hidrotech123"
passwordBD="admin123"

print('software tech hidroituango')
print('**************************')
UserName=input('Digita tu usuario: ')
UserPassword=input('Digita tu contraseña: ')

if userBD==UserName and passwordBD==UserPassword:
    print("Exito en su usuario")
else:
    print('fallaste')


print ("Exito en su usuario")if userBD==UserName and passwordBD==UserPassword else print('fallaste')
#operador ternario




