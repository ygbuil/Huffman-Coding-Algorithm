# Huffman Coding Algorithm Implementation

This is my own implementation of the Huffman coding algorithm from scratch using plain Python with no external libraries (with the exception of the copy library, which has nothing to do with the algorithm).

## What is Huffman Coding?

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to each symbol or character in a given input text. It works by constructing a binary tree of nodes called a Huffman tree, where each leaf node represents a symbol in the input text. The algorithm then assigns shorter codes to the more frequently occurring symbols and longer codes to the less frequently occurring symbols, such that the total number of bits required to represent the input text is minimized.

For example, consider the string "HELLO WORLD!". This string consists of 12 characters, which can be represented using 96 bits (8 bits per character). However, using Huffman coding, we can compress this string by assigning shorter codes to the more frequently occurring symbols. In this case, the compression results in the following encoding: `0100111101000011011010011001011111110` *(note that different encodings are possible for the same string depending on how the Huffman tree is build)*. This encoding requires only 37 bits, which is a significant reduction in size compared to the original 96 bits.

## Motivation of the project

Nowadays we mostly rely on libraries to perform algorithmic tasks (such as sorting, compressing, permutating...). My motivation behind this project was to create an algorithm from scratch to deeply understand how it works and to put in practice various Data Structures such as Binary Trees, Tuples, Dictionaries... I chose a compression algorithm because I always found it strange how can computers zip files without losing information, and now I have an idea how it works :)
