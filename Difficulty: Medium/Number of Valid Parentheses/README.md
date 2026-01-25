<h2><a href="https://www.geeksforgeeks.org/problems/valid-number-of-parenthesis/1">Number of Valid Parentheses</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given a number <strong>n</strong>, your task is to find the number of <strong>all </strong>the valid parentheses expressions of that length using only <strong>"("</strong> and <strong>")"</strong> brackets.<br></span></p>
<p><span style="font-size: 18px;">An input string of parentheses is valid if :</span></p>
<ul>
<li><span style="font-size: 18px;">Open brackets must be closed in <strong>correct </strong>order.</span></li>
<li><span style="font-size: 18px;"><strong>Every </strong>close bracket has a corresponding open bracket.</span></li>
</ul>
<p><span style="font-size: 18px;">For example - <strong>"()()"</strong> or <strong>"(())"</strong> are valid while<strong> ")()("</strong> or <strong>"))(("</strong> are invalid parentheses expressions.<br></span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> </span><span style="font-size: 18px;">n = 2</span>
<strong><span style="font-size: 18px;">Output: </span></strong><span style="font-size: 18px;">1</span>
<span style="font-size: 14pt;"><strong>Explanation: </strong>There is only one possibe valid expressions of length 2 i.e., "()".</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> </span><span style="font-size: 18px;">n = 4</span>
<strong><span style="font-size: 18px;">Output: </span></strong><span style="font-size: 18px;">2<br></span><strong><span style="font-size: 18px;">Explanation: </span></strong><span style="font-size: 18px;">P</span><span style="font-size: 14pt;">ossibe valid expressions of length 4 are "(())" and "()()".<br></span></pre>
<pre><strong><span style="font-size: 14pt;">Input:</span></strong><span style="font-size: 14pt;"> n = 6<br><strong>Output: </strong>5<br></span><strong><span style="font-size: 14pt;">Explanation: </span></strong><span style="font-size: 14pt;">Possibe valid expressions of length 6 are "((()))", "(())()", "()(())", "()()()" and "(()())".</span></pre>
<p><strong><span style="font-size: 18px;">Constraints:</span></strong><br><span style="font-size: 18px;">1 ≤ n ≤ 20</span></p></div>