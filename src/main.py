import os
from typing import Any
from arguments import read_arguments
from obj.Sender import Sender
from obj.Receiver import Receiver
from obj.Transmitter import Transmitter

def start(args:dict[str, Any]):
    os.system('cls' if os.name == 'nt' else 'clear')

    length:int = args['length']
    noise:float = args['noise']
    amount:int = args['amount']

    sender = Sender(amount, length)
    receiver = Receiver()
    transmitter = Transmitter(noise, sender, receiver)

    transmitter.transmit()
    results = transmitter.statuses
    
    print('--------------')

    exists = os.path.exists('results.csv')
    with open('results.csv', 'a') as f:
        if not exists:
            f.write(f'noise: {noise}\n')
            f.write(f'length: {length}\n\n')
            f.write('TN,FN,TP,FP\n')

        for i, res in enumerate(results):
            status = results[res]
            last_it = i == len(results)-1
            f.write(str(status['value']) + ('\n' if last_it else ','))
            print(status['name'] + ':\t', status['value'], '\t- ' + status['info'], end=('\r' if last_it else '\n'))

    print()
    print()
    if args['repeat'] == 1:
        if args['show']:
            print('Powtorzenia: ')
            print([signal.repeat_count for signal in sender.signals], end='\n\n')

        print('Dlugosc sygnalow:  ', length)
        print('Ilosc sygnalow:    ', amount)
        print('Moc szumu:         ', noise, end='\n\n')

if __name__ == '__main__':
    default_length = 10     # domyslna dlugosc sygnalu jezeli nie ma argumentu --length
    default_amount = 100    # domyslna ilosc sygnalow do wyslania
    default_noise = 0.05    # domyslna sila szumu jezeli nie ma argumentu --noise
    default_repeat = 100    # domyslna ilosc powtorzen symulacji

    args = read_arguments(default_length, default_amount, default_noise, default_repeat)

    for r in range(args['repeat']):
        start(args)