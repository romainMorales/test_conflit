import string
import pandas as pd

alphabet = string.ascii_lowercase
lst_id = range(1, len(alphabet) + 1, 1)

dict_alphabet = {key:value for key, value in zip(lst_id, alphabet)}
print(dict_alphabet)



