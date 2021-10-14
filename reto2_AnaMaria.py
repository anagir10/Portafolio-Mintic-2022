def estado_nivel(datos_tanque:dict)->dict:
    if (datos_tanque["sensor1"]==True and datos_tanque["sensor2"]== True and datos_tanque["sensor3"]==False):
        nivel="nivel medio"
        dicsalida={"codigoTanque":datos_tanque["codigo"],"nivel":nivel
        }
    else: 
        if(datos_tanque["sensor1"]==False and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
            nivel="vacío"
            dicsalida={ "codigo_tanque":datos_tanque["codigo"],"nivel":nivel
            }
        else:
         if(datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
            nivel="nivelbajo"
            dicsalida={"codigoTanque":datos_tanque["codigo"],"nivel":nivel
            }
         else:
          if(datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==True and datos_tanque["sensor3"]==True):
            nivel="nivel alto"
            dicsalida= {"codigoTanque":datos_tanque["codigo"],"nivel":nivel
            }
          else:
             nivel="revisar sensores"
            
def estado_nivel(datos_tanque:dict)->dict:
    if (datos_tanque["sensor1"]==True and datos_tanque["sensor2"]== True and datos_tanque["sensor3"]==False):
        nivel="nivel medio"
        dicsalida={'codigoTanque':datos_tanque["codigo"],'nivel':nivel}
    else: 
        if(datos_tanque["sensor1"]==False and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
            nivel="vacío"
            dicsalida={'codigoTanque':datos_tanque["codigo"],'nivel':nivel}
        else:
            if(datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==False and datos_tanque["sensor3"]==False):
                nivel="nivel bajo"
                dicsalida={'codigoTanque':datos_tanque["codigo"],'nivel':nivel}
            else:
                if(datos_tanque["sensor1"]==True and datos_tanque["sensor2"]==True and datos_tanque["sensor3"]==True):
                    nivel="nivel alto"
                    dicsalida={'codigoTanque':datos_tanque["codigo"],'nivel':nivel}
                else:
                    nivel="revisar sensores"
                    dicsalida={'codigoTanque':datos_tanque["codigo"],'nivel':nivel}
    
    return f"Estado del nivel del líquido del tanque {dicsalida['codigoTanque']}: {dicsalida['nivel']}"
                
datos_tanque = {'codigo': 'TA001',
                'sensor1': True,
                'sensor2': True,
                'sensor3': False
                }               
#print (estado_nivel(datos_tanque))

print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = False)))
