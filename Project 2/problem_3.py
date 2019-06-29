

class HuffmanCode:
    def __init__(self, path):
        self.path = path
        
    def make_dictionary(self):
        st = self.path
        d ={}
        for ch in st:
            d[ch]=d.get(ch,0)+1
        return d

    def build_codes(self):
        d_freq = self.make_dictionary()
        q = [(ch, count) for (ch, count) in d_freq.items()]
        while(len(q)>1):
            A, cntA = self.extract_min(q)
            B, cntB = self.extract_min(q)
            chars = [A, B]
            wt = cntA + cntB
            q.append((chars, wt))
        root, wt = self.extract_min(q)
        codebook = self.generate_codes(root, prefix = "")
        #print(codebook)
        return codebook
    
    def generate_codes(self, huffman_tree, prefix = ""):
        if isinstance(huffman_tree, str):
            return ({huffman_tree:prefix})
        lchild, rchild = huffman_tree[0],  huffman_tree[1]
        codebook = {}
        codebook.update(self.generate_codes(lchild , prefix + "0"))
        codebook.update(self.generate_codes(rchild , prefix + "1"))
        return codebook

    def extract_min(self, q):
        min_pair = q[0]
        for pair in q:
            if pair[1]<min_pair[1]:
                min_pair = pair
        q.remove(min_pair)
        return (min_pair)
    
    def compress(self):
        codebook = self.build_codes()
        print(codebook)
        bits = ""
        for ch in self.path:
            bits += codebook[ch]
        return bits
    
    def reverse_dict(self):
        d = self.build_codes()
        return {y:x for (x, y) in d.items()}

    def decode(self, bits):
        rev_dict = self.reverse_dict()
        #print(rev_dict)
        prefix = ""
        result = []
        for bit in bits:
            prefix += bit
            if prefix in rev_dict:
                result.append(rev_dict[prefix])
                prefix = ""
        assert prefix == ""
        return("".join(result))

#Test case 1
s = HuffmanCode("aaabccdeeeeeffg")
bits = s.compress()
print(bits)
print(s.decode(bits))
"""output
{'a': '00', 'g': '010', 'c': '011', 'f': '100', 'b': '1010', 'd': '1011', 'e': '11'}
000000101001101110111111111111100100010
aaabccdeeeeeffg"""

#Test case 2

s = HuffmanCode("The bird is the word")
bits = s.compress()
print(bits)
print(s.decode(bits))

"""output
{'i': '000', 'r': '001', 'd': '010', 'T': '0110', 'b': '0111', 's': '1000', 't': '1001', 'w': '1010', 'o': '1011', ' ': '110', 'h': '
1110', 'e': '1111'}
0110111011111100111000001010110000100011010011110111111010101011001010
The bird is the word"""

#Test Case 3

s = HuffmanCode("aaaaaaaan")
bits = s.compress()
print(bits)
print(s.decode(bits))

"""
{'n': '0', 'a': '1'}
111111110
aaaaaaaan
"""