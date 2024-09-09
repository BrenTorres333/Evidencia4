class Ventilador:
    def __init__(self):
            
            self.velocidades = {
            0: {'potencia': '0 W', 'consumo de energia':'1 hora' ,'rpm': 700 },
            1: {'potencia': '20 W', 'consumo de energia':'1 hora' ,'rpm': 700},# Velocidad Baja
            2: {'potencia': '35 W', 'consumo de energia':'1 hora', 'rpm': 1100}, # Velocidad Media
            3: {'potencia': '75 W', 'consumo de energia':'1 hora' ,'rpm': 1750}   # Velocidad Alta
            
            }
            self.estados = {
            0: 'El ventilador se encuentra apagado',
            1: 'El ventilador se encendio y esta funcionando a una velocidad baja',
            2: 'Velocidad Media',
            3: 'Velocidad Alta'

            }

            self.estado = 0       

    """Encender el ventilador , y colocarlo en la velocidad mas baja"""
    def encender(self):
    
        self.estado = 1
        return self.estados[self.estado]

    def __str__(self):
        return self.estados.get(self.estado)


    """Realizar un cambio de velocidad de 1 a 3"""
    def cambiar_velocidad(self, nueva_velocidad):
        acciones = {
            velocidad: f"Velocidad ajustada a {velocidad}: potencia={datos['potencia']} por hora, rpm={datos['rpm']}"
            for velocidad, datos in self.velocidades.items()
        }

        self.estado = nueva_velocidad
        return acciones.get(nueva_velocidad)

    def __str__(self):
        return self.estados.get(self.estado)

    """Calcular el consumo de energia por cantidad de horas"""
    def consumo_energia(self, velocidad, horas):
        consumo_por_hora_str = self.velocidades.get(velocidad, {'potencia': '0 W'}).get('potencia', '0 W')
        potencia = float(consumo_por_hora_str.replace(' W', ''))  # Convertir potencia a número
        
        
        consumo_total = potencia * horas
        return f"Consumo de energia en velocidad {velocidad} durante {horas} horas: {int(consumo_total)} W"





mi_ventilador = Ventilador()

print("Estado inicial:")
print(mi_ventilador) 

print("\nCambio de estado:")
print(mi_ventilador.encender()) 

print("\nCambio de velocidad:")
print(mi_ventilador.cambiar_velocidad(3))

print("\nConsumo de energia:")
print(mi_ventilador.consumo_energia(3, 2))