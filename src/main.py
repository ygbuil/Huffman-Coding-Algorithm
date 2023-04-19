# local libraries
import objects.objects as o


def main(s):
    '''
    Generates the Huffman tree for the given string, encodes it to binary, and
    decodes it again to the original string.

    Parameters
    ----------
    s : str
        String to encode.

    Returns
    -------
    encoded_s : str
        String encoded as a binary.
    decoded_s : str
        Decoded (original) string.

    '''

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
