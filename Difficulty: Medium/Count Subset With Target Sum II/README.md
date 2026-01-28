<h2><a href="https://www.geeksforgeeks.org/problems/count-the-subset-with-sum-equal-to-k/1">Count Subset With Target Sum II</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong> and an integer <strong>k</strong>, find the count of <strong>subsets</strong> whose sum is equals to k.</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> It is guaranteed that the no of valid subsets&nbsp;will fit within a 32-bit integer.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">arr[] = [1, 3, 2], k = 3
<strong>Output: </strong>2<br><strong>Explanation:</strong> The two subsets whose sum is equals to k are [1, 2] and [3].</span>
</pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">arr[] = [4, 2, 3, 1, 2], k = 4
<strong>Output: </strong>3<br><strong>Explanation:</strong> The three subsets whose sum is equals to k are [4], [2, 2] and [3, 1].
</span></pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">arr[] = [10, 20, 30], k = 25
<strong>Output: </strong>0<br><strong>Explanation:</strong> No subsets exits with sum equals to k.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 40<br>-10<sup>7</sup> ≤ arr[i], k ≤ 10<sup>7</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Algorithms</code>&nbsp;