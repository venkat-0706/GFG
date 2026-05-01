<h2><a href="https://www.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1">Kth Largest in a Stream</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given an input stream <strong>arr[] </strong>of <strong>n</strong> integers. Find the <strong>K</strong><sup>th</sup> <strong>largest </strong>element (not <strong>K</strong><sup>th</sup> largest unique element) after insertion of each element in the stream and if the <strong>K<sup>th</sup></strong> largest element doesn't exist, the answer will be -1 for that insertion.&nbsp; </span></p>
<p><span style="font-size: 14pt;">Return a list of size n, where each element represents the Kth largest value after the corresponding insertion.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[]<strong> </strong>=<strong> </strong>[1, 2, 3, 4, 5, 6], k = 4
<strong>Output: </strong>[-1, -1, -1, 1, 2, 3]
<strong>Explanation: </strong></span><span style="font-size: 18px;"><span style="font-size: 14pt;"><span style="font-size: 14pt;"><br></span></span></span><span style="font-size: 18px;"><span style="font-family: monospace;"><span style="font-size: 18.6667px; white-space: pre;">After inserting 1, there is only 1 element, so the 4th largest does not exist. Output is -1.
After inserting 2, there are only 2 elements, so the 4th largest does not exist. Output is -1.
After inserting 3, there are only 3 elements, so the 4th largest does not exist. Output is -1.
After inserting 4, the elements are [<span style="text-decoration: underline;">1</span>, 2, 3, 4]. The 4th largest element is 1.
After inserting 5, the elements are [1, <span style="text-decoration: underline;">2</span>, 3, 4, 5]. The 4th largest element is 2.
After inserting 6, the elements are [1, 2, <span style="text-decoration: underline;">3</span>, 4, 5, 6]. The 4th largest element is 3.</span></span></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [3, 2, 1, 3, 3], k = 2
<strong>Output: </strong>[-1, 2, 2, 3, 3]
<strong>Explanation:</strong> 
After inserting 3, there is only 1 element, so the 2nd largest does not exist. Output is -1.
After inserting 2, the elements are [3, <span style="text-decoration: underline;">2</span>]. The 2nd largest element is 2.
After inserting 1, the elements are [3, <span style="text-decoration: underline;">2</span>, 1]. The 2nd largest element is 2.
After inserting 3, the elements are [3, 2, 1, <span style="text-decoration: underline;">3</span>]. The 2nd largest element is 3.
After inserting 3, the elements are [3, 2, 1, <span style="text-decoration: underline;">3</span>, 3]. The 2nd largest element is 3.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">1 ≤ k ≤ n ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Hike</code>&nbsp;<code>Walmart</code>&nbsp;<code>Cisco</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Heap</code>&nbsp;<code>Data Structures</code>&nbsp;