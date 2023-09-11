# utils.py

class utils:

    def reversed(x):
        num_string = str(x)
        return int(num_string[::-1]) if num_string.isdigit() else "ERROR: Input must be an int."

    def formatter(x): 
        if str(x).isdigit():
            return bin(x), oct(x)
        else:
            return "ERROR: Input must be an int."
