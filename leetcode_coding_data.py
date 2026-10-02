"""
Comprehensive LeetCode Coding Questions Dataset for 25 Technical Domains
Each domain has 10 authentic LeetCode problems (IDs 31-40) with problem description,
examples, constraints, starter templates, and test cases.
"""

true = True
false = False
null = None

DOMAIN_LEETCODE_QUESTIONS = {
    "python": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 39,
            "is_coding": true,
            "domain": "python"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "python"
        }
    ],
    "java": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 88: Merge Sorted Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in non-decreasing order, and two integers <code>m</code> and <code>n</code>, representing the number of elements in <code>nums1</code> and <code>nums2</code> respectively.<br><br>\nMerge <code>nums1</code> and <code>nums2</code> into a single array sorted in non-decreasing order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3\nOutput: [1,2,2,3,5,6]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>nums1.length == m + n</code>",
            "starter_code": "def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:\n    p1 = m - 1\n    p2 = n - 1\n    p = m + n - 1\n    while p1 >= 0 and p2 >= 0:\n        if nums1[p1] > nums2[p2]:\n            nums1[p] = nums1[p1]\n            p1 -= 1\n        else:\n            nums1[p] = nums2[p2]\n            p2 -= 1\n        p -= 1\n    while p2 >= 0:\n        nums1[p] = nums2[p2]\n        p2 -= 1\n        p -= 1\n    return nums1",
            "test_cases": [
                {
                    "input": "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3",
                    "expected_output": "[1, 2, 2, 3, 5, 6]",
                    "raw_input": {
                        "nums1": [
                            1,
                            2,
                            3,
                            0,
                            0,
                            0
                        ],
                        "m": 3,
                        "nums2": [
                            2,
                            5,
                            6
                        ],
                        "n": 3
                    },
                    "expected": [
                        1,
                        2,
                        2,
                        3,
                        5,
                        6
                    ]
                }
            ],
            "explanation": "Fill nums1 from the back using three pointers (p1, p2, p). Time: O(m + n), Space: O(1).",
            "id": 36,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 136: Single Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a non-empty array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.<br><br>\nYou must implement a solution with a linear runtime complexity <code>O(n)</code> and use only constant extra space <code>O(1)</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,2,1]\nOutput: 1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [4,1,2,1,2]\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def singleNumber(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def singleNumber(nums: list[int]) -> int:\n    xor = 0\n    for n in nums:\n        xor ^= n\n    return xor",
            "test_cases": [
                {
                    "input": "nums = [2,2,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            2,
                            2,
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [4,1,2,1,2]",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            4,
                            1,
                            2,
                            1,
                            2
                        ]
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all elements leaves the single non-duplicated element. Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "java"
        },
        {
            "title": "LeetCode 15: 3Sum",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.<br><br>\nNotice that the solution set must not contain duplicate triplets.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,1]\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>3 <= nums.length <= 3000</code>",
            "starter_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i - 1]:\n            continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            s = nums[i] + nums[l] + nums[r]\n            if s == 0:\n                res.append([nums[i], nums[l], nums[r]])\n                while l < r and nums[l] == nums[l + 1]: l += 1\n                while l < r and nums[r] == nums[r - 1]: r -= 1\n                l += 1\n                r -= 1\n            elif s < 0:\n                l += 1\n            else:\n                r -= 1\n    return res",
            "test_cases": [
                {
                    "input": "nums = [-1,0,1,2,-1,-4]",
                    "expected_output": "[[-1, -1, 2], [-1, 0, 1]]",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            1,
                            2,
                            -1,
                            -4
                        ]
                    },
                    "expected": [
                        [
                            -1,
                            -1,
                            2
                        ],
                        [
                            -1,
                            0,
                            1
                        ]
                    ]
                },
                {
                    "input": "nums = [0,1,1]",
                    "expected_output": "[]",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            1
                        ]
                    },
                    "expected": []
                }
            ],
            "explanation": "Sort the array, then iterate through elements and use two pointers (left & right) for 2Sum. Skip duplicates. Time: O(n^2), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "java"
        }
    ],
    "c": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 344: Reverse String",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a function that reverses a string (represented as a list of characters <code>s</code>) in-place with <code>O(1)</code> extra memory.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"h\",\"e\",\"l\",\"l\",\"o\"]\nOutput: [\"o\",\"l\",\"l\",\"e\",\"h\"]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]\nOutput: [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>5</sup></code>",
            "starter_code": "def reverseString(s: list[str]) -> list[str]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def reverseString(s: list[str]) -> list[str]:\n    left, right = 0, len(s) - 1\n    while left < right:\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    return s",
            "test_cases": [
                {
                    "input": "s = [\"h\",\"e\",\"l\",\"l\",\"o\"]",
                    "expected_output": "[\"o\", \"l\", \"l\", \"e\", \"h\"]",
                    "raw_input": {
                        "s": [
                            "h",
                            "e",
                            "l",
                            "l",
                            "o"
                        ]
                    },
                    "expected": [
                        "o",
                        "l",
                        "l",
                        "e",
                        "h"
                    ]
                },
                {
                    "input": "s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]",
                    "expected_output": "[\"h\", \"a\", \"n\", \"n\", \"a\", \"H\"]",
                    "raw_input": {
                        "s": [
                            "H",
                            "a",
                            "n",
                            "n",
                            "a",
                            "h"
                        ]
                    },
                    "expected": [
                        "h",
                        "a",
                        "n",
                        "n",
                        "a",
                        "H"
                    ]
                }
            ],
            "explanation": "Two pointers moving inward swapping opposite elements in place. Time: O(n), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 27: Remove Element",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> in-place. Return the number of elements in <code>nums</code> which are not equal to <code>val</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,2,3], val = 3\nOutput: 2 (nums = [2,2,_,_])</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,2,2,3,0,4,2], val = 2\nOutput: 5</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= nums.length <= 100</code>",
            "starter_code": "def removeElement(nums: list[int], val: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def removeElement(nums: list[int], val: int) -> int:\n    k = 0\n    for x in nums:\n        if x != val:\n            nums[k] = x\n            k += 1\n    return k",
            "test_cases": [
                {
                    "input": "nums = [3,2,2,3], val = 3",
                    "expected_output": "2",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            2,
                            3
                        ],
                        "val": 3
                    },
                    "expected": 2
                },
                {
                    "input": "nums = [0,1,2,2,3,0,4,2], val = 2",
                    "expected_output": "5",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            2,
                            2,
                            3,
                            0,
                            4,
                            2
                        ],
                        "val": 2
                    },
                    "expected": 5
                }
            ],
            "explanation": "Two pointer writer pattern. Write elements != val to index k and increment k. Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 26: Remove Duplicates from Sorted Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code> sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,1,2]\nOutput: 2</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,0,1,1,1,2,2,3,3,4]\nOutput: 5</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def removeDuplicates(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def removeDuplicates(nums: list[int]) -> int:\n    if not nums: return 0\n    k = 1\n    for i in range(1, len(nums)):\n        if nums[i] != nums[i - 1]:\n            nums[k] = nums[i]\n            k += 1\n    return k",
            "test_cases": [
                {
                    "input": "nums = [1,1,2]",
                    "expected_output": "2",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            2
                        ]
                    },
                    "expected": 2
                },
                {
                    "input": "nums = [0,0,1,1,1,2,2,3,3,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "nums": [
                            0,
                            0,
                            1,
                            1,
                            1,
                            2,
                            2,
                            3,
                            3,
                            4
                        ]
                    },
                    "expected": 5
                }
            ],
            "explanation": "Two pointers: compare current element with previous. If different, write to index k. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 36,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 136: Single Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a non-empty array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.<br><br>\nYou must implement a solution with a linear runtime complexity <code>O(n)</code> and use only constant extra space <code>O(1)</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,2,1]\nOutput: 1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [4,1,2,1,2]\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def singleNumber(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def singleNumber(nums: list[int]) -> int:\n    xor = 0\n    for n in nums:\n        xor ^= n\n    return xor",
            "test_cases": [
                {
                    "input": "nums = [2,2,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            2,
                            2,
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [4,1,2,1,2]",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            4,
                            1,
                            2,
                            1,
                            2
                        ]
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all elements leaves the single non-duplicated element. Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "c"
        },
        {
            "title": "LeetCode 9: Palindrome Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer <code>x</code>, return <code>true</code> if <code>x</code> is a palindrome, and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: x = 121\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: x = -121\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code>",
            "starter_code": "def isPalindrome(x: int) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(x: int) -> bool:\n    if x < 0: return False\n    s = str(x)\n    return s == s[::-1]",
            "test_cases": [
                {
                    "input": "x = 121",
                    "expected_output": "true",
                    "raw_input": {
                        "x": 121
                    },
                    "expected": true
                },
                {
                    "input": "x = -121",
                    "expected_output": "false",
                    "raw_input": {
                        "x": -121
                    },
                    "expected": false
                },
                {
                    "input": "x = 10",
                    "expected_output": "false",
                    "raw_input": {
                        "x": 10
                    },
                    "expected": false
                }
            ],
            "explanation": "Negative numbers cannot be palindromes. Convert to string and verify mirror equality. Time: O(log10 x), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "c"
        }
    ],
    "cpp": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 36,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 15: 3Sum",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.<br><br>\nNotice that the solution set must not contain duplicate triplets.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,1]\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>3 <= nums.length <= 3000</code>",
            "starter_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i - 1]:\n            continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            s = nums[i] + nums[l] + nums[r]\n            if s == 0:\n                res.append([nums[i], nums[l], nums[r]])\n                while l < r and nums[l] == nums[l + 1]: l += 1\n                while l < r and nums[r] == nums[r - 1]: r -= 1\n                l += 1\n                r -= 1\n            elif s < 0:\n                l += 1\n            else:\n                r -= 1\n    return res",
            "test_cases": [
                {
                    "input": "nums = [-1,0,1,2,-1,-4]",
                    "expected_output": "[[-1, -1, 2], [-1, 0, 1]]",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            1,
                            2,
                            -1,
                            -4
                        ]
                    },
                    "expected": [
                        [
                            -1,
                            -1,
                            2
                        ],
                        [
                            -1,
                            0,
                            1
                        ]
                    ]
                },
                {
                    "input": "nums = [0,1,1]",
                    "expected_output": "[]",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            1
                        ]
                    },
                    "expected": []
                }
            ],
            "explanation": "Sort the array, then iterate through elements and use two pointers (left & right) for 2Sum. Skip duplicates. Time: O(n^2), Space: O(1) auxiliary.",
            "id": 37,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 11: Container With Most Water",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.<br><br>\nFind two lines that together with the x-axis form a container, such that the container contains the most water. Return <em>the maximum amount of water a container can store</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,1]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= height.length <= 10<sup>5</sup></code>",
            "starter_code": "def maxArea(height: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxArea(height: list[int]) -> int:\n    l, r = 0, len(height) - 1\n    max_a = 0\n    while l < r:\n        h = min(height[l], height[r])\n        max_a = max(max_a, h * (r - l))\n        if height[l] < height[r]:\n            l += 1\n        else:\n            r -= 1\n    return max_a",
            "test_cases": [
                {
                    "input": "height = [1,8,6,2,5,4,8,3,7]",
                    "expected_output": "49",
                    "raw_input": {
                        "height": [
                            1,
                            8,
                            6,
                            2,
                            5,
                            4,
                            8,
                            3,
                            7
                        ]
                    },
                    "expected": 49
                },
                {
                    "input": "height = [1,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "height": [
                            1,
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Two pointers at left and right boundaries. Move the pointer with smaller height inward. Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "cpp"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 40,
            "is_coding": true,
            "domain": "cpp"
        }
    ],
    "javascript": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 33,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 37,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "javascript"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "javascript"
        }
    ],
    "typescript": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 33,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "typescript"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "typescript"
        }
    ],
    "golang": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 136: Single Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a non-empty array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.<br><br>\nYou must implement a solution with a linear runtime complexity <code>O(n)</code> and use only constant extra space <code>O(1)</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,2,1]\nOutput: 1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [4,1,2,1,2]\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def singleNumber(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def singleNumber(nums: list[int]) -> int:\n    xor = 0\n    for n in nums:\n        xor ^= n\n    return xor",
            "test_cases": [
                {
                    "input": "nums = [2,2,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            2,
                            2,
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [4,1,2,1,2]",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            4,
                            1,
                            2,
                            1,
                            2
                        ]
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all elements leaves the single non-duplicated element. Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "golang"
        },
        {
            "title": "LeetCode 344: Reverse String",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a function that reverses a string (represented as a list of characters <code>s</code>) in-place with <code>O(1)</code> extra memory.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"h\",\"e\",\"l\",\"l\",\"o\"]\nOutput: [\"o\",\"l\",\"l\",\"e\",\"h\"]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]\nOutput: [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>5</sup></code>",
            "starter_code": "def reverseString(s: list[str]) -> list[str]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def reverseString(s: list[str]) -> list[str]:\n    left, right = 0, len(s) - 1\n    while left < right:\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    return s",
            "test_cases": [
                {
                    "input": "s = [\"h\",\"e\",\"l\",\"l\",\"o\"]",
                    "expected_output": "[\"o\", \"l\", \"l\", \"e\", \"h\"]",
                    "raw_input": {
                        "s": [
                            "h",
                            "e",
                            "l",
                            "l",
                            "o"
                        ]
                    },
                    "expected": [
                        "o",
                        "l",
                        "l",
                        "e",
                        "h"
                    ]
                },
                {
                    "input": "s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]",
                    "expected_output": "[\"h\", \"a\", \"n\", \"n\", \"a\", \"H\"]",
                    "raw_input": {
                        "s": [
                            "H",
                            "a",
                            "n",
                            "n",
                            "a",
                            "h"
                        ]
                    },
                    "expected": [
                        "h",
                        "a",
                        "n",
                        "n",
                        "a",
                        "H"
                    ]
                }
            ],
            "explanation": "Two pointers moving inward swapping opposite elements in place. Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "golang"
        }
    ],
    "csharp": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 136: Single Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a non-empty array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.<br><br>\nYou must implement a solution with a linear runtime complexity <code>O(n)</code> and use only constant extra space <code>O(1)</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,2,1]\nOutput: 1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [4,1,2,1,2]\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def singleNumber(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def singleNumber(nums: list[int]) -> int:\n    xor = 0\n    for n in nums:\n        xor ^= n\n    return xor",
            "test_cases": [
                {
                    "input": "nums = [2,2,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            2,
                            2,
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [4,1,2,1,2]",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            4,
                            1,
                            2,
                            1,
                            2
                        ]
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all elements leaves the single non-duplicated element. Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "csharp"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "csharp"
        }
    ],
    "ruby": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 136: Single Number",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a non-empty array of integers <code>nums</code>, every element appears <em>twice</em> except for one. Find that single one.<br><br>\nYou must implement a solution with a linear runtime complexity <code>O(n)</code> and use only constant extra space <code>O(1)</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,2,1]\nOutput: 1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [4,1,2,1,2]\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>",
            "starter_code": "def singleNumber(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def singleNumber(nums: list[int]) -> int:\n    xor = 0\n    for n in nums:\n        xor ^= n\n    return xor",
            "test_cases": [
                {
                    "input": "nums = [2,2,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            2,
                            2,
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [4,1,2,1,2]",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            4,
                            1,
                            2,
                            1,
                            2
                        ]
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Bitwise XOR property: a ^ a = 0 and a ^ 0 = a. XORing all elements leaves the single non-duplicated element. Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 344: Reverse String",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a function that reverses a string (represented as a list of characters <code>s</code>) in-place with <code>O(1)</code> extra memory.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"h\",\"e\",\"l\",\"l\",\"o\"]\nOutput: [\"o\",\"l\",\"l\",\"e\",\"h\"]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]\nOutput: [\"h\",\"a\",\"n\",\"n\",\"a\",\"H\"]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>5</sup></code>",
            "starter_code": "def reverseString(s: list[str]) -> list[str]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def reverseString(s: list[str]) -> list[str]:\n    left, right = 0, len(s) - 1\n    while left < right:\n        s[left], s[right] = s[right], s[left]\n        left += 1\n        right -= 1\n    return s",
            "test_cases": [
                {
                    "input": "s = [\"h\",\"e\",\"l\",\"l\",\"o\"]",
                    "expected_output": "[\"o\", \"l\", \"l\", \"e\", \"h\"]",
                    "raw_input": {
                        "s": [
                            "h",
                            "e",
                            "l",
                            "l",
                            "o"
                        ]
                    },
                    "expected": [
                        "o",
                        "l",
                        "l",
                        "e",
                        "h"
                    ]
                },
                {
                    "input": "s = [\"H\",\"a\",\"n\",\"n\",\"a\",\"h\"]",
                    "expected_output": "[\"h\", \"a\", \"n\", \"n\", \"a\", \"H\"]",
                    "raw_input": {
                        "s": [
                            "H",
                            "a",
                            "n",
                            "n",
                            "a",
                            "h"
                        ]
                    },
                    "expected": [
                        "h",
                        "a",
                        "n",
                        "n",
                        "a",
                        "H"
                    ]
                }
            ],
            "explanation": "Two pointers moving inward swapping opposite elements in place. Time: O(n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "ruby"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "ruby"
        }
    ],
    "problem_solving": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 21: Merge Two Sorted Lists",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given the heads of two sorted lists <code>list1</code> and <code>list2</code>. Merge the two lists into one sorted list and return it.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: list1 = [1,2,4], list2 = [1,3,4]\nOutput: [1,1,2,3,4,4]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: list1 = [], list2 = []\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 Both lists are sorted in non-decreasing order.",
            "starter_code": "def mergeTwoLists(list1: list[int], list2: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def mergeTwoLists(list1: list[int], list2: list[int]) -> list[int]:\n    i, j = 0, 0\n    res = []\n    while i < len(list1) and j < len(list2):\n        if list1[i] <= list2[j]:\n            res.append(list1[i])\n            i += 1\n        else:\n            res.append(list2[j])\n            j += 1\n    res.extend(list1[i:])\n    res.extend(list2[j:])\n    return res",
            "test_cases": [
                {
                    "input": "list1 = [1,2,4], list2 = [1,3,4]",
                    "expected_output": "[1, 1, 2, 3, 4, 4]",
                    "raw_input": {
                        "list1": [
                            1,
                            2,
                            4
                        ],
                        "list2": [
                            1,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        1,
                        1,
                        2,
                        3,
                        4,
                        4
                    ]
                },
                {
                    "input": "list1 = [], list2 = []",
                    "expected_output": "[]",
                    "raw_input": {
                        "list1": [],
                        "list2": []
                    },
                    "expected": []
                }
            ],
            "explanation": "Iterate through both lists comparing current elements and appending smaller one. Time: O(n + m), Space: O(n + m).",
            "id": 33,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 36,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 15: 3Sum",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.<br><br>\nNotice that the solution set must not contain duplicate triplets.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,1]\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>3 <= nums.length <= 3000</code>",
            "starter_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i - 1]:\n            continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            s = nums[i] + nums[l] + nums[r]\n            if s == 0:\n                res.append([nums[i], nums[l], nums[r]])\n                while l < r and nums[l] == nums[l + 1]: l += 1\n                while l < r and nums[r] == nums[r - 1]: r -= 1\n                l += 1\n                r -= 1\n            elif s < 0:\n                l += 1\n            else:\n                r -= 1\n    return res",
            "test_cases": [
                {
                    "input": "nums = [-1,0,1,2,-1,-4]",
                    "expected_output": "[[-1, -1, 2], [-1, 0, 1]]",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            1,
                            2,
                            -1,
                            -4
                        ]
                    },
                    "expected": [
                        [
                            -1,
                            -1,
                            2
                        ],
                        [
                            -1,
                            0,
                            1
                        ]
                    ]
                },
                {
                    "input": "nums = [0,1,1]",
                    "expected_output": "[]",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            1
                        ]
                    },
                    "expected": []
                }
            ],
            "explanation": "Sort the array, then iterate through elements and use two pointers (left & right) for 2Sum. Skip duplicates. Time: O(n^2), Space: O(1) auxiliary.",
            "id": 37,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 38,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 39,
            "is_coding": true,
            "domain": "problem_solving"
        },
        {
            "title": "LeetCode 11: Container With Most Water",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.<br><br>\nFind two lines that together with the x-axis form a container, such that the container contains the most water. Return <em>the maximum amount of water a container can store</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,1]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= height.length <= 10<sup>5</sup></code>",
            "starter_code": "def maxArea(height: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxArea(height: list[int]) -> int:\n    l, r = 0, len(height) - 1\n    max_a = 0\n    while l < r:\n        h = min(height[l], height[r])\n        max_a = max(max_a, h * (r - l))\n        if height[l] < height[r]:\n            l += 1\n        else:\n            r -= 1\n    return max_a",
            "test_cases": [
                {
                    "input": "height = [1,8,6,2,5,4,8,3,7]",
                    "expected_output": "49",
                    "raw_input": {
                        "height": [
                            1,
                            8,
                            6,
                            2,
                            5,
                            4,
                            8,
                            3,
                            7
                        ]
                    },
                    "expected": 49
                },
                {
                    "input": "height = [1,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "height": [
                            1,
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Two pointers at left and right boundaries. Move the pointer with smaller height inward. Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "problem_solving"
        }
    ],
    "sql": [
        {
            "title": "LeetCode 175: Combine Two Tables",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to report the <code>firstName</code>, <code>lastName</code>, <code>city</code>, and <code>state</code> of each person in the <code>Person</code> table. If the address of a <code>personId</code> is not present in the <code>Address</code> table, report <code>null</code> instead.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Person table:\n+----------+----------+-----------+\n| personId | lastName | firstName |\n+----------+----------+-----------+\n| 1        | Wang     | Allen     |\n| 2        | Alice    | Bob       |\n+----------+----------+-----------+\nAddress table:\n+-----------+----------+---------------+------------+\n| addressId | personId | city          | state      |\n+-----------+----------+---------------+------------+\n| 1         | 2        | New York City | New York   |\n+-----------+----------+---------------+------------+\nOutput:\n+-----------+----------+---------------+----------+\n| firstName | lastName | city          | state    |\n+-----------+----------+---------------+----------+\n| Allen     | Wang     | Null          | Null     |\n| Bob       | Alice    | New York City | New York |\n+-----------+----------+---------------+----------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT p.firstName, p.lastName, a.city, a.state\nFROM Person p\nLEFT JOIN Address a ON p.personId = a.personId;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Person (personId INT, lastName TEXT, firstName TEXT);\nCREATE TABLE Address (addressId INT, personId INT, city TEXT, state TEXT);\nINSERT INTO Person VALUES (1, 'Wang', 'Allen'), (2, 'Alice', 'Bob');\nINSERT INTO Address VALUES (1, 2, 'New York City', 'New York');",
                    "input": "Person: [(1, 'Wang', 'Allen'), (2, 'Alice', 'Bob')], Address: [(1, 2, 'New York City', 'New York')]",
                    "expected_output": "[('Allen', 'Wang', None, None), ('Bob', 'Alice', 'New York City', 'New York')]",
                    "expected": [
                        [
                            "Allen",
                            "Wang",
                            null,
                            null
                        ],
                        [
                            "Bob",
                            "Alice",
                            "New York City",
                            "New York"
                        ]
                    ]
                }
            ],
            "explanation": "Use LEFT OUTER JOIN on personId so all persons are returned even without matching addresses.",
            "id": 31,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 176: Second Highest Salary",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a SQL query to report the <strong>second highest distinct salary</strong> from the <code>Employee</code> table. If there is no second highest salary, return <code>null</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Employee table:\n+----+--------+\n| id | salary |\n+----+--------+\n| 1  | 100    |\n| 2  | 200    |\n| 3  | 300    |\n+----+--------+\nOutput:\n+---------------------+\n| SecondHighestSalary |\n+---------------------+\n| 200                 |\n+---------------------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT (\n    SELECT DISTINCT salary\n    FROM Employee\n    ORDER BY salary DESC\n    LIMIT 1 OFFSET 1\n) AS SecondHighestSalary;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Employee (id INT, salary INT);\nINSERT INTO Employee VALUES (1, 100), (2, 200), (3, 300);",
                    "input": "Employee table with salaries 100, 200, 300",
                    "expected_output": "[(200,)]",
                    "expected": [
                        [
                            200
                        ]
                    ]
                }
            ],
            "explanation": "Subquery with DISTINCT salary ordered DESC with LIMIT 1 OFFSET 1 safely returns NULL if no second salary exists.",
            "id": 32,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 181: Employees Earning More Than Their Managers",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to find the employees who earn more than their managers.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Employee table:\n+----+-------+--------+-----------+\n| id | name  | salary | managerId |\n+----+-------+--------+-----------+\n| 1  | Joe   | 70000  | 3         |\n| 2  | Henry | 80000  | 4         |\n| 3  | Sam   | 60000  | Null      |\n| 4  | Max   | 90000  | Null      |\n+----+-------+--------+-----------+\nOutput:\n+----------+\n| Employee |\n+----------+\n| Joe      |\n+----------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT e.name AS Employee\nFROM Employee e\nJOIN Employee m ON e.managerId = m.id\nWHERE e.salary > m.salary;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Employee (id INT, name TEXT, salary INT, managerId INT);\nINSERT INTO Employee VALUES (1, 'Joe', 70000, 3), (2, 'Henry', 80000, 4), (3, 'Sam', 60000, NULL), (4, 'Max', 90000, NULL);",
                    "input": "Employees Joe (70k, mgr 3), Henry (80k, mgr 4), Sam (60k), Max (90k)",
                    "expected_output": "[('Joe',)]",
                    "expected": [
                        [
                            "Joe"
                        ]
                    ]
                }
            ],
            "explanation": "Self JOIN Employee on e.managerId = m.id where e.salary > m.salary.",
            "id": 33,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 182: Duplicate Emails",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to report all the <strong>duplicate emails</strong> in the <code>Person</code> table.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Person table:\n+----+---------+\n| id | email   |\n+----+---------+\n| 1  | a@b.com |\n| 2  | c@d.com |\n| 3  | a@b.com |\n+----+---------+\nOutput:\n+---------+\n| Email   |\n+---------+\n| a@b.com |\n+---------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Person (id INT, email TEXT);\nINSERT INTO Person VALUES (1, 'a@b.com'), (2, 'c@d.com'), (3, 'a@b.com');",
                    "input": "Person table with emails ['a@b.com', 'c@d.com', 'a@b.com']",
                    "expected_output": "[('a@b.com',)]",
                    "expected": [
                        [
                            "a@b.com"
                        ]
                    ]
                }
            ],
            "explanation": "GROUP BY email HAVING COUNT(email) > 1 filters to emails with frequency strictly greater than 1.",
            "id": 34,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 183: Customers Who Never Order",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to find all customers who never order anything from the <code>Customers</code> and <code>Orders</code> tables.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Customers table:\n+----+-------+\n| id | name  |\n+----+-------+\n| 1  | Joe   |\n| 2  | Henry |\n| 3  | Sam   |\n| 4  | Max   |\n+----+-------+\nOrders table:\n+----+------------+\n| id | customerId |\n+----+------------+\n| 1  | 3          |\n| 2  | 1          |\n+----+------------+\nOutput:\n+-----------+\n| Customers |\n+-----------+\n| Henry     |\n| Max       |\n+-----------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT c.name AS Customers\nFROM Customers c\nLEFT JOIN Orders o ON c.id = o.customerId\nWHERE o.customerId IS NULL;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Customers (id INT, name TEXT);\nCREATE TABLE Orders (id INT, customerId INT);\nINSERT INTO Customers VALUES (1, 'Joe'), (2, 'Henry'), (3, 'Sam'), (4, 'Max');\nINSERT INTO Orders VALUES (1, 3), (2, 1);",
                    "input": "Customers: [Joe, Henry, Sam, Max], Orders by customer: [3, 1]",
                    "expected_output": "[('Henry',), ('Max',)]",
                    "expected": [
                        [
                            "Henry"
                        ],
                        [
                            "Max"
                        ]
                    ]
                }
            ],
            "explanation": "Use LEFT JOIN and filter with WHERE Orders.customerId IS NULL to identify unlinked records.",
            "id": 35,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 196: Delete Duplicate Emails",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a query to report the smallest <code>id</code> for each unique email in the <code>Person</code> table (simulating keeping only the unique email with smallest id).<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Person table:\n+----+------------------+\n| id | email            |\n+----+------------------+\n| 1  | john@example.com |\n| 2  | bob@example.com  |\n| 3  | john@example.com |\n+----+------------------+\nOutput:\n+----+------------------+\n| id | email            |\n+----+------------------+\n| 1  | john@example.com |\n| 2  | bob@example.com  |\n+----+------------------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT MIN(id) AS id, email\nFROM Person\nGROUP BY email\nORDER BY id ASC;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Person (id INT, email TEXT);\nINSERT INTO Person VALUES (1, 'john@example.com'), (2, 'bob@example.com'), (3, 'john@example.com');",
                    "input": "Person table with duplicate emails",
                    "expected_output": "[(1, 'john@example.com'), (2, 'bob@example.com')]",
                    "expected": [
                        [
                            1,
                            "john@example.com"
                        ],
                        [
                            2,
                            "bob@example.com"
                        ]
                    ]
                }
            ],
            "explanation": "GROUP BY email with MIN(id) retrieves the earliest record for each email.",
            "id": 36,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 197: Rising Temperature",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to find all dates' <code>id</code> with higher temperatures compared to its previous dates (yesterday).<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Weather table:\n+----+------------+-------------+\n| id | recordDate | temperature |\n+----+------------+-------------+\n| 1  | 2015-01-01 | 10          |\n| 2  | 2015-01-02 | 25          |\n| 3  | 2015-01-03 | 20          |\n| 4  | 2015-01-04 | 30          |\n+----+------------+-------------+\nOutput:\n+----+\n| id |\n+----+\n| 2  |\n| 4  |\n+----+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT w1.id\nFROM Weather w1\nJOIN Weather w2 ON date(w1.recordDate, '-1 day') = date(w2.recordDate)\nWHERE w1.temperature > w2.temperature;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Weather (id INT, recordDate DATE, temperature INT);\nINSERT INTO Weather VALUES (1, '2015-01-01', 10), (2, '2015-01-02', 25), (3, '2015-01-03', 20), (4, '2015-01-04', 30);",
                    "input": "Weather with dates 2015-01-01 to 04 and temps [10, 25, 20, 30]",
                    "expected_output": "[(2,), (4,)]",
                    "expected": [
                        [
                            2
                        ],
                        [
                            4
                        ]
                    ]
                }
            ],
            "explanation": "Join Weather on date offset by 1 day and compare temperatures.",
            "id": 37,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 595: Big Countries",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA country is big if it has an area of at least 3,000,000 km<sup>2</sup> or a population of at least 25,000,000.<br>\nWrite a solution to report the name, population, and area of the big countries.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">World table:\n+-------------+------------+---------+\n| name        | population | area    |\n+-------------+------------+---------+\n| Afghanistan | 25500100   | 652230  |\n| Albania     | 28748      | 28748   |\n| Algeria     | 37100000   | 2381741 |\n+-------------+------------+---------+\nOutput:\n+-------------+------------+---------+\n| name        | population | area    |\n+-------------+------------+---------+\n| Afghanistan | 25500100   | 652230  |\n| Algeria     | 37100000   | 2381741 |\n+-------------+------------+---------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT name, population, area\nFROM World\nWHERE area >= 3000000 OR population >= 25000000;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE World (name TEXT, population INT, area INT);\nINSERT INTO World VALUES ('Afghanistan', 25500100, 652230), ('Albania', 28748, 28748), ('Algeria', 37100000, 2381741);",
                    "input": "World table with Afghanistan, Albania, Algeria",
                    "expected_output": "[('Afghanistan', 25500100, 652230), ('Algeria', 37100000, 2381741)]",
                    "expected": [
                        [
                            "Afghanistan",
                            25500100,
                            652230
                        ],
                        [
                            "Algeria",
                            37100000,
                            2381741
                        ]
                    ]
                }
            ],
            "explanation": "Simple filter with WHERE area >= 3000000 OR population >= 25000000.",
            "id": 38,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 584: Find Customer Referee",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nFind the names of the customer that are <strong>not referred by the customer with id = 2</strong>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Customer table:\n+----+------+------------+\n| id | name | referee_id |\n+----+------+------------+\n| 1  | Will | null       |\n| 2  | Jane | null       |\n| 3  | Alex | 2          |\n| 4  | Bill | null       |\n| 5  | Zack | 1          |\n+----+------+------------+\nOutput:\n+------+\n| name |\n+------+\n| Will |\n| Jane |\n| Bill |\n| Zack |\n+------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Customer (id INT, name TEXT, referee_id INT);\nINSERT INTO Customer VALUES (1, 'Will', NULL), (2, 'Jane', NULL), (3, 'Alex', 2), (4, 'Bill', NULL), (5, 'Zack', 1);",
                    "input": "Customer table with referee IDs [null, null, 2, null, 1]",
                    "expected_output": "[('Will',), ('Jane',), ('Bill',), ('Zack',)]",
                    "expected": [
                        [
                            "Will"
                        ],
                        [
                            "Jane"
                        ],
                        [
                            "Bill"
                        ],
                        [
                            "Zack"
                        ]
                    ]
                }
            ],
            "explanation": "Remember three-valued SQL logic: must explicitly include OR referee_id IS NULL.",
            "id": 39,
            "is_coding": true,
            "domain": "sql"
        },
        {
            "title": "LeetCode 620: Not Boring Movies",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nWrite a solution to report the movies with an <strong>odd-numbered ID</strong> and a description that is <strong>not 'boring'</strong>, ordered by <code>rating</code> in <strong>descending order</strong>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Cinema table:\n+----+------------+-------------+--------+\n| id | movie      | description | rating |\n+----+------------+-------------+--------+\n| 1  | War        | great 3D    | 8.9    |\n| 2  | Science    | fiction     | 8.5    |\n| 3  | irish      | boring      | 6.2    |\n| 4  | Ice song   | Fantacy     | 8.6    |\n| 5  | House card | Interesting | 9.1    |\n+----+------------+-------------+--------+\nOutput:\n+----+------------+-------------+--------+\n| id | movie      | description | rating |\n+----+------------+-------------+--------+\n| 5  | House card | Interesting | 9.1    |\n| 1  | War        | great 3D    | 8.9    |\n+----+------------+-------------+--------+</pre>",
            "starter_code": "-- Write your SQL query statement below\nSELECT ",
            "solution_code": "SELECT id, movie, description, rating\nFROM Cinema\nWHERE id % 2 = 1 AND description != 'boring'\nORDER BY rating DESC;",
            "test_cases": [
                {
                    "schema_sql": "CREATE TABLE Cinema (id INT, movie TEXT, description TEXT, rating REAL);\nINSERT INTO Cinema VALUES (1, 'War', 'great 3D', 8.9), (2, 'Science', 'fiction', 8.5), (3, 'irish', 'boring', 6.2), (4, 'Ice song', 'Fantacy', 8.6), (5, 'House card', 'Interesting', 9.1);",
                    "input": "Cinema table entries 1 to 5",
                    "expected_output": "[(5, 'House card', 'Interesting', 9.1), (1, 'War', 'great 3D', 8.9)]",
                    "expected": [
                        [
                            5,
                            "House card",
                            "Interesting",
                            9.1
                        ],
                        [
                            1,
                            "War",
                            "great 3D",
                            8.9
                        ]
                    ]
                }
            ],
            "explanation": "Filter with id % 2 = 1 and description != 'boring', then ORDER BY rating DESC.",
            "id": 40,
            "is_coding": true,
            "domain": "sql"
        }
    ],
    "oops": [
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 31,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 155: Min Stack",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a stack that supports push, pop, top, and retrieving the minimum element in constant time <code>O(1)</code>.<br><br>\nImplement the <code>MinStack</code> class:<br>\n\u2022 <code>MinStack()</code> initializes the stack object.<br>\n\u2022 <code>void push(int val)</code> pushes the element <code>val</code> onto the stack.<br>\n\u2022 <code>void pop()</code> removes the element on the top of the stack.<br>\n\u2022 <code>int top()</code> gets the top element of the stack.<br>\n\u2022 <code>int getMin()</code> retrieves the minimum element in the stack.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MinStack\",\"push\",\"push\",\"push\",\"getMin\",\"pop\",\"top\",\"getMin\"]\n[[],[-2],[0],[-3],[],[],[],[]]\nOutput: [null,null,null,null,-3,null,0,-2]</pre>",
            "starter_code": "class MinStack:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, val: int) -> None:\n        # Write only your solution logic here\n        pass\n\n    def pop(self) -> None:\n        # Write only your solution logic here\n        pass\n\n    def top(self) -> int:\n        # Write only your solution logic here\n        pass\n\n    def getMin(self) -> int:\n        # Write only your solution logic here\n        pass",
            "solution_code": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min_stack = []\n\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        min_val = min(val, self.min_stack[-1] if self.min_stack else val)\n        self.min_stack.append(min_val)\n\n    def pop(self) -> None:\n        self.stack.pop()\n        self.min_stack.pop()\n\n    def top(self) -> int:\n        return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min_stack[-1]",
            "test_cases": [
                {
                    "operations": [
                        "MinStack",
                        "push",
                        "push",
                        "push",
                        "getMin",
                        "pop",
                        "top",
                        "getMin"
                    ],
                    "args": [
                        [],
                        [
                            -2
                        ],
                        [
                            0
                        ],
                        [
                            -3
                        ],
                        [],
                        [],
                        [],
                        []
                    ],
                    "input": "MinStack() -> push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()",
                    "expected_output": "[null, null, null, null, -3, null, 0, -2]",
                    "expected": [
                        null,
                        null,
                        null,
                        null,
                        -3,
                        null,
                        0,
                        -2
                    ]
                }
            ],
            "explanation": "Maintain dual stacks: main stack for data and min_stack tracking current minimum at every depth. All operations O(1) time and space.",
            "id": 32,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 232: Implement Queue using Stacks",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement a first in first out (FIFO) queue using only two stacks.<br><br>\nImplement <code>MyQueue</code> class with <code>push(x)</code>, <code>pop()</code>, <code>peek()</code>, and <code>empty()</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput: [null, null, null, 1, 1, false]</pre>",
            "starter_code": "class MyQueue:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, x: int) -> None:\n        pass\n\n    def pop(self) -> int:\n        pass\n\n    def peek(self) -> int:\n        pass\n\n    def empty(self) -> bool:\n        pass",
            "solution_code": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def push(self, x: int) -> None:\n        self.in_stack.append(x)\n\n    def pop(self) -> int:\n        self.peek()\n        return self.out_stack.pop()\n\n    def peek(self) -> int:\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack[-1]\n\n    def empty(self) -> bool:\n        return not self.in_stack and not self.out_stack",
            "test_cases": [
                {
                    "operations": [
                        "MyQueue",
                        "push",
                        "push",
                        "peek",
                        "pop",
                        "empty"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [],
                        [],
                        []
                    ],
                    "input": "MyQueue() -> push(1), push(2), peek(), pop(), empty()",
                    "expected_output": "[null, null, null, 1, 1, false]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        1,
                        false
                    ]
                }
            ],
            "explanation": "Two stacks (in_stack and out_stack). Pop transfers elements when out_stack is empty. Amortized O(1) time per operation.",
            "id": 33,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 34,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 38,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 39,
            "is_coding": true,
            "domain": "oops"
        },
        {
            "title": "LeetCode 621: Task Scheduler",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a characters array <code>tasks</code> representing the tasks a CPU needs to do, and a non-negative integer <code>n</code> representing the cooldown period between identical tasks, return <em>the least number of units of times that the CPU will take to finish all the given tasks</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2\nOutput: 8\nExplanation: A -> B -> idle -> A -> B -> idle -> A -> B</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0\nOutput: 6</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= tasks.length <= 10<sup>4</sup></code><br>\n\u2022 <code>0 <= n <= 100</code>",
            "starter_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)",
            "test_cases": [
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2",
                    "expected_output": "8",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 2
                    },
                    "expected": 8
                },
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0",
                    "expected_output": "6",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 0
                    },
                    "expected": 6
                }
            ],
            "explanation": "Greedy calculation: arrange most frequent tasks into slots of length (n + 1). Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "oops"
        }
    ],
    "os": [
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 31,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 621: Task Scheduler",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a characters array <code>tasks</code> representing the tasks a CPU needs to do, and a non-negative integer <code>n</code> representing the cooldown period between identical tasks, return <em>the least number of units of times that the CPU will take to finish all the given tasks</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2\nOutput: 8\nExplanation: A -> B -> idle -> A -> B -> idle -> A -> B</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0\nOutput: 6</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= tasks.length <= 10<sup>4</sup></code><br>\n\u2022 <code>0 <= n <= 100</code>",
            "starter_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)",
            "test_cases": [
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2",
                    "expected_output": "8",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 2
                    },
                    "expected": 8
                },
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0",
                    "expected_output": "6",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 0
                    },
                    "expected": 6
                }
            ],
            "explanation": "Greedy calculation: arrange most frequent tasks into slots of length (n + 1). Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq). Time: O(n), Space: O(1).",
            "id": 32,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 253: Meeting Rooms II",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, return <em>the minimum number of conference rooms (or server resources) required</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[0,30],[5,10],[15,20]]\nOutput: 2</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[7,10],[2,4]]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= intervals.length <= 10<sup>4</sup></code>",
            "starter_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    if not intervals: return 0\n    starts = sorted([i[0] for i in intervals])\n    ends = sorted([i[1] for i in intervals])\n    s_ptr = e_ptr = 0\n    used_rooms = max_rooms = 0\n    while s_ptr < len(starts):\n        if starts[s_ptr] < ends[e_ptr]:\n            used_rooms += 1\n            max_rooms = max(max_rooms, used_rooms)\n            s_ptr += 1\n        else:\n            used_rooms -= 1\n            e_ptr += 1\n    return max_rooms",
            "test_cases": [
                {
                    "input": "intervals = [[0,30],[5,10],[15,20]]",
                    "expected_output": "2",
                    "raw_input": {
                        "intervals": [
                            [
                                0,
                                30
                            ],
                            [
                                5,
                                10
                            ],
                            [
                                15,
                                20
                            ]
                        ]
                    },
                    "expected": 2
                },
                {
                    "input": "intervals = [[7,10],[2,4]]",
                    "expected_output": "1",
                    "raw_input": {
                        "intervals": [
                            [
                                7,
                                10
                            ],
                            [
                                2,
                                4
                            ]
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Sort start times and end times separately. Track overlapping intervals with two pointers. Time: O(n log n), Space: O(n).",
            "id": 33,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 155: Min Stack",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a stack that supports push, pop, top, and retrieving the minimum element in constant time <code>O(1)</code>.<br><br>\nImplement the <code>MinStack</code> class:<br>\n\u2022 <code>MinStack()</code> initializes the stack object.<br>\n\u2022 <code>void push(int val)</code> pushes the element <code>val</code> onto the stack.<br>\n\u2022 <code>void pop()</code> removes the element on the top of the stack.<br>\n\u2022 <code>int top()</code> gets the top element of the stack.<br>\n\u2022 <code>int getMin()</code> retrieves the minimum element in the stack.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MinStack\",\"push\",\"push\",\"push\",\"getMin\",\"pop\",\"top\",\"getMin\"]\n[[],[-2],[0],[-3],[],[],[],[]]\nOutput: [null,null,null,null,-3,null,0,-2]</pre>",
            "starter_code": "class MinStack:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, val: int) -> None:\n        # Write only your solution logic here\n        pass\n\n    def pop(self) -> None:\n        # Write only your solution logic here\n        pass\n\n    def top(self) -> int:\n        # Write only your solution logic here\n        pass\n\n    def getMin(self) -> int:\n        # Write only your solution logic here\n        pass",
            "solution_code": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min_stack = []\n\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        min_val = min(val, self.min_stack[-1] if self.min_stack else val)\n        self.min_stack.append(min_val)\n\n    def pop(self) -> None:\n        self.stack.pop()\n        self.min_stack.pop()\n\n    def top(self) -> int:\n        return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min_stack[-1]",
            "test_cases": [
                {
                    "operations": [
                        "MinStack",
                        "push",
                        "push",
                        "push",
                        "getMin",
                        "pop",
                        "top",
                        "getMin"
                    ],
                    "args": [
                        [],
                        [
                            -2
                        ],
                        [
                            0
                        ],
                        [
                            -3
                        ],
                        [],
                        [],
                        [],
                        []
                    ],
                    "input": "MinStack() -> push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()",
                    "expected_output": "[null, null, null, null, -3, null, 0, -2]",
                    "expected": [
                        null,
                        null,
                        null,
                        null,
                        -3,
                        null,
                        0,
                        -2
                    ]
                }
            ],
            "explanation": "Maintain dual stacks: main stack for data and min_stack tracking current minimum at every depth. All operations O(1) time and space.",
            "id": 35,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 232: Implement Queue using Stacks",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement a first in first out (FIFO) queue using only two stacks.<br><br>\nImplement <code>MyQueue</code> class with <code>push(x)</code>, <code>pop()</code>, <code>peek()</code>, and <code>empty()</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput: [null, null, null, 1, 1, false]</pre>",
            "starter_code": "class MyQueue:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, x: int) -> None:\n        pass\n\n    def pop(self) -> int:\n        pass\n\n    def peek(self) -> int:\n        pass\n\n    def empty(self) -> bool:\n        pass",
            "solution_code": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def push(self, x: int) -> None:\n        self.in_stack.append(x)\n\n    def pop(self) -> int:\n        self.peek()\n        return self.out_stack.pop()\n\n    def peek(self) -> int:\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack[-1]\n\n    def empty(self) -> bool:\n        return not self.in_stack and not self.out_stack",
            "test_cases": [
                {
                    "operations": [
                        "MyQueue",
                        "push",
                        "push",
                        "peek",
                        "pop",
                        "empty"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [],
                        [],
                        []
                    ],
                    "input": "MyQueue() -> push(1), push(2), peek(), pop(), empty()",
                    "expected_output": "[null, null, null, 1, 1, false]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        1,
                        false
                    ]
                }
            ],
            "explanation": "Two stacks (in_stack and out_stack). Pop transfers elements when out_stack is empty. Amortized O(1) time per operation.",
            "id": 36,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 37,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 39,
            "is_coding": true,
            "domain": "os"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 40,
            "is_coding": true,
            "domain": "os"
        }
    ],
    "cn": [
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 31,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 33,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 125: Valid Palindrome",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nA phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.<br><br>\nGiven a string <code>s</code>, return <code>true</code> <em>if it is a palindrome, or <code>false</code> otherwise</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"A man, a plan, a canal: Panama\"\nOutput: true\nExplanation: \"amanaplanacanalpanama\" is a palindrome.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"race a car\"\nOutput: false\nExplanation: \"raceacar\" is not a palindrome.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 2 * 10<sup>5</sup></code><br>\n\u2022 <code>s</code> consists only of printable ASCII characters.",
            "starter_code": "def isPalindrome(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isPalindrome(s: str) -> bool:\n    filtered = [c.lower() for c in s if c.isalnum()]\n    return filtered == filtered[::-1]",
            "test_cases": [
                {
                    "input": "s = \"A man, a plan, a canal: Panama\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "A man, a plan, a canal: Panama"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"race a car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "race a car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \" \"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": " "
                    },
                    "expected": true
                }
            ],
            "explanation": "Clean string by retaining only alphanumeric characters in lowercase and verify symmetry. Time: O(n), Space: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 37,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "cn"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "cn"
        }
    ],
    "web_dev": [
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 32,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 33,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 36,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 37,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "web_dev"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "web_dev"
        }
    ],
    "react": [
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 31,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 33,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 3: Longest Substring Without Repeating Characters",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code>, find the length of the <strong>longest substring</strong> without repeating characters.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"abcabcbb\"\nOutput: 3\nExplanation: The answer is \"abc\", with the length of 3.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"bbbbb\"\nOutput: 1\nExplanation: The answer is \"b\", with the length of 1.</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"pwwkew\"\nOutput: 3\nExplanation: The answer is \"wke\", with the length of 3.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>0 <= s.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of English letters, digits, symbols and spaces.",
            "starter_code": "def lengthOfLongestSubstring(s: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def lengthOfLongestSubstring(s: str) -> int:\n    used = {}\n    max_len = start = 0\n    for i, c in enumerate(s):\n        if c in used and start <= used[c]:\n            start = used[c] + 1\n        else:\n            max_len = max(max_len, i - start + 1)\n        used[c] = i\n    return max_len",
            "test_cases": [
                {
                    "input": "s = \"abcabcbb\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "abcabcbb"
                    },
                    "expected": 3
                },
                {
                    "input": "s = \"bbbbb\"",
                    "expected_output": "1",
                    "raw_input": {
                        "s": "bbbbb"
                    },
                    "expected": 1
                },
                {
                    "input": "s = \"pwwkew\"",
                    "expected_output": "3",
                    "raw_input": {
                        "s": "pwwkew"
                    },
                    "expected": 3
                }
            ],
            "explanation": "Sliding Window with Hash Map to store last seen index of each character. Time: O(n), Space: O(min(m, n)).",
            "id": 36,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 70: Climbing Stairs",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are climbing a staircase. It takes <code>n</code> steps to reach the top.<br><br>\nEach time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 2\nOutput: 2\nExplanation: There are two ways: 1 step + 1 step, or 2 steps.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: n = 3\nOutput: 3\nExplanation: There are three ways: (1+1+1), (1+2), or (2+1).</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= n <= 45</code>",
            "starter_code": "def climbStairs(n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def climbStairs(n: int) -> int:\n    if n <= 2:\n        return n\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    return b",
            "test_cases": [
                {
                    "input": "n = 2",
                    "expected_output": "2",
                    "raw_input": {
                        "n": 2
                    },
                    "expected": 2
                },
                {
                    "input": "n = 3",
                    "expected_output": "3",
                    "raw_input": {
                        "n": 3
                    },
                    "expected": 3
                },
                {
                    "input": "n = 5",
                    "expected_output": "8",
                    "raw_input": {
                        "n": 5
                    },
                    "expected": 8
                }
            ],
            "explanation": "Fibonacci dynamic programming relation: ways(n) = ways(n-1) + ways(n-2). Time: O(n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "react"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "react"
        }
    ],
    "nodejs": [
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 34,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 35,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 38,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "nodejs"
        },
        {
            "title": "LeetCode 621: Task Scheduler",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a characters array <code>tasks</code> representing the tasks a CPU needs to do, and a non-negative integer <code>n</code> representing the cooldown period between identical tasks, return <em>the least number of units of times that the CPU will take to finish all the given tasks</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2\nOutput: 8\nExplanation: A -> B -> idle -> A -> B -> idle -> A -> B</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0\nOutput: 6</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= tasks.length <= 10<sup>4</sup></code><br>\n\u2022 <code>0 <= n <= 100</code>",
            "starter_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)",
            "test_cases": [
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2",
                    "expected_output": "8",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 2
                    },
                    "expected": 8
                },
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0",
                    "expected_output": "6",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 0
                    },
                    "expected": 6
                }
            ],
            "explanation": "Greedy calculation: arrange most frequent tasks into slots of length (n + 1). Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq). Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "nodejs"
        }
    ],
    "rest_api": [
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 32,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 33,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 36,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 37,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 39,
            "is_coding": true,
            "domain": "rest_api"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "rest_api"
        }
    ],
    "django": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 35,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 36,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "django"
        },
        {
            "title": "LeetCode 242: Valid Anagram",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise</em>.<br><br>\nAn <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"anagram\", t = \"nagaram\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"rat\", t = \"car\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length, t.length <= 5 * 10<sup>4</sup></code><br>\n\u2022 <code>s</code> and <code>t</code> consist of lowercase English letters.",
            "starter_code": "def isAnagram(s: str, t: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isAnagram(s: str, t: str) -> bool:\n    if len(s) != len(t):\n        return False\n    from collections import Counter\n    return Counter(s) == Counter(t)",
            "test_cases": [
                {
                    "input": "s = \"anagram\", t = \"nagaram\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "anagram",
                        "t": "nagaram"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"rat\", t = \"car\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "rat",
                        "t": "car"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"a\", t = \"ab\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "a",
                        "t": "ab"
                    },
                    "expected": false
                }
            ],
            "explanation": "Compare character frequencies using hash table or fixed array of 26 letters. Time: O(n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "django"
        }
    ],
    "flask": [
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 35,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "flask"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 40,
            "is_coding": true,
            "domain": "flask"
        }
    ],
    "spring_boot": [
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 32,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 155: Min Stack",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a stack that supports push, pop, top, and retrieving the minimum element in constant time <code>O(1)</code>.<br><br>\nImplement the <code>MinStack</code> class:<br>\n\u2022 <code>MinStack()</code> initializes the stack object.<br>\n\u2022 <code>void push(int val)</code> pushes the element <code>val</code> onto the stack.<br>\n\u2022 <code>void pop()</code> removes the element on the top of the stack.<br>\n\u2022 <code>int top()</code> gets the top element of the stack.<br>\n\u2022 <code>int getMin()</code> retrieves the minimum element in the stack.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MinStack\",\"push\",\"push\",\"push\",\"getMin\",\"pop\",\"top\",\"getMin\"]\n[[],[-2],[0],[-3],[],[],[],[]]\nOutput: [null,null,null,null,-3,null,0,-2]</pre>",
            "starter_code": "class MinStack:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, val: int) -> None:\n        # Write only your solution logic here\n        pass\n\n    def pop(self) -> None:\n        # Write only your solution logic here\n        pass\n\n    def top(self) -> int:\n        # Write only your solution logic here\n        pass\n\n    def getMin(self) -> int:\n        # Write only your solution logic here\n        pass",
            "solution_code": "class MinStack:\n    def __init__(self):\n        self.stack = []\n        self.min_stack = []\n\n    def push(self, val: int) -> None:\n        self.stack.append(val)\n        min_val = min(val, self.min_stack[-1] if self.min_stack else val)\n        self.min_stack.append(min_val)\n\n    def pop(self) -> None:\n        self.stack.pop()\n        self.min_stack.pop()\n\n    def top(self) -> int:\n        return self.stack[-1]\n\n    def getMin(self) -> int:\n        return self.min_stack[-1]",
            "test_cases": [
                {
                    "operations": [
                        "MinStack",
                        "push",
                        "push",
                        "push",
                        "getMin",
                        "pop",
                        "top",
                        "getMin"
                    ],
                    "args": [
                        [],
                        [
                            -2
                        ],
                        [
                            0
                        ],
                        [
                            -3
                        ],
                        [],
                        [],
                        [],
                        []
                    ],
                    "input": "MinStack() -> push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()",
                    "expected_output": "[null, null, null, null, -3, null, 0, -2]",
                    "expected": [
                        null,
                        null,
                        null,
                        null,
                        -3,
                        null,
                        0,
                        -2
                    ]
                }
            ],
            "explanation": "Maintain dual stacks: main stack for data and min_stack tracking current minimum at every depth. All operations O(1) time and space.",
            "id": 33,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 232: Implement Queue using Stacks",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement a first in first out (FIFO) queue using only two stacks.<br><br>\nImplement <code>MyQueue</code> class with <code>push(x)</code>, <code>pop()</code>, <code>peek()</code>, and <code>empty()</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput: [null, null, null, 1, 1, false]</pre>",
            "starter_code": "class MyQueue:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, x: int) -> None:\n        pass\n\n    def pop(self) -> int:\n        pass\n\n    def peek(self) -> int:\n        pass\n\n    def empty(self) -> bool:\n        pass",
            "solution_code": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def push(self, x: int) -> None:\n        self.in_stack.append(x)\n\n    def pop(self) -> int:\n        self.peek()\n        return self.out_stack.pop()\n\n    def peek(self) -> int:\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack[-1]\n\n    def empty(self) -> bool:\n        return not self.in_stack and not self.out_stack",
            "test_cases": [
                {
                    "operations": [
                        "MyQueue",
                        "push",
                        "push",
                        "peek",
                        "pop",
                        "empty"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [],
                        [],
                        []
                    ],
                    "input": "MyQueue() -> push(1), push(2), peek(), pop(), empty()",
                    "expected_output": "[null, null, null, 1, 1, false]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        1,
                        false
                    ]
                }
            ],
            "explanation": "Two stacks (in_stack and out_stack). Pop transfers elements when out_stack is empty. Amortized O(1) time per operation.",
            "id": 34,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 35,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 37,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 38,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 39,
            "is_coding": true,
            "domain": "spring_boot"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "spring_boot"
        }
    ],
    "ai": [
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 31,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 32,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 34,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 35,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 36,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 11: Container With Most Water",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.<br><br>\nFind two lines that together with the x-axis form a container, such that the container contains the most water. Return <em>the maximum amount of water a container can store</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,8,6,2,5,4,8,3,7]\nOutput: 49</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: height = [1,1]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= height.length <= 10<sup>5</sup></code>",
            "starter_code": "def maxArea(height: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxArea(height: list[int]) -> int:\n    l, r = 0, len(height) - 1\n    max_a = 0\n    while l < r:\n        h = min(height[l], height[r])\n        max_a = max(max_a, h * (r - l))\n        if height[l] < height[r]:\n            l += 1\n        else:\n            r -= 1\n    return max_a",
            "test_cases": [
                {
                    "input": "height = [1,8,6,2,5,4,8,3,7]",
                    "expected_output": "49",
                    "raw_input": {
                        "height": [
                            1,
                            8,
                            6,
                            2,
                            5,
                            4,
                            8,
                            3,
                            7
                        ]
                    },
                    "expected": 49
                },
                {
                    "input": "height = [1,1]",
                    "expected_output": "1",
                    "raw_input": {
                        "height": [
                            1,
                            1
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Two pointers at left and right boundaries. Move the pointer with smaller height inward. Time: O(n), Space: O(1).",
            "id": 37,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 215: Kth Largest Element in an Array",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k<sup>th</sup></code> largest element in the array.<br><br>\nNote that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,1,5,6,4], k = 2\nOutput: 5</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,3,1,2,4,5,5,6], k = 4\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= k <= nums.length <= 10<sup>5</sup></code>",
            "starter_code": "def findKthLargest(nums: list[int], k: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def findKthLargest(nums: list[int], k: int) -> int:\n    import heapq\n    min_heap = []\n    for x in nums:\n        heapq.heappush(min_heap, x)\n        if len(min_heap) > k:\n            heapq.heappop(min_heap)\n    return min_heap[0]",
            "test_cases": [
                {
                    "input": "nums = [3,2,1,5,6,4], k = 2",
                    "expected_output": "5",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            1,
                            5,
                            6,
                            4
                        ],
                        "k": 2
                    },
                    "expected": 5
                },
                {
                    "input": "nums = [3,2,3,1,2,4,5,5,6], k = 4",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            3,
                            1,
                            2,
                            4,
                            5,
                            5,
                            6
                        ],
                        "k": 4
                    },
                    "expected": 4
                }
            ],
            "explanation": "Maintain a Min-Heap of size k. After scanning nums, the root of the heap is the k-th largest element. Time: O(n log k), Space: O(k).",
            "id": 39,
            "is_coding": true,
            "domain": "ai"
        },
        {
            "title": "LeetCode 15: 3Sum",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.<br><br>\nNotice that the solution set must not contain duplicate triplets.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,1]\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>3 <= nums.length <= 3000</code>",
            "starter_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i - 1]:\n            continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            s = nums[i] + nums[l] + nums[r]\n            if s == 0:\n                res.append([nums[i], nums[l], nums[r]])\n                while l < r and nums[l] == nums[l + 1]: l += 1\n                while l < r and nums[r] == nums[r - 1]: r -= 1\n                l += 1\n                r -= 1\n            elif s < 0:\n                l += 1\n            else:\n                r -= 1\n    return res",
            "test_cases": [
                {
                    "input": "nums = [-1,0,1,2,-1,-4]",
                    "expected_output": "[[-1, -1, 2], [-1, 0, 1]]",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            1,
                            2,
                            -1,
                            -4
                        ]
                    },
                    "expected": [
                        [
                            -1,
                            -1,
                            2
                        ],
                        [
                            -1,
                            0,
                            1
                        ]
                    ]
                },
                {
                    "input": "nums = [0,1,1]",
                    "expected_output": "[]",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            1
                        ]
                    },
                    "expected": []
                }
            ],
            "explanation": "Sort the array, then iterate through elements and use two pointers (left & right) for 2Sum. Skip duplicates. Time: O(n^2), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "ai"
        }
    ],
    "ml": [
        {
            "title": "LeetCode 215: Kth Largest Element in an Array",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k<sup>th</sup></code> largest element in the array.<br><br>\nNote that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,1,5,6,4], k = 2\nOutput: 5</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,3,1,2,4,5,5,6], k = 4\nOutput: 4</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= k <= nums.length <= 10<sup>5</sup></code>",
            "starter_code": "def findKthLargest(nums: list[int], k: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def findKthLargest(nums: list[int], k: int) -> int:\n    import heapq\n    min_heap = []\n    for x in nums:\n        heapq.heappush(min_heap, x)\n        if len(min_heap) > k:\n            heapq.heappop(min_heap)\n    return min_heap[0]",
            "test_cases": [
                {
                    "input": "nums = [3,2,1,5,6,4], k = 2",
                    "expected_output": "5",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            1,
                            5,
                            6,
                            4
                        ],
                        "k": 2
                    },
                    "expected": 5
                },
                {
                    "input": "nums = [3,2,3,1,2,4,5,5,6], k = 4",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            3,
                            1,
                            2,
                            4,
                            5,
                            5,
                            6
                        ],
                        "k": 4
                    },
                    "expected": 4
                }
            ],
            "explanation": "Maintain a Min-Heap of size k. After scanning nums, the root of the heap is the k-th largest element. Time: O(n log k), Space: O(k).",
            "id": 31,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 53: Maximum Subarray",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: The subarray [4,-1,2,1] has the largest sum 6.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1]\nOutput: 1</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [5,4,-1,7,8]\nOutput: 23</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxSubArray(nums: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxSubArray(nums: list[int]) -> int:\n    max_so_far = nums[0]\n    cur_sum = 0\n    for x in nums:\n        cur_sum = max(x, cur_sum + x)\n        max_so_far = max(max_so_far, cur_sum)\n    return max_so_far",
            "test_cases": [
                {
                    "input": "nums = [-2,1,-3,4,-1,2,1,-5,4]",
                    "expected_output": "6",
                    "raw_input": {
                        "nums": [
                            -2,
                            1,
                            -3,
                            4,
                            -1,
                            2,
                            1,
                            -5,
                            4
                        ]
                    },
                    "expected": 6
                },
                {
                    "input": "nums = [1]",
                    "expected_output": "1",
                    "raw_input": {
                        "nums": [
                            1
                        ]
                    },
                    "expected": 1
                },
                {
                    "input": "nums = [5,4,-1,7,8]",
                    "expected_output": "23",
                    "raw_input": {
                        "nums": [
                            5,
                            4,
                            -1,
                            7,
                            8
                        ]
                    },
                    "expected": 23
                }
            ],
            "explanation": "Kadane's Dynamic Programming Algorithm: cur_sum = max(x, cur_sum + x). Time: O(n), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 238: Product of Array Except Self",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <em>an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code></em>.<br><br>\nYou must write an algorithm that runs in <code>O(n)</code> time and without using the division operator.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: [24,12,8,6]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,1,0,-3,3]\nOutput: [0,0,9,0,0]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-30 <= nums[i] <= 30</code>",
            "starter_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    prefix = 1\n    for i in range(n):\n        res[i] = prefix\n        prefix *= nums[i]\n    postfix = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= postfix\n        postfix *= nums[i]\n    return res",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "[24, 12, 8, 6]",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": [
                        24,
                        12,
                        8,
                        6
                    ]
                },
                {
                    "input": "nums = [-1,1,0,-3,3]",
                    "expected_output": "[0, 0, 9, 0, 0]",
                    "raw_input": {
                        "nums": [
                            -1,
                            1,
                            0,
                            -3,
                            3
                        ]
                    },
                    "expected": [
                        0,
                        0,
                        9,
                        0,
                        0
                    ]
                }
            ],
            "explanation": "Compute prefix products in first pass, then accumulate postfix products in backward pass. Time: O(n), Space: O(1) auxiliary.",
            "id": 34,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 704: Binary Search",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> which is sorted in ascending order, and an integer <code>target</code>, write a function to search <code>target</code> in <code>nums</code>. If <code>target</code> exists, then return its index. Otherwise, return <code>-1</code>.<br><br>\nYou must write an algorithm with <code>O(log n)</code> runtime complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 All integers in <code>nums</code> are unique and sorted.",
            "starter_code": "def search(nums: list[int], target: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def search(nums: list[int], target: int) -> int:\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1",
            "test_cases": [
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 9",
                    "expected_output": "4",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 9
                    },
                    "expected": 4
                },
                {
                    "input": "nums = [-1,0,3,5,9,12], target = 2",
                    "expected_output": "-1",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            3,
                            5,
                            9,
                            12
                        ],
                        "target": 2
                    },
                    "expected": -1
                },
                {
                    "input": "nums = [5], target = 5",
                    "expected_output": "0",
                    "raw_input": {
                        "nums": [
                            5
                        ],
                        "target": 5
                    },
                    "expected": 0
                }
            ],
            "explanation": "Classic Binary Search with left and right pointers. Halves search space each iteration. Time: O(log n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 121: Best Time to Buy and Sell Stock",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nYou are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.<br><br>\nYou want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.<br><br>\nReturn <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,1,5,3,6,4]\nOutput: 5\nExplanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: prices = [7,6,4,3,1]\nOutput: 0\nExplanation: In this case, no transactions are done and the max profit = 0.</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= prices.length <= 10<sup>5</sup></code><br>\n\u2022 <code>0 <= prices[i] <= 10<sup>4</sup></code>",
            "starter_code": "def maxProfit(prices: list[int]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def maxProfit(prices: list[int]) -> int:\n    min_price = float('inf')\n    max_p = 0\n    for p in prices:\n        if p < min_price:\n            min_price = p\n        elif p - min_price > max_p:\n            max_p = p - min_price\n    return max_p",
            "test_cases": [
                {
                    "input": "prices = [7,1,5,3,6,4]",
                    "expected_output": "5",
                    "raw_input": {
                        "prices": [
                            7,
                            1,
                            5,
                            3,
                            6,
                            4
                        ]
                    },
                    "expected": 5
                },
                {
                    "input": "prices = [7,6,4,3,1]",
                    "expected_output": "0",
                    "raw_input": {
                        "prices": [
                            7,
                            6,
                            4,
                            3,
                            1
                        ]
                    },
                    "expected": 0
                },
                {
                    "input": "prices = [2,4,1]",
                    "expected_output": "2",
                    "raw_input": {
                        "prices": [
                            2,
                            4,
                            1
                        ]
                    },
                    "expected": 2
                }
            ],
            "explanation": "Single-pass algorithm tracking lowest price seen so far. Time Complexity: O(n), Space Complexity: O(1).",
            "id": 36,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 217: Contains Duplicate",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,1]\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [1,2,3,4]\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= nums.length <= 10<sup>5</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>",
            "starter_code": "def containsDuplicate(nums: list[int]) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def containsDuplicate(nums: list[int]) -> bool:\n    return len(nums) != len(set(nums))",
            "test_cases": [
                {
                    "input": "nums = [1,2,3,1]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            1
                        ]
                    },
                    "expected": true
                },
                {
                    "input": "nums = [1,2,3,4]",
                    "expected_output": "false",
                    "raw_input": {
                        "nums": [
                            1,
                            2,
                            3,
                            4
                        ]
                    },
                    "expected": false
                },
                {
                    "input": "nums = [1,1,1,3,3,4,3,2,4,2]",
                    "expected_output": "true",
                    "raw_input": {
                        "nums": [
                            1,
                            1,
                            1,
                            3,
                            3,
                            4,
                            3,
                            2,
                            4,
                            2
                        ]
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a hash set to detect duplicate values in O(1) amortized lookup. Time: O(n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 38,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 39,
            "is_coding": true,
            "domain": "ml"
        },
        {
            "title": "LeetCode 15: 3Sum",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.<br><br>\nNotice that the solution set must not contain duplicate triplets.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [-1,0,1,2,-1,-4]\nOutput: [[-1,-1,2],[-1,0,1]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [0,1,1]\nOutput: []</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>3 <= nums.length <= 3000</code>",
            "starter_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def threeSum(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    for i in range(len(nums) - 2):\n        if i > 0 and nums[i] == nums[i - 1]:\n            continue\n        l, r = i + 1, len(nums) - 1\n        while l < r:\n            s = nums[i] + nums[l] + nums[r]\n            if s == 0:\n                res.append([nums[i], nums[l], nums[r]])\n                while l < r and nums[l] == nums[l + 1]: l += 1\n                while l < r and nums[r] == nums[r - 1]: r -= 1\n                l += 1\n                r -= 1\n            elif s < 0:\n                l += 1\n            else:\n                r -= 1\n    return res",
            "test_cases": [
                {
                    "input": "nums = [-1,0,1,2,-1,-4]",
                    "expected_output": "[[-1, -1, 2], [-1, 0, 1]]",
                    "raw_input": {
                        "nums": [
                            -1,
                            0,
                            1,
                            2,
                            -1,
                            -4
                        ]
                    },
                    "expected": [
                        [
                            -1,
                            -1,
                            2
                        ],
                        [
                            -1,
                            0,
                            1
                        ]
                    ]
                },
                {
                    "input": "nums = [0,1,1]",
                    "expected_output": "[]",
                    "raw_input": {
                        "nums": [
                            0,
                            1,
                            1
                        ]
                    },
                    "expected": []
                }
            ],
            "explanation": "Sort the array, then iterate through elements and use two pointers (left & right) for 2Sum. Skip duplicates. Time: O(n^2), Space: O(1) auxiliary.",
            "id": 40,
            "is_coding": true,
            "domain": "ml"
        }
    ],
    "devops": [
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 31,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 32,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 33,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 621: Task Scheduler",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a characters array <code>tasks</code> representing the tasks a CPU needs to do, and a non-negative integer <code>n</code> representing the cooldown period between identical tasks, return <em>the least number of units of times that the CPU will take to finish all the given tasks</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2\nOutput: 8\nExplanation: A -> B -> idle -> A -> B -> idle -> A -> B</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0\nOutput: 6</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= tasks.length <= 10<sup>4</sup></code><br>\n\u2022 <code>0 <= n <= 100</code>",
            "starter_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)",
            "test_cases": [
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2",
                    "expected_output": "8",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 2
                    },
                    "expected": 8
                },
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0",
                    "expected_output": "6",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 0
                    },
                    "expected": 6
                }
            ],
            "explanation": "Greedy calculation: arrange most frequent tasks into slots of length (n + 1). Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq). Time: O(n), Space: O(1).",
            "id": 34,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 35,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 20: Valid Parentheses",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>s</code> containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.<br><br>\nAn input string is valid if:<br>\n1. Open brackets must be closed by the same type of brackets.<br>\n2. Open brackets must be closed in the correct order.<br>\n3. Every close bracket has a corresponding open bracket of the same type.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()\"\nOutput: true</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"()[]{}\"\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: s = \"(]\"\nOutput: false</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= s.length <= 10<sup>4</sup></code><br>\n\u2022 <code>s</code> consists of parentheses only <code>'()[]{}'</code>.",
            "starter_code": "def isValid(s: str) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isValid(s: str) -> bool:\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            top = stack.pop() if stack else '#'\n            if mapping[char] != top:\n                return False\n        else:\n            stack.append(char)\n    return not stack",
            "test_cases": [
                {
                    "input": "s = \"()\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"()[]{}\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "()[]{}"
                    },
                    "expected": true
                },
                {
                    "input": "s = \"(]\"",
                    "expected_output": "false",
                    "raw_input": {
                        "s": "(]"
                    },
                    "expected": false
                },
                {
                    "input": "s = \"([{}])\"",
                    "expected_output": "true",
                    "raw_input": {
                        "s": "([{}])"
                    },
                    "expected": true
                }
            ],
            "explanation": "Use a Stack (LIFO). Push opening brackets; when closing bracket is seen, pop and match. Time: O(n), Space: O(n).",
            "id": 36,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 253: Meeting Rooms II",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, return <em>the minimum number of conference rooms (or server resources) required</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[0,30],[5,10],[15,20]]\nOutput: 2</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[7,10],[2,4]]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= intervals.length <= 10<sup>4</sup></code>",
            "starter_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    if not intervals: return 0\n    starts = sorted([i[0] for i in intervals])\n    ends = sorted([i[1] for i in intervals])\n    s_ptr = e_ptr = 0\n    used_rooms = max_rooms = 0\n    while s_ptr < len(starts):\n        if starts[s_ptr] < ends[e_ptr]:\n            used_rooms += 1\n            max_rooms = max(max_rooms, used_rooms)\n            s_ptr += 1\n        else:\n            used_rooms -= 1\n            e_ptr += 1\n    return max_rooms",
            "test_cases": [
                {
                    "input": "intervals = [[0,30],[5,10],[15,20]]",
                    "expected_output": "2",
                    "raw_input": {
                        "intervals": [
                            [
                                0,
                                30
                            ],
                            [
                                5,
                                10
                            ],
                            [
                                15,
                                20
                            ]
                        ]
                    },
                    "expected": 2
                },
                {
                    "input": "intervals = [[7,10],[2,4]]",
                    "expected_output": "1",
                    "raw_input": {
                        "intervals": [
                            [
                                7,
                                10
                            ],
                            [
                                2,
                                4
                            ]
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Sort start times and end times separately. Track overlapping intervals with two pointers. Time: O(n log n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 39,
            "is_coding": true,
            "domain": "devops"
        },
        {
            "title": "LeetCode 2727: Is Object Empty",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an object or an array <code>obj</code>, return <code>true</code> if it is empty (contains no key-value pairs or elements), and <code>false</code> otherwise.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {\"x\": 5, \"y\": 42}\nOutput: false</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = {}\nOutput: true</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: obj = [null, false, 0]\nOutput: false</pre>",
            "starter_code": "def isEmpty(obj) -> bool:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def isEmpty(obj) -> bool:\n    return len(obj) == 0",
            "test_cases": [
                {
                    "input": "obj = {\"x\": 5, \"y\": 42}",
                    "expected_output": "false",
                    "raw_input": {
                        "obj": {
                            "x": 5,
                            "y": 42
                        }
                    },
                    "expected": false
                },
                {
                    "input": "obj = {}",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": {}
                    },
                    "expected": true
                },
                {
                    "input": "obj = []",
                    "expected_output": "true",
                    "raw_input": {
                        "obj": []
                    },
                    "expected": true
                }
            ],
            "explanation": "Check if length of keys/elements is 0. Time: O(1), Space: O(1).",
            "id": 40,
            "is_coding": true,
            "domain": "devops"
        }
    ],
    "aws": [
        {
            "title": "LeetCode 468: Validate IP Address",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.<br><br>\nA valid IPv4 is four decimal numbers separated by dots, each 0-255 without leading zeros.<br>\nA valid IPv6 is eight groups of four hexadecimal digits separated by colons.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"172.16.254.1\"\nOutput: \"IPv4\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"\nOutput: \"IPv6\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: queryIP = \"256.256.256.256\"\nOutput: \"Neither\"</pre>",
            "starter_code": "def validIPAddress(queryIP: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def validIPAddress(queryIP: str) -> str:\n    if '.' in queryIP:\n        parts = queryIP.split('.')\n        if len(parts) != 4: return \"Neither\"\n        for p in parts:\n            if not p or not p.isdigit() or (len(p) > 1 and p[0] == '0'):\n                return \"Neither\"\n            if not (0 <= int(p) <= 255):\n                return \"Neither\"\n        return \"IPv4\"\n    elif ':' in queryIP:\n        parts = queryIP.split(':')\n        if len(parts) != 8: return \"Neither\"\n        hexdigits = \"0123456789abcdefABCDEF\"\n        for p in parts:\n            if not p or len(p) > 4 or any(c not in hexdigits for c in p):\n                return \"Neither\"\n        return \"IPv6\"\n    return \"Neither\" ",
            "test_cases": [
                {
                    "input": "queryIP = \"172.16.254.1\"",
                    "expected_output": "\"IPv4\"",
                    "raw_input": {
                        "queryIP": "172.16.254.1"
                    },
                    "expected": "IPv4"
                },
                {
                    "input": "queryIP = \"2001:0db8:85a3:0:0:8A2E:0370:7334\"",
                    "expected_output": "\"IPv6\"",
                    "raw_input": {
                        "queryIP": "2001:0db8:85a3:0:0:8A2E:0370:7334"
                    },
                    "expected": "IPv6"
                },
                {
                    "input": "queryIP = \"256.256.256.256\"",
                    "expected_output": "\"Neither\"",
                    "raw_input": {
                        "queryIP": "256.256.256.256"
                    },
                    "expected": "Neither"
                }
            ],
            "explanation": "Inspect delimiters. Validate 4 octets [0-255] no leading zeros for IPv4; validate 8 hex segments of 1-4 chars for IPv6. Time: O(1), Space: O(1).",
            "id": 31,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 71: Simplify Path",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an absolute path for a Unix-style file system, which begins with a slash <code>'/'</code>, transform this path into its <strong>simplified canonical path</strong>.<br><br>\nThe rules are:<br>\n\u2022 A single period <code>'.'</code> refers to the current directory.<br>\n\u2022 A double period <code>'..'</code> refers to the directory up a level.<br>\n\u2022 Multiple consecutive slashes such as <code>'//'</code> are treated as a single slash <code>'/'</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/\"\nOutput: \"/home\"</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home//foo/\"\nOutput: \"/home/foo\"</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: path = \"/home/user/Documents/../Pictures\"\nOutput: \"/home/user/Pictures\"</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= path.length <= 3000</code>",
            "starter_code": "def simplifyPath(path: str) -> str:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '..':\n            if stack:\n                stack.pop()\n        elif p and p != '.':\n            stack.append(p)\n    return '/' + '/'.join(stack)",
            "test_cases": [
                {
                    "input": "path = \"/home/\"",
                    "expected_output": "\"/home\"",
                    "raw_input": {
                        "path": "/home/"
                    },
                    "expected": "/home"
                },
                {
                    "input": "path = \"/home//foo/\"",
                    "expected_output": "\"/home/foo\"",
                    "raw_input": {
                        "path": "/home//foo/"
                    },
                    "expected": "/home/foo"
                },
                {
                    "input": "path = \"/home/user/Documents/../Pictures\"",
                    "expected_output": "\"/home/user/Pictures\"",
                    "raw_input": {
                        "path": "/home/user/Documents/../Pictures"
                    },
                    "expected": "/home/user/Pictures"
                },
                {
                    "input": "path = \"/../\"",
                    "expected_output": "\"/\"",
                    "raw_input": {
                        "path": "/../"
                    },
                    "expected": "/"
                }
            ],
            "explanation": "Split string on slashes and use a stack. Pop for '..', ignore empty or '.', push valid directories. Time: O(n), Space: O(n).",
            "id": 32,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 146: LRU Cache",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nDesign a data structure that follows the constraints of a <strong>Least Recently Used (LRU) cache</strong>.<br><br>\nImplement the <code>LRUCache</code> class:<br>\n\u2022 <code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.<br>\n\u2022 <code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.<br>\n\u2022 <code>void put(int key, int value)</code> Update or insert the value. When capacity reached, evict the least recently used key.<br><br>\nThe functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"LRUCache\", \"put\", \"put\", \"get\", \"put\", \"get\", \"put\", \"get\", \"get\", \"get\"]\n[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]\nOutput: [null, null, null, 1, null, -1, null, -1, 3, 4]</pre>",
            "starter_code": "class LRUCache:\n    def __init__(self, capacity: int):\n        # Write only your solution logic here\n        pass\n\n    def get(self, key: int) -> int:\n        # Write only your solution logic here\n        pass\n\n    def put(self, key: int, value: int) -> None:\n        # Write only your solution logic here\n        pass",
            "solution_code": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity: int):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
            "test_cases": [
                {
                    "operations": [
                        "LRUCache",
                        "put",
                        "put",
                        "get",
                        "put",
                        "get",
                        "put",
                        "get",
                        "get",
                        "get"
                    ],
                    "args": [
                        [
                            2
                        ],
                        [
                            1,
                            1
                        ],
                        [
                            2,
                            2
                        ],
                        [
                            1
                        ],
                        [
                            3,
                            3
                        ],
                        [
                            2
                        ],
                        [
                            4,
                            4
                        ],
                        [
                            1
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ]
                    ],
                    "input": "LRUCache(2) -> put(1,1), put(2,2), get(1), put(3,3), get(2), put(4,4), get(1), get(3), get(4)",
                    "expected_output": "[null, null, null, 1, null, -1, null, -1, 3, 4]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        null,
                        -1,
                        null,
                        -1,
                        3,
                        4
                    ]
                }
            ],
            "explanation": "Doubly Linked List + Hash Map (or Python OrderedDict). All operations in O(1) time.",
            "id": 33,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 380: Insert Delete GetRandom O(1)",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement the <code>RandomizedSet</code> class:<br>\n\u2022 <code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if item was not present, <code>false</code> otherwise.<br>\n\u2022 <code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if item was present, <code>false</code> otherwise.<br>\n\u2022 <code>int getRandom()</code> Returns a random element from the current set of elements.<br><br>\nYou must implement the functions such that each function works in <strong>average <code>O(1)</code></strong> time complexity.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"RandomizedSet\", \"insert\", \"remove\", \"insert\", \"getRandom\", \"remove\", \"insert\", \"getRandom\"]\n[[], [1], [2], [2], [], [1], [2], []]\nOutput: [null, true, false, true, 2, true, false, 2]</pre>",
            "starter_code": "class RandomizedSet:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def insert(self, val: int) -> bool:\n        pass\n\n    def remove(self, val: int) -> bool:\n        pass\n\n    def getRandom(self) -> int:\n        pass",
            "solution_code": "import random\n\nclass RandomizedSet:\n    def __init__(self):\n        self.nums = []\n        self.indices = {}\n\n    def insert(self, val: int) -> bool:\n        if val in self.indices:\n            return False\n        self.indices[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.indices:\n            return False\n        idx = self.indices[val]\n        last_val = self.nums[-1]\n        self.nums[idx] = last_val\n        self.indices[last_val] = idx\n        self.nums.pop()\n        del self.indices[val]\n        return True\n\n    def getRandom(self) -> int:\n        return random.choice(self.nums)",
            "test_cases": [
                {
                    "operations": [
                        "RandomizedSet",
                        "insert",
                        "remove",
                        "insert"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            2
                        ]
                    ],
                    "input": "RandomizedSet() -> insert(1), remove(2), insert(2)",
                    "expected_output": "[null, true, false, true]",
                    "expected": [
                        null,
                        true,
                        false,
                        true
                    ]
                }
            ],
            "explanation": "Array + Hash Map of value to index. Deletion swaps target element with array tail before popping in O(1). Time: O(1) average.",
            "id": 34,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 621: Task Scheduler",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven a characters array <code>tasks</code> representing the tasks a CPU needs to do, and a non-negative integer <code>n</code> representing the cooldown period between identical tasks, return <em>the least number of units of times that the CPU will take to finish all the given tasks</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2\nOutput: 8\nExplanation: A -> B -> idle -> A -> B -> idle -> A -> B</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0\nOutput: 6</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= tasks.length <= 10<sup>4</sup></code><br>\n\u2022 <code>0 <= n <= 100</code>",
            "starter_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)",
            "test_cases": [
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2",
                    "expected_output": "8",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 2
                    },
                    "expected": 8
                },
                {
                    "input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0",
                    "expected_output": "6",
                    "raw_input": {
                        "tasks": [
                            "A",
                            "A",
                            "A",
                            "B",
                            "B",
                            "B"
                        ],
                        "n": 0
                    },
                    "expected": 6
                }
            ],
            "explanation": "Greedy calculation: arrange most frequent tasks into slots of length (n + 1). Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq). Time: O(n), Space: O(1).",
            "id": 35,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 165: Compare Version Numbers",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven two version numbers, <code>version1</code> and <code>version2</code>, compare them.<br><br>\nVersion numbers consist of one or more revisions joined by a dot <code>'.'</code>.<br>\n\u2022 If <code>version1 < version2</code>, return <code>-1</code>.<br>\n\u2022 If <code>version1 > version2</code>, return <code>1</code>.<br>\n\u2022 Otherwise, return <code>0</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.2\", version2 = \"1.10\"\nOutput: -1</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: version1 = \"1.01\", version2 = \"1.001\"\nOutput: 0</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= version1.length, version2.length <= 500</code>",
            "starter_code": "def compareVersion(version1: str, version2: str) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def compareVersion(version1: str, version2: str) -> int:\n    v1 = [int(x) for x in version1.split('.')]\n    v2 = [int(x) for x in version2.split('.')]\n    max_len = max(len(v1), len(v2))\n    for i in range(max_len):\n        num1 = v1[i] if i < len(v1) else 0\n        num2 = v2[i] if i < len(v2) else 0\n        if num1 > num2: return 1\n        elif num1 < num2: return -1\n    return 0",
            "test_cases": [
                {
                    "input": "version1 = \"1.2\", version2 = \"1.10\"",
                    "expected_output": "-1",
                    "raw_input": {
                        "version1": "1.2",
                        "version2": "1.10"
                    },
                    "expected": -1
                },
                {
                    "input": "version1 = \"1.01\", version2 = \"1.001\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.01",
                        "version2": "1.001"
                    },
                    "expected": 0
                },
                {
                    "input": "version1 = \"1.0\", version2 = \"1.0.0.0\"",
                    "expected_output": "0",
                    "raw_input": {
                        "version1": "1.0",
                        "version2": "1.0.0.0"
                    },
                    "expected": 0
                }
            ],
            "explanation": "Split revisions by dot and pad missing segments with 0. Compare integer values left to right. Time: O(n + m), Space: O(n + m).",
            "id": 36,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 253: Meeting Rooms II",
            "difficulty": "Medium",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start_i, end_i]</code>, return <em>the minimum number of conference rooms (or server resources) required</em>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[0,30],[5,10],[15,20]]\nOutput: 2</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: intervals = [[7,10],[2,4]]\nOutput: 1</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>1 <= intervals.length <= 10<sup>4</sup></code>",
            "starter_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def minMeetingRooms(intervals: list[list[int]]) -> int:\n    if not intervals: return 0\n    starts = sorted([i[0] for i in intervals])\n    ends = sorted([i[1] for i in intervals])\n    s_ptr = e_ptr = 0\n    used_rooms = max_rooms = 0\n    while s_ptr < len(starts):\n        if starts[s_ptr] < ends[e_ptr]:\n            used_rooms += 1\n            max_rooms = max(max_rooms, used_rooms)\n            s_ptr += 1\n        else:\n            used_rooms -= 1\n            e_ptr += 1\n    return max_rooms",
            "test_cases": [
                {
                    "input": "intervals = [[0,30],[5,10],[15,20]]",
                    "expected_output": "2",
                    "raw_input": {
                        "intervals": [
                            [
                                0,
                                30
                            ],
                            [
                                5,
                                10
                            ],
                            [
                                15,
                                20
                            ]
                        ]
                    },
                    "expected": 2
                },
                {
                    "input": "intervals = [[7,10],[2,4]]",
                    "expected_output": "1",
                    "raw_input": {
                        "intervals": [
                            [
                                7,
                                10
                            ],
                            [
                                2,
                                4
                            ]
                        ]
                    },
                    "expected": 1
                }
            ],
            "explanation": "Sort start times and end times separately. Track overlapping intervals with two pointers. Time: O(n log n), Space: O(n).",
            "id": 37,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 2677: Chunk Array",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array <code>arr</code> and a chunk size <code>size</code>, return a chunked array.<br><br>\nA chunked array contains the original elements in <code>arr</code>, but consists of subarrays each of length <code>size</code>. The length of the last subarray may be less than <code>size</code> if <code>arr.length</code> is not evenly divisible by <code>size</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,2,3,4,5], size = 1\nOutput: [[1],[2],[3],[4],[5]]</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: arr = [1,9,6,3,2], size = 3\nOutput: [[1,9,6],[3,2]]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>size >= 1</code>",
            "starter_code": "def chunk(arr: list, size: int) -> list[list]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def chunk(arr: list, size: int) -> list[list]:\n    return [arr[i:i + size] for i in range(0, len(arr), size)]",
            "test_cases": [
                {
                    "input": "arr = [1,2,3,4,5], size = 1",
                    "expected_output": "[[1], [2], [3], [4], [5]]",
                    "raw_input": {
                        "arr": [
                            1,
                            2,
                            3,
                            4,
                            5
                        ],
                        "size": 1
                    },
                    "expected": [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ],
                        [
                            4
                        ],
                        [
                            5
                        ]
                    ]
                },
                {
                    "input": "arr = [1,9,6,3,2], size = 3",
                    "expected_output": "[[1, 9, 6], [3, 2]]",
                    "raw_input": {
                        "arr": [
                            1,
                            9,
                            6,
                            3,
                            2
                        ],
                        "size": 3
                    },
                    "expected": [
                        [
                            1,
                            9,
                            6
                        ],
                        [
                            3,
                            2
                        ]
                    ]
                },
                {
                    "input": "arr = [8,5,3,2,6], size = 6",
                    "expected_output": "[[8, 5, 3, 2, 6]]",
                    "raw_input": {
                        "arr": [
                            8,
                            5,
                            3,
                            2,
                            6
                        ],
                        "size": 6
                    },
                    "expected": [
                        [
                            8,
                            5,
                            3,
                            2,
                            6
                        ]
                    ]
                }
            ],
            "explanation": "Slice input array in steps of size. Time: O(n), Space: O(n).",
            "id": 38,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 232: Implement Queue using Stacks",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nImplement a first in first out (FIFO) queue using only two stacks.<br><br>\nImplement <code>MyQueue</code> class with <code>push(x)</code>, <code>pop()</code>, <code>peek()</code>, and <code>empty()</code>.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">[\"MyQueue\", \"push\", \"push\", \"peek\", \"pop\", \"empty\"]\n[[], [1], [2], [], [], []]\nOutput: [null, null, null, 1, 1, false]</pre>",
            "starter_code": "class MyQueue:\n    def __init__(self):\n        # Write only your solution logic here\n        pass\n\n    def push(self, x: int) -> None:\n        pass\n\n    def pop(self) -> int:\n        pass\n\n    def peek(self) -> int:\n        pass\n\n    def empty(self) -> bool:\n        pass",
            "solution_code": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def push(self, x: int) -> None:\n        self.in_stack.append(x)\n\n    def pop(self) -> int:\n        self.peek()\n        return self.out_stack.pop()\n\n    def peek(self) -> int:\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack[-1]\n\n    def empty(self) -> bool:\n        return not self.in_stack and not self.out_stack",
            "test_cases": [
                {
                    "operations": [
                        "MyQueue",
                        "push",
                        "push",
                        "peek",
                        "pop",
                        "empty"
                    ],
                    "args": [
                        [],
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [],
                        [],
                        []
                    ],
                    "input": "MyQueue() -> push(1), push(2), peek(), pop(), empty()",
                    "expected_output": "[null, null, null, 1, 1, false]",
                    "expected": [
                        null,
                        null,
                        null,
                        1,
                        1,
                        false
                    ]
                }
            ],
            "explanation": "Two stacks (in_stack and out_stack). Pop transfers elements when out_stack is empty. Amortized O(1) time per operation.",
            "id": 39,
            "is_coding": true,
            "domain": "aws"
        },
        {
            "title": "LeetCode 1: Two Sum",
            "difficulty": "Easy",
            "question_text": "<strong>Problem Statement:</strong><br>\nGiven an array of integers <code>nums</code> and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.<br><br>\nYou may assume that each input would have <strong>exactly one solution</strong>, and you may not use the same element twice. You can return the answer in any order.<br><br>\n<strong>Example 1:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: Because nums[0] + nums[1] == 9, we return [0, 1].</pre>\n<strong>Example 2:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,2,4], target = 6\nOutput: [1,2]</pre>\n<strong>Example 3:</strong><br>\n<pre style=\"background: #0f172a; color: #38bdf8; padding: 0.6rem 0.9rem; border-radius: 6px;\">Input: nums = [3,3], target = 6\nOutput: [0,1]</pre>\n<strong>Constraints:</strong><br>\n\u2022 <code>2 <= nums.length <= 10<sup>4</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code><br>\n\u2022 <code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code><br>\n\u2022 Only one valid answer exists.",
            "starter_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    # Write only your solution logic here\n    pass",
            "solution_code": "def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        diff = target - num\n        if diff in seen:\n            return [seen[diff], i]\n        seen[num] = i\n    return []",
            "test_cases": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            2,
                            7,
                            11,
                            15
                        ],
                        "target": 9
                    },
                    "expected": [
                        0,
                        1
                    ]
                },
                {
                    "input": "nums = [3,2,4], target = 6",
                    "expected_output": "[1, 2]",
                    "raw_input": {
                        "nums": [
                            3,
                            2,
                            4
                        ],
                        "target": 6
                    },
                    "expected": [
                        1,
                        2
                    ]
                },
                {
                    "input": "nums = [3,3], target = 6",
                    "expected_output": "[0, 1]",
                    "raw_input": {
                        "nums": [
                            3,
                            3
                        ],
                        "target": 6
                    },
                    "expected": [
                        0,
                        1
                    ]
                }
            ],
            "explanation": "Use a Hash Map to store complement (target - num). Time Complexity: O(n), Space Complexity: O(n).",
            "id": 40,
            "is_coding": true,
            "domain": "aws"
        }
    ]
}
