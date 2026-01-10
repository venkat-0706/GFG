<h2><a href="https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1">Minimum Window Subsequence</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given two strings, <strong>s1</strong> and <strong>s2</strong>. Your task is to find the smallest <strong>substring</strong> in <strong>s1</strong> such that <strong>s2</strong> appears as a <strong>subsequence</strong> within that substring.</span></p>
<ol>
<li><span style="font-size: 14pt;">The characters of s2 must appear in the same sequence within the substring of s1.</span></li>
<li><span style="font-size: 14pt;">If there are multiple valid substrings of the same minimum length, return the one that appears first in s1.</span></li>
<li><span style="font-size: 14pt;">If no such substring exists, return an empty string.</span></li>
</ol>
<p dir="ltr"><span style="font-family: andale mono, monospace;"><span style="font-size: 18.6667px;"><strong>Note:</strong> Both the strings contain only lowercase english letters.</span></span></p>
<p dir="ltr"><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Input:</strong> s1 = "geeksforgeeks", s2 = "eksrg"
<strong>Output: </strong>"eksforg"
<strong>Explanation: </strong>"eksforg" satisfies all required conditions. s2 is its subsequence and it is smallest and leftmost among all possible valid substrings of s1.
</span></pre>
<pre><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Input:</strong> s1 = "abcdebdde", s2 = "bde" <br><strong>Output: </strong>"bcde"</span><br><span style="font-size: 14pt;"><strong style="font-family: 'andale mono', monospace;">Explanation: </strong><span style="font-family: andale mono, monospace;"> "bcde" and "bdde" are two substring of s1 where s2 occurs as subsequence but "bcde" occur first so we return that.<br></span></span></pre>
<pre><span style="font-family: 'andale mono', monospace; font-size: 14pt;"><strong>Input:</strong> s1 = "ad", s2 = "b" <br><strong>Output: </strong>""</span><br><span style="font-size: 14pt;"><strong style="font-family: 'andale mono', monospace;">Explanation: </strong>There is no substring exists.</span></pre>
<p dir="ltr"><span style="font-size: 14pt; font-family: 'andale mono', monospace;"><strong>Constraints:<br></strong>1 ≤ s1.length ≤ 10<sup>4<br></sup>1 ≤ s2.length ≤ 50</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Arrays</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;