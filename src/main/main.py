# libraries
import os
import sys
from pathlib import Path

# root path
path = Path('C:/Users/llorenc.buil/github/Huffman-Coding-Algorithm')
sys.path.append(path) if path not in sys.path else None
os.chdir(path)

# local libraries
import src.objects.objects as o


def main(s):
    queue = o.get_character_frequency(s)

    tree = o.generate_tree(queue=queue)

    dict_encoding = o.find_encoding_in_tree(tree=tree, queue=queue)

    encoded_s = o.encode_string(s=s, dict_encoding=dict_encoding)

    decoded_s = o.decode_string(
        encoded_s=encoded_s, dict_encoding=dict_encoding
    )

    return encoded_s, decoded_s


if __name__ == '__main__':
    encoded_s, decoded_s = main(s='HELLO WORLD!')
