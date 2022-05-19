from datetime import datetime
import os
import re

def registro():
  #Defino el centinela en None.
  centinela = None
  #Inicio el ciclo principal. 
  
  while (centinela == None):
      #Inicio el ciclo primero.
      while(centinela == None):
          #Defino x(str) con un input.
          tipo_doc = input('Cual es tu tipo de documento?\t (CC,PA,TI o CE)\n  => ').upper()
          os.system ("clear")
          #Condicion de prueba para x
          if (tipo_doc == 'CC' or tipo_doc == 'TI' or tipo_doc == 'PA' or tipo_doc == 'CE'):
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
            
              #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
          #Si la condicion Falla.
          else:
              #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
      #Cambio el estado de centinela para salir al segundo ciclo.        
      centinela = None
  
      #Inicio el ciclo segundo.
      while(centinela == None):
      #Inicio el ciclo secundario.
          numero_doc = input("Cual es el numero de numero de documento?\t (Solo numeros, sin puntos ni comas.)\n  => ")
          os.system ("clear")
          #Condicion de prueba para y
          if numero_doc.isnumeric() and len(numero_doc) <= 12 :
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n """)
          #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
      #Si la condicion Falla.           
          else:
          #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
              centinela = None
      #Cambio el estado de centinela para salir al tercer ciclo.        
      centinela = None
  
      #Inicio el ciclo tercero.
      while(centinela == None):
      #Inicio el ciclo secundario.
          nombre = input('Digite su nombre:\n  =>  ').capitalize()
          os.system ("clear")
          #Condicion de prueba para y
          if nombre.isalpha() and len(nombre)<=30:
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*- 
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
          #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
      #Si la condicion Falla.           
          else:
          #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
              centinela = None
      #Cambio el estado de centinela para salir al tercer ciclo.        
      centinela = None
    
      #Inicio el ciclo cuarto.
      while(centinela == None):
      #Inicio el ciclo secundario.
          apellido = input('Digite su apellido:\n  =>  ').capitalize()
          os.system ("clear")
          #Condicion de prueba para y
          if apellido.isalpha() and len(nombre)<=30:
          #Imprimo un mensaje de prueba.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*- 
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Apellido.\t | {apellido} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
          #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
      #Si la condicion Falla.           
          else:
          #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
              centinela = None          
      centinela = None
  
      #Inicio el ciclo quinto.
      while(centinela == None):
      #Inicio el ciclo secundario.
          fecha = input("Cual es su fecha de nacimiento?\t (AAAA-MM-DD)\n  => ")
          os.system ("clear")
          try:
            fecha1 = datetime.strptime(fecha, '%Y-%m-%d').date()
            #Condicion de prueba para y
            if len(fecha)<=10:
            #Imprimo un mensaje de prueba.
                print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
    | Tipo de Doc.\t | {tipo_doc} | 
    -*-*-*-*-*-*-*-*-*-*-*-  
    | Numero de Doc.\t | {numero_doc} | 
    -*-*-*-*-*-*-*-*-*-*-*-
    | Nombre.\t\ | {nombre} | 
    -*-*-*-*-*-*-*-*-*-*-*-
    | Apellido.\t | {apellido} | 
    -*-*-*-*-*-*-*-*-*-*-*-
    | Fecha de Nacimiento.\t | {fecha1} | 
    -*-*-*-*-*-*-*-*-*-*-*-\n""")
          except ValueError :
            os.system ("clear")
            print(fecha)
            print("Error: Dato incorrecto.\n")
            centinela = None
          #Cambio el centinela para que salga de el ciclo secundario.
          else:
            centinela = True
      centinela = None
    
      #Inicio el ciclo sexto.
      while(centinela == None):
          #Defino x(str) con un input.
          rh_gs = input('Cual es tu tipo sangre (O,A,B) y RH (+,-)\n  => ').upper()
          os.system ("clear")
          #Condicion de prueba para x
          if (rh_gs[0]=="O" or rh_gs[0]=="A" or rh_gs[0]=="B")and(rh_gs[1] == "+" or rh_gs[1] == "-"):
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Apellido.\t | {apellido} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Fecha de Nacimiento.\t | {fecha1} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Tipo de sangre.\t | {rh_gs[0]} {rh_gs[1]} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
            
              #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
          #Si la condicion Falla.
          else:
              #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
      #Cambio el estado de centinela para salir al segundo ciclo.        
      centinela = None
  
      #Inicio el ciclo primero.
      while(centinela == None):
          #Defino x(str) con un input.
          correo = input('Cual es tu correo electronico\n  => ')
          os.system ("clear")
          #Condicion de prueba para x
          if (
            len(correo)<=50 and
            re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,3}$',correo.lower())
          ):
              
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Apellido.\t | {apellido} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Fecha de Nacimiento.\t | {fecha1} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Tipo de sangre.\t | {rh_gs[0]} {rh_gs[1]} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Correo.\t | {correo} | 
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
  
            
              #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
          #Si la condicion Falla.
          else:
              #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
      #Cambio el estado de centinela para salir al segundo ciclo.        
      centinela = None
  
      while(centinela == None):
          #Defino x(str) con un input.
          numero_tel = input('Cual es tu número de telefono?\t \n  => ').upper()
          os.system ("clear")
          #Condicion de prueba para x
          if (len(numero_tel) <11 and numero_tel.isnumeric()):
              #Imprimo un mensaje solicitando los datos al usuario.
              print(f"""\n-*-*-*-*-*-*-*-*-*-*-*-  
  | Tipo de Doc.\t | {tipo_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-  
  | Numero de Doc.\t | {numero_doc} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Nombre.\t | {nombre} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Apellido.\t | {apellido} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Fecha de Nacimiento.\t | {fecha1} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Tipo de sangre.\t | {rh_gs[0]} {rh_gs[1]} | 
  -*-*-*-*-*-*-*-*-*-*-*-
  | Correo.\t | {correo} |
  -*-*-*-*-*-*-*-*-*-*-*-
  | número.\t | {numero_tel} |                  
  -*-*-*-*-*-*-*-*-*-*-*-\n""")
            
              #Cambio el centinela para que salga de el ciclo secundario.
              centinela = True
          #Si la condicion Falla.
          else:
              #Imprimo mensaje de Error.
              os.system ("clear")
              print("Error: Dato incorrecto.\n")
      #Cambio el estado de centinela para salir al segundo ciclo.        
      centinela = None
  
    
  #Mensaje de salida o reinicio de sisitema
      continuar = input("Desea iniciar de nuevo?\t (Si = 1, Salir = Enter.)\n  => ")
      if continuar == 1:
          centinela = None
      else:
          print("Finalizado")