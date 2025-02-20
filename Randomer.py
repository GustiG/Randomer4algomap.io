# Run it to pick a random chapter & exercise from algomap.io

import random
import time

chapters = [
    'Arrays & Strings',
    'Hashmaps & Sets',
    '2 Pointers',
    'Stacks',
    'Linked Lists',
    'Binary Search',
    'Sliding Window',
    'Trees',
    'Heaps',
    'Recursive Backtracking',
    'Graphs',
    'Dynamic Programming'
]

random_chapter = random.choice(chapters)
print(f'From chapter: {random_chapter}')

exercises_dict = {
    "Arrays & Strings": [
        'Find Closest Number to Zero',
        'Merge Strings Alternately',
        'Roman to Integer',
        'Is Subsequence',
        'Best Time to Buy and Sell Stock',
        'Longest Common Prefix',
        'Summary Ranges',
        'Product of Array Except Self',
        'Merge Intervals',
        'Spiral Matrix',
        'Rotate Image'
    ],
    "Hashmaps & Sets": [
        'Jewels and Stones',
        'Contains Duplicate',
        'Ransom Note',
        'Valid Anagram',
        'Maximum Number of Balloons',
        'Two Sum',
        'Valid Sudoku',
        'Group Anagrams',
        'Majority Element',
        'Longest Consecutive Sequence'
    ],
    "2 Pointers": [
        'Squares of a Sorted Array',
        'Reverse String',
        'Two Sum II - Input Array Is Sorted',
        'Valid Palindrome',
        '3Sum',
        'Container With Most Water',
        'Trapping Rain Water'
    ],
    "Stacks": [
        'Baseball Game',
        'Valid Parentheses',
        'Evaluate Reverse Polish Notation (RPN)',
        'Daily Temperatures',
        'Min Stack'
    ],
    "Linked Lists": [
        'Remove Duplicates from Sorted List',
        'Reverse Linked List',
        'Merge Two Sorted Lists',
        'Linked List Cycle',
        'Middle of the Linked List',
        'Remove Nth Node from End of List',
        'Copy List with Random Pointer'
    ],
    "Binary Search": [
        'Binary Search',
        'Search Insert Position',
        'First Bad Version',
        'Valid Perfect Square',
        'Search a 2D Matrix',
        'Find Minimum in Rotated Sorted Array',
        'Search in Rotated Sorted Array',
        'Koko Eating Bananas'
    ],
    "Sliding Window": [
        'Maximum Average Subarray I',
        'Max Consecutive Ones III',
        'Longest Substring Without Repeating Characters',
        'Longest Repeating Character Replacement',
        'Minimum Size Subarray Sum',
        'Permutation in String'
    ],
    "Trees": [
        'Invert Binary Tree',
        'Maximum Depth of Binary Tree',
        'Balanced Binary Tree',
        'Diameter of Binary Tree',
        'Same Binary Tree',
        'Symmetric Tree',
        'Path Sum',
        'Subtree of Another Tree',
        'Binary Tree Level Order Traversal (BFS)',
        'Kth Smallest Element in a BST',
        'Minimum Absolute Difference in BST',
        'Validate Binary Search Tree',
        'Lowest Common Ancestor of a Binary Search Tree',
        'Implement Trie (Prefix Tree)'
    ],
    "Heaps": [
        'Last Stone Weight',
        'Kth Largest Element in an Array',
        'Top K Frequent Elements',
        'K Closest Points to Origin',
        'Merge K Sorted Linked Lists'
    ],
    "Recursive Backtracking": [
        'Subsets',
        'Permutations',
        'Combinations',
        'Combination Sum',
        'Letter Combinations of a Phone Number',
        'Generate Parentheses',
        'Word Search'
    ],
    "Graphs": [
        'Find if Path Exists in Graph',
        'Number of Islands',
        'Max Area of Island',
        'Course Schedule (Detecting Cycles in a Graph)',
        'Course Schedule II (Topological Sort)',
        'Pacific Atlantic Water Flow',
        'Clone Graph',
        'Rotting Oranges',
        "Min Cost to Connect All Points (Prim's Algorithm to Create MST)",
        "Network Delay Time (Dijkstra's Algorithm)"
    ],
    "Dynamic Programming": [
        'Fibonacci Number',
        'Climbing Stairs',
        'Min Cost Climbing Stairs',
        'House Robber',
        'Unique Paths',
        "Maximum Subarray (Kadane's Algorithm)",
        'Jump Game',
        'Coin Change',
        'Longest Increasing Subsequence',
        'Longest Common Subsequence'
    ]
}

exercises = exercises_dict.get(random_chapter, [])


time.sleep(1.2)
print(f'Exercise: {random.choice(exercises)}')
