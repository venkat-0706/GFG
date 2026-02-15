<h2><a href="https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1">Chocolate Distribution Problem</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[] </strong>of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are <strong>m</strong> students, the task is to distribute chocolate packets among <strong>m</strong> students such that - <br>&nbsp; &nbsp; &nbsp; i. Each student gets <strong>exactly</strong> one packet.<br>&nbsp; &nbsp; &nbsp;ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5<strong>
Output: </strong>6
<strong>Explanation: </strong>The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following m packets :[3, 4, 9, 7, 9].
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [7, 3, 2, 4, 9, 12, 56], m = 3
<strong>Output: </strong>2
<strong>Explanation: </strong>The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 by choosing following m packets :[3, 2, 4].</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [3, 4, 1, 9, 56], m = 5<strong>
Output: </strong>55<br><strong>Explanation</strong>: With 5 packets for 5 students, each student will receive one packet, so the difference is 56 - 1 = 55.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ m &lt;= arr.size ≤ 10<sup>5</sup><br>1 ≤ arr[i] ≤ 10<sup>9</sup><br></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Sorting</code>&nbsp;<code>Algorithms</code>&nbsp;