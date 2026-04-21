<h2><a href="https://www.geeksforgeeks.org/problems/two-water-jug-problem3402/1">Two water Jug problem</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are at the side of a river. You are given a&nbsp;<strong>m</strong>&nbsp;litre jug and a&nbsp;<strong>n</strong> litre jug . Both the jugs are initially empty. The jugs dont have markings to allow measuring smaller quantities. You have to use the jugs to measure <strong>d</strong> litres of water . Determine the <strong>minimum no of operations</strong> to be performed to obtain d litres of water in one of the jugs.<br>The operations you can perform are:</span></p>
<ol>
<li><span style="font-size: 18px;">Empty a Jug</span></li>
<li><span style="font-size: 18px;">Fill a Jug</span></li>
<li><span style="font-size: 18px;">Pour water from one jug to the other until one of the jugs is either empty or full.</span></li>
</ol>
<p><span style="font-size: 18px;"><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; white-space: normal;">Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>m = 3, n = 5, d = 4
<strong>Output: </strong>6
<strong>Explanation:</strong> Operations are as follow-<br></span><span style="font-size: 14pt;">1. Fill up the 5 litre jug.
2. Then fill up the 3 litre jug using 5 litre jug. Now 5 litre jug contains 2 litre water.
3. Empty the 3 litre jug.
4. Now pour the 2 litre of water from 5 litre jug to 3 litre jug.
5. Now 3 litre jug contains 2 litre of water and 5 litre jug is empty.<br>6. Now fill up the 5 litre jug.
7. Now fill one litre of water from 5 litre jug to 3 litre jug. Now we have 4 litre water in 5 litre jug.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>m = 8, n = 56, d = 46
<strong>Output: </strong>-1
<strong>Explanation: </strong>Not possible to fill any one of the jug with 46 litre of water.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n, m ≤ 100<br>1 ≤ d ≤ 100</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>MakeMyTrip</code>&nbsp;<code>MAQ Software</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Algorithms</code>&nbsp;