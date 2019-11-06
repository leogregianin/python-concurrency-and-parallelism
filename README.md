# python-concurrency
Concurrency and parallelism in Python

> Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once. **-- Rob Pike, co-inventor da linguagem Go - Concurrency is not Parallelism (it's better)**

>Ao preparar vários pratos ao mesmo tempo o cozinheiro está trabalhando de forma concorrente, porque normalmente ele só cuida de um prato por vez, mas vários estão sendo preparados ao mesmo tempo. 
> Por outro lado, um fogão de 6 bocas permite aquecer 6 panelas em paralelo. 
> Ou seja, o cozinheiro trabalha em modo concorrente e o fogão em modo paralelo. **-- [Garoa Hacker Clube](https://garoa.net.br/wiki/Python_Concorrente)**

# Install packages

    * requests
    * asyncio
    * aiohttp


# Benchmarks

Benchmark name                       | (1)        | (2)        | (3)        | (4)
-------------------------------------|-----------:|-----------:|-----------:|-----------:
synchronous (sync.py)                | 17.366073  | 17.226306  | 15.457684  | 15.195825  
thread with 5 workers (thread.py)    |  3.248359  |  2.758202  |  1.843235  |  1.813232
thread with 50 workers (thread.py)   |  0.625699  |  0.756632  |  0.573231  |  0.587740
parallelism (multiprocess.py)        |  3.607703  |  3.317795  |  2.845974  |  2.705426 
asynchronous coroutines (async.py)   |  0.586605  |  0.609510  |  0.571612  |  0.579693

 * Time in seconds
 * (1) with Python 3.6.5
 * (2) with Python 3.6.5
 * (3) with Python 3.8.0
 * (4) with Python 3.8.0

# References

 * [en] [Coroutines and Tasks - Official Python Docs](https://docs.python.org/3/library/asyncio-task.html)
 * [en] [threading — Thread-based parallelism - Official Python Docs](https://docs.python.org/3/library/threading.html)
 * [en] [multiprocessing — Process-based parallelism - Official Python Docs](https://docs.python.org/3/library/multiprocessing.html)
 * [en] [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency)
 * [en] [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading)
 * [en] [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python)
 * [en] [AsyncIO for the Working Python Developer - Yeray Diaz](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e)
 * [pt-br] [AsyncIO - O futuro do Python mudou completamente! - Bruno Rocha](http://brunorocha.org/python/asyncio-o-futuro-do-python-mudou-completamente.html)
