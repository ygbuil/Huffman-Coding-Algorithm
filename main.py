from copy import deepcopy





def generate_tree(queue):
    while len(queue) > 1:
        curr = Node(val=None)
        curr.l = Node(val=queue.pop()) if type(queue[-1][0]) == str else queue.pop()[0]
        curr.r = Node(val=queue.pop()) if type(queue[-1][0]) == str else queue.pop()[0]

        l_char = curr.l.val[0]
        r_char = curr.r.val[0]
        l_val = curr.l.val[1]
        r_val = curr.r.val[1]

        curr.val = (l_char + r_char, l_val + r_val)

        queue.append((curr, curr.val[1]))
        queue = sorted(queue, key=lambda x: x[1], reverse=True)

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



def find_encoding_in_tree(tree):
    dict_encoding = {}

    unique_chars = ''.join(set(s))
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


class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None



s = 'FAAABCBA'

queue = get_character_frequency(s)

tree = generate_tree(queue=queue)

dict_encoding = find_encoding_in_tree(tree=tree)
