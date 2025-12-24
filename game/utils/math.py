import time

def tick_calculation(now, delta, last_time, accumulator):
    '''
    Расчет тиков для игры
    '''
    now = time.perf_counter()
    delta = now - last_time
    last_time = now

    accumulator += delta