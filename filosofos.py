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