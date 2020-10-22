# python-concurrency-and-parallelism
Concurrency and parallelism in Python

> Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once. **-- Rob Pike, co-inventor da linguagem Go - Concurrency is not Parallelism (it's better)**

>Ao preparar vários pratos ao mesmo tempo o cozinheiro está trabalhando de forma concorrente, porque normalmente ele só cuida de um prato por vez, mas vários estão sendo preparados ao mesmo tempo. 
> Por outro lado, um fogão de 6 bocas permite aquecer 6 panelas em paralelo. 
> Ou seja, o cozinheiro trabalha em modo concorrente e o fogão em modo paralelo. **-- [Garoa Hacker Clube](https://garoa.net.br/wiki/Python_Concorrente)**

# Install packages

    * pipenv install

    or

    * requests
    * asyncio
    * aiohttp
    * httpx


# Benchmarks

Benchmark name                       | (1)       | (2)       | (3)       | (4)       | (5)       | (6)
-------------------------------------|----------:|----------:|----------:|----------:|----------:|----------:
synchronous (sync.py)                | 17.36607  | 17.22630  | 15.45768  | 15.19582  |  5.01565  |  4.41665
thread with 5 workers (thread.py)    |  3.24835  |  2.75820  |  1.84323  |  1.81323  |  0.50936  |  0.51072
thread with 50 workers (thread.py)   |  0.62569  |  0.75663  |  0.57323  |  0.58774  |  0.29404  |  0.25039
parallelism (multiprocess.py)        |  3.60770  |  3.31779  |  2.84597  |  2.70542  |  0.37044  |  0.36182
asynchronous coroutines (async.py)   |  0.58660  |  0.60951  |  0.57161  |  0.57969  |  0.27758  |  0.23457


 * Time in seconds
 * (1) with Python 3.6.5 (win32)
 * (2) with Python 3.6.5 (win32)
 * (3) with Python 3.8.0 (win32)
 * (4) with Python 3.8.0 (win32)
 * (5) with Python 3.7.4 (linux gcc 8.3.0)
 * (6) with Python 3.7.4 (linux gcc 8.3.0)


# References

 * [en] [Coroutines and Tasks - Official Python Docs](https://docs.python.org/3/library/asyncio-task.html)
 * [en] [threading — Thread-based parallelism - Official Python Docs](https://docs.python.org/3/library/threading.html)
 * [en] [multiprocessing — Process-based parallelism - Official Python Docs](https://docs.python.org/3/library/multiprocessing.html)
 * [en] [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency)
 * [en] [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading)
 * [en] [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python)
 * [en] [AsyncIO for the Working Python Developer - Yeray Diaz](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e)
 * [pt-br] [AsyncIO - O futuro do Python mudou completamente! - Bruno Rocha](http://brunorocha.org/python/asyncio-o-futuro-do-python-mudou-completamente.html)
