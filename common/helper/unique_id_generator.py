import datetime as dt
import random as _r

STRING_APLHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class RandomIDNumberGenerator:
    def __init__(self):
        pass

    def generate_random_id_number(self, optional_number : int | None = None, length : int = 16, use_alphanumeric : bool = False) -> str:
        if optional_number is None:
            optional_number = _r.randint(10, 99)
        elif optional_number < 10:
            optional_number = _r.randint(10, 99)
        elif optional_number > 99:
            optional_number = str(optional_number)[:2]
        if use_alphanumeric:
            random_string = "".join(_r.choices(STRING_APLHA, k=4))
        current_time = dt.datetime.now()
        milliseconds = current_time.microsecond // 1000 
        microseconds = current_time.microsecond % 1000 
        combined_number = int(optional_number) * 1000000 + milliseconds * 1000 + microseconds
        if not use_alphanumeric:
            return str(combined_number)[:length]
        return (random_string + str(combined_number))[:length]