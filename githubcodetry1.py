

class TrieNode:
	
	# Each node in the trie has a value, a list of children, 
	# and a "complete" value that keeps track of whether that
	# node completes a word in the trie. It contains "None" if 
	# it doesn't. If it does, it contains the word, which will
	# be equal to the concatenation of the values of all the
	# nodes on the path from the root to this node
	def __init__(self, value):
		self.value = value
		self.children = []
		self.complete = None

	# Adds a child to the node
	def add(self, child):
		self.children.append(child)

	# Returns the child node with the requested value if it
	# exists, and returns None otherwise. Allows us to search
	# the trie for a word letter-by-letter
	def get_child(self, value):
		for child in self.children:
			if child.value == value:
				return child
		return None

	# Tells Python that, when we call "print" on a node,
	# we want to print its value field
	def __str__(self):
		return str(self.value)


class Trie:
	
	# The root of a trie is the empty string
	def __init__(self, listy=None):
		self.root = TrieNode('')

		# If we pass in the optional listy parameter, 
		# the list of words is added to the trie
		if listy != None:
			self.add_to_trie(listy)


	# Takes a list of words and adds all of them to the trie
	def add_to_trie(self, listy): 
	
		for word in listy:

			current_node = self.root

			# We search for each letter of the current word on 
			# the next level of the trie by looking for it in the
			# current TrieNode's children. If it isn't there, we 
			# add it and keep going. 
			for letter in list(word):
				next_node = current_node.get_child(letter)
				if next_node == None:
					next_node = TrieNode(letter)
					current_node.add(next_node)
				current_node = next_node

			# Once each word has completed, we add it to the 'complete'
			# field of the current node to indicate that the current node,
			# which iss the last letter in the word, completes that word.
			current_node.complete = word
            
# First, we grab all the valid boggle words from the dictionary
file = open("words.txt", 'r')
dictionary = []
# in boggle, words must be of length >= 3
for word in file:
	# accounts for new line character
	if len(word) < 1:
		continue
	# removes new line character
	dictionary.append(word[:-1])

# makes a trie out of all the words in the dictionary
trie = Trie()
trie.add_to_trie(dictionary)


# Takes in a boggle board and returns the set
# of valid words on that boggle board
def solve_boggle(board, trie=trie):

	# # verifies that the input board is a valid N x M array
	# if not check_valid_matrix(board):
	# 	return ["invalid board"]

	make_lower_case(board)

	# the solutions will be stored in a set to eliminate duplicates
	solutions = set()

	# from each starting location on the board (every i,j coordinate),
	# we'll collect the set of valid words that begin at that location
	for i in range(len(board)):
		for j in range(len(board[0])):

			solutions.update(words_from_start(board, i, j, trie))

	return solutions


# Constants for indexing the tuples that contain relevant information
# about which letter we're looking at an what word we're considering
# it to be a part of as we traverse the board
ROW = 0
COL = 1
NODE = 2
GRID = 3


# Returns all the valid words that start at the given 
# i,j coordinate on the board
def words_from_start(board, i, j, trie):

	solutions = set()

	# stack for depth-first search
	stack = []
	# push on the coordinates of the start letter 
	# along with the root of the trie
	stack.append((i, j, trie.root, board))

	while len(stack) > 0:

		curr_letter = stack.pop()
		curr_node = curr_letter[NODE]

		# use a helper function to get all the letters to which our current
		# letter is adjacent
		neighbors = find_neighbors(board, curr_letter[ROW], curr_letter[COL])

		# for each of these neighbors, 
		for neighbor in neighbors:

			x = neighbor[ROW]
			y = neighbor[COL]

			board_copy = copy_matrix(curr_letter[GRID])

			child = curr_node.get_child(board_copy[x][y])

			# if there isn't a node in the dictionary trie suggesting that
			# this letter is part of any word, we stop going down this path
			# by not pushing these current coordinates onto the stack
			if not child:
				continue

			if child.complete:
				solutions.add(child.complete)

			# essentially marks the node we just visited as visited
			board_copy[x][y] = None

			stack.append((x, y, child, board_copy))

	return solutions


# Takes a matrix and a position in that 
# matrix and returns a list of the positions
# in a circle around that position 
def find_neighbors(mat, i, j):

	rows = len(mat)
	cols = len(mat[0])

	# We use max and min to avoid going outside
	# the bounds of the matrix 	
	row_start = max(0, i-1)
	row_end = min(rows, i+2)

	col_start = max(0, j-1)
	col_end = min(cols, j+2)

	neighbors = []

	for x in range(row_start, row_end):
		for y in range(col_start, col_end):

			# We don't want to input coordinate
			# to be in its list of neighbors
			if x != i or y != j:
				neighbors.append((x, y))

	return neighbors


# Simply takes a two-dimensional array
# and returns a copy of it that can be
# modified without disrupting the original
def copy_matrix(mat):

	copy = []
	for row in mat:

		row_copy = []
		for col in row:
			row_copy.append(col)

		copy.append(row_copy)

	return copy


# makes sure the boggle board has the same 
# number of letters in each row 
def check_valid_matrix(mat):

	length = len(mat[0])

	for row in mat[1:]:
		if len(row) != length:
			return False

	return True


# converts all the letters on the boggle board to 
# so that our input is not case sensitive
def make_lower_case(mat):

	length = len(mat[0])

	for row in range(length):
		for col in range(length):
			mat[row][col] = mat[row][col].lower()
			


if __name__ == "__main__":

	# An example Boggle board
    if __name__ == '__main__':
        with open('matrix.txt') as f:
            lines = [line for line in f]
    
        lst=[] 
        # removing the new line characters
        with open('matrix.txt') as f:
            lines = [line.rstrip() for line in f]
            for i in lines:
                lst.append(i.split())
          
        
        board=lst
      
        
        
            
	# Call our solve_boggle function on the board, 
	# which returns a list of all the legal words on it
    	result = solve_boggle(board)
    	print(result)
    
    
    
# All of boggle-solving code is in the file boggle_solver.py
#import boggle_solver

# used for randomly filling a boggle board

# A conventional boggle grid is 4 x 4
SIZE = 8
# A letter bank for "randomly" selecting letters. More useful 
# letters have a higher probability of being selected.
alphabet = \
	"AAAAAABBCCDDDEEEEEEEEEEEFFGGHHHHHIIIIIIJKLLLLMM"+\
	"NNNNNNOOOOOOOPPQRRRRRSSSSSSTTTTTTTTTUUUVVWWWXYYYZ"



	


	
    
    
