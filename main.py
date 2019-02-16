# ref: https://leetcode.com/problems/number-of-islands/discuss/121164/Python-BFS-and-DFS-solution
# ref: https://github.com/billamiable/Reinforcement_Learning_Assignment/blob/master/Ex2_Q/run_dqn_atari.py - argpars
import util

class Solution:
    def __init__(self, filename):
        mylist = util.read_input(filename)
        self.trie = util.construct_trie( mylist)
        self.res = []
    def boggle(self, in_list):
        assert len(in_list) == len(in_list[0])
        in_size = len(in_list)
        # go through every word starts with in_list[i][j]
        for i in range(in_size):
            for j in range(in_size):
                # contruct a grid to store whether the index (i,j) has been traversed (not yet 0, traversed 1)
                grid = [[0 for _j in range(in_size)] for _i in range(in_size)]
                grid[i][j] = 1
                self.dfs(in_list, grid, i, j, in_size, "")
        # copy the results and clear self.result
        # res = self.res.copy()
        # self.res = []
        return self.res
    def dfs(self, in_list, grid, r, c, in_size, cur_res):
        cur_res += in_list[r][c]
        # if current result is in the Trie, append answer
        if self.trie.search(cur_res):
            self.res.append(cur_res)
        # skip if no word starts with current result
        if not self.trie.startsWith(cur_res):
            return
        # traverse its ajacent points
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                direction =  (i-1, j-1)
                n_r, n_c = r + direction[0], c + direction[1]
                if 0 <= n_r< in_size and 0 <= n_c< in_size and grid[n_r][n_c]==0 :
                    grid[n_r][n_c] = 1
                    self.dfs(in_list, grid, n_r, n_c, in_size, cur_res)
                    grid[n_r][n_c] = 0
        # cur_res = cur_res[:-1]

"""
# Default test case:
test_input = [['c', 'j', 'e'],\
              ['e', 'a', 'o'],\
              ['i', 't', 'e']]

"""

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--testfile', help= "your input test file here" , type=str, default='test.txt')
    args = parser.parse_args()
    # reads in test input
    test_input = util.read_test(args.testfile)
    # construct the trie by dictionary "words_alph.txt"
    sol = Solution("words_alpha.txt")
    # do the boggle search
    print('result:', sol.boggle(test_input))


if __name__ == "__main__":
    main()
