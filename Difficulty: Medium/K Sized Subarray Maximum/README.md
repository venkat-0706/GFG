<h2><a href="https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1">K Sized Subarray Maximum</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array&nbsp;<strong>arr[]</strong> of positive integers and an integer <strong>k.</strong> You have to find the <strong>maximum value</strong> for each contiguous subarray of size <strong>k</strong>. Return an array of maximum values corresponding to each contiguous subarray.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
<strong>Output: </strong>[3, 3, 4, 5, 5, 5, 6]
<strong>Explanation: </strong>
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4<br></span><span style="font-size: 14pt;">4th contiguous subarray [1, 4, 5], max = 5<br>5th contiguous subarray [4, 5, 2], max = 5<br></span><span style="font-size: 14pt;">6th contiguous subarray [5, 2, 3], max = 5<br>7th contiguous subarray [2, 3, 6], max = 6<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [5, 1, 3, 4, 2], k = 1
<strong>Output: </strong>[5, 1, 3, 4, 2]
<strong>Explanation: </strong>When k = 1, each element in the array is its own subarray, so the output is simply the same array
</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>6</sup><br>1 ≤ k ≤ arr.size()<br>0 ≤ arr[i] ≤ 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Directi</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>Arrays</code>&nbsp;<code>Queue</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;<code>Deque</code>&nbsp;