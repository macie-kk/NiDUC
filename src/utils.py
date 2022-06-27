from typing import Literal

def get_control_sum(arr) -> Literal[0, 1]:
    return sum(arr) % 2