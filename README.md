# Problema de los filosofos

Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando. Cada filósofo tiene un plato de fideos y un tenedor a la izquierda de su plato. Para comer los fideos son necesarios dos tenedores y cada filósofo sólo puede tomar los que están a su izquierda y derecha. Si cualquier filósofo toma un tenedor y el otro está ocupado, se quedará esperando, con el tenedor en la mano, hasta que pueda tomar el otro tenedor, para luego empezar a comer. 

Si dos filósofos adyacentes intentan tomar el mismo tenedor a una vez, se produce una condición de carrera: ambos compiten por tomar el mismo tenedor, y uno de ellos se queda sin comer. 

Si todos los filósofos toman el tenedor que está a su derecha al mismo tiempo, entonces todos se quedarán esperando eternamente, porque alguien debe liberar el tenedor que les falta. Nadie lo hará porque todos se encuentran en la misma situación (esperando que alguno deje sus tenedores). Entonces los filósofos se morirán de hambre. Este bloqueo mutuo se denomina interbloqueo o deadlock. 

# Diagrama de flujo
![Sin título_0](https://user-images.githubusercontent.com/107761268/228698071-194eace6-e373-4b5a-99fb-2331b7bf2ed9.jpg)

# Codigo de python que utilize 

````
import threading
import time
import random

NUM_FILOSOFOS = 5
TIEMPO_MAX_PENSAR = 5
TIEMPO_MAX_COMER = 3
MAX_TIEMPO_ESPERA = 1

class MonitorComedor:
    def __init__(self):
        self.tenedores = [threading.Condition() for i in range(NUM_FILOSOFOS)]
        self.filosofos = [False] * NUM_FILOSOFOS
    
    def puede_comer(self, filosofo):
        tenedor_izq = filosofo
        tenedor_der = (filosofo + 1) % NUM_FILOSOFOS
        
        if self.filosofos[tenedor_izq] or self.filosofos[tenedor_der]:
            return False
        else:
            self.filosofos[filosofo] = True
            self.tenedores[tenedor_izq].acquire()
            self.tenedores[tenedor_der].acquire()
            return True
        
    def termino_de_comer(self, filosofo):
        tenedor_izq = filosofo
        tenedor_der = (filosofo + 1) % NUM_FILOSOFOS
        
        self.tenedores[tenedor_izq].release()
        self.tenedores[tenedor_der].release()
        self.filosofos[filosofo] = False

class Filosofo(threading.Thread):
    def __init__(self, filosofo, monitor):
        threading.Thread.__init__(self)
        self.filosofo = filosofo
        self.monitor = monitor
    
    def run(self):
        while True:
            print(f"Filósofo {self.filosofo} está pensando...")
            time.sleep(random.randint(0, TIEMPO_MAX_PENSAR))
            print(f"Filósofo {self.filosofo} quiere comer...")
            
            if not self.monitor.puede_comer(self.filosofo):
                print(f"Filósofo {self.filosofo} está esperando...")
                time.sleep(random.randint(0, MAX_TIEMPO_ESPERA))
            else:
                print(f"Filósofo {self.filosofo} está comiendo...")
                time.sleep(random.randint(0, TIEMPO_MAX_COMER))
                self.monitor.termino_de_comer(self.filosofo)

if __name__ == "__main__":
    monitor = MonitorComedor()
    filosofos = [Filosofo(i, monitor) for i in range(NUM_FILOSOFOS)]
    
    for filosofo in filosofos:
        filosofo.start()
````

# Video explicativo

[HACCER CLIC PARA VER EL VIDEO](https://drive.google.com/file/d/14dmi6Mp9eX1Egxsz54oLHqL7pYGrzVdV/view?usp=sharing)

# Investigancion
![](https://user-images.githubusercontent.com/107761268/226145345-714825c7-9a2c-4776-856a-518e4a353e2a.png)

## Temas


- [Concurrencia](Concurrencia.md)
- [Paralelismo vs Concurrencia en informática](Paralelismo_vs_Concurrencia.md)
- [Hilos implementación en Python](hilos_implementación_en_python.md)
- [Deadlock](deadlock.md)
- [Exclusión mutual](exclusión_mutual.md)
- [Mantenga y espere](mantenga_&_espere.md)
- [No preventivo](no_preventivo.md)
- [Espera circular](espera_circular.md)
- [Como manejar el interbloque en sistemas operativos – Compara con el problema de los filósofos](manejo_interbloqueo.md)

# Precentación

Nombre: Esteban Pacheco

Matricula: 2021-1076

