<h2><a href="https://softeer.ai/practice/9497">[한양대_HCPC_2023]_Recovering_the_Region</a></h2><h3>Lv. 2</h3>
<br/><p><strong>입력형식</strong><p>첫 번째 줄에 보드의 크기 N이 주어진다.두 번째 줄부터 N개의 줄에 걸쳐 세훈이가 보드에 채운 수들이 공백으로 구분되어 주어진다. i+1번째 줄의 j번째 수는 세훈이가 i번 가로줄과 j번 세로줄이 교차하는 위치에 적은 수 Ai,j​를 의미한다.세훈이는 퍼즐을 잘 풀기 때문에, 가능한 구역의 배치가 항상 존재하는 입력만 들어온다.</p></p><p><strong>출력형식</strong><p>가능한 구역의 배치를 다음 조건에 맞게 공백으로 구분해 출력한다.출력은 N개의 줄로 이루어져야 하며, 각 줄에는 N개의 정수가 있어야 한다.출력되는 모든 수는 1 이상 N 이하여야 한다.변을 공유하는 두 칸이 같은 구역에 속한다면, 같은 수로 표현해야 한다.변을 공유하는 두 칸이 다른 구역에 속한다면, 다른 수로 표현해야 한다.변을 공유하지 않는 두 다른 구역은 같은 수로 표현할 수 있다.모든 구역은 문제의 조건을 충족해야 한다.만일 가능한 구역의 배치가 여러 가지라면, 그중 아무거나 출력한다.</p></p>
<br/><p><strong class="example">Example 1:</strong>
<pre><strong>Input
</strong>6
1 2 5 4 6 3
6 4 3 2 1 5
3 6 2 1 5 4
2 3 1 5 4 6
4 5 6 3 2 1
5 1 4 6 3 2
<strong>
Output
</strong>1 1 1 3 3 2
1 1 3 3 3 2
1 2 4 4 3 2
2 2 2 4 4 2
2 2 4 4 2 2
3 3 3 3 3 3
</pre></p>
<br/><p><strong>Constraints</strong><ul><li><p class="qti-paragraph"><span data-lexical-equation="MVxsZSBOXGxlIDUw" data-lexical-inline="true"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="base"><span class="strut" style="height: 0.7804em; vertical-align: -0.136em;"></span><span class="mord">1</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.8193em; vertical-align: -0.136em;"></span><span class="mord mathnormal" style="margin-right: 0.109em;">N</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">50</span></span></span></span></span><span> </span></p></li></ul></p>