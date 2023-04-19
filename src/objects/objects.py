# libraries
from copy import deepcopy


class Node:
    '''
    Node of a tree.

    Attributes
    ----------
    val : any
        Node value.
    l : any
        Left leave value.
    r : any
        Right leave value.

    '''

    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


def get_character_frequency(s):
    '''
    Get the frequency of occurance of each character and return it in
    descending order.

    Parameters
    ----------
    s : str
        String to encode.

    Returns
    -------
    queue : list
        List of tupples containing the frequency of occurance of each
        character.

    '''

    queue = {}

    for letter in s:
        if letter in queue:
            queue[letter] += 1
        else:
            queue[letter] = 1

    queue = sorted(queue.items(), key=lambda x: x[1], reverse=True)

    return queue


def generate_tree(queue):
    '''
    Generate Huffman tree.

    Parameters
    ----------
    queue : list
        List of tupples containing the frequency of occurance of each
        character.

    Returns
    -------
    curr : class
        Root node of the Huffman tree.

    '''

    queue_copy = queue.copy()

    while len(queue_copy) > 1:
        # init Node
        curr = Node(val=None)

        # add last element of the queue to the left branch and second last
        # element to the right branch. If the queue element is already a Node,
        # it is added straight forward. If it is a character, a Node is created
        curr.l = (
            Node(val=queue_copy.pop()) if type(queue_copy[-1][0]) == str
            else queue_copy.pop()[0]
        )
        curr.r = (
            Node(val=queue_copy.pop()) if type(queue_copy[-1][0]) == str
            else queue_copy.pop()[0]
        )

        # assign value of current node to:
        # (concatenation of characters of leafs,
        # sum of frequency of occurrence of leafs)
        l_char = curr.l.val[0]
        r_char = curr.r.val[0]
        l_val = curr.l.val[1]
        r_val = curr.r.val[1]
        curr.val = (l_char + r_char, l_val + r_val)

        queue_copy.append((curr, curr.val[1]))
        queue_copy = sorted(queue_copy, key=lambda x: x[1], reverse=True)

    return curr





def find_encoding_in_tree(tree, queue):
    '''
    Calculates the binary encoding for each character based on the Huffman
    tree. Each character is searched from the top to the bottom of the tree.
    Every left turn correspond to a 0 and every rigth turn corresponds to a 1.
    When the bottom of the tree is reached, the current character is encoded as
    the concatenation of all 0s and 1s encounter in the top to bottom search.

    Parameters
    ----------
    tree : class
        Root node of the Huffman tree.
    queue :  list
        List of tupples containing the frequency of occurance of each
        character.

    Returns
    -------
    dict_encoding : dict
        Key value pairs of character and encoding.

    '''

    dict_encoding = {}

    # important: the dict_encoding must contain the string characters ordered
    # by frequency in descending order (most frequent on the left and least
    # frequent on the right). This will be important when decoding. The queue
    # object is already ordered this way, so the dict_encoding will be as well.
    unique_chars = [x[0] for x in queue]

    for char in unique_chars:
        char_encoding = ''
        curr = deepcopy(tree)

        while curr.l or curr.r is not None:
            if char in curr.l.val[0]:
                curr = curr.l
                char_encoding += '0'
            elif char in curr.r.val[0]:
                curr = curr.r
                char_encoding += '1'

        dict_encoding[char] = char_encoding

    return dict_encoding


def encode_string(s, dict_encoding):
    '''
    Encode string based on the dict_encoding.

    Parameters
    ----------
    s : str
        String to encode.
    dict_encoding : dict
        Key value pairs of character and encoding.

    Returns
    -------
    encoded_s : str
        String encoded as a binary.

    '''

    encoded_s = ''

    for char in s:
        encoded_s += dict_encoding[char]

    return encoded_s


def decode_string(encoded_s, dict_encoding):
    '''
    Decodes the string from its binary form to its original string form.

    Parameters
    ----------
    encoded_s : str
        String encoded as a binary.
    dict_encoding : dict
        Key value pairs of character and encoding.

    Returns
    -------
    decoded_s : str
        Decoded (original) string.

    '''

    keys = list(dict_encoding)
    decoded_s = ''
    i = last_i = 0
    # iterate over the encoded_s bits
    #for i in range(len(encoded_s)):
    while i < len(encoded_s):
        # iterate over keys
        for key in keys:
            i = last_i
            # exit condition
            if i >= len(encoded_s):
                break
            # iterate over current key bits
            for k in range(len(dict_encoding[key])):
                if encoded_s[i] == dict_encoding[key][k]:
                    if k == len(dict_encoding[key]) - 1:
                        decoded_s += key
                        i += 1
                        last_i = i
                    i += 1
                else:
                    break

    return decoded_s
