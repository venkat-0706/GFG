<h2><a href="https://www.geeksforgeeks.org/problems/chocolates-pickup/1">Chocolates Pickup</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given a 2D matrix <strong>grid[][]</strong> of size <strong>n*m</strong>,&nbsp;</span><span style="font-size: 18px;">where each cell <strong>grid[i][j]</strong> represents the number of chocolates available at position <strong>(i, j)</strong>.</span></p>
<p><span style="font-size: 18px;">Two robots are collecting chocolates from this grid:</span></p>
<ul>
<li><span style="font-size: 18px;">Robot 1 starts at the top-left corner (0, 0)</span></li>
<li>Robot 2 starts at the top-right corner (0, m - 1)</li>
</ul>
<p><span style="font-size: 18px;">Your task is to determine the <strong>maximum total number</strong> of chocolates both robots can collect while following these rules:</span></p>
<ul>
<li><span style="font-size: 18px;">From a cell&nbsp;<code>(i, j)</code>, robots can move to cell&nbsp;<code>(i + 1, j - 1)</code>,&nbsp;<code>(i + 1, j)</code>, or&nbsp;<code>(i + 1, j + 1)</code>.</span></li>
<li><span style="font-size: 18px;">When a robot visits a cell, it collects all the chocolates there.</span></li>
<li><span style="font-size: 18px;">If both robots land on the same cell, the chocolates in that cell are collected only once.</span></li>
<li><span style="font-size: 18px;">Robots cannot move outside the boundaries of the grid.</span></li>
<li><span style="font-size: 18px;">Both robots must continue moving until they reach the bottom row of the grid.</span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Example:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>grid[][] = [[4, 1, 2], [3, 6, 1], [1, 6, 6], [3, 1, 2]]
<strong>Output: </strong>32</span><span style="font-size: 18px;">
<strong>Explanation: </strong></span><span style="font-size: 18px;">The path followed by first robot is: (0, 0) -&gt; (1, 0) -&gt; (2, 1) -&gt; (3, 0), so first robot collected: 4 + 3 + 6 + 3 = 16 chocolates.<br>The path followed by second robot is: (0, 2) -&gt; (1, 1) -&gt; (2, 2) -&gt; (3, 2), so second robot collected: 2 + 6 + 6 + 2 = 16 chocolates</span>.<br><span style="font-size: 18px;">Total both robots collected 16 + 16 = 32 chocolates.</span></pre>
<p><strong><span style="font-size: 18px;">Constraint:</span></strong><br><span style="font-size: 18px;">2 ≤ n, m ≤ 70<br>0 ≤ grid[i][j] ≤ 100</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>NPCI</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;