<h2><a href="https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1">Substrings with K Distinct</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given a string <strong>s</strong> consisting<strong>&nbsp;</strong>of lowercase characters and an integer <strong>k</strong>, You have to count all possible <strong>substrings </strong>that have <strong>exactly k distinct</strong> characters.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "abc", k = 2
<strong>Output: </strong>2
<strong>Explanation</strong>: Possible substrings are ["ab", "bc"]
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: s = "aba", k = 2
<strong>Output: </strong>3
<strong>Explanation</strong>: Possible substrings are ["ab", "ba", "aba"]</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "aa", k = 1
<strong>Output: </strong>3<br></span><strong><span style="font-size: 14pt; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Explanation</span></strong><span style="font-size: 14pt; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"><strong>:</strong> Possible substrings are ["a", "a", "aa"]</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 10<sup>6</sup><br>1 ≤ k ≤ 26</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>D-E-Shaw</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;<code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Algorithms</code>&nbsp;