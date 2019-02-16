import collections

# ref: https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution
class TrieNode:
# Initialize your data structure here.
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.is_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		if len(word) < 3: 
			# print(word)
			return
		else:
			current = self.root
			for letter in word:
				current = current.children[letter]
			current.is_word = True

	def search(self, word):
		current = self.root
		for letter in word:
			current = current.children.get(letter)
			if current is None:
				return False
		return current.is_word

	def startsWith(self, prefix):
		current = self.root
		for letter in prefix:
			current = current.children.get(letter)
			if current is None:
				return False
		return True

# ref: http://flothesof.github.io/preparing-hashcode-2018.html
# 	   https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
def read_input(filename):
	with open(filename) as f:
		mylist = f.read().splitlines()
	print("read in data of length:", len(mylist))
	return mylist


def construct_trie(mylist):
	res_trie = Trie()
	for word in mylist:
		res_trie.insert(word)
	return res_trie

def read_test(filename):
	myiter = iter(read_input(filename))
	num = int(next(myiter))
	res = []
	for _ in range(num):
		res.append(next(myiter).split())
	print("current test case is:", res)
	return res