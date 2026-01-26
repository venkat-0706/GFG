<h2><a href="https://www.geeksforgeeks.org/problems/generate-permutations-of-an-array/1">Generate Permutations of an array</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;"><span style="font-size: 18px;">Given an array&nbsp;</span><strong style="font-size: 18px;">arr[]</strong><span style="font-size: 18px;"> of unique elements. Generate all possible <strong>permutations </strong>of the elements in the array.</span><br><strong style="font-size: 18px;">Note:</strong><span style="font-size: 18px;"> You can return the permutations in any order, the driver code will print them in sorted order.</span></span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [1, 2, 3]
<strong>Output</strong>: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
<strong>Explanation</strong>: There are 6 possible permutations (3! = 6) of the array.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [1, 3]
<strong>Output</strong>: [[1, 3], [3, 1]]<br><strong>Explanation:</strong> There are 2 possible permutations (2! = 2) of the array.
</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 ≤ arr.size() ≤ 9</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Backtracking</code>&nbsp;<code>Arrays</code>&nbsp;<code>Recursion</code>&nbsp;