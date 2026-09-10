<h2><a href="https://www.geeksforgeeks.org/problems/possible-pairs1550/1">Pairs with Given GCD and LCM</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given two integers <strong>x</strong> and <strong>y</strong> representing the GCD and LCM of two unknown positive integers&nbsp;<strong>a</strong> and <strong>b</strong>, count the number of valid pairs <strong>(a, b)</strong> satisfying these conditions. Note that <strong>(a, b) </strong>and <strong>(b, a)</strong> are counted as distinct pairs when <strong>a ≠ b</strong>.</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>x = 2, y = 12<strong>
Output: </strong>4<strong>
Explanation: </strong>The valid pairs are (2, 12), (4, 6), (6, 4), and (12, 2), since each pair has GCD = 2 and LCM = 12.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>x = 6, y = 4<strong>
Output: </strong>0<strong>
Explanation: </strong>LCM must always be a multiple of GCD. Since y is not divisible by x, no valid pair exists.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ x, y&nbsp;≤ 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematics</code>&nbsp;<code>Factorization</code>&nbsp;