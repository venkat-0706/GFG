<h2><a href="https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1">Smallest window containing all characters</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given two strings <strong>s</strong> and <strong>p</strong>. Find the smallest substring in <strong>s</strong> consisting of all the characters (<strong>including duplicates</strong>) of the string <strong>p</strong>. Return empty string in case no such substring is present. <br></span><span style="font-size: 14pt;">If there are multiple such substring of the same length found, return the one with the <strong>least starting index</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "timetopractice", p = "toc"
<strong>Output: </strong>"toprac"<strong>
Explanation: </strong>"toprac" is the smallest substring in which "toc" can be found.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "zoomlazapzo", p = "oza"
<strong>Output: </strong>"apzo"<strong>
Explanation: </strong>"apzo" is the smallest substring in which "oza" can be found.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>s = "zoom", p = "zooe"
<strong>Output:</strong> ""<strong>
Explanation: </strong>No substring is present containing all characters of p.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:&nbsp;</strong><br>1 ≤ s.length(), p.length() ≤ 10<sup>6<br></sup></span><span style="font-size: 14pt;">s, p consists of lowercase english letters</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Google</code>&nbsp;<code>Streamoid Technologies</code>&nbsp;<code>Media.net</code>&nbsp;<code>Atlassian</code>&nbsp;<code>NPCI</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>Hash</code>&nbsp;<code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Binary Search</code>&nbsp;