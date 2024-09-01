<h2><a href="https://softeer.ai/practice/9498">[한양대_HCPC_2023]_Yeah,_but_How?</a></h2><h3>Lv. 2</h3>
<br/><p><strong>입력형식</strong><p>첫 번째 줄에 균형 잡힌 괄호 문자열 S가 주어진다. </p></p><p><strong>출력형식</strong><p>첫 번째 줄에 주어진 괄호 문자열로 만들 수 있는 수식 T를 출력한다.출력되는 수식 T는 다음 조건을 충족해야 한다.수식의 길이는 500000 이하여야 한다.T는 제대로 된 수식이어야 한다.T에서 (와 )만 남기면 S가 만들어져야 한다.T는 (, ), 1, +로만 이루어져야 한다. 특히, 수식의 중간에 공백 등의 문자가 들어가면 안 된다.입력 조건 내에서, 위 조건을 충족하는 수식을 만들 수 있음을 증명할 수 있다.가능한 수식이 여러 가지인 경우, 그중 아무거나 하나를 출력한다.</p></p>
<br/><p><strong class="example">Example 1:</strong>
<pre><strong>Input
</strong>(()())
<strong>
Output
</strong>((1+1)+(1)+1)
</pre></p>
<p><strong class="example">Example 2:</strong>
<pre><strong>Input
</strong>()()()
<strong>
Output
</strong>(1)+(1)+(1)
</pre></p>
<br/><p><strong>Constraints</strong><ul><li><p class="qti-paragraph"><span data-lexical-equation="MlxsZVxsdmVydCBTXHJ2ZXJ0XGxlIDIwMFwsIDAwMA==" data-lexical-inline="true"><span class="katex"><span aria-hidden="true" class="katex-html"><span class="base"><span class="strut" style="height: 0.7804em; vertical-align: -0.136em;"></span><span class="mord">2</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">∣</span><span class="mord mathnormal" style="margin-right: 0.0576em;">S</span><span class="mclose">∣</span><span class="mspace" style="margin-right: 0.2778em;"></span><span class="mrel">≤</span><span class="mspace" style="margin-right: 0.2778em;"></span></span><span class="base"><span class="strut" style="height: 0.6444em;"></span><span class="mord">200</span><span class="mspace" style="margin-right: 0.1667em;"></span><span class="mord">000</span></span></span></span></span></p></li></ul></p>