## Deadlock

![deadblock](https://i.imgur.com/O76Ijev.png)

Un deadlock (o "bloqueo") se produce cuando dos o más procesos quedan bloqueados permanentemente mientras esperan uno al otro para liberar un recurso. En otras palabras, cada proceso está esperando a que el otro libere el recurso que necesita para continuar.

Un deadlock puede ocurrir en cualquier sistema que tenga recursos compartidos y múltiples procesos o hilos de ejecución que intentan acceder a ellos simultáneamente. Por ejemplo, en un sistema de bases de datos, dos transacciones pueden estar esperando mutuamente la liberación de recursos bloqueados por la otra transacción.

Los deadlocks son problemáticos porque los procesos bloqueados no pueden continuar, lo que lleva a una pérdida de tiempo y recursos del sistema. Además, si el deadlock no se resuelve automáticamente, puede causar un fallo en el sistema.

Hay varias técnicas para prevenir y resolver deadlocks, como el uso de técnicas de exclusión mutua, como semáforos y monitores, para evitar que varios procesos accedan simultáneamente a los mismos recursos. Además, los algoritmos de planificación de procesos pueden detectar y resolver los deadlocks mediante la detección de ciclos de dependencias y la liberación de recursos.
