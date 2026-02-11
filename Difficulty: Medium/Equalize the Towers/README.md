<h2><a href="https://www.geeksforgeeks.org/problems/equalize-the-towers2804/1">Equalize the Towers</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given an array <strong><code>heights[]</code></strong> representing the heights of towers and another array <strong><code>cost[]</code></strong> where each element represents the cost of modifying the <strong>height </strong>of respective tower. </span></p>
<ul>
<li><span style="font-size: 14pt;">The goal is to make all towers of same height by either adding or removing blocks from each tower.</span></li>
<li><span style="font-size: 14pt;">Modifying the height of tower <strong>'i'</strong> by 1 unit (add or remove) costs <strong>cost[i]</strong>.</span></li>
</ul>
<p><span style="font-size: 14pt;">Return the <strong>minimum </strong>cost to equalize the heights of all the towers.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>heights[] = [1, 2, 3], cost[] = [10, 100, 1000]
<strong>Output:</strong> 120
<strong>Explanation</strong>: The heights can be equalized by either "Removing one block from 3 and adding one in 1" or "Adding two blocks in 1 and adding one in 2". Since the cost of operation in tower 3 is 1000, the first process would yield 1010 while the second one yields 120.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>heights[] = [7, 1, 5], cost[] = [1, 1, 1]
<strong>Output:</strong> 6<br><strong>Explanation:</strong> </span><span style="font-size: 18.6667px;">The minimum cost to equalize the towers is 6, achieved by setting all towers to height 5.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ heights.size() = cost.size() ≤ 10<sup>5</sup><br>1 ≤ heights[i] ≤ 10<sup>4<br></sup>1 ≤ cost[i] ≤ 10<sup>3</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Binary Search</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;