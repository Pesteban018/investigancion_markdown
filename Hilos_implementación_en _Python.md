#Hilos implementación en Python

 [hilos](https://i.imgur.com/Mb5ZYbT.jpg)
 
 ### Que son los hilos?

Un hilo es un proceso del sistema operativo con características distintas de las de un proceso normal: Los hilos existen como subconjuntos de los procesos. Los hilos comparten memoria y recursos


Los hilos nos permiten aprovechar las capacidades multiprocesador de nuestras máquinas para ejecutar varias instrucciones a la vez, como subprocesos independientes.


## Hilos implementación en Python
En Python, los hilos se pueden implementar utilizando la biblioteca estándar **threading**. La biblioteca threading proporciona un conjunto de herramientas para crear y administrar hilos en un programa Python.

Para crear un hilo en Python, primero debe definir una función que represente la tarea que desea realizar en paralelo. Luego, puede crear una instancia de la clase **Thread** en la biblioteca threading y proporcionar la función como argumento. A continuación, puede iniciar el hilo utilizando el método start().

Aquí hay un ejemplo de cómo implementar hilos en Python usando la biblioteca threading:

````
import threading

def tarea():
    print("Hola, estoy corriendo en un hilo")

hilo = threading.Thread(target=tarea)

hilo.start()
hilo.join()

````

En este ejemplo, se define una función **tarea()** que simplemente imprime un mensaje en la consola. Luego, se crea una instancia de la clase **Thread** y se proporciona la función como argumento. Finalmente, se inicia el hilo utilizando el método **start()** y se espera a que el hilo termine utilizando el método **join()**. Después de que el hilo termina su tarea, se imprime un mensaje en la consola.
