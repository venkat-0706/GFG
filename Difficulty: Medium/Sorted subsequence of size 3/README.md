<h2><a href="https://www.geeksforgeeks.org/problems/sorted-subsequence-of-size-3/1">Sorted subsequence of size 3</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong>, find any subsequence of three elements such that, </span><span style="font-size: 18px;"><strong>arr[i] &lt; arr[j] &lt; arr[k]</strong> and (<strong>i &lt; j &lt; k</strong>).</span></p>
<p><span style="font-size: 18px;">If such a subsequence exists, return the three elements as an array. Otherwise, return an empty array.</span></p>
<p><strong><span style="font-size: 18px;">Note:</span></strong></p>
<ul>
<li><span style="font-size: 18px;">The driver code will print 1 if the returned subsequence is valid and present in the array.</span></li>
<li><span style="font-size: 18px;">The driver code will print 0 if no such subsequence exists.</span></li>
<li><span style="font-size: 18px;">If the returned subsequence does not satisfy the required format or conditions, the output will be -1.</span></li>
</ul>
<p><strong><span style="font-size: 18px;">Examples :</span></strong></p>
<pre><span style="font-size: 14pt;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">arr[] = [12, 11, 10, 5, 6, 2, 30]</span><strong style="font-size: 18px;">
Output:</strong><span style="font-size: 18px;"> 1
</span><strong style="font-size: 18px;">Explanation: </strong><span style="font-size: 18px;">As 5 &lt; 6 &lt; 30, and they  appear in the same sequence in the array. So output is 1.</span></span></pre>
<pre><span style="font-size: 14pt;"><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [1, 2, 3, 4]
<strong>Output:</strong> 1 
<strong>Explanation:</strong> As the array is sorted, for every i, j, k, where i &lt; j &lt; k, arr[i] &lt; arr[j] &lt; arr[k].So output is 1.</span></span></pre>
<pre><strong><span style="font-size: 18px;">Input: </span></strong><span style="font-size: 18px;">arr[] = [4, 3, 2, 1]
<strong>Output: </strong>0<strong>
Explanation: </strong>No such Subsequence exist, so empty array is returned (the driver code automatically prints 0 in this case).</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>6</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>FactSet</code>&nbsp;<code>Walmart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;