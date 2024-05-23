# Librería Threading

<p align="center">
  <img src="thread.png">
</p>

Los hilos nos permiten aprovechar las capacidades multiprocesador de nuestras máquinas para ejecutar varias instrucciones a la vez, como subprocesos independientes.



## Lo más importante

1.  threading.Thread():

    Crea un nuevo hilo de ejecución. Permite especificar la función a ejecutar y los argumentos de esa función.

2.  threading.Lock():

    Crea un objeto de bloqueo. Los bloqueos se utilizan para asegurar que solo un hilo acceda a una sección crítica del código a la vez.

3.  threading.Event():

    Crea un objeto de evento. Los eventos se utilizan para la comunicación entre hilos, permitiendo a un hilo esperar a que otro hilo le notifique.

4.  threading.current_thread():

    Devuelve el objeto del hilo actual, permitiendo acceder a sus atributos y métodos.

5.  threading.Timer():

    Crea un temporizador que ejecuta una función después de un tiempo especificado.

6.  threading.RLock:

    Crea un bloqueo reentrante. A diferencia de un bloqueo normal, un RLock puede ser adquirido varias veces por el mismo hilo.

<br>
<br>
<br>

### Todo el contenido

threading.active_count <br>
threading.Condition <br>
threading.current_thread <br>
threading.enumerate <br>
threading.Event <br>
threading.get_ident <br>
threading.get_native_id <br>
threading.local <br>
threading.Lock <br>
threading.main_thread <br>
threading.RLock <br>
threading.Semaphore <br>
threading.BoundedSemaphore <br>
threading.setprofile <br>
threading.settrace <br>
threading.stack_size <br>
threading.Thread <br>
threading.TIMEOUT_MAX <br>
threading.Timer <br>
threading.Barrier <br>
threading.BrokenBarrierError <br>
threading.wait <br>
threading.excepthook <br>
threading.TIMEOUT_MAX <br>
threading.ThreadError <br>
threading.thread_time <br>
threading.thread_time_ns <br>
threading.TIMEOUT_MAX <br>
threading.LockType <br>
threading.Thread.setName <br>
threading.Thread.getName <br>
threading.Thread.is_alive <br>
threading.Thread.isDaemon <br>
threading.Thread.join <br>
threading.Thread.run <br>
threading.Thread.start <br>
threading.Thread.getName <br>
threading.Thread.ident <br>
threading.Thread.name <br>
threading.Thread.daemon <br>
threading.Thread.native_id <br>
threading.Thread.target <br>
threading.Thread.setName <br>
threading.Thread.getName <br>
threading.Thread.is_alive <br>
threading.Thread.isDaemon <br>
threading.Thread.join <br>
threading.Thread.run <br>
threading.Thread.start <br>
threading.Thread.getName <br>
threading.Thread.ident <br>
threading.Thread.name <br>
threading.Thread.daemon <br>
threading.Thread.native_id <br>
threading.Thread.target <br>
threading.Lock.acquire <br>
threading.Lock.release <br>
threading.Lock.locked <br>
threading.RLock.acquire <br>
threading.RLock.release <br>
threading.RLock.locked <br>
threading.RLock._acquire_restore <br>
threading.RLock._is_owned <br>
threading.RLock._release_save <br>
threading.Condition.acquire <br>
threading.Condition.release <br>
threading.Condition.wait <br>
threading.Condition.notify <br>
threading.Condition.notify_all <br>
threading.Condition.wait_for <br>
threading.Event.clear <br>
threading.Event.is_set <br>
threading.Event.set <br>
threading.Event.wait <br>
threading.Semaphore.acquire <br>
threading.Semaphore.release <br>
threading.BoundedSemaphore.acquire <br>
threading.BoundedSemaphore.release <br>
threading.Barrier.abort <br>
threading.Barrier.reset <br>
threading.Barrier.wait <br>
threading.local.__getattribute__ <br>
threading.local.__setattr__ <br>
threading.local.__delattr__ <br>
threading.local.__dict__ <br>
threading.main_thread <br>
threading.get_native_id <br>
threading.excepthook <br>
threading.setprofile <br>
threading.settrace <br>
threading.stack_size <br>
threading.TIMEOUT_MAX <br>
threading.TIMEOUT_MAX <br>
threading._after_fork <br>
threading._enumerate <br>
threading._active <br>
threading._pickled_thread <br>
threading._pickled_main_thread <br>
threading._register_at_fork <br>
threading._shutdown <br>
threading._start_new_thread <br>
threading._terminate <br>
threading._timer <br>
threading._unwind_forked <br>
threading._unwind_defer <br>
threading._warnings <br>
threading._WeakSet <br>
threading._time <br>
threading._state_lock <br>
threading._bootstrap <br>
threading._bootstrap_inner <br>
threading._delete <br>
threading._finish <br>
threading._initialized <br>
threading._interpreter_lock <br>
threading._lock <br>
threading._note <br>
threading._profile_hook <br>
threading._sys <br>
threading._thread <br>
threading._thread_time <br>
threading._trace_hook <br>
threading._traceback <br>
threading._warn <br>
threading._warn_unclosed_file <br>
threading._warn_unclosed_socket <br>
threading._warn_unclosed_files <br>
threading._warn_unclosed_sockets <br>
threading._wrapper <br>
threading.__all__ <br>
threading.__builtins__ <br>
threading.__cached__ <br>
threading.__doc__ <br>
threading.__file__ <br>
threading.__loader__ <br>
threading.__name__ <br>
threading.__package__ <br>
threading.__spec__ <br>
threading.__warn__ <br>
threading.__warnings__ <br>
threading.__warningregistry__ <br>
threading.__traceback__ <br>
threading.__traceback_limit__ <br>
threading.__exit__ <br>
threading.__enter__ <br>
threading.__init__ <br>
threading.__main__ <br>
threading.__message__ <br>
threading.__stderr__ <br>
threading.__stderr__ <br>