<h2><a href="https://www.geeksforgeeks.org/problems/find-position-of-set-bit3706/1">Position of the Set Bit</a></h2><h3>Difficulty Level : Difficulty: Basic</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 18px;">Given an integer&nbsp;<strong>n</strong>, determine position of the <strong>only set bit&nbsp;</strong>(1) in its binary representation. The position is counted starting from 1 at the least significant bit (LSB).</span></p>
<ul>
<li><span style="font-size: 18px;">If n contains exactly one set bit, return its position.</span></li>
<li><span style="font-size: 18px;">If n contains no set bits or more than one set bit, return -1.</span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input:</strong> </span><span style="font-size: 18px;">n =<strong> </strong>2</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Output:</span> </strong></span><span style="font-size: 18px;">2</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Explanation:</span> </strong></span><span style="font-size: 14pt;">2 is represented as "10" in binary. It has only one set bit, which is at position 2.</span><span style="font-size: 18px;"><br></span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input:</strong><strong> </strong></span><span style="font-size: 18px;">n =<strong> </strong>5</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Output:</span> </strong></span><span style="font-size: 18px;">-1</span>
<span style="font-size: 18px;"><strong><span style="font-size: 18px;">Explanation:</span> </strong></span><span style="font-size: 14pt;">5 is represented as "101" in binary. It has two set bits; therefore, the output is -1.
</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span><br><span style="font-size: 18px;">0&nbsp;<span style="font-size: 18.6667px;">≤</span>&nbsp;n&nbsp;<span style="font-size: 18.6667px;">≤</span>&nbsp;10<sup>8</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Bit Magic</code>&nbsp;<code>Data Structures</code>&nbsp;