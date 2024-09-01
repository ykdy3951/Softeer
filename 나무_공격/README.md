<h2><a href="https://softeer.ai/practice/9657">나무_공격</a></h2><h3>Lv. 2</h3>
<br/><p><strong>입력형식</strong><p>첫 번째 줄에는 격자의 크기를 나타내는 n과 m이 공백을 사이에 두고 주어집니다.두 번째 줄부터는 n개의 줄에 걸쳐 각 행에 해당하는 m개의 격자 정보가 공백을 사이에 두고 주어집니다. 격자 내 숫자는 0, 1로만 주어지며 0은 비어있는 칸을, 1은 환경 파괴범이 있는 칸임을 뜻합니다.n+2번째 줄에는 첫 번째 공격 정보에 해당하는 L1​,R1​값이 공백을 사이에 두고 주어집니다. 이는 L1​번째 행부터 R1​번째 행까지 공격이 이루어짐을 뜻하며, R1​−L1​은 항상 4임을 가정해도 좋습니다.n+3번째 줄에는 두 번째 공격 정보에 해당하는 L2​,R2​값이 공백을 사이에 두고 주어집니다. 이는 L2​번째 행부터 R2​번째 행까지 공격이 이루어짐을 뜻하며, R2​−L2​는 항상 4임을 가정해도 좋습니다.</p></p><p><strong>출력형식</strong><p>첫 번째 줄에 두 번의 공격 이후 격자에 남아있는 서로 다른 환경 파괴범의 수를 출력합니다.</p></p>
<br/><p><strong class="example">Example 1:</strong>
<pre><strong>Input
</strong>6 8
0 0 1 0 0 0 1 0
0 0 0 1 0 0 0 0
0 0 1 0 0 1 1 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
1 5
2 6
<strong>
Output
</strong>2
</pre></p>
<p><strong class="example">Example 2:</strong>
<pre><strong>Input
</strong>8 8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 5
4 8
<strong>
Output
</strong>54
</pre></p>
<br/><p><strong>Constraints</strong><ul><li><p class="qti-paragraph" dir="ltr"><span>[조건 1] 5 ≤ n, m ≤ 100</span></p></li><li><p class="qti-paragraph" dir="ltr"><span>[조건 2] 1 ≤ L</span><sub><span class="EditorTheme__textSubscript">1</span></sub><span>, L</span><sub><span class="EditorTheme__textSubscript">2</span></sub><span>, R</span><sub><span class="EditorTheme__textSubscript">1</span></sub><span>, R</span><sub><span class="EditorTheme__textSubscript">2</span></sub><span> ≤ n</span></p></li></ul></p>