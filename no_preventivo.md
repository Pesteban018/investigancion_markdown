# No preventivo

![no](https://dirigentesdigital.com/multimedia/img/big/desarrollosoftware_41-116547_20190111134203.jpg)

En el contexto de la programación concurrente, "no preventivo" se refiere a un modelo en el que el sistema operativo o el lenguaje de programación no interrumpen automáticamente los procesos o hilos de ejecución en un momento determinado. En otras palabras, los procesos o hilos no son "prevenidos" de ejecutar indefinidamente sin dar paso a otros procesos.

En un modelo no preventivo, los procesos o hilos deben cooperar explícitamente para permitir que otros procesos o hilos obtengan acceso a los recursos compartidos y evitar bloqueos o deadlocks. Los procesos o hilos pueden suspenderse o ponerse en espera explícitamente para esperar a que otros procesos completen sus operaciones.

El modelo no preventivo se utiliza en muchos sistemas de tiempo real y en sistemas operativos en tiempo compartido, donde se prefiere maximizar la eficiencia del sistema y minimizar la sobrecarga de conmutación de contexto. Sin embargo, el modelo no preventivo también puede ser más difícil de programar y depurar, ya que los procesos o hilos deben cooperar explícitamente para evitar problemas de sincronización y exclusión mutua.

Por otro lado, el modelo preventivo, también conocido como modelo de planificación de tiempo compartido, utiliza una política de planificación en la que el sistema operativo interrumpe automáticamente los procesos o hilos en momentos determinados, llamados "quantum" o "tiempo de rebanada". Esta política de planificación se utiliza en sistemas operativos de uso general como Windows y Linux, donde la prioridad y la justicia son factores importantes.
