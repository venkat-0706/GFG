<h2><a href="https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1">Smallest window containing 0, 1 and 2</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given a string <strong>s</strong> consisting only of the characters '<strong>0'</strong>, '<strong>1'</strong> and '<strong>2'</strong>, determine the length of the <strong>smallest substring</strong> that contains all three characters at least once.</span></p>
<p><span style="font-size: 18px;">If no such substring exists, return <strong>-1</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "10212"
<strong>Output: </strong>3
<strong>Explanation: </strong></span><span style="font-size: 18px;">The substring "102" is the shortest substring that contains all three characters '0', '1', and '2', so the answer is 3.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "12121"
<strong>Output: </strong>-1
<strong>Explanation: </strong>The character '0' is not present in the string, so no substring can contain all three characters '0', '1', and '2'. Hence, the answer is -1.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 10<sup>5</sup><br></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Paytm</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;<code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;