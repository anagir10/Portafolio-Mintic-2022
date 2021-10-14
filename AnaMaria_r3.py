datos_clientes = [
    {'codigo':'010010','nom':'Juan Pérez','dir':'cr 30 25 80','zona':1,'sensores':7},
    {'codigo':'020008','nom':'Carolina Charris','dir':'cr 84 70 27 Bod 4','zona':2,'sensores':5},
    {'codigo':'030011','nom':'Juan Pérez','dir':'cr 30 10 80','zona':3,'sensores':5},
    {'codigo':'020114','nom':'Omar Acosta','dir':'cr 30 25 80','zona':2,'sensores':5},
    {'codigo':'020115','nom':'Camilo Fernández','dir':'cr 30 25 80','zona':2,'sensores':5},
    {'codigo':'010020','nom':'Juan Pérez','dir':'cr 30 15 80','zona':1,'sensores':8}
]

def monitoreo(codigo:str,sensores:tuple)->list:
    if sensores.count(1) == 0:
        Salida = [{}]
    else:
        for x in datos_clientes:
            if codigo == x['codigo']:
                if len(sensores) != x['sensores']:
                    alarma = 'revisar'
                else:
                    alarma = 'correcto'
                if 'zona' == 1:
                    Num_guardias = '3 guardias'
                else:
                    Num_guardias = '2 guardias'
                Salida =[{'codigo_cliente': x['codigo'], 'direccion': x['dir'],  'cantidad_guardias':Num_guardias, 'sensores_activos':sensores.count(1), 'estado_sensores': alarma}]
    return Salida

print(monitoreo('020114',(0,0,1,0,0)))
print(monitoreo('010010',(0,0,0,0,0)))
print(monitoreo('020115',(0,0,1,1,1)))
print(monitoreo('010020',(1,0,1,0,0)))
