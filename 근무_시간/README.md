<h2><a href="https://softeer.ai/practice/6254">근무_시간</a></h2><h3>Lv. 1</h3>
<br/><p><strong>입력형식</strong><p>첫 번째 줄에는 월요일에 출근한 시각과 월요일에 퇴근한 시각이 공백 하나를 사이로 두고 주어진다.  두 번째 줄에는 화요일에 출근한 시각과 화요일에 퇴근한 시각이 공백 하나를 사이로 두고 주어진다.  세 번째 줄에는 수요일에 출근한 시각과 수요일에 퇴근한 시각이 공백 하나를 사이로 두고 주어진다.  네 번째 줄에는 목요일에 출근한 시각과 목요일에 퇴근한 시각이 공백 하나를 사이로 두고 주어진다.  다섯 번째 줄에는 금요일에 출근한 시각과 금요일에 퇴근한 시각이 공백 하나를 사이로 두고 주어진다.</p></p><p><strong>출력형식</strong><p>첫 번째 줄에 직원의 총 근무 시간을 분 단위로 출력한다.</p></p>
<br/><p><strong class="example">Example 1:</strong>
<pre><strong>Input
</strong>10:00 19:00
09:00 15:00
10:00 11:00
11:00 22:00
09:00 15:00
<strong>
Output
</strong>1980
</pre></p>
<p><strong class="example">Example 2:</strong>
<pre><strong>Input
</strong>09:17 18:34
09:17 18:34
09:17 18:34
09:17 18:34
09:17 18:34
<strong>
Output
</strong>2785
</pre></p>
<p><strong class="example">Example 3:</strong>
<pre><strong>Input
</strong>09:17 19:24
10:11 18:45
09:34 18:27
10:47 15:33
08:47 18:32
<strong>
Output
</strong>2525
</pre></p>
<br/><p><strong>Constraints</strong><ul><li><p class="qti-paragraph" dir="ltr"><span>직원은 밤을 새서 일하지 않았다. 즉, 출근 시각과 퇴근 시각은 00:00 이후, 24:00 이전에 이루어졌다.</span></p></li><li><p class="qti-paragraph" dir="ltr"><br/></p></li><li><p class="qti-paragraph" dir="ltr"><span>출퇴근 시각은 HH:MM과 같은 형식으로 주어진다.</span><br/><span>  HH는 00, 01, 02, .., 22, 23 중 하나이다.</span><br/><span>  MM는 00, 01, 02, .., 58, 59 중 하나이다.</span><br/><span>  직원은 매일 1분 이상은 일하였다. </span><br/></p></li></ul></p>