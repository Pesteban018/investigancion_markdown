# Espera circular

![espera](https://i.imgur.com/8vWrNMo.png)

La espera circular es una situación en la que dos o más procesos o hilos se bloquean mutuamente, cada uno esperando que el otro libere un recurso que necesita para continuar. Esta situación puede causar un deadlock, que es un estado en el que ningún proceso puede avanzar porque están todos bloqueados esperando que se liberen los recursos que otros procesos están reteniendo.

Por ejemplo, supongamos que dos procesos, A y B, necesitan acceder a dos recursos diferentes, X e Y, respectivamente. Si el proceso A adquiere el recurso X y luego intenta adquirir el recurso Y, mientras que al mismo tiempo el proceso B adquiere el recurso Y y luego intenta adquirir el recurso X, puede ocurrir una espera circular. En este caso, tanto el proceso A como el proceso B se bloquean esperando que el otro libere el recurso que necesita para continuar.

Para evitar la espera circular y los deadlocks, es necesario utilizar técnicas de sincronización adecuadas, como exclusión mutua y espera activa. Además, es importante asegurarse de que los recursos se adquieran y liberen en el mismo orden por todos los procesos que los utilizan. De esta manera, se puede garantizar que no haya conflicto en el acceso a los recursos y se pueden evitar las situaciones de espera circular.
