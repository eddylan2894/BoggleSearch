# BoggleSearch

This is the coding challenge assigned by Jobox. The detailed problem statement is described in `problem.pdf`.
My approach is to use a Trie (Prefix tree) to store the dictionary followed by a depth frist search (DFS).
The prefix tree provides an O(n) search time complexity where n is the length of the input word. Because a valid word is at least three characters long, I do not insert words less than 3 characters into the tree. 
DFS were performed on every character in the input test file (Default file name is `test.txt`). I constructed another grid to store the visited spots in the DFS, which costs additional O(m^2) space complexity for m x m matrix.

To run the program, use `python main.py --testfile <filename>`. For example if the input test file is `test.txt`, use `python main.py --testfile test.txt`.