<h2><a href="https://www.geeksforgeeks.org/problems/minimum-cost-to-connect-all-houses-in-a-city/1">Minimum cost to connect all houses in a city</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given a 2D array <strong>houses[][]</strong>, consisting of <strong>n</strong> 2D coordinates <strong>{x, y}</strong> where each coordinate represents the <strong>location of each house</strong>, the task is to find the<strong> minimum cost to connect</strong> all the houses of the city.</span></p>
<p><span style="font-size: 14pt;">The <strong>cost of connecting</strong> two houses is the <strong>Manhattan Distance</strong> between the two points (x<sub>i</sub>, y<sub>i</sub>) and (x<sub>j</sub>, y<sub>j</sub>) i.e., |x<sub>i</sub>&nbsp;– x<sub>j</sub>| + |y<sub>i</sub>&nbsp;– y<sub>j</sub>|, where |p| denotes the absolute value of p.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>n = 5 houses[][] = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]
<strong>Output: </strong>105<br><strong>Explanation:</strong><br>Connect house 1 (0, 7) and house 2 (0, 9) with cost = 2
Connect house 1 (0, 7) and house 3 (20, 7) with cost = 20
Connect house 3 (20, 7) with house 4 (30, 7) with cost = 10 
At last, connect house 4 (30, 7) with house 5 (40, 70) with cost 73.
All the houses are connected now.
The overall minimum cost is 2 + 10 + 20 + 73 = 105.<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892720/Web/Other/blobid0_1744176520.jpg" width="375" height="286"><br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>n = 4 houses[][] = [[0, 0], [1, 1], [1, 3], [3, 0]]
<strong>Output: </strong>7<br><strong>Explanation:</strong> 
Connect house 1 (0, 0) with house 2 (1, 1) with cost = 2
Connect house 2 (1, 1) with house 3 (1, 3) with cost = 2 
Connect house 1 (0, 0) with house 4 (3, 0) with cost = 3 
The overall minimum cost is 3 + 2 + 2 = 7.
</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraint:</strong><br>1 ≤ n ≤ 10<sup>3</sup><br>0 ≤ houses[i][j] ≤ 10<sup>3</sup></span></p></div>