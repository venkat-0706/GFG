<h2><a href="https://www.geeksforgeeks.org/problems/max-xor-subarray-of-size-k/1">Max Xor Subarray of size K</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of integers<strong>&nbsp;arr[]&nbsp;</strong>&nbsp;and a number<strong>&nbsp;k</strong>. Return&nbsp;the&nbsp;<strong>maximum xor</strong>&nbsp;of a subarray of size k.</span></p>
<p><span style="font-size: 14pt;"><strong>Note:</strong>&nbsp;A subarray is a contiguous part of any given array.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [2, 5, 8, 1, 1, 3], k = 3
<strong>Output: </strong>15
<strong>Explanation:</strong> arr[0] ^ arr[1] ^ arr[2] = 15, which is maximum.</span></pre>
<pre><span style="font-size: 18px;"><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [1, 2, 4, 5, 6] , k = 2
<strong>Output: </strong>6
<strong>Explanation:</strong> arr[1]</span><span style="font-size: 14pt;"><span style="font-size: 14pt;"> ^ arr[2] </span><span style="font-size: 14pt;">= 6, which is maximum.</span></span></span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>6<br></sup>0 ≤ arr[i] ≤ 10<sup>6<br></sup></span><span style="font-size: 18px;">1 ≤ k ≤ arr.size()</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Bit Magic</code>&nbsp;<code>sliding-window</code>&nbsp;<code>Arrays</code>&nbsp;