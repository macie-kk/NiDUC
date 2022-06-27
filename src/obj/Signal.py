import utils

class Signal:
    def __init__(self, bits:list[int]):
        self.bits = self.control = bits
        self.repeat_count:int = 0

    def was_repeated(self) -> None:
        self.repeat_count += 1
    
    def verify(self) -> dict[str, bool]:
        parity_check = utils.get_control_sum(self.bits[:-1]) == self.bits[-1]
        content_check = self.control[:-1] == self.bits[:-1]

        return {
            'parity_check': parity_check,
            'content_check': content_check
        }