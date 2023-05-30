from heapq import heappop, heappush
from collections import defaultdict

class Codec:
    base_url = "http://tinyurl.com/"

    def __init__(self):
        self.url_map = {}
        self.huffman_tree = None

    def build_huffman_tree(self, freq_map):
        heap = [[weight, [char, ""]] for char, weight in freq_map.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return heap[0]

    def get_char_frequencies(self, string):
        freq_map = defaultdict(int)
        for char in string:
            freq_map[char] += 1
        freq_map['$'] = 1
        return freq_map

    def generate_encoding_map(self, node, encoding_map, prefix=""):
        if len(node) == 2:
            encoding_map[node[1]] = prefix
        else:
            self.generate_encoding_map(node[1], encoding_map, prefix + "0")
            self.generate_encoding_map(node[2], encoding_map, prefix + "1")

    def encode(self, longUrl: str) -> str:
        freq_map = self.get_char_frequencies(longUrl)
        self.huffman_tree = self.build_huffman_tree(freq_map)
        encoding_map = {}
        self.generate_encoding_map(self.huffman_tree, encoding_map)
        encoded_url = "".join(encoding_map.get(char, '') for char in longUrl)
        self.url_map[encoded_url] = longUrl
        return Codec.base_url + encoded_url

    def decode(self, shortUrl: str) -> str:
        encoded_url = shortUrl.replace(Codec.base_url, "")
        longUrl = self.url_map[encoded_url]
        return longUrl
