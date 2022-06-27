from argparse import ArgumentParser, ArgumentTypeError
from typing import Union

# only allow positive length value
def check_positive(value) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise ArgumentTypeError('Length value must be positive')
    return ivalue

# only allow noise value from range [0-1]
def check_noise(value) -> float:
    fvalue = float(value)
    if fvalue < 0 or fvalue > 1:
        raise ArgumentTypeError('Noise value must be from range [0-1]')
    return fvalue

# add and read all arguments
def read_arguments(default_length: int, default_amount:int, default_noise: float, default_repeat: int) -> dict[str, Union[int, float]]:
    parser = ArgumentParser()
    parser.add_argument('-l', '--length', type=check_positive, default=[default_length], nargs=1, help='Specify signal length')
    parser.add_argument('-a', '--amount', type=check_positive, default=[default_amount], nargs=1, help='Specify amount of signals to be sent')
    parser.add_argument('-n', '--noise', type=check_noise, default=[default_noise], nargs=1, help='Specify noise strength [0-1]')
    parser.add_argument('-s', '--show', action='store_true', help='Show retries for each signal')
    parser.add_argument('-r', '--repeat', type=check_positive, default=[default_repeat], nargs=1, help='Specify amount of times to repeat the simulation')

    parsed = parser.parse_args()
    return {
        'length':   parsed.length[0],
        'noise':    parsed.noise[0],
        'amount':   parsed.amount[0],
        'show':     parsed.show,
        'repeat':   parsed.repeat[0]
    }