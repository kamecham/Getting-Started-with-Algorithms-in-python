""" Euclid's reciprocal division method """
#ユークリッド互除法

DATA_1 = 36
DATA_2 = 124

def euclid_func(data_1, data_2):
    """
    A function that performs Euclid's reciprocal division method.
    Returns the greatest common divisor of the two arguments.
    """
    if data_1 < data_2:
        data_1, data_2 = data_2, data_1
    while 1:
        amari = data_1 % data_2
        if amari == 0:
            return_value = data_2
            break
        data_1, data_2 = data_2, amari
    return return_value


print(euclid_func(DATA_1, DATA_2))
