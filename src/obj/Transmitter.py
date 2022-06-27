import random
from obj.Signal import Signal
from obj.Sender import Sender
from obj.Receiver import Receiver

class Transmitter():
    def __init__(self, noise_strength:float, sender:Sender, receiver:Receiver):
        self.noise_strength = noise_strength
        self.sender = sender
        self.receiver = receiver
        self.statuses = {
            'true_negative': {
                'name': 'True Negative',
                'info': 'Faktycznie nie ma bledu',
                'value': 0,
            },
            'false_negative': {
                'name': 'False Negative',
                'info': 'Blad wystapil ale nie zostal wykryty (zmiana 2n bitow)',
                'value': 0
            },
            'true_positive': {
                'name': 'True Positive',
                'info': 'Blad wystapil i zostal wykryty',
                'value': 0
            },
            'false_positive': {
                'name': 'False Positive',
                'info': 'Wykryty zostal blad ktory nie wystapil (zmiana bitu kontrolnego)',
                'value': 0
            },
        }
    
    def transmit(self) -> None:
        for signal in self.sender.send():            
            parity_check = False
            while(not parity_check):                                        # wysylanie do skutku
                noised_signal = self.get_noised_signal(signal)              # tablica z sygnalem po przejsciu przez szum

                parity_check = self.receiver.receive(noised_signal)         # wartosc logiczna jako wynik sprawdzenia parzystosci sygnalu
                content_check = signal.control[:-1] == noised_signal[:-1]   # wartosc logicnza jako wynik sprawdzenia zawartosci sygnalu
                
                self.check_status(parity_check, content_check)              # zapisanie statusu sygnalu

                if not parity_check:
                    signal.was_repeated()

    def check_status(self, parity_check:bool, content_check:bool) -> None:
        if parity_check and content_check:
            self.statuses['true_negative']['value'] += 1

        if parity_check and not content_check:
            self.statuses['false_negative']['value'] += 1

        if not parity_check and not content_check:
            self.statuses['true_positive']['value'] += 1

        if not parity_check and content_check:
            self.statuses['false_positive']['value'] += 1

    def get_noised_signal(self, signal:Signal) -> list[int]:
        return [
            int(not bit) if random.random() <= self.noise_strength else bit
            for bit in signal.bits
        ]