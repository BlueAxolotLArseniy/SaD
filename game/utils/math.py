import time
import game.consts as consts   # ← ОБЯЗАТЕЛЬНО

def tick_calculation(now, delta, last_time, accumulator) -> int:
    now = time.perf_counter()
    delta = now - last_time
    last_time = now
    accumulator += delta
    return now, delta, last_time, accumulator
