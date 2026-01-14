<h2><a href="https://www.geeksforgeeks.org/problems/police-and-thieves--141631/1">Police and Thieves</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong>, where each element contains either a <strong>'P'</strong> for policeman or a <strong>'T'</strong> for thief. Find the <strong>maximum number of thieves </strong>that can be caught by the police.&nbsp;<br>Keep in mind the following conditions :</span></p>
<ol>
<li><span style="font-size: 18px;">Each policeman can catch only one thief.</span></li>
<li><span style="font-size: 18px;">A policeman cannot catch a thief who is more than <strong>k</strong> units away from him.</span></li>
</ol>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = ['P', 'T', 'T', 'P', 'T'], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> Maximum 2 thieves can be caught. First policeman catches first thief and second police man can catch either second or third thief.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = ['T', 'T', 'P', 'P', 'T', 'P'], k = 2
<strong>Output:</strong> 3
<strong>Explanation: </strong>Maximum 3 thieves can be caught.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><br>1 ≤ k ≤ 1000<br>arr[i] = 'P' or 'T'</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Greedy</code>&nbsp;<code>Algorithms</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;