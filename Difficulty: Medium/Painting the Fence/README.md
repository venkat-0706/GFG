<h2><a href="https://www.geeksforgeeks.org/problems/painting-the-fence3727/1">Painting the Fence</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a fence with <strong>n </strong>posts and <strong>k</strong> colours, find out the number of ways of painting the fence so that <strong>not more than two </strong>consecutive posts have the same colours</span><span style="font-size: 18px;"><span style="font-size: 18px;">.<br>Answers are guaranteed to be fit into a 32 bit integer.</span></span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 3, k = 2 
<strong>Output:</strong> 6
<strong>Explanation</strong>: Let the 2 colours be 'R' and 'B'. </span><span style="font-size: 18px;"><span style="font-size: 18px;">We have following possible combinations:<br>1. RRB
2. RBR
3. RBB
4. BRR
5. BRB
6. BBR</span></span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 2, k = 4 
<strong>Output:</strong> 16
<strong>Explanation</strong>: </span><span style="font-size: 14pt;">After coloring first post with 4 possible combinations, you can still color </span><span style="font-size: 14pt;">next posts with all 4 colors. Total possible </span><span style="font-size: 14pt;">combinations will be 4x4=16</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n ≤ 300<br>1 ≤ k ≤ 10<sup>5</sup><br></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;