import utils
import random
from typing import Generator
from obj.Signal import Signal

class Sender:
    def __init__(self, total_signals:int, signal_length:int):
        self.signals:list[Signal] = [self.generate_signal(signal_length) for i in range(total_signals)]
        
    def send(self) -> Generator[Signal, None, None]:
        for signal in self.signals:
            yield signal

    def generate_signal(self, n:int) -> list[Signal]:
        arr = [random.getrandbits(1) for i in range(n)]     # generowanie n losowych bitow
        arr.append(utils.get_control_sum(arr))              # dodanie bitu parzystosci
        return Signal(arr)