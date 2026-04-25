<h2><a href="https://www.geeksforgeeks.org/problems/asteroid-collision/1">Opposite Sign Pair Reduction</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[] </strong>, return the final array by repeatedly apply the following operation from left to right until no more valid operations can be performed.</span></p>
<p><span style="font-size: 14pt;">If two adjacent elements have opposite signs:</span></p>
<ul>
<li><span style="font-size: 14pt;">If their absolute values are different, remove both elements and insert the one with the greater absolute value, preserving its sign.</span></li>
<li><span style="font-size: 14pt;">If their absolute values are equal, remove both elements without inserting any new element.</span></li>
</ul>
<p><span style="font-size: 14pt;"><strong>Examples :&nbsp;</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [10, -5, -8, 2, -5]
<strong>Output:</strong> [10]<br><strong>Explanation:</strong> <br>At Index 0 : Element 10 has positive sign.
At Index 1 : -5  has lesser absolute value than 10. Replace both of them with 10.
At Index 2 : -8  has lesser absolute value than 10. Replace both of them with 10.
At Index 3 : 2 has positive sign. So it will be in the array.
At Index 4 : -5  has greater absolute value than 2. Replace both of them with 5.
Now -5  has lesser absolute value than 10. Replace both of them with 10.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [5, -5, -2, -10]<br><strong>Output:</strong> [-2, -10]<br><strong>Explanation:</strong> 1st and 2nd element gets discarded because both elements have same values but opposite sign. 3rd and 4th elements have same sign. So, both will be in the array.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [-20, 1, 20]<br><strong>Output:</strong> []<br><strong>Explanation:</strong> 1st and 2nd elements are removed, and -20 is inserted since it has the larger absolute value. Then, the remaining elements [-20, 20] are removed (equal absolute values, opposite signs).</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>-10000 ≤ arr[i] ≤ 10000<br>arr[i] != 0</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Stack</code>&nbsp;<code>Data Structures</code>&nbsp;