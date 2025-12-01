# 第17章. 零知识证明

在本章中，我们将探索 *零知识密码学* 的迷人世界，并了解它如何完美地应用于以太坊的路线图，使其能够真正扩展并满足大规模采用对区块空间的需求。零知识技术是一个非常复杂的主题，依赖于许多我们无法详细解释的数学规则。本章的目标是确保你能够理解为什么零知识密码学为以太坊提供了一个独特的机会，并且非常适合其扩展路线图。在本章结束时，你将了解零知识密码学在高级别上的工作原理，它的有用属性是什么，以及以太坊将如何使用它来改进协议。

## 历史

*零知识证明* 在1985年由Shafi Goldwasser、Silvio Micali和Charles Rackoff发表的论文 ["交互式证明系统的知识复杂性"](https://oreil.ly/a6KH6) 中被提出，他们将零知识证明描述为一种向另一方证明你知道某些事情是真的，而不透露任何信息，除了你的声明实际上是真的之外的方法。
尽管零知识证明是在20世纪80年代被发现的，但它们的实际用例非常有限。一切都在2011年随着 [BIT+11](https://oreil.ly/C6HvM) 论文的出现而改变，该论文介绍了 *SNARKs* (*简洁的非交互式知识论证*)，作为为任意计算创建零知识证明的理论框架。两年后，在2013年，[Pinocchio PGHR13](https://oreil.ly/4uU6x) 论文提供了第一个通用SNARK的实际实现，使SNARKs在现实世界的应用中成为可能。这是第一次可以在不必重新执行的情况下证明一个通用程序已被正确执行，并且无需透露实际的计算细节。

革命开始了。从那时起，零知识证明领域以惊人的速度发展。2016年，[Groth16算法](https://oreil.ly/rxlOL) 通过减少证明大小和验证时间，显着提高了zk-SNARKs的效率。由于其卓越的简洁性，尽管有更新的系统可用，Groth16至今仍被广泛使用。例如，去中心化混合器应用程序Tornado Cash使用它来实现链上的零知识证明。

2017年，[Bulletproofs](https://oreil.ly/ZUeIe) 通过消除对 *可信设置* 的需求引入了一项突破性进展（在后面的章节中，我们将深入探讨可信设置的实际含义），尽管代价是更大的证明大小。紧随其后的是2018年的 [*zk-STARKs*](https://oreil.ly/TCnTT)，它不仅消除了对可信设置的需求，还提供了后量子安全性——这意味着它们的密码学基础能够抵抗来自量子计算机的攻击。前者现在被用于加密货币项目Monero中，以混淆交易金额，而后者构成了以太坊L2 Starknet的密码学基础。

2019年，[PLONK](https://oreil.ly/3453_) 和 [Sonic](https://oreil.ly/f6_Sq) 通过引入通用且可更新的可信设置做出了重大贡献，这使得SNARKs对于通用应用程序来说更加灵活和实用。这些创新继续影响着现代的零知识系统。

零知识证明仍在积极开发中，最近的进展带来了证明时间、递归效率和实际应用（如zk-EVM和现代zk-VM）的改进。新的结构和优化不断涌现，推动着零知识技术可能实现的边界。

这在很大程度上要归功于加密货币领域带来的资金。以太坊基金会本身已经通过提供多项资助和设立专门的团队来研究该主题做出了贡献（并且仍在贡献）。

## 定义和属性

现在，让我们更具体地定义什么是零知识证明以及它必须具备哪些属性。我们已经说过，零知识证明是一种协议，它允许一方——通常称为 *证明者* (P)—向另一方——通常称为 *验证者* (V)—证明一个陈述是真实的，而不透露任何信息，除了那个特定的陈述是真实的。

让我们形式化一些重要的定义：

**陈述 (Statement)**

待证明的声明。该陈述是公开的，可以被任何人验证，并且不包含私密信息。

**见证 (Witness)**

证明该陈述为真的秘密信息。只有证明者知道该见证。

**证明 (Proof)**

一种密码学对象，它说服验证者该陈述为真，而不泄露见证。

所有零知识证明系统都必须遵守以下三个属性：

**完备性 (Completeness)**

如果证明者P持有一个真实的陈述，那么它必须能够通过遵循协议规则来计算出一个有效的零知识证明。不能存在证明者在正确遵循所有规则的情况下却无法生成有效证明。

**可靠性 (Soundness)**

对于任何恶意的证明者来说，伪造一个虚假陈述的有效证明必须是不可行的。如果一个零知识证明被验证者接受，那么证明者创建它的唯一方式必须是通过相应地遵循所有协议规则，从一个真实的陈述开始。

**零知识性 (Zero knowledge)**

顾名思义，验证者在遵循协议时，除了初始陈述的有效性之外，不应该知道任何其他信息。

## 以太坊如何使用零知识证明

你可能想知道这种非常新的密码学对于以太坊的未来发展和路线图为何如此重要。答案实际上非常简单。

零知识证明系统在以太坊环境中的真正力量在于，它们使验证一个陈述的有效性成为可能，而无需执行获得最终陈述所需的所有计算。首先，证明者计算某个陈述，并附加一个零知识证明；然后，所有验证者都可以简单地使用零知识协议，并信任地将该陈述视为真，而无需执行与证明者相同的计算。

细心的读者可能已经发现这完美地适用于以太坊的哪些方面：区块执行和状态更新——换句话说，*EVM状态转换函数*。每个新区块都会通过处理其中包含的所有交易来更新当前状态。图17-1很好地展示了这一点。

![EVM 状态转换函数](images/ch17/maet_1701.png)

图17-1. EVM 状态转换函数

你可以将EVM视为一个黑盒子，它将区块链的当前状态和包含大量交易的新接收区块作为输入，然后返回链的新更新的状态。目前，当以太坊全节点收到一个新区块时，它会重新执行该区块中包含的所有交易，以便它可以信任地更新状态，而无需依赖任何受信任的第三方。
这种方法的主要问题是区块执行成为潜在的瓶颈，因为它非常耗费资源。你最终需要在全节点必须遵守的硬件要求之间进行平衡，以使其能够正常工作并与链的顶端保持同步，同时还要与你希望在网络中拥有的去中心化程度相平衡。你越是希望通过提高全节点的要求来扩展，你就越会损害去中心化，因为不那么成熟的参与者无法在经济上维持运行一个全节点。反之亦然：你越是降低硬件要求，以便任何人都可以运行节点，你就越会受到区块链可以处理的最大吞吐量的限制。以太坊一直倾向于这种权衡的去中心化分支，保持较低的硬件要求，以允许独立质押者和全节点运行者存在。

这就是零知识证明系统发挥作用的地方。如果有一种方法可以让全节点在无需执行任何交易的情况下信任地更新其状态——基本上无需执行EVM状态转换函数的繁重计算，那会怎么样？这个想法可以概括为以下示例：

1. 一些参与者通过执行包含在每个新区块中的所有交易并生成链的更新状态来执行实际的EVM计算。
2. 这些参与者创建一个零知识证明来证明状态的有效性，并将它和新的更新状态一起分享给所有全节点。
3. 当所有其他全节点收到链的新状态和零知识证明时，他们只需验证证明的有效性，如果有效，他们就可以信任地使用他们刚刚收到的新状态来更新他们自己的链状态。

这样，你仍然需要有节点——可能由资金雄厚的公司维护——确实需要执行所有交易，但是所有其他节点都可以很廉价，因为它们只需要验证一个证明。你可以将第一种节点的硬件要求提高到非常高的水平，以便你可以处理更大的吞吐量，并且仍然可以通过零知识证明的“魔力”来保持高水平的去中心化。

到目前为止，我们一直假设生成和验证零知识证明是快速而直接的。事实上，如果验证零知识证明比重新执行一个普通以太坊区块中包含的所有交易更快，那么前面的步骤才有意义。但事实证明，今天很难实现这样的属性。但这只是一个优化问题：这只是一个时间问题，而不是是否可行的问题。我们很快就会达到可以实时生成和验证以太坊区块的零知识证明的程度。如果你对这个主题的发展感兴趣，Ethproofs 是一个非常酷的网站可以关注。

## L2 也能从 ZK 中受益

以太坊主网并不是唯一从零知识证明技术中受益的东西。事实上，正如你可能已经在第16章中读到的那样，有一类 Rollup 称为 *ZK rollups*。顾名思义，它们使用零知识证明系统来证明EVM的执行，以便它们可以发布其链的状态更新，并附带一个零知识证明，以确保新状态已被正确计算。

你可能想知道，如果正如我们之前所说的那样，目前无法实现平均以太坊区块的实时证明，那么ZK rollup是如何使用零知识技术的。答案是它们并没有做到；它们甚至不需要为L2的每个区块做实时证明。通常，它们每小时左右发布一次聚合的零知识证明，以证明自上次零知识证明后发生的所有状态更新都已正确执行。

每个零知识证明之间经过的时间只会影响汇总本身的最终确定时间。如果每小时发布一次证明，这意味着平均而言，你需要等待30分钟才能认为你的交易真正最终确定（在L1上）。

## 一个小例子

为了更熟悉零知识证明系统的工作方式，让我们从一个简单的小例子开始：*划分问题*。这是一个众所周知的问题，包括“确定给定的正整数多重集S是否可以划分为两个子集S1和S2，使得S1中的数字之和等于S2中的数字之和”的任务。

> **注意**
>
> 划分问题是一个决策问题，而以太坊依靠零知识证明来验证计算轨迹。尽管以太坊对零知识证明的主要用例是执行轨迹验证，但解决划分问题仍然是建立你对零知识证明系统如何工作的直觉的绝佳方法。

如果我们有 S = [1, 1, 5, 7]，我们可以通过将其划分为 S1 = [1, 1, 5] 和 S2 = [7] 来满足问题。但是，并非总是可以为此问题生成正确的解决方案。实际上，如果 S = [1, 1, 5, 8]，则不可能将其划分为总和相同的两个子集。

划分问题是 NP 完全问题，这意味着不存在可以在多项式时间内解决它的算法——也就是说，在短时间内提供解决方案（如果有）或证明该解决方案存在。

### 让我们证明它

划分问题的结构完美地适用于我们目前所看到的零知识证明系统的属性。事实上，由于很难找到解决方案，因此将寻找解决方案的计算能力委托给配备超级计算机的富有的证明者，然后使用零知识技术来证明它找到了有效的解决方案而无需其他每个人都执行相同的繁重计算，但实际上也没有透露该解决方案，这可能很有趣。

为了使划分问题适合零知识证明系统，我们需要稍微调整一下。假设我们有一个正整数列表 `s`。如果满足以下条件，我们将说另一个列表 `a` 是一个 *满足赋值*：

1. `len(s) == len(a)`
2. `a` 的所有元素都是 1 或 –1
3. `s` 和 `a` 之间的点积为 0

请注意，此构造与划分问题完全类似。如果我们采用先前初始列表 S = [1, 1, 5, 7]，则满足赋值 `a` 等于：

```
a = [1, 1, 1, –1]
```

你可以手动检查所有三个条件是否为真：

1. `len(s) = 4 == len(a) = 4`
2. `a` 的所有元素都是 1 或 –1
3. 点积：1 × 1 + 1 × 1 + 1 × 5 + (–1) × 7 = 1 + 1 + 5 – 7 = 0

两个长度相等的列表之间的 *点积* 是通过将第一个列表的每个成员乘以第二个列表的相应元素，然后将所有结果相加来计算的。更技术地讲，如果我们有长度相等的 `n` 的列表 `s = [s0, s1, s2, sn]` 和 `a = [a0, a1, a2, an]`，则点积计算如下：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathcolor="#000000">s</mi>
  <mo mathcolor="#000000">⋅</mo>
  <mi mathcolor="#000000">a</mi>
  <mo mathcolor="#000000">=</mo>
  <mrow>
    <munderover>
      <mo stretchy="false">∑</mo>
      <mrow>
        <mi mathcolor="#000000">i</mi>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">0</mn>
      </mrow>
      <mrow>
        <mi mathcolor="#000000">n</mi>
      </mrow>
    </munderover>
    <mrow>
      <mfenced separators="">
        <mrow>
          <msub>
            <mrow>
              <mi mathcolor="#000000">s</mi>
            </mrow>
            <mrow>
              <mi mathcolor="#000000">i</mi>
            </mrow>
          </msub>
          <mo mathcolor="#000000">×</mo>
          <msub>
            <mrow>
              <mi mathcolor="#000000">a</mi>
            </mrow>
            <mrow>
              <mi mathcolor="#000000">i</mi>
            </mrow>
          </msub>
        </mrow>
      </mfenced>
    </mrow>
  </mrow>
  <mo mathcolor="#000000">=</mo>
  <msub>
    <mrow>
      <mi mathcolor="#000000">a</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">0</mn>
    </mrow>
  </msub>
  <msub>
    <mrow>
      <mi mathcolor="#000000">s</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">0</mn>
    </mrow>
  </msub>
  <mo mathcolor="#000000">+</mo>
  <msub>
    <mrow>
      <mi mathcolor="#000000">a</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">1</mn>
    </mrow>
  </msub>
  <msub>
    <mrow>
      <mi mathcolor="#000000">s</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">1</mn>
    </mrow>
  </msub>
  <mo mathcolor="#000000">+</mo>
  <msub>
    <mrow>
      <mi mathcolor="#000000">a</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">2</mn>
    </mrow>
  </msub>
  <msub>
    <mrow>
      <mi mathcolor="#000000">s</mi>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">2</mn>
    </mrow>
  </msub>
  <mo mathcolor="#000000">+</mo>
  <mo mathcolor="#000000">.</mo>
  <mo mathcolor="#000000">.</mo>
  <mo mathcolor="#000000">.</mo>
  <mo mathcolor="#000000">+</mo>
  <msub>
    <mrow>
      <mi mathcolor="#000000">a</mi>
    </mrow>
    <mrow>
      <mi mathcolor="#000000">n</mi>
    </mrow>
  </msub>
  <msub>
    <mrow>
      <mi mathcolor="#000000">s</mi>
    </mrow>
    <mrow>
      <mi mathcolor="#000000">n</mi>
    </mrow>
  </msub>
</math>

当然，我们可以立即将`a`提供给验证者，他们可以很容易地检查它是否是有效的解决方案，但这将违反不透露解决方案的零知识假设。

让我们通过创建 *部分和列表* 来开始生成一个不同的列表`w`——也就是说，`w[i]`等于`s`和`a`到`i`的部分点积。在零知识证明系统的上下文中，`w` 也称为 *见证*。按照我们的例子，我们可以计算 `w`：

```
w = [1, 2, 7, 0]
```

请注意，如果`a` 是有效的满足赋值，那么`w` 总是以 0 结尾。

为了使证明系统更好地工作，让我们对我们到目前为止构建的证明`p`进行一些小的修改。特别是，我们将列表`w`的最后一个项目放在第一个位置，所以我们之前的`w`现在变为：

```
w = [0, 1, 2, 7]
```

太棒了！这个列表 `w` 有一个非常酷的属性：

```
|s[i]| = |w[i + 1] – w[i]|
```

你可以自己检查此语句的有效性：

```
|s[0]| = |w[0 + 1] – w[0]| = |w[1] – w[0]| = |1 – 0| = |1| = 1
|s[1]| = |w[1 + 1] – w[1]| = |w[2] – w[1]| = |2 – 1| = |1| = 1
|s[2]| = |w[2 + 1] – w[2]| = |w[3] – w[2]| = |7 – 2| = |5| = 5
|s[3]| = |w[3 + 1] – w[3]| = |w[4] – w[3]| = |w[0] – w[3]| = |0 – 7| = |–7| = 7
```

请注意，要计算 `s[3]`，我们需要访问 `w[4]`，因为 `w` 只有四个项目（并且我们从零开始索引），所以它不存在。但是，有一个非常简单的解决方案：你只需要回到 `w` 的第一个元素，就像 `w` 是循环的一样。

验证者可以要求 `w` 的两个连续元素，并检查先前的关系是否成立。请记住，验证者可以访问 `s`，因为它是公开可用的。它表示此问题的输入，但无权访问 `a`，而 `a` 代表问题的解决方案。如果该等式成立，则意味着证明者知道此问题的满足赋值 `a`。

### 问题

到目前为止，我们所构建的是一个非常简单的证明系统。事实上，它有三个大问题：

1. 先前，我们说过，一旦验证者要求两个连续的 `w` 元素，并且等式成立，则验证者已经验证了证明者知道此问题的解决方案。这不是真的。仅进行一次查询，验证者不能完全确定；他们必须对 `w` 的连续元素进行多次查询，才能以非常高的概率确定这一点。
2. 验证者确实可以验证证明者对此问题有解决方案，但此证明系统依赖于证明者的完整性。如果证明者是恶意的并且撒谎怎么办？当验证者要求两个连续的 `w` 元素时，证明者可以提供仍然满足该等式的两个随机数。
3. 此外，该证明系统不是零知识的。事实上，通过要求 `w` 的连续元素，验证者可以了解关于满足赋值 `a` 的很多信息。验证者知道 `w` 是如何构建的，因此他们对 `w` 了解得越多，他们对解决方案 `a` 了解得就越多。

现在让我们解决这些问题，并尝试构建一个更好的证明系统。

### 零知识

让我们向系统添加零知识。到目前为止，我们构建的协议的主要问题是我们将 `w` 的真实值发送给验证者，这使验证者能够理解关于 `a` 的大量信息。为了在实践中看到这一点，让我们在证明者和验证者之间进行两个简单的交互步骤。

验证者要求 `w[1]` 和 `w[2]` 并检查 `|w[2] – w[1]| = |s[1]|`，因此证明者提供 `w[1] = 1` 和 `w[2] = 2`，并且验证者可以确认等式成立：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfenced open="|" close="" separators="|">
    <mrow>
      <mi mathcolor="#000000">s</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mi mathcolor="#000000">w</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">2</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
      <mo mathcolor="#000000">−</mo>
      <mi mathcolor="#000000">w</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">2</mn>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">1</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">1</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
      <mn mathcolor="#000000">1</mn>
    </mrow>
  </mfenced>
</math>

然后，验证者要求进行另一个查询：`w[2]` 和 `w[3]`。证明者提供 `w[2] = 2` 和 `w[3] = 7`，并且验证者检查等式：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfenced open="|" close="" separators="|">
    <mrow>
      <mi mathcolor="#000000">s</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">2</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mi mathcolor="#000000">w</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">3</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
      <mo mathcolor="#000000">−</mo>
      <mi mathcolor="#000000">w</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">2</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">7</mn>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">2</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">5</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
      <mn mathcolor="#000000">5</mn>
    </mrow>
  </mfenced>
</math>

通过这两个交互，验证者可以了解 w 的三个元素：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mtable>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">w</mi>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">1</mn>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">w</mi>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">2</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">2</mn>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">w</mi>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">3</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">7</mn>
      </mtd>
    </mtr>
  </mtable>
</math>

由于验证者已经知道 `s = [1, 1, 5, 7]` 并且知道 `w` 是如何计算的，他们可以得出解决方案 `a` 的初始部分等于 `[1, 1, 1]`，因为这是获得 `w[3] = 7`、`w[2] = 2` 和 `w[1] = 1` 的唯一方法。

我们需要找到一种方法来掩盖 `w` 的真实值，但仍然能够满足新的 `w` 和输入列表 `s` 之间的关系。为了达到这个目标，我们需要以非常具体的方式添加一些随机性。

首先，我们掷硬币而不是 `a`，如果正面朝上，我们就保持原样；否则，我们更改所有元素的符号，因此所有 1 都变为 –1，反之亦然。请注意，此更改不会破坏使赋值 `a` 满足问题的那三个主要属性。

然后，我们获得一个新的随机整数值 `r`。我们以与之前相同的方式计算 `w`，但是我们将 `r` 添加到其每个元素。即使此更改也不会破坏 `s` 和 `w` 之间的关键关系。

每次验证者要求进行新的查询时，我们都必须掷硬币并计算不同的随机值 `r`。这样，尽管验证者仍然能够验证等式的有效性，但他们无法了解关于 `a` 的任何信息，因为所有 `w` 值对他们来说都是随机的。

让我们做一个小演示。请记住，证明者（在本例中为我们）从 `s` 和 `a` 开始：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mtable>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">s</mi>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo
        <mn mathcolor="#000000">5</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">7</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">a</mi>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">1</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
  </mtable>
</math>

现在，验证者要求 `w[1]` 和 `w[2]` 来检查 `|w[2] – w[1]| = |s[1]|`。

首先，我们需要掷硬币以最终更改 `a` 的所有值。这是反面，因此我们需要翻转所有符号，并且 `a` 变为：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathcolor="#000000">a</mi>
  <mo mathcolor="#000000">′</mo>
  <mo mathcolor="#000000">=</mo>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mo mathcolor="#000000">−</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mo mathcolor="#000000">−</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mo mathcolor="#000000">−</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">1</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math>

然后，我们计算一个随机值 `r = 4`。我们计算 `w` 并将 `r` 添加到每个元素：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mtable>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">w</mi>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">0</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">2</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">7</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <mi mathcolor="#000000">w</mi>
        <mo mathcolor="#000000">′</mo>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">4</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">3</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">2</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">3</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
  </mtable>
</math>
我们提供 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">1</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">3</mn>
</math> 和 <math xmlns="http://www.w3.org/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">2</mn>
</math>。

验证者仍然可以确认等式的有效性：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfenced open="|" close="|" separators="|">
    <mrow>
      <mi mathcolor="#000000">s</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
  </mfenced>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">−</mo>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mfenced open="" close="" separators="|">
    <mrow>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">2</mn>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">3</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">1</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
      <mn mathcolor="#000000">1</mn>
    </mrow>
  </mfenced>
</math>

现在，验证者运行另一个查询，请求 `w[2]` 和 `w[3]`。同样，我们需要抛硬币来最终改变 `a` 的所有值。这次是正面，所以我们不改变符号：

然后，我们计算一个随机值 `r = 1`。我们计算 `w` 并将 `r` 添加到每个元素：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathcolor="#000000">a</mi>
  <mo mathcolor="#000000">=</mo>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mo mathcolor="#000000">−</mo>
  <mn mathcolor="#000000">1</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math>

我们提供 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">″</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">3</mn>
</math> 和 <math xmlns="http://www.w3.org/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">″</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">3</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">8</mn>
</math>。
验证者仍然可以确认等式的有效性：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfenced open="|" close="|" separators="|">
    <mrow>
      <mi mathcolor="#000000">s</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">2</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
  </mfenced>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">″</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">3</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">−</mo>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">″</mo>
    </mrow>
  </msup>
  <mfenced open="" close="" separators="|">
    <mrow>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">2</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">8</mn>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">3</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">5</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
      <mn mathcolor="#000000">5</mn>
    </mrow>
  </mfenced>
</math>

但是现在，验证者对满足条件的赋值 a 了解不多。事实上，他们现在有以下信息：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mtable>
    <mtr>
      <mtd/>
      <mtd>
        <msup>
          <mrow>
            <mi mathcolor="#000000">w</mi>
          </mrow>
          <mrow>
            <mo mathcolor="#000000">′</mo>
          </mrow>
        </msup>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">3</mn>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <msup>
          <mrow>
            <mi mathcolor="#000000">w</mi>
          </mrow>
          <mrow>
            <mo mathcolor="#000000">′</mo>
          </mrow>
        </msup>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">2</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">2</mn>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <msup>
          <mrow>
            <mi mathcolor="#000000">w</mi>
          </mrow>
          <mrow>
            <mo mathcolor="#000000">″</mo>
          </mrow>
        </msup>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">2</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">3</mn>
      </mtd>
    </mtr>
    <mtr>
      <mtd/>
      <mtd>
        <msup>
          <mrow>
            <mi mathcolor="#000000">w</mi>
          </mrow>
          <mrow>
            <mo mathcolor="#000000">″</mo>
          </mrow>
        </msup>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">3</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
        <mo mathcolor="#000000">=</mo>
        <mn mathcolor="#000000">8</mn>
      </mtd>
    </mtr>
  </mtable>
</math>

不同查询中的 `w` 值对他们来说看起来是随机的，并且他们无法重构赋值 `a`。

很好！我们设法将零知识添加到证明系统中。现在让我们解决一个恶意的证明者。

### 证明者承诺

我们需要解决的问题是，证明者可以对验证者撒谎，提供完全虚构的数字，而不是计算出的见证 `w` 的真实值。这非常糟糕，因为证明者将能够提供虚假陈述的有效证明——也就是说，即使证明者实际上没有满足条件的赋值 `a`，他们也可能欺骗验证者相信他们有。

我们需要找到一种方法来确保证明者不会在不被抓住的情况下撒谎。从本质上讲，我们需要证明者在向验证者提供所有 `w` 值之前对它们进行*承诺*。

这就是梅克尔树再次帮助我们的地方。我们在第 14 章中介绍了它们，因此我们不会在此处详细介绍它们的工作原理。

让我们做一个新的例子，看看实践中的新构造。我们（证明者）有：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mtable>
    <mtr>
      <mtd>
        <mi mathcolor="#000000">s</mi>
      </mtd>
      <mtd>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">5</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">7</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
    <mtr>
      <mtd>
        <mi mathcolor="#000000">a</mi>
      </mtd>
      <mtd>
        <mo mathcolor="#000000">=</mo>
        <mo stretchy="false" mathcolor="#000000">[</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mn mathcolor="#000000">1</mn>
        <mo mathcolor="#000000">,</mo>
        <mo mathcolor="#000000">−</mo>
        <mn mathcolor="#000000">1</mn>
        <mo stretchy="false" mathcolor="#000000">]</mo>
      </mtd>
    </mtr>
  </mtable>
</math>

我们掷硬币，结果是正面，所以我们不需要改变赋值 `a` 的所有符号。然后我们计算 `w` 作为 `a` 和 `s` 之间的点积（第一个和最后一个元素之间交换）：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathcolor="#000000">w</mi>
  <mo mathcolor="#000000">=</mo>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">0</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">1</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">2</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">7</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math>

我们计算一个随机值 `r = 8`，并将其添加到 `w` 的每个元素：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathcolor="#000000">w</mi>
  <mo mathcolor="#000000">′</mo>
  <mo mathcolor="#000000">=</mo>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">8</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">9</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">10</mn>
  <mo mathcolor="#000000">,</mo>
  <mn mathcolor="#000000">15</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math>

现在我们需要承诺所有 `w′` 的值，并将承诺发送给验证者，以便我们确保如果我们通过提供 `w′` 的假值来作弊，那么很容易发现它。图 17-2 显示了使用所有 `w′` 值作为叶子构建的梅克尔树。

![梅克尔树承诺](images/ch17/maet_1702.png)

图 17-2. 使用 `w′` 值构建的梅克尔树

梅克尔根是发送给验证者的最终承诺。

此时，验证者开始请求第一个查询：<math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">1</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math> 和 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
</math>。我们可以向验证者提供 <math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">1</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">9</mn>
</math> 和 <math xmlns="http://www.w3.org/Math/MathML">
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">=</mo>
  <mn mathcolor="#000000">10</mn>
</math>，他们可以检查：

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfenced open="|" close="|" separators="|">
    <mrow>
      <mi mathcolor="#000000">s</mi>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
  </mfenced>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mo stretchy="false" mathcolor="#000000">[</mo>
  <mn mathcolor="#000000">2</mn>
  <mo stretchy="false" mathcolor="#000000">]</mo>
  <mo mathcolor="#000000">−</mo>
  <msup>
    <mrow>
      <mi mathcolor="#000000">w</mi>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">′</mo>
    </mrow>
  </msup>
  <mfenced open="" close="" separators="|">
    <mrow>
      <mo stretchy="false" mathcolor="#000000">[</mo>
      <mn mathcolor="#000000">1</mn>
      <mo stretchy="false" mathcolor="#000000">]</mo>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">10</mn>
      <mo mathcolor="#000000">−</mo>
      <mn mathcolor="#000000">9</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
    </mrow>
    <mrow>
      <mn mathcolor="#000000">1</mn>
    </mrow>
    <mrow>
      <mo mathcolor="#000000">=</mo>
      <mn mathcolor="#000000">1</mn>
    </mrow>
  </mfenced>
</math>

现在，验证者需要确保我们没有作弊，所以他们还要求证明者提供*验证路径*，其中包含他们需要自行重新创建梅克尔树的所有数据，以便检查梅克尔根是否与我们发送的承诺相同。如果是这种情况，那么他们确信我们没有作弊；否则，他们立即知道我们作弊了。

具体来说，此查询的验证路径包含：

- 哈希 8
- 哈希 15

这样，验证者可以重新创建梅克尔树直到根，并验证承诺。因此，我们将哈希 8 和哈希 15 发送给验证者，验证者检查承诺的有效性，最后，此查询结束。

但是，您可能已经发现了一个新问题。事实上，由于验证路径的要求，我们最终发送了一些关于 `w′` 的额外数据：哈希 8 和哈希 15。虽然反转哈希函数在计算上应该是不可行的——也就是说，从它们的哈希值中获取实际值 8 和 15——一个恶意的验证者可以尝试暴力攻击，并可能成功找出我们不打算泄露的梅克尔树的一部分。幸运的是，我们有一个简单而巧妙的调整可以解决这个问题。

### 向承诺添加随机性

这个想法类似于我们之前为我们的证明系统添加零知识属性所做的事情。这一次，我们需要向承诺添加随机性，以便我们不在验证路径中泄露关于 `w`（或 `w′`）的任何信息。

当我们创建梅克尔树时，我们不是只使用 `w′` 的每个元素的确切值的哈希作为树的叶子，而是添加一个我们不会提供给验证者的随机字符串。图 17-3 显示了使用这种新方法构建的新梅克尔树。

![带有随机性的梅克尔树](images/ch17/maet_1703.png)

图 17-3. 带有为零知识属性添加的随机性的梅克尔树

在此示例中，我们使用字符串“eth”来掩盖见证 `w′` 的每个项目。请注意，如果您没有这个秘密字符串，则不可能解码实际值。现在，当我们在验证路径中将哈希* 8 和哈希* 15 发送给验证者时，他们真的不知道哈希背后的具体 `w′` 值。即使他们尝试暴力攻击，他们也不知道我们用来进一步隐藏 `w′` 项的秘密字符串。

### 结论？或者不是……

我们做到了！我们设法为我们最初的划分问题创建了一个（非常幼稚和基本的）零知识证明系统！

您可能仍然认为：“这是一个很棒的证明系统，但它仍然需要在证明者和验证者之间进行大量交互。他们需要同时在线以确保协议成功。有没有办法修复它并将这个交互式零知识证明系统转换为非交互式零知识证明系统？”

而且你说的完全正确。我们的系统确实需要在证明者和验证者之间进行交互才能正常工作，这对大多数用例来说真的很烦人。我们再次很幸运（这里有很多运气，对吧？）。有一篇科学论文可以帮助我们。

## Fiat-Shamir 启发式

1986 年，两位著名的密码学家 Amos Fiat 和 Adi Shamir 发表了论文“[How to Prove Yourself: Practical Solutions to Identification and Signature Problems](https://oreil.ly/TGfa-)”，他们在其中发明了至今仍被广泛使用的转换协议，并以他们的名字命名：*Fiat-Shamir 启发式* 或转换。

> **注意**
>
> Adi Shamir 是密码学领域真正的传奇人物：他是 RSA 算法中的 S，RSA 算法是最早也是最广泛使用的公钥密码系统之一。Amos Fiat 是他在以色列魏茨曼科学研究所的同事。

Fiat-Shamir 启发式是一种协议，它可以通过用密码哈希函数替换验证者的随机挑战，将交互式零知识证明系统转换为非交互式系统。

如果您考虑一下验证者在我们迄今为止构建的系统中必须做的事情，您会注意到它本质上是在给证明者一些随机数——查询——证明者必须使用这些随机数来生成相应的证明。

请记住，我们过去常说，“现在验证者请求 `w[1]` 和 `w[2]`。” 这可以转化为验证者给证明者数字 1 和 2，以为 `w[1]` 和 `w[2]` 创建证明。

我们可以通过以下方式总结原始的交互式协议，跳过证明者创建见证 `w` 并将其调整为 `w′` 的部分：

1. 证明者生成对 `w′` 的承诺并将其发送给验证者。
2. 验证者发送一个随机挑战——一个查询。
3. 证明者发送对挑战的响应——一个证明。
4. 验证者验证证明的有效性。
对于验证者提出的每个不同的查询，都会重复此过程。并且一切运行良好，因为证明者事先不知道验证者将要提出哪些查询——它们对证明者来说是随机的。因此，如果我们找到一种方法使证明者本身以随机但可预测的方式生成所有查询，我们就可以将整个过程转换为非交互式协议。

在他们 1986 年的论文中，Fiat 和 Shamir 建议使用哈希函数作为“随机预言机”来模拟验证者的随机挑战。让我们做一个快速示例，仅包含两轮协议。

在第一轮中：

1. 证明者生成承诺。
2. 证明者获取承诺和问题的公共输入，并将它们连接并进行哈希处理。结果将是第一个挑战：

    ```
    challenge = hash(commitment || public inputs)
    ```

3. 证明者计算对挑战的响应——证明。

在第二轮中：

1. 证明者生成新的承诺。
2. 证明者获取新的承诺以及协议中到目前为止计算的所有内容（旧承诺、证明和公共输入），并将它们连接并进行哈希处理。结果将是新的挑战：

    ```
    new challenge = hash(commitment || proof || new_commitment || public inputs)
    ```

3. 证明者计算对新挑战的响应——新的证明。

此时，证明者可以将协议的整个记录发送给验证者。验证者需要：

1. 通过使用哈希函数和所有有效输入来确保所有挑战都已正确计算。这是为了确保证明者没有尝试使用虚构的挑战进行欺骗。
2. 以与之前在交互式协议中相同的方式验证所有证明的有效性。这是为了确保证明者实际上知道初始问题的解决方案。

图 17-4 显示了验证者在验证零知识证明的有效性之前，确保挑战已正确计算的过程。

![验证者验证过程](images/ch17/maet_1704.png)

图 17-4. Fiat-Shamir 启发式使协议成为非交互式的

就是这样！感谢 Fiat-Shamir 启发式，我们现在有了一个非交互式零知识证明系统。免费提供的很酷的功能是证明者现在能够生成任何人都可以验证的有效证明。因此，我们只需要一个诚实的参与者来验证证明，以检测证明者是否试图作弊。

### 结论？

在本节中，我们为划分问题构建了我们的第一个非交互式零知识证明系统。现代零知识架构要复杂得多，本书肯定不会解释所有这些（即使您可以在本章末尾找到一些非常好的论文供进一步阅读）。尽管如此，我们到目前为止所讨论的内容是所有新零知识技术的基础。如果您理解了这一点，您就可以陷入零知识的兔子洞，并开始探索其背后的所有细枝末节。

在下一节中，我们将研究两个最广泛使用的用于构建零知识证明系统的真实框架：SNARK 和 STARK。

## SNARK vs STARK

之前，我们能够为我们最初的划分问题创建一个零知识证明系统。这是一个好的开始。现在，如果我们想为完全不同的计算创建一个零知识证明系统怎么办？我们可以重用我们以前为划分问题构建的相同架构吗？

事实证明我们不能：承诺 `w` 及其属性——例如，`|s[i]| = |w[i+1] – w[i]|`——对于划分问题来说太具体了，无法应用于其他问题。但是，这并不是一个很大的缺点：我们可以利用我们从构建此零知识证明系统中学到的知识来开发一种更通用的方法。
这就是 SNARK 登场的地方。正如我们已经在“历史”中讨论过的，SNARK 在 2011 年的 BIT+11 论文中作为一种通用框架引入，用于为任意计算构建零知识证明。仅仅两年后，Pinocchio 论文创建了第一个可在实际应用程序中使用的实现。

SNARK 系统依赖于称为*可信设置*的密码秘密，以非交互方式工作。您可以将其视为与密码协议的所有参与者共享的通用知识库：一种初始化阶段，您需要在其中生成一些秘密并使用它们来计算一些其他值——证明和验证密钥——这些密钥对于 SNARK 协议的正确执行是必需的。

通常，可信设置是通过使用*多方计算*获得的：许多参与者各自生成不同的秘密（也称为*有毒废物*），计算证明和验证密钥，并删除其初始秘密。然后，将这些密钥加在一起以获得两个最终密钥，这些密钥将在 SNARK 协议中使用。这的主要好处是，您只需要一个仁慈的实体来删除其有毒废物，以确保任何人都无法作弊，并且可信设置是以防篡改的方式生成的。在第 4 章中，我们在讨论 KZG 承诺时对此进行了介绍。

即使 SNARK 协议可以完美运行，但可信设置的 N 分之 1 信任假设，以及创建非常具有弹性的初始仪式以生成最终公钥的困难，始终引发了大量的讨论，并促使一些研究人员和公司寻找完全无需它的无信任零知识证明系统。此外，SNARK 系统依赖于非抗量子椭圆曲线密码学，这是人们指出的另一个关键方面。

2018 年，Eli Ben-Sasson、Iddo Bentov、Yinon Horesh 和 Michael Riabzev 撰写的一篇论文，题为“[Scalable, Transparent, and Post-Quantum Secure Computational Integrity](https://oreil.ly/TCnTT)”，引入了一个新的无信任框架，用于构建通用的零知识证明系统：zk-STARK。
STARK 代表“*可扩展透明的知识论证*”。特别是，*透明*指的是不需要可信设置的突破性属性。它还依赖于抗冲突哈希函数而不是椭圆曲线密码学，使其甚至具有抗量子性。

这些优势解释了为什么现在大多数人认为 STARK 是最现代的零知识证明系统。然而，SNARK 并不是一种过时的技术。它们在某些情况下确实具有一些优势，主要是在证明大小方面，这在带宽受限的环境（如区块链）中可能是至关重要的。此外，已经开发了几种混合方法，试图取长补短。

## Zk-EVM 和 zk-VM

现在我们已经深入了解了零知识证明系统的工作原理，我们终于可以回到以太坊，看看这项技术近年来是如何发展的。

我们已经解释了如何使用零知识证明系统来改进以太坊——也就是说，证明一个区块的 EVM 执行，以便完整节点不必重新执行包含在该区块中的所有交易来无信任地更新其状态。相反，他们可以只验证零知识证明，如果它是有效的，他们就知道新的最初，每个想要构建 ZK rollup 的项目都必须着手创建用于 EVM 状态转换函数的正确的零知识电路。 这就是为什么在撰写本文时（2025 年 6 月），我们有比 ZK rollup 更多的 optimistic rollup。 但由于 zk-VM 的出现，情况变化非常快。
*Zk-VM* 极大地改变了构建 ZK rollup 以及更普遍地用于 EVM 状态转换函数的零知识证明系统的视角。 这个想法非常简单：与其为每个不同的计算创建自定义电路，以便随后应用 SNARK 或 STARK 框架，不如创建一个可以用于所有类型计算的通用电路？ 它将是一种通用零知识计算机，可以处理任何任意计算。 这种抽象层非常强大：“一个电路统治一切”。

这样，你只需要专注于你想证明的计算，而 zk-VM 则处理生成证明的所有困难工作。 目前最著名的 zk-VM 是 [SP1](https://oreil.ly/kgVYY) 和 [RISC Zero](https://oreil.ly/z6v2l)。

图 17-5 提供了一个简化的可视化，捕捉了 zk-EVM 和 zk-VM 框架的核心要素。

![zk-EVM and zk-VM comparison](images/ch17/maet_1705.png)

图 17-5. zk-EVM 和 zk-VM 框架的比较

## 结论

在最后一章中，我们探讨了零知识技术的基础知识：从 1985 年的首次发明到 Bit+11 和 Pinocchio 论文的开创性创新，这些创新真正将其应用于实际应用，尤其是在区块链领域。 我们以小分区问题为例，了解这些复杂系统如何在底层工作，后来我们研究了更通用的方法，例如 SNARK 和 STARK 框架，这些框架使得可以应用标准方法来为任何任意计算构建零知识证明系统。 最后，我们介绍了一个非常新的发展：zk-VM，由于它们具有能够处理任意计算的单个电路的显着优势，因此无需开发人员花费时间创建与他们想要证明的特定计算相关的自定义电路，因此它们正在迅速彻底改变该领域。

以太坊的未来无疑将与零知识技术相交，无论是在 L2 级别还是直接在 L1 级别。 最终将占上风的具体解决方案仍然未知； 也许这将是不同方法的组合，以确保对错误或故障具有更大的弹性。 只有时间会证明一切……

有关此主题的更多阅读材料，请参见以下内容：

- [一个简单的例子](https://oreil.ly/jVNdu)
- Ethan Buchman 的 [“你本可以发明 SNARK”](https://oreil.ly/jiaOa)
- Maksym Petkus 的 [“为什么以及 zk-SNARK 如何工作：权威解释”](https://oreil.ly/EUUzt)
- [RareSkills 零知识之书](https://oreil.ly/tpHrl)
