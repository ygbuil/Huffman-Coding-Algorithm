from copy import deepcopy


def generate_tree(queue):
    queue_aux = deepcopy(queue)

    while len(queue_aux) > 1:
        curr = Node(val=None)
        curr.l = (
            Node(val=queue_aux.pop()) if type(queue_aux[-1][0]) == str
            else queue_aux.pop()[0]
        )
        curr.r = (
            Node(val=queue_aux.pop()) if type(queue_aux[-1][0]) == str
            else queue_aux.pop()[0]
        )

        l_char = curr.l.val[0]
        r_char = curr.r.val[0]
        l_val = curr.l.val[1]
        r_val = curr.r.val[1]

        curr.val = (l_char + r_char, l_val + r_val)

        queue_aux.append((curr, curr.val[1]))
        queue_aux = sorted(queue_aux, key=lambda x: x[1], reverse=True)

    return curr


def get_character_frequency(s):
    queue = {}

    for letter in s:
        if letter in queue:
            queue[letter] += 1
        else:
            queue[letter] = 1

    queue = sorted(queue.items(), key=lambda x: x[1], reverse=True)

    return queue


def find_encoding_in_tree(tree, queue):
    dict_encoding = {}

    # important: the dict_encoding must contain the string characters ordered
    # by frequency in descending order (most frequent on the left and least
    # frequent on the right). This will be important when decoding. The queue
    # object is already ordered this way.
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
    encoded_s = ''

    for char in s:
        encoded_s += dict_encoding[char]

    return encoded_s


def decode_string(encoded_s):
    keys = list(dict_encoding)
    decoded_s = ''
    last_i = 0
    i = 0
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









class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None



s = 'AABCBAD'


queue = get_character_frequency(s)

tree = generate_tree(queue=queue)

dict_encoding = find_encoding_in_tree(tree=tree, queue=queue)

encoded_s = encode_string(s=s, dict_encoding=dict_encoding)

decoded_s = decode_string(encoded_s)
