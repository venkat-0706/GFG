<h2><a href="https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1">Isomorphic Strings</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given two strings <strong>s1</strong>&nbsp;and <strong>s2 </strong>consisting of only lowercase English letters and of <strong>equal length</strong>, check if these two strings are <strong>isomorphic </strong>to each other.<br></span><span style="font-size: 14pt;">If the characters in s1 can be changed to get s2, then two strings, s1 and s2 are isomorphic. A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "aab", s2 = "xxy"
<strong>Output: </strong>true<strong>
Explanation: </strong>Each character in s1 can be consistently mapped to a unique character in s2 (a → x, b → y).
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "aab", s2 = "xyz"
<strong>Output: </strong>false<strong>
Explanation: </strong>S</span><span style="font-size: 18.6667px;">ame character 'a' in s1 maps to two different characters 'x' and 'y' in s2.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s1 = "abc", s2 = "xxz"
<strong>Output: </strong>false<strong>
Explanation: </strong>Two different characters 'a' and 'b' in s1 maps with same character 'x' in s2. </span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ s1.size() = s2.size() ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Hash</code>&nbsp;