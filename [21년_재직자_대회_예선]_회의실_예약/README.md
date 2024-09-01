<h2><a href="https://softeer.ai/practice/6266">[21년_재직자_대회_예선]_회의실_예약</a></h2><h3>Lv. 2</h3>
<br/><p><strong>입력형식</strong><p>첫째 줄에 회의실의 수와 예약된 회의의 수를 나타내는 정수 N과 M이 공백을 사이에 두고 주어진다.이어 N개의 줄에는 각 회의실의 이름이 주어진다.이어 M개의 줄에는 각 회의가 배정된 회의실의 이름 r과 시작 시각 s, 그리고 종료 시각 t가 공백을 사이에 두고 주어진다.</p></p><p><strong>출력형식</strong><p>각 회의실에 대한 정보를 회의실 이름의 오름차순으로 출력한다.각 회의실에 대한 정보는 다음과 같다.첫째 줄에는 { Room 회의실이름: } (중괄호 제외)을 출력한다.둘째 줄에는 예약가능 시간을 출력한다.- 예약 가능한 시간대의 개수를 n이라고 할 때, { n available: } (중괄호 제외)을 출력하고, 뒤따른 n개의 줄에 예약 가능한 시간대를 { 09-18 } (하이픈 한개, 중괄호 제외)형태로 출력해야 한다. 한 자리 수의 경우 앞에 0을 붙여 두 자리 수로 만들어야 함에 유의하라.- 예약 가능한 시간이 없다면, Not available을 출력한다.각 회의실에 대한 정보 사이에는 ----- (하이픈 다섯 개)로 구분선이 출력되어야 한다.</p></p>
<br/><p><strong class="example">Example 1:</strong>
<pre><strong>Input
</strong>3 7
grandeur
avante
sonata
sonata 14 16
grandeur 11 12
avante 15 18
sonata 10 11
avante 9 12
grandeur 16 18
avante 12 15
<strong>
Output
</strong>Room avante:
Not available
-----
Room grandeur:
2 available:
09-11
12-16
-----
Room sonata:
3 available:
09-10
11-14
16-18
</pre></p>
<p><strong class="example">Example 2:</strong>
<pre><strong>Input
</strong>3 2
santafe
aerocity
porter
santafe 9 12
porter 9 18
<strong>
Output
</strong>Room aerocity:
1 available:
09-18
-----
Room porter:
Not available
-----
Room santafe:
1 available:
12-18
</pre></p>
<br/><p><strong>Constraints</strong><ul><li><p class="qti-paragraph" dir="ltr"><span>1 ≤ N ≤ 50</span></p></li><li><p class="qti-paragraph" dir="ltr"><span>1 ≤ M ≤ 100</span></p></li><li><p class="qti-paragraph" dir="ltr"><span>회의실의 이름은 영문 알파벳 소문자로만 이루어져 있으며 길이는 1 이상 10 이하이다.</span></p></li><li><p class="qti-paragraph" dir="ltr"><span>주어지는 모든 시각은 9 이상 18 이하이다.</span></p></li><li><p class="qti-paragraph" dir="ltr"><span>회의의 시작 시각은 회의의 종료 시각을 1시간 이상 앞선다.</span></p></li></ul></p>