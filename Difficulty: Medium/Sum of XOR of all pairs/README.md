<h2><a href="https://www.geeksforgeeks.org/problems/sum-of-xor-of-all-pairs0723/1">Sum of XOR of all pairs</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 20px;">Given an integer array <strong>arr[]</strong> of size <strong>n</strong>, compute the sum of the <strong>bitwise XOR</strong> for all distinct pairs of elements. That is, consider every pair of indices <strong>(i, j)</strong> such that <strong>0 ≤ i &lt; j &lt; n</strong>, and calculate the total sum of <strong>(arr[i] XOR arr[j]) </strong>over all such pairs.</span></p>
<p><span style="font-size: 20px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 20px;"><strong>Input :</strong> arr[] = [7, 3, 5]
<strong>Output :</strong> 12
<strong>Explanation: <br></strong>All pairs (i, j) such that i &lt; j and their XOR values are:<br>7 ^ 3 = 4<br>7 ^ 5 = 2<br>3 ^ 5 = 6<br>Sum of all XOR values = 4 + 2 + 6 = 12.
</span></pre>
<pre><span style="font-size: 20px;"><strong style="font-size: 20px;">Input :</strong><span style="font-size: 20px;"> arr[] = [5, 9, 7, 6] </span><strong style="font-size: 20px;">
Output :</strong><span style="font-size: 20px;"> 47<br></span><strong style="font-size: 20px;">Explanation:<br></strong><span style="font-size: 20px;">All pairs (i, j) such that i &lt; j and their XOR values are:<br>5 ^ 9 = 12
5 ^ 7 = 2
5 ^ 6 = 3
9 ^ 7 = 14
9 ^ 6 = 15
7 ^ 6 = 1<br>Sum of all XOR values = 12 + 2 + 3 + 14 + 15 + 1 = 47.</span></span></pre>
<pre><span style="font-size: 20px;"><strong style="font-size: 20px;">Input :</strong><span style="font-size: 20px;"> arr[] = [10] </span><strong style="font-size: 20px;">
Output :</strong><span style="font-size: 20px;"> 0<br></span><strong style="font-size: 20px;">Explanation:</strong><span style="font-size: 20px;"> Since there are no pairs, sum is 0.</span></span></pre>
<p><span style="font-size: 20px;"><strong>Constraints</strong><br>1 ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5 </sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;