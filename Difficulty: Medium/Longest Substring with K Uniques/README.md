<h2><a href="https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1">Longest Substring with K Uniques</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p data-start="157" data-end="313"><span style="font-size: 14pt;">You are given a string <strong>s</strong> </span><span style="font-size: 18.6667px;">consisting only lowercase alphabets </span><span style="font-size: 14pt;">and an integer </span><strong style="font-size: 14pt;">k</strong><span style="font-size: 14pt;">. Your task is to find the <strong>length </strong>of the <strong>longest substring</strong> that contains exactly </span><strong style="font-size: 14pt;">k</strong><span style="font-size: 14pt;"> distinct characters.</span></p>
<p data-start="157" data-end="313"><span style="font-size: 14pt;"><span style="font-size: 14pt;"><strong>Note :</strong> If no such substring exists, return </span><strong style="font-size: 14pt;">-1</strong><span style="font-size: 14pt;">.&nbsp;</span></span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>s = "aabacbebebe</span><span style="font-size: 18px;">", k = 3
<strong>Output:</strong> 7
<strong>Explanation</strong>: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
</span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: s = "aaaa", k = 2
<strong>Output:</strong> -1
<strong>Explanation</strong>: There's no substring with 2 distinct characters.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "aabaaab", k = 2
<strong>Output:</strong> 7
<strong>Explanation</strong>: </span><span style="font-size: 14pt;">The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ s.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ 26<br></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Google</code>&nbsp;<code>SAP Labs</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>two-pointer-algorithm</code>&nbsp;<code>Hash</code>&nbsp;<code>Strings</code>&nbsp;<code>Map</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;