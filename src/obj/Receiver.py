import utils

class Receiver:
    def __init__(self):
        pass

    def receive(self, bits:list[int]) -> bool:
        return utils.get_control_sum(bits[:-1]) == bits[-1]
