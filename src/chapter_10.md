# 第 10 章 代币

*代币 (token)* 这个词源于古英语 *tācen*，意思是符号或象征。它通常用于指私人发行的、具有特殊用途的、类似硬币的物品，其内在价值微不足道，例如交通代币、洗衣代币和街机游戏代币。如今，在区块链上管理的代币正在重新定义这个词，指的是可以拥有的、基于区块链的抽象概念，代表着资产、货币或访问权限。

*代币* 这个词与微不足道的价值之间的关联，与代币的物理版本的有限用途有很大关系。物理代币通常仅限于特定的企业、组织或地点，不易交换，通常只有一种功能。有了区块链代币，这些限制被取消了，或者更准确地说，是被完全重新定义了。许多区块链代币在全球范围内具有多种用途，并且可以在全球流动市场上相互交易或与其他货币进行交易。随着使用和所有权限制的消失，“微不足道的价值”的期望也已成为过去。

在本章中，我们将研究代币的各种用途以及如何创建代币。我们还将讨论代币的属性，例如同质性和内在性。最后，我们将检查它们所基于的标准和技术，并通过构建我们自己的代币进行实验。

## 代币的用途

代币最明显的用途是作为数字私人货币。然而，这只是一个可能的用途。可以对代币进行编程以服务于许多不同的功能，这些功能通常会重叠。例如，代币可以同时传达投票权、访问权和对资源的所有权。如下面的列表所示，货币只是第一个“应用程序”：

**货币**

代币可以作为一种货币形式，其价值通过私人交易确定。

**资源**

代币可以代表在共享经济或资源共享环境中获得或产生的资源，例如，存储或 CPU 代币代表可以通过网络共享的资源。

**资产**

代币可以代表对内在或外在的、有形或无形资产的所有权，例如黄金、房地产、汽车、石油、能源、MMOG 项目等。

**访问权限**

代币可以代表访问权限，并且可以授予对数字或物理财产的访问权限，例如讨论论坛、独家网站、酒店房间或租赁汽车。

**股权**

代币可以代表数字组织（例如 DAO）或法律实体（例如公司）中的股东权益。

**投票**

代币可以代表数字或法律系统中的投票权。

**收藏品**

代币可以代表数字收藏品（例如 CryptoPunks）或物理收藏品（例如绘画）。

**身份**

代币可以代表数字身份（例如头像）或法律身份（例如国民身份证）。

**证明**

代币可以代表由某个权威机构或去中心化信誉系统对事实的认证或证明（例如，结婚记录、出生证明或大学学位）。

**实用性**

代币可用于访问或支付服务。

通常，单个代币包含这些功能中的几个。有时很难区分它们，因为物理等价物一直密不可分地联系在一起。例如，在物理世界中，驾驶执照（证明）也是一种身份证明（身份），两者不能分开。在数字领域，以前混合的功能可以分离并独立开发（例如，匿名证明）。

## 代币与同质化

[维基百科](https://en.wikipedia.org/wiki/Fungibility) 说：“在经济学中，同质性是一种商品或商品的基本单位本质上可以互换的属性。” 当我们可以用代币的任何单个单位替换另一个单位，而其价值或功能没有任何差异时，代币就是 *同质的*。

*非同质化* *代币* (NFT) 是指每个代币代表一个独特的有形或无形物品，因此不可互换。例如，代表拥有 *特定* 梵高画作的代币不等同于代表毕加索的另一个代币，即使它们可能是同一个“艺术所有权代币”系统的一部分。同样，代表一个 *特定* 数字收藏品（例如，特定的 CryptoKitty）的代币不能与任何其他 CryptoKitty 互换。每个 NFT 都与一个唯一的标识符相关联，例如序列号。

我们将在本章后面看到同质化和非同质化代币的例子。

> **注意**
> 
> 请注意，*同质化* 通常用于表示“可以直接兑换成金钱”（例如，赌场代币可以“兑现”，而洗衣代币通常不能）。这不是我们在这里使用这个词的含义。

## 交易对手风险

*交易对手风险* 是指交易中的 *另一方* 未能履行其义务的风险。某些类型的交易会遭受额外的交易对手风险，因为涉及的当事方不止两个。例如，如果您持有贵金属的存款凭证并将其出售给他人，则该交易中至少有三个当事方：卖方、买方和贵金属的保管人。有人持有实物资产；他们必然成为交易履行的当事方，并给涉及该资产的任何交易增加交易对手风险。一般来说，当资产通过交换所有权代币间接交易时，资产的保管人会带来额外的交易对手风险。他们拥有资产吗？他们会根据代币（例如凭证、契约、所有权或数字代币）的转移来承认（或允许）所有权的转移吗？在代表资产的数字代币世界中，与非数字世界一样，重要的是要了解谁持有代币所代表的资产，以及适用于该基础资产的规则。

## 代币与内在性

*内在* 这个词源于拉丁语 *intra*，意思是“来自内部”。有些代币代表区块链固有的数字项目。这些数字资产受共识规则约束，就像代币本身一样。这具有重要的意义：代表内在资产的代币不承担额外的交易对手风险。如果您持有 CryptoKitty 的密钥，则没有其他方为您持有该 CryptoKitty，您可以直接拥有它。区块链共识规则适用，并且您对私钥的所有权（即控制权）等同于对资产的所有权，没有任何中介。

相反，许多代币用于代表 *外在* 的事物，例如房地产、公司投票股份、商标、金条和债券。这些项目的非 “在区块链内” 的所有权受法律、习俗和政策的约束，与管理代币的共识规则分开。换句话说，代币发行人和所有者可能仍然依赖现实世界中的非智能合约。因此，这些外在资产会带来额外的交易对手风险，因为它们由托管人持有、记录在外部注册机构中，或受区块链环境之外的法律和政策控制。

基于区块链的代币最重要的后果之一是能够将外在资产转换为内在资产，从而消除交易对手风险。一个很好的例子是从公司中的股权（外在）转移到 DAO 或类似（内在）组织中的股权或投票代币。Stablecoin 是另一个例子，充当与法定货币挂钩并由国库券和现金储备等外在资产支持的基于区块链的代币。

## 实用、股权还是圈钱？

几乎每个以太坊项目似乎都启动了一些代币。但是所有这些项目真的需要代币吗？“将所有东西代币化” 的口号听起来很吸引人，但现实要复杂得多。代币可以是组织和激励社区的强大工具，但它们也已成为投机和炒作的代名词。

从理论上讲，代币有两个主要目的。首先，有 *实用代币*。它们旨在提供对特定生态系统中的服务或资源的访问权限。例如，代币可能代表去中心化网络上的存储空间或对 [DApp](https://learnblockchain.cn/tags/DApp) 中高级功能的访问权限。在这种情况下，代币的价值与其在平台中的功能相关。其次，我们有 *股权代币*，它们应该像公司中的股份一样运作。这些代币可以代表项目中的所有权或控制权，例如 DAO 中的投票权或利润分成。

在实践中，这些类别之间的区别往往模糊不清。许多实用代币在很大程度上仍然是投机性的，用户持有它们更多是作为资产而不是访问凭证。类似股权的代币可能授予治理权，但通常缺乏确保有意义参与的机制。一些项目将其代币深入集成到其经济模型中，但这些案例仍然是例外而不是规则。

这就引出了一个问题：代币本质上是坏的吗？一点也不。代币对于创建和激励社区或在 DAO 中支持去中心化治理可能非常有效。但现实情况是，大多数代币的推出都是以利润而不是实用性为主要动机。如果您正在考虑推出代币或投资代币，值得提出一些难题。代币是否真正服务于协议中必要的目标，还是仅仅是一种筹款工具？没有它，项目是否也能运行良好？诚实地回答这些问题可以帮助您区分真正的创新和营销驱动的炒作。

很明显，代币格局仍在不断发展，代币本身并没有好坏之分；它们的价值取决于它们的设计和实施方式。挑战在于将有意义的与无意义的分开，并抵制下一个 meme 币的诱惑。

> **注意**
>
> 在撰写本章（2025 年 1 月）期间，新当选的总统唐纳德·特朗普推出了自己的 meme 币，该币在一天之内达到了 150 亿美元的市值。许多人曾预期他的总统任期会出台有利的加密政策，但相反，我们得到了一种 meme 币。这一事件突显了主导加密货币的投机狂潮，在这种狂潮中，炒作往往胜过实质。

## 这是鸭子！

长期以來，代币一直是初创公司最喜欢的融资工具。它们承诺创新、去中心化，有时甚至是彻底的财务自由。但问题是：向公众提供证券在大多数司法管辖区都是受监管的活动，而代币很容易越过界限进入证券领域。多年来，各项目一直试图通过将其代币标记为 “实用代币” 来规避法规，声称它们只是对未来服务的预售。其逻辑是：如果该代币不是股权，那么它就不是证券。但正如老话所说，“如果它走起路来像鸭子，叫起来像鸭子，那么它就是鸭子。” 而监管机构，尤其是美国证券交易委员会 (SEC)，正在关注这些鸭子。

在过去几年中，SEC 对代币发行采取了越来越积极的立场，打击了试图跨越实用性和股权之间界限的项目。例如，在 2020 年，SEC 起诉了 Ripple Labs 的 XRP 代币，认为它是一种未注册的证券。Ripple 声称 XRP 是一种货币，而不是证券，但法院的部分裁决表明这些案例可能是多么微妙。

即使是以太坊本身也没有免受审查。早在 2018 年，前 SEC 官员就宣布以太币 “足够去中心化”，因此不是证券。但就在 2024 年，SEC 暗示以太坊向 [PoS](https://learnblockchain.cn/tags/PoS) 的过渡可能会使其再次受到关注。为什么？因为 staking 奖励类似于股息，而股息是证券的标志。这些发展表明，监管环境变得多么不稳定和不可预测。

令人着迷且令人沮丧的是，这些案例往往归结为语义。项目声称他们的代币是实用工具，例如服务的门票。但如果买家的主要动机是投机，SEC 会认为它是证券，仅此而已。挑战在于，用于做出这些决定的法律框架是在区块链技术出现很久以前创建的。《豪威测试》成立于 20 世纪 40 年代，旨在定义投资合同，但并非为去中心化网络或可编程资产而设计。因此，将其应用于加密项目并不总是那么简单。创新者希望筹集资金并建立社区，但监管机构希望保护投资者免受误导。结果是什么？一场在法庭上反复上演的戏剧，数十亿美元和整个生态系统悬而未决。

## 以太坊上的代币

区块链代币在以太坊之前就存在了。在某些方面，第一个区块链货币[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)本身就是一种代币。在以太坊之前，许多代币平台也在[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)和其他加密货币上开发。然而，第一个代币标准在以太坊上的推出导致了代币的爆炸式增长。

[Vitalik](https://learnblockchain.cn/tags/Vitalik?map=EVM) Buterin 建议将代币作为一种通用可编程区块链（如以太坊）最明显和最有用的应用之一。事实上，在以太坊的第一年，经常看到 Buterin 和其他人穿着印有以太坊标志和智能合约示例的 T 恤。这件 T 恤有几种变体，但最常见的是代币的实现。

在我们深入研究在以太坊上创建代币的细节之前，重要的是要概述代币在以太坊上的工作方式。代币与以太币不同，因为以太坊协议对它们一无所知。发送以太币是以太坊平台的内在操作，但发送甚至拥有代币则不是。以太坊[账户](https://learnblockchain.cn/tags/账户?map=EVM)的以太币余额在协议级别处理，而以太坊[账户](https://learnblockchain.cn/tags/账户?map=EVM)的代币余额在智能合约级别处理。要在以太坊上创建新的代币，您必须创建新的智能合约。部署智能合约后，它将处理所有事情，包括所有权、转移和访问权限。您可以编写智能合约来执行您想要的任何必要操作，但遵循现有标准可能是最明智的。接下来我们将研究这些标准。

## ERC-20 代币标准

第一个标准是由 Fabian Vogelsteller 在 2015 年 11 月作为 ERC 提出的。它被自动分配了 GitHub 问题编号 20，从而产生了名称 “ERC-20 代币”。绝大多数代币目前都基于 ERC-20 标准。ERC-20 征求意见稿最终成为 EIP-20，但它仍然主要以原始名称 ERC-20 称呼。

ERC-20 是同质化代币的标准，这意味着 ERC-20 代币的不同单位可以互换且没有唯一属性。[ERC-20 标准](https://github.com/ethereum/ercs/blob/master/ERCS/erc-20.md) 为实现代币的合约定义了一个公共接口，以便可以以相同的方式访问和使用任何兼容的代币。该接口由必须存在于标准每个实现中的许多函数以及开发者可以添加的一些可选函数和属性组成。

### ERC-20 必需的函数和事件

符合 ERC-20 的代币合约必须至少提供以下函数和事件：

`totalSupply`

返回当前存在的此代币的总单位数。ERC-20 代币可以具有固定或可变的供应量。

`balanceOf`

给定一个地址，返回该地址的代币余额。

`transfer`

给定一个地址和金额，将该数量的代币从执行转移的地址的余额转移到该地址。

`transferFrom`

给定一个发送者、接收者和金额，将代币从一个帐户转移到另一个帐户。与 `approve` 结合使用。

`approve`

给定一个接收者地址和金额，授权该地址从发出批准的帐户执行多次转移，最高可达该金额。

`allowance`

给定一个所有者地址和一个花费者地址，返回花费者被批准从所有者处提取的剩余金额。

`transfer`

成功转移时触发的事件（调用 `transfer` 或 `transferFrom`），即使对于零值转移也是如此。

`approval`

成功调用 `approve` 时记录的事件。

#### ERC-20 可选函数

除了上一节中列出的必需函数外，标准还定义了以下可选函数：

**名称**

返回代币的人工可读名称（例如 “美元”）。

**符号**

返回代币的人工可读符号（例如 “USD”）。

**小数位数**

返回用于除代币金额的小数位数。例如，如果小数位数为 2，则代币金额 1,000 实际上表示余额为 10。

#### 在 Solidity 中定义的 ERC-20 接口

以下是 ERC-20 接口规范在 Solidity 中的样子：

```solidity
contract ERC20 {
  function totalSupply() public view returns (uint256 theTotalSupply);
  function balanceOf(address _owner) public view returns (uint256 balance);
  function transfer(address _to, uint256 _value) public returns (bool success);
  function transferFrom(address _from, address _to, uint256 _value) public returns
      (bool success);
  function approve(address _spender, uint256 _value) public returns (bool success);
  function allowance(address _owner, address _spender) public view returns
      (uint256 remaining);
  event Transfer(address indexed _from, address indexed _to, uint256 _value);
  event Approval(address indexed _owner, address indexed _spender, uint256 _value);
}
```

#### ERC-20 数据结构

如果您检查任何 ERC-20 实现，您会发现它包含两个数据结构：一个用于跟踪余额，一个用于跟踪限额。在 Solidity 中，它们使用 *数据映射* 实现。

第一个数据映射实现了按所有者划分的内部代币余额表。这使代币合约可以跟踪谁拥有代币。每次转账都是从一个余额中扣除并添加到另一个余额中：

```solidity
mapping(address account => uint256) _balances;
```

第二个数据结构是限额的数据映射。正如我们将在下一节中看到的那样，使用 ERC-20 代币，代币的所有者可以将控制权委托给花费者，允许他们从所有者的余额中花费特定金额（限额）。ERC-20 合约使用二维映射跟踪限额，其中主键是代币所有者的地址，映射到花费者地址和限额：

```solidity
mapping(address account => mapping(address spender => uint256)) public _allowances;
```

#### ERC-20 工作流程：“Transfer” 和 “approve and transferFrom”

ERC-20 代币标准有两个转移函数。您可能想知道为什么。

ERC-20 允许两种不同的工作流程。第一个是使用 `transfer` 函数的简单的单事务工作流程。此工作流程是钱包用于将代币发送到其他钱包的工作流程。绝大多数代币交易都是通过 `transfer` 工作流程进行的。

执行转移合约非常简单。如果 Alice 想要向 Bob 发送 10 个代币，她的钱包会向代币合约的地址发送一个事务，调用 `transfer` 函数，并将 Bob 的地址和 `10` 作为参数。代币合约调整 Alice 的余额（-10）和 Bob 的余额（+10），并发出一个 `Transfer` 事件。

第二个工作流程是使用 `approve`，然后使用 `transferFrom` 的两事务工作流程。此工作流程允许代币所有者将其控制权委托给另一个地址。它最常用于将控制权委托给合约以进行代币分发，但也可以用于交易所。例如，如果一家公司正在出售代币以进行 ICO，它们可以 `approve` 一个众筹合约地址，以分发一定数量的代币。然后，众筹合约可以将代币合约所有者的余额 `transferFrom` 到每个代币购买者，如图 10-1 所示。

![The two-step approve and transferFrom workflow of ERC-20 tokens](https://img.learnblockchain.cn/masterethereumbook/images/ch10/maet_1001.png)

**图 10-1.** ERC-20 代币的两步 `approve` 和 `transferFrom` 工作流程

> **注意**
>
> *首次代币发行* (ICO) 是一种众筹机制，公司和组织通过出售代币来筹集资金。该术语源自 *首次公开募股* (IPO)，后者是一家上市公司在股票交易所向投资者出售股份的过程。与受到高度监管的 IPO 市场不同，ICO 是开放的、全球性的且混乱的。

对于 `approve` 和 `transferFrom` 工作流程，需要两个事务。假设 Alice 想要允许 `AliceICO` 合约向 Bob 和 Charlie 等买家出售所有 AliceCoin 代币的 50%。首先，Alice 启动 `AliceCoin` ERC-20 合约，将所有 AliceCoin 发行到她自己的地址。然后，Alice 启动可以出售代币以换取以太币的 `AliceICO` 合约。接下来，Alice 启动 `approve` 和 `transferFrom` 工作流程。她向 `AliceCoin` 合约发送一个事务，调用 `approve`，并将 `AliceICO` 合约的地址和 `totalSupply` 的 50% 作为参数。这将触发 `Approval` 事件。现在，`AliceICO` 合约可以出售 AliceCoin。

当 `AliceICO` 合约从 Bob 收到以太币时，它需要向 Bob 发送一些 AliceCoin 作为回报。在 `AliceICO` 合约中，AliceCoin 和以太币之间存在汇率。Alice 在创建 `AliceICO` 合约时设置的汇率决定了 Bob 为发送到 `AliceICO` 合约的以太币数量将收到多少代币。当 `AliceICO` 合约调用 AliceCoin `transferFrom` 函数时，它会将 Alice 的地址设置为发送者，将 Bob 的地址设置为接收者，并使用汇率来确定将有多少 AliceCoin 代币转移到 Bob 的 `value` 字段中。`AliceCoin` 合约将余额从 Alice 的地址转移到 Bob 的地址，并触发 `Transfer` 事件。`AliceICO` 合约可以调用 `transferFrom` 无限次，只要它不超过 Alice 设置的批准限制。`AliceICO` 合约可以通过调用 `allowance` 函数来跟踪它可以出售多少 AliceCoin 代币。

#### ERC-2612：带有“permit”的无 Gas 转移

在第 9 章中，我们全面探讨了 ERC-20 代币的传统 `transfer` 和 `transferFrom` 流程的来龙去脉。虽然这些方法一直是代币转移的支柱，但它们并非没有局限性。两者都需要发送方直接与区块链交互，这意味着他们必须手头有一些原生加密货币来支付 Gas 费用。这造成了一个重大障碍，特别是当代币被发送到一个没有任何原生资金的全新地址时。这是一种令人沮丧的体验，远非理想。

这就是 ERC-2612 的用武之地。它是 ERC-20 代币标准的一个巧妙补充，它允许用户批准代币转移，而无需自己接触区块链。以下是它的工作原理：无需发送链上事务来批准转移，您只需使用您的钱包签署必要的数据 — 例如接收者的地址、代币数量、到期时间和随机数。这将创建一个签名，并且任何需要执行转移的人（无论是接收者还是另一方）都可以将该签名提交给代币合约的 `permit` 方法。合约读取签名、验证签名并处理批准，所有这些都无需您为初始步骤支付 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 费用。它既高效又安全，并且消除了流程中的许多麻烦。

为了使 ERC-2612 工作，代币开发者需要扩展他们的 ERC-20 合约以包含此功能。一旦到位，它将为用户提供两个主要优势。首先，它简化了整个过程。无需批准每次转移，用户只需一个签名即可授予权限。第二，它节省了 [Gas](https://learnblockchain.cn/tags/Gas?map=EVM) 成本，因为您减少了所需的交易数量。

#### ERC-20 实现

虽然可以使用大约 30 行 Solidity 代码来实现与 ERC-20 兼容的代币，但大多数实现都更复杂。这是为了解决潜在的安全漏洞。EIP-20 标准提到了 Consensys 和 OpenZeppelin 开发的两种实现。Consensys EIP-20 代币自 2018 年以来一直没有维护，而 [OpenZeppelin 的 ERC-20 代币](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol) 已成为开发人员事实上的标准，并且正在积极维护。此实现构成了 OpenZeppelin 库的基础，该库实现了更复杂的与 ERC-20 兼容的代币，具有筹款上限、代币化金库、归属计划和其他功能。

### 启动我们自己的 ERC-20 代币

让我们创建并启动我们自己的代币。对于此示例，我们将使用 Foundry 框架。此示例假定您已[安装 Foundry](https://getfoundry.sh/introduction/installation/) 并对其进行了配置，并且您熟悉其基本操作。

我们将我们的代币称为 “Mastering Ethereum Token”，符号为 MET。首先，让我们使用以下命令创建并初始化 Foundry 项目目录：

```bash
$ mkdir METoken
$ cd METoken
$ forge init
```

您现在应该具有以下目录结构：

```
METoken/
├── foundry.toml
├── lib
│  └── forge-std
│      └── ...
├── README.md
├── script
│  └── Counter.s.sol
├── src
│  └── Counter.sol
└── test
     └── Counter.t.sol
```

`Counter` 是 Foundry 的默认示例合约，它带有自己的测试和部署脚本。我们将删除所有相关文件以为我们的代币合约腾出空间。

对于我们的示例，我们将导入 OpenZeppelin 库，这是基于 Solidity 的代币的行业标准：

```bash
$ forge install OpenZeppelin/openzeppelin-contracts
[...]
Installed openzeppelin-contracts v5.2.0
```

在 *METoken/lib/openzeppelin-contracts/contracts* 中，我们现在可以看到所有 OpenZeppelin 合约。OpenZeppelin 库包含的内容远不止 ERC-20 代币，但我们将只使用其中的一小部分。

接下来，让我们编写我们的代币合约。创建一个新文件 *METoken.sol*，并复制示例 10-1 中的代码。我们的合约非常简单，因为它从 OpenZeppelin 库继承了所有功能。

**示例 10-1. METoken.sol：一个实现 ERC-20 代币的 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 合约**

```solidity
pragma solidity 0.8.28;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract METoken is ERC20 {
    constructor(uint256 initialSupply) ERC20("METoken", "MET") {
        _mint(msg.sender, initialSupply);
    }
}
```

在这里，我们将 `"METoken"` 和 `"MET"` 作为名称和符号传递给 ERC-20 合约的构造函数。代币的初始供应量在部署期间作为构造函数参数提供，并将发送到此代币合约的部署者 (`msg.sender`)。我们正在使用小数位数的默认值 18，这是 ERC-20 代币的广泛采用的标准。

我们现在可以使用 Foundry 编译 `METoken` 合约：

```bash
$ forge build
[⠊] Compiling...
[⠒] Compiling 6 files with Solc 0.8.28
[⠢] Solc 0.8.28 finished in 36.18ms
Compiler run successful!
```

让我们设置一个部署脚本，将 `METoken` 合约带到区块链上。在 *METoken/script* 文件夹中创建一个新文件 *METokenDeploy.s.sol*，并复制以下代码：

```solidity
pragma solidity 0.8.28;
import {Script, console} from "forge-std/Script.sol";
import {METoken} from "../src/METoken.sol";
contract METokenDeployer is Script {
     METoken public _METoken;
     function run() public {
         vm.startBroadcast();
         _METoken = new METoken(50_000_000e18);
         vm.stopBroadcast();
     }
}
```

在此示例中，我们将 5000 万作为初始供应量传递。您是否注意到我们正在乘以 1e18？这些是代币的小数位数。请记住，为了拥有 *X* 个代币的余额，我们需要 *X* × 10 ^ 小数位数的代币数量。

> **注意**
>
> 脚本的后缀 *.s.sol* 是 Foundry 的命名约定，用于快速识别文件的用途。这不是必需的 — 将脚本文件放置在脚本文件夹中就足够了 — 但这是一个很好的实践，在开发期间会派上用场。同样的适用于带有 *.t.sol* 后缀的测试。

在我们部署到以太坊测试网络之一之前，让我们启动一个本地区块链来测试所有内容。我们将使用 Foundry 工具箱中的另一个工具：Anvil，一个本地以太坊开发节点。要使用它，只需打开一个新终端并键入 `anvil`。控制台将显示可用帐户列表、其私钥、链 ID、RPC URL 和其他信息。RPC URL 是 Foundry（或任何以太坊客户端）用于与我们的本地区块链节点通信的端点，从而实现事务、合约部署和数据检索。Anvil 的默认 RPC 是 *http://127.0.0.1:8545*。为了告诉我们的部署脚本部署到我们的本地区块链，我们需要通过标志 `--rpc-url "http://127.0.0.1:8545"` 将 Anvil 的 RPC URL 作为控制台参数提供。

我们需要的最后一部分是部署者帐户的私钥。由于这是一个本地区块链，我们在以太坊主网或测试网上使用的地址在这里没有任何资金，并且我们不想不必要地暴露真实的私钥。相反，我们将使用 Anvil 启动时生成的测试帐户。这些帐户在我们的本地链上预加载了 10,000 个 ETH，使其非常适合开发和测试。

我们已准备好通过运行以下命令来部署我们的代币：

```bash
$ forge script script/METokenDeploy.s.sol --broadcast --rpc-url "http://127.0.0.1:8545"
--private-key <DEPLOYER_PRIVATE_KEY>
[⠊] Compiling...
No files changed, compilation skipped
Script ran successfully.
```

> **注意**
>
> 您可能想知道 `--broadcast` 标志是做什么用的。这告诉 Foundry 实际将事务广播到区块链。没有它，Foundry 只会模拟事务。

控制台输出告诉我们部署脚本已成功运行。如果我们看一下运行 Anvil 的终端，我们会注意到很多活动，其中包括我们的合约创建：

```
   Transaction: 0xd01e3a90e1f2ee60112658e92f4ebf04c24df67d2ec1315cfb79d145729d15ec
     Contract created: 0x5FbDB2315678afecb367f032d93F642f64180aa3
     Gas used: 941861
     Block Number: 1
     Block Hash: 0x748b6058dea932317cacf45bb63be82f253554f359b97ace224e35979a92b00a
     Block Time: "Fri, 31 Jan 2025 19:10:42 +0000"
```

我们的 METoken 已成功部署到以下地址：

```
0x5FbDB2315678afecb367f032d93F642f64180aa3
```

或者，我们可以使用 forge 的 `create` 控制台命令来部署我们的代币：

```bash
$ forge create METoken --broadcast --rpc-url http://127.0.0.1:8545 --private-key
<DEPLOYER_PRIVATE_KEY> --constructor-args 50000000000000000000000000
```

这里，总供应量作为构造函数参数传递，并考虑到小数位数。

#### 与 METoken 交互

我们可以通过多种方式与我们的合约交互。我们可以使用 Remix（就像我们在第 2 章中所做的那样）、像 Foundry 的 Chisel 这样的 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) REPL 或像 [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) 这样的 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 库。我们也可以使用 [Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM) 脚本执行事务，这就是我们将用于示例的内容。

以太坊地址是 40 个字符的十六进制字符串，它们并不容易读取。为了使我们的示例更清晰，我们将为我们正在使用的两个地址分配昵称：Deployer 用于部署 MET 合约的地址，Alice 用于辅助地址。我们还将使用 Anvil 的一个预资助地址作为 Alice。

让我们创建一个 [Foundry](https://learnblockchain.cn/tags/Foundry?map=EVM) 脚本，以检查 Deployer 的 METoken 余额并将一些 METoken 发送到 Alice。复制以下代码段中的内容并将它们粘贴到新文件 *METoken/script/METokenInteraction.s.sol* 中：

```solidity
pragma solidity 0.8.28;
import {Script, console} from "forge-std/Script.sol";
import {METoken} from "../src/METoken.sol";
contract METokenInteraction is Script {
     METoken public _METoken = METoken(0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512);
     address alice = 0x70997970C51812dc3A010C7d01b50e0d17dc79C8;
     function run() public {
         vm.startBroadcast();
         uint256 ourBalance = _METoken.balanceOf(msg.sender);
         console.log("Deployer initial balance:", ourBalance);
         uint256 aliceBalance = _METoken.balanceOf(alice);
         console.log("Alice initial balance:", aliceBalance);
         uint256 amountToTransfer = 50e18;
         bool success = _METoken.transfer(alice, amountToTransfer);
         if (success) {
             console.log("Transfer successful");
         } else {
             console.log("Transfer failed");
             revert();
         }
         ourBalance = _METoken.balanceOf(msg.sender);
         console.log("Deployer final balance:", ourBalance);
         aliceBalance = _METoken.balanceOf(alice);
         console.log("Alice final balance:", aliceBalance);
         vm.stopBroadcast();
     }
}
```

我们可以使用以下控制台命令运行脚本：

```bash
$ forge script script/METokenInteraction.s.sol --private-key <DEPLOYER_PRIVATE_KEY>
--rpc-url "http://127.0.0.1:8545" -vv
```

重要的是要使用与部署相同的私钥。这样可以确保 `msg.sender` 对应于持有初始代币供应量的部署者地址。

> **注意**
>
> Foundry 的 `-v` 标志控制运行 `forge script` 或 `forge build` 等命令时输出的详细级别。增加 `v` 的数量会增加输出详细程度以包含更多信息。要显示控制台日志，我们需要至少 `-vv`，而 `-vvvv` 提供最大verbose。

一旦我们运行脚本，以下内容将打印在控制台中：

```bash
[⁘] Compiling...
[:] Compiling 1 files with Solc 0.8.28
[⁖] Solc 0.8.28 finished in 312.39ms
Compiler run successful!
Script ran successfully.
== Logs ==
   Deploy```solidity
pragma solidity 0.8.28;
contract NaiveFaucet {
    receive() external payable {}
    // Function to withdraw Ether from the contract
    // 从合约中提取 Ether 的函数
    function withdraw(uint256 amount) public {
        require(amount <= address(this).balance, "faucet 中的余额不足");
        payable(msg.sender).transfer(amount);
    }
}
```

我们的目录应该像这样：

```
METoken/
+---- src
|   +---- NaiveFaucet.sol
|   +---- METoken.sol
```

让我们编译和部署 `NaiveFaucet` 合约：

```bash
$ forge create NaiveFaucet --broadcast --rpc-url http://localhost:8545
--private-key <部署者_私钥>
[⁘] 编译中...
[:] 使用 Solc 0.8.28 编译 1 个文件
[⁖] Solc 0.8.28 在 8.69ms 内完成
编译器运行成功!
部署者: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
已部署到: 0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0
交易哈希: 0x4d1947547e3cfec8db670f3c1b7ff309b41de8aacee42165578a3ddf8619f63f
```

太好了，我们的 `NaiveFaucet` 合约已经部署到地址 `0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0`。现在，让我们通过将以下脚本复制到 *METoken/script/METokenSend.s.sol* 来向 `NaiveFaucet` 合约发送一些 MET：

```solidity
pragma solidity 0.8.28;
import {Script, console} from "forge-std/Script.sol";
import {METoken} from "../src/METoken.sol";
contract METokenSend is Script {
    METoken public _METoken = METoken(0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512);
    address naiveFaucet = 0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0;
    function run() public {
        vm.startBroadcast();
        uint256 amountToSend = 100e18;
        bool success = _METoken.transfer(naiveFaucet, amountToSend);
        if (success) {
            console.log("Transfer successful");
        } else {
            console.log("Transfer failed");
            revert();
        }
        uint256 faucetBalance = _METoken.balanceOf(naiveFaucet);
        console.log("Faucet balance:", faucetBalance);
        vm.stopBroadcast();
    }
}
```

我们可以使用以下命令运行它：

```bash
$ forge script script/METokenSend.s.sol --private-key <部署者_私钥>
--rpc-url "http://127.0.0.1:8545" -vv
[⁘] 编译中...
[:] 使用 Solc 0.8.28 编译 1 个文件
[⁖] Solc 0.8.28 在 413.41ms 内完成
编译器运行成功!
脚本运行成功。
== 日志 ==
  转移成功
  Faucet 余额: 100000000000000000000
```

同样，我们需要使用部署者的私钥使其工作，因为这是启动转移的地址。

我们已经将 100 MET 转移到 `NaiveFaucet` 合约。现在，我们如何提取这些代币？

请记住，*NaiveFaucet.sol* 是一个非常简单的合约。它只有一个函数 `withdraw`，用于提取 *ether*。它没有用于提取 MET 或任何其他 ERC-20 代币的函数。如果我们使用 `withdraw`，它将尝试发送 ether，但由于 `NaiveFaucet` 还没有 ether 的余额，它将失败。

`METoken` 合约知道 `NaiveFaucet` 有余额，但转移该余额的唯一方法是它收到来自合约地址的 `transfer` 调用。在某种程度上，我们需要使 `NaiveFaucet` 合约调用 `METoken` 中的 `transfer` 函数。

如果您想知道接下来该做什么，请不要。这个问题没有解决方案。发送到 `NaiveFaucet` 的 MET 被卡住，永远卡住了。只有 `NaiveFaucet` 合约可以转移它，而 `NaiveFaucet` 合约没有代码来调用 ERC-20 代币合约的 `transfer` 函数。

也许您预料到了这个问题。很可能，你没有。事实上，成百上千的 Ethereum 用户也没有，他们不小心将各种代币转移到没有任何 ERC-20 功能的合约中。多年来，惊人的数百万美元像这样“卡住”并且永远丢失。

#### 演示 “approve and transferFrom” 工作流

我们的 `NaiveFaucet` 合约无法处理 ERC-20 代币。使用 `transfer` 函数将代币发送到它导致这些代币丢失。现在让我们重写合约，使其处理 ERC-20 代币。具体来说，我们将把它变成一个 faucet，向任何需要的人赠送 MET。

我们的新 faucet 合约 *METFaucet.sol* 将如例 10-2 所示。

**例 10-2. METFaucet.sol：METoken 的 faucet**

```solidity
pragma solidity 0.8.28;
import "@openzeppelin/contracts/token/[ERC20](https://learnblockchain.cn/tags/ERC20?map=EVM)/IERC20.sol";
contract METFaucet {
    IERC20 public _METoken;
    address public _METOwner;
    constructor(address _metokenAddress, address metOwner) {
        _METoken = IERC20(_metokenAddress);
        _METOwner = metOwner;
    }
    // Function to withdraw METoken from the contract
    // 从合约中提取 METoken 的函数
    function withdraw(uint256 amount) public {
        require(amount <= 10e18, "最多 10 MET");
        require(_METoken.transferFrom(_METOwner, msg.sender, amount), "转移失败");
    }
}
```

我们对基本的 `Faucet` 示例进行了一些更改。由于 `METFaucet` 将使用 `METoken` 中的 `transferFrom` 函数，因此它需要两个额外的变量。一个将保存 `METoken` 合约的地址。另一个将保存 MET 所有者的地址，他们将批准 faucet 提款。在我们的例子中，所有者是部署者，因为他们收到了初始供应。`METFaucet` 合约将调用 `METoken.transferFrom` 并指示它将 MET 从所有者移动到 faucet 提款请求来自的地址。

我们在这里声明这两个变量：

```solidity
IERC20 public _METoken;
address public _METOwner;
```

由于我们的 faucet 需要使用 `METoken` 和 `METOwner` 的正确地址进行初始化，因此我们需要声明一个自定义构造函数：

```solidity
// METFaucet constructor - provide the address of the METoken contract and
// METFaucet 构造函数 - 提供 METoken 合约的地址和
// the owner address we will be approved to transferFrom
// 我们将被批准从其转移的所有者地址
constructor(address _metokenAddress, address metOwner) {
    _METoken = IERC20(_metokenAddress);
    _METOwner = metOwner;
}
```

下一个更改是 `withdraw` 函数。`METFaucet` 不调用 `transfer`，而是使用 `METoken` 中的 `transferFrom` 函数，并要求 `METoken` 将 MET 转移到 faucet 接收者：

```solidity
// Use the transferFrom function of METoken
// 使用 METoken 的 transferFrom 函数
_METoken.transferFrom(metOwner, msg.sender, withdraw_amount);
```

最后，由于我们的 faucet 不再发送 ether，我们可能应该阻止任何人向 `METFaucet` 发送 ether，因为我们不希望它被卡住。为了拒绝传入的 ether，只需从我们的合约中删除 `receive` 函数即可。

现在我们的 *METFaucet.sol* 代码已准备就绪，我们可以通过提供 MET 代币地址及其部署者作为地址参数来部署它：

```bash
$ forge create METFaucet --broadcast --rpc-url http://localhost:8545 --private-key
<部署者_私钥> --constructor-args
"0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512""0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
[⁘] 编译中...
没有文件更改，跳过编译
部署者: 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266
已部署到: 0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9
交易哈希: 0xa8bfbde9489ee40d41328a80538d0d3e7778b7f3b896c1d51897bf85bb25cec2
```

`METFaucet` 合约已部署到 `0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9`，我们几乎准备好测试它了。首先，让我们编写一个 *METApprove.s.sol* 脚本，以允许 `METFaucet` 合约花费所有者的 MET 代币：

```solidity
pragma solidity 0.8.28;
import {Script, console} from "forge-std/Script.sol";
import {METoken} from "../src/METoken.sol";
contract METApprove is Script {
    METoken public _METoken = METoken(0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512);
    address _METFaucet = 0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9;
    function run() public {
        vm.startBroadcast();
        bool success = _METoken.approve(_METFaucet, type(uint256).max);
        if (success) {
            console.log("Approve successful");
        } else {
            console.log("Approve failed");
            revert();
        }
        vm.stopBroadcast();
    }
}
```

我们可以使用以下命令运行它：

```bash
$ forge script script/METApprove.s.sol --broadcast --private-key <部署者_私钥>
--rpc-url "http://127.0.0.1:8545" -vv
[⠊] 编译中...
[⠰] 使用 Solc 0.8.28 编译 2 个文件
[⠔] Solc 0.8.28 在 327.90ms 内完成
编译器运行成功!
脚本运行成功。
== 日志 ==
  批准成功
```

现在，我们可以编写一个脚本，让辅助地址与 `METFaucet` 合约交互，以提取 10 个 MET 代币，并在操作前后记录其余额。让我们创建一个如示例 10-3 所示的 *METFaucetWithdraw.s.sol* 脚本。

**示例 10-3. METFaucetWithdraw: faucet 提款脚本**

```solidity
pragma solidity 0.8.28;
import {Script, console} from "forge-std/Script.sol";
import {METoken} from "../src/METoken.sol";
import {METFaucet} from "../src/METFaucet.sol";
contract METFaucetWithdraw is Script {
    METoken public _METoken = METoken(0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512);
    METFaucet public _METFaucet = METFaucet(0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9);
    function run() public {
        vm.startBroadcast();
       uint256 balanceBefore = _METoken.balanceOf(msg.sender);
       console.log("Alice balance before:", balanceBefore);
       _METFaucet.withdraw(10e18);
       uint256 balanceAfter = _METoken.balanceOf(msg.sender);
       console.log("Alice balance after:", balanceAfter);
        vm.stopBroadcast();
    }
}
```

我们现在可以通过在运行脚本时提供 Alice 的私钥来从 Alice 的地址运行此脚本：

```bash
$ forge script script/METFaucetWithdraw.s.sol --broadcast --private-key <ALICE_私钥>
--rpc-url "http://127.0.0.1:8545" -vv
[⠊] 编译中...
[⠰] 使用 Solc 0.8.28 编译 1 个文件
[⠔] Solc 0.8.28 在 330.97ms 内完成
编译器运行成功!
脚本运行成功。
== 日志 ==
  Alice 之前的余额: 0
  Alice 之后的余额: 10000000000000000000
```

正如您从结果中看到的那样，我们可以使用 `approve` 和 `transferFrom` 工作流来授权一个合约转移在另一个代币中定义的代币。如果使用得当，ERC-20 代币可以被 EOA 和其他合约使用。但是，正确管理 ERC-20 代币的负担被推到了用户界面。如果用户错误地尝试将 ERC-20 代币转移到合约地址，并且该合约没有配备接收 ERC-20 代币的功能，则代币将丢失。

### ERC-20 代币的问题

ERC-20 代币标准的采用确实具有爆炸性。已经启动了数千个代币，既可以试验新功能，也可以在各种“众筹”拍卖和 ICO 中筹集资金。但是，正如我们在将代币转移到合约地址的问题中所看到的那样，存在一些潜在的陷阱。

ERC-20 代币不太明显的问题之一是，它们暴露了代币和 ether 本身之间的细微差异。当 ether 通过以接收者地址作为其目的地的交易转移时，代币转移发生在*特定的代币合约状态*中，并将代币合约作为其目的地，而不是接收者的地址。代币合约跟踪余额并发出事件。在代币转移中，实际上没有交易发送给代币的接收者。相反，接收者的地址被添加到代币合约本身内的映射中。将 ether 发送到地址的交易会更改地址的状态。将代币转移到地址的交易只会更改代币合约的状态，而不会更改接收者地址的状态。即使具有 ERC-20 代币支持的钱包也不会意识到代币余额，除非用户显式添加特定的代币合约以“监视”。一些钱包会监视最受欢迎的代币合约，以检测它们控制的地址持有的余额，但这仅限于现有 ERC-20 合约的一小部分。

事实上，用户不太可能*想要*跟踪所有可能的 ERC-20 代币合约中的所有余额。许多 ERC-20 代币更像是电子邮件垃圾邮件，而不是可用的代币。它们自动为具有 ether 活动的帐户创建余额，以吸引用户。如果您有一个具有长期活动历史的 Ethereum 地址，尤其是在预售中创建的地址，您会发现它充满了凭空出现的“垃圾”代币。当然，该地址实际上并没有充满代币；而是代币合约中有您的地址。您只有在区块浏览器或您用于查看地址的钱包正在监视这些代币合约时才能看到这些余额。

代币的行为方式与 ether 不同。Ether 使用 `send` 函数发送，并被合约中的任何可支付函数或任何外部拥有的地址接受。代币使用仅存在于 ERC-20 合约中的 `transfer` 或 `approve` 和 `transferFrom` 函数发送，并且不（至少在 ERC-20 中）触发接收者合约中的任何可支付函数。代币旨在像 ether 这样的加密货币一样运作，但它们带有一些打破这种错觉的差异。

让我们关注 `approve` 和 `transferFrom` 模式。对于较新的用户，`approve`-`transferFrom` 系统可能特别具有误导性。许多人认为转移代币是一个单一的操作，因此遇到一个两步式过程会感到困惑和违反直觉。更糟糕的是，`approve` 操作看起来无害但可能是一个陷阱。当用户批准合约时，他们可能会在不知不觉中授予无限权限，从而允许恶意行为者稍后耗尽他们的代币。这种理解上的差距使网络钓鱼攻击更容易，并突出了系统的设计如何与新手期望与区块链交互的方式不符。

考虑另一个问题。要发送 ether 或使用任何 Ethereum 合约，您需要 ether 来支付 gas。要发送代币，您*也需要 ether*。您不能使用代币支付交易的 gas，并且代币合约无法为您支付 gas。例如，假设您使用交易所将一些 Bitcoin 转换为代币。您在跟踪该代币合约并显示您的余额的钱包中“收到”该代币。它看起来与您钱包中的任何其他加密货币相同。尝试发送该代币，但您的钱包会通知您需要 ether 才能这样做。您可能会感到困惑——毕竟，您不需要 ether 才能收到该代币。也许您没有 ether。也许您甚至不知道该代币是 Ethereum 上的 ERC-20 代币；也许您认为它是一种具有自己区块链的加密货币。这个错觉破灭了。

我们可以使用 ERC-2612 的 `permit` 函数以及智能钱包（如 EIP-4337 和 EIP-7702）提供的 gas 费用赞助功能来部分解决此问题。ERC-2612 允许您通过签署链下消息来批准代币授权，从而跳过链上批准交易的需要。EIP-4337 和其他智能钱包架构允许第三方支付您的 gas 费用，以换取 ERC-20 代币的报销。挑战在于代币中对 ERC-2612 的采用有限以及智能钱包缺乏广泛使用。

这些问题中的一些是 ERC-20 代币特有的。其他问题是与 Ethereum 中抽象和接口边界相关的更普遍的问题。一些问题可以通过更改代币接口来解决，而另一些问题可能需要更改 Ethereum 中的基本结构（例如 EOA 和合约之间以及交易和消息之间的区别）。一些问题可能无法完全“解决”，可能需要用户界面设计来隐藏细微差别并使用户体验保持一致，而不管底层的区别如何。

在以下各节中，我们将研究尝试解决其中一些问题的各种提案。

### ERC-223：一种提议的代币合约接口标准

ERC-223 提案试图通过检测目标地址是否为合约来解决无意中将代币转移到合约（可能支持或不支持代币）的问题。ERC-223 要求设计为接受代币的合约实现一个名为 `tokenFallback` 的函数。如果转移的目标是一个合约，并且该合约不支持代币（即不实现 `tokenFallback`），则转移失败。

为了检测目标地址是否为合约，ERC-223 参考实现以相当有创意的方式使用了内联字节码的一小段：

```solidity
function isContract(address _addr) private view returns (bool is_contract) {
  uint256 length;
    assembly {
      // retrieve the size of the code on target address; this needs assembly
      // 检索目标地址上的代码大小；这需要汇编
      length := extcodesize(_addr)
    }
    return (length>0);
}
```

> **注意**
>
> `extcodesize` 返回存储在给定地址的字节码的大小。从历史上看，这是 EOA 和智能合约之间的主要区别：EOA 没有代码，而合约有代码。但该假设不再成立。使用 EIP-7702，EOA 现在可以附加代码，从而完全模糊了界限。
> 还有一个重要的边缘情况：在合约的构造函数阶段，其代码尚未存储在链上。EVM 仅在构造函数完成执行后才将合约的字节码写入地址。因此，如果您从其构造函数（或尚未完成部署的另一个合约）中调用合约自身地址上的 `extcodesize`，它将返回 `0`，即使该地址最终将包含代码。因此，如果一个地址没有代码，它可能是一个 EOA 或一个仍在构建中的合约。如果它确实有代码，它可能是一个已部署的合约或一个使用自定义代码有效载荷的 EOA。简而言之，此检查不再能可靠地告诉我们地址是否为合约。

ERC-223 合约接口规范是：

```solidity
interface ERC223Token {
  uint256 public totalSupply;
  function balanceOf(address who) public view returns (uint256);
  function name() public view returns (string _name);
  function symbol() public view returns (string _symbol);
  function decimals() public view returns (uint8 _decimals);
  function totalSupply() public view returns (uint256 _supply);
  function transfer(address to, uint256 value) public returns (bool success);
  function transfer(address to, uint256 value, bytes data) public returns (bool success);
  function transfer(address to, uint256 value, bytes data, string custom_fallback)
      public returns (bool success);
  event Transfer(address indexed from, address indexed to, uint256 value,
                  bytes indexed data);
}
```

ERC-223 没有得到广泛实施，并且在 [ERC 讨论线程](https://github.com/ethereum/EIPs/issues/223) 中对于在合约接口级别还是用户界面级别实施更改之间的向后兼容性和权衡有一些争论。争论仍在继续。

### ERC-777：本可能实现的未来

ERC-777 通过引入*挂钩*为代币交互带来了一种新的方法：在代币转移期间触发的函数。这些挂钩与 ERC-20 完全兼容，确保现有系统可以无缝地与 ERC-777 代币交互。

发送者的挂钩 `tokensToSend` 在代币离开帐户之前执行，允许发送者添加逻辑，如日志记录或条件检查。另一方面，接收者的挂钩 `tokensReceived` 在代币到达帐户时会立即生效。ERC-777 挂钩架构的核心是 ERC-1820 注册表，它记录了哪些地址实现了所需的挂钩：发送者的 `tokensToSend` 和接收者的`tokensReceived`。这确保了仅当双方都准备好处理转移时，转移才会成功，从而防止了常见的代币丢失等问题。

挂钩还简化了交易。对于 ERC-20，将代币转移到合约通常需要一个繁琐的两步式过程：`approve`，然后是 `transferFrom`。ERC-777 取消了这一点，允许通过其挂钩进行原子交易。它高效、直观，而且坦率地说，早就该这样做了。

ERC-777 的另一个有趣的功能是其运营商机制，该机制允许授权地址（通常是智能合约，如交易所或支付处理器）代表持有人发送和销毁代币。持有人可以随时授予或撤回对运营商的授权，让他们完全控制哪些第三方可以在任何给定时刻管理他们的代币。每个授权或撤销都会发出一个事件，从而提供授权更改的可见性。

ERC-777 合约接口规范是：

```solidity
interface ERC777Token {
    function name() public view returns (string);
    function symbol() public view returns (string);
    function totalSupply() public view returns (uint256);
    function granularity() public view returns (uint256);
    function balanceOf(address owner) public view returns (uint256);
    function send(address to, uint256 amount, bytes userData) public;
    function authorizeOperator(address operator) public;
    function revokeOperator(address operator) public;
    function isOperatorFor(address operator, address tokenHolder)
        public constant returns (bool);
    function operatorSend(address from, address to, uint256 amount,
                         bytes userData,bytes operatorData) public;
    event Sent(address indexed operator, address indexed from,
                 address indexed to, uint256 amount, bytes userData,
                 bytes operatorData);
    event Minted(address indexed operator, address indexed to,
                  uint256 amount, bytes operatorData);
    event Burned(address indexed operator, address indexed from,
                  uint256 amount, bytes userData, bytes operatorData);
    event AuthorizedOperator(address indexed operator,
                                 address indexed tokenHolder);
    event RevokedOperator(address indexed operator, address indexed tokenHolder);
}
```

#### ERC-777 代币的问题

虽然 ERC-777 使代币交互更加直观，但它的挂钩引入了一些重大的挑战——最值得注意的是，重入攻击的风险。这些攻击利用了合约在完全更新其状态之前重新进入其自身逻辑的能力，通常会导致严重的后果。ERC-777 挂钩的本质是在代币转移期间将执行控制权传递给发送者和接收者，这为这种漏洞创造了一个理想的场景。这意味着开发人员必须小心处理这些挂钩，以避免漏洞。

由 ERC-777 代币集成引起的重入最臭名昭著的案例是 2020 年 4 月的 Uniswap v1 事件。Uniswap 是一种去中心化交换协议，由于 ERC-777 的挂钩，无意中将其储备暴露于利用。攻击者可以在操作中途回调到 Uniswap 合约，从而利用代币和 ether 储备之间的差异来提取资金。虽然此漏洞特定于 Uniswap 与 ERC-777 的交互方式，但它清楚地提醒了这些挂钩引入的风险。

另一个值得注意的问题是 DoS 攻击的可能性。假设一个合约将 ERC-777 代币分发给多个帐户。如果其中一个接收者是恶意合约，该合约被编程为在 `tokensReceived` 挂钩期间恢复交易，则整个分发过程将被阻止。

这些风险突出了为什么集成 ERC-777 并不像交换 ERC-20 那么简单。开发人员需要采用最佳实践，例如依赖重入锁来缓解漏洞。

#### 本可能实现的未来

ERC-777 本可能成为 Ethereum 代币标准的下一个演变。它解决了 ERC-20 的许多痛点，尤其是在用户体验和代币处理方面。防止代币丢失、启用原子交易以及构建更丰富的合约交互的能力都是引人注目的进步。

然而，Ethereum 社区变得犹豫不决。潜在的 DoS 和重入场景投下了长长的阴影。开发人员担心集成 ERC-777 的复杂性和风险，即使这些风险可以通过正确的预防措施来管理。我们没有迎接挑战，而是坚持使用熟悉但有限的 ERC-20。这是一个错失的机会，无法采用一种使代币更接近 Ethereum 理念的标准，同时提供卓越的功能。

最后，ERC-777 的挂钩不是罪魁祸首；不正确的实施是。通过一些努力并遵守安全编码实践，ERC-777 可以为更无缝的 Ethereum 生态系统铺平道路。要进一步研究这个问题，建议阅读 OpenZeppelin 库[关于 ERC-777 弃用的讨论](https://github.com/OpenZeppelin/openzeppelin-contracts/issues/2620)。

## ERC-721：NFT 标准

到目前为止，我们已经探索了可替代代币的代币标准，如 ERC-20，其中每个单元都是可互换的，并且系统只关心帐户余额。现在，让我们深入研究一些不同的和更独特的东西：ERC-721，非同质化代币的标准，或者正如现在大家都知道的那样，NFT。您可能在 2021 年的狂热期间听说过 NFT，当时像 CryptoPunks、Bored Ape Yacht Club 和 NBA Top Shot 这样的数字收藏品占据了头条新闻，并以惊人的价格售出。像 OpenSea 和 Rarible 这样的交易平台成为加密货币世界的家喻户晓的名字。

但究竟是什么使 NFT 如此特别？与 ERC-20 代币不同，NFT 全都是关于独特性。每个代币代表对不同项目的拥有权，该项目可以是任何东西：数字收藏品、游戏内资产、艺术品，甚至是房地产或汽车等现实世界的资产。ERC-721 的美妙之处在于它的灵活性。它不在乎代币代表什么，只要它是唯一的并且可以用数字识别。在底层，这是通过每个 NFT 的 `uint256` 标识符来实现的。可以将其视为区分一个代币与另一个代币的序列号。在 ERC-20 中，我们通过将帐户映射到其持有的金额来跟踪余额，但在 ERC-721 中，除了余额之外，我们还将每个唯一的代币 ID 映射到其所有者：

```solidity
mapping (uint256 => address) private _owners;
```

结构上的这种微妙变化改变了一切。每个 NFT 都与特定的所有者相关联，并且可以直接跟踪其历史、来源和唯一属性。这就是使 ERC-721 非常适合于个性化很重要的情况，例如证明对独一无二的艺术品、稀有的游戏内剑甚至元宇宙中的一块土地的所有权。

使 ERC-721 真正强大和通用的原因在于可选的 ERC-721 元数据扩展，该扩展允许将每个代币 ID 绑定到统一资源标识符 (URI)。此 URI 可以指向描述 NFT 的元数据，例如其名称、描述和图像。该 URI 可能是指向集中式服务器的标准 HTTP 链接，也可能是指向去中心化存储的星际文件系统 (IPFS) 链接。集中式服务器可能会离线或完全消失，从而使 NFT 依赖于第三方基础设施。相比之下，IPFS 有助于确保元数据保持可访问且防篡改，因此是存储 NFT 元数据的首选。将每个代币与元数据 URI 相关联的能力使 NFT 能够携带丰富的、描述性数据和多媒体内容，从而进一步增强其独特性和可用性。

NFT 的投机性使用，尤其是作为数字收藏品，不可否认地主导了公众的叙述。这些代币成为炒作的象征，其价值由稀缺性、名人代言和社区情绪驱动。然而，在引人注目的头条新闻背后，是一个具有重新定义行业潜力的实际应用世界。例如，NFT 可以用于供应链管理，以跟踪商品的来源，确保消费者的真实性和透明度。它们可以代表产权契约，通过自动化所有权转移和减少欺诈来简化房地产交易。NFT 还可以用于教育，以发放可验证的凭证，如学位和证书，这些凭证具有防篡改性并且可以普遍访问。

虽然收藏品将 NFT 带入了人们的视线，但它们的真正希望在于这些实际的、变革性的用途。通过结合独特性、可追溯性和可编程性，ERC-721 代币有望成为数字经济的基础构建块。无论您是铸造古怪的艺术品还是对挽救生命的医疗记录进行代币化，ERC-721 都使开发人员能够创建远远超出投机的解决方案。

ERC-721 合约接口规范如下：

```solidity
interface [ERC721](https://learnblockchain.cn/tags/ERC721?map=EVM) /* is ERC165 */ {
    event Transfer(address indexed _from, address indexed _to, uint256 _deedId);
    event Approval(address indexed _owner, address indexed _approved,
                    uint256 _deedId);
    event ApprovalForAll(address indexed _owner, address indexed _operator,
                                bool _approved);
    function balanceOf(address _owner) external view returns (uint256 _balance);
    function ownerOf(uint256 _deedId) external view returns (address _owner);
    function transfer(address _to, uint256 _deedId) external payable;
    function transferFrom(address _from, address _to, uint256 _deedId)
        external payable;
    function approve(address _approved, uint256 _deedId) external payable;
    function setApprovalForAll(address _operator, boolean _approved) payable;
    function supportsInterface(bytes4 interfaceID) external view returns (bool);
}
```

## ERC-1155：多代币标准

自从 ERC-20 和 ERC-721 为可替代和不可替代代币奠定了基础以来，Ethereum 已经走了很长一段路。ERC-1155 多代币标准结合了两者的优势，以实现高效和通用的代币管理。

想象一下你是一名游戏开发人员。你想要创建一个系统，让玩家可以收集金币（可替代）、独特的剑（不可替代）和可堆叠消耗的药水（半可替代）。对于 ERC-20 或 ERC-721，你将需要为每种类型的代币创建一个单独的智能合约。每个新合约都会增加 gas 成本并增加复杂性，因为你还需要管理这些合约之间的权限和交互。ERC-1155 解决了这个问题。它允许我们部署一个智能合约来管理多种代币类型。每种代币类型都由唯一的 ID 标识，并且合约可以处理任何代币类型组合的所有操作，包括转移、余额和元数据检索。这种简化的方法减少了冗余和交易成本，使 ERC-1155 成为广泛采用的标准。

ERC-1155 的批量操作是一个突出的功能。它们让我们在单个交易中转移或查询多个代币，节省 gas 并使该标准更具可扩展性。此外，ERC-1155 包括安全机制来防止锁定代币等问题。将代币转移到智能合约时，接收合约必须实现 `IERC1155Receiver` 接口；否则，交易将回退。这些挂钩支持代币转移期间的高级交互。例如，一个合约可以实现在收到代币时执行的自定义逻辑，例如更新游戏内排行榜或触发事件。但是，正如在 ERC-777 中看到的那样，如果这些挂钩处理不当，它们可能会引入漏洞，例如重入攻击。开发人员必须确保适当的安全措施，例如使用检查-效果-交互模式和重入锁，以在实施 ERC-1155 代币时保护他们的合约。

ERC-1155 合约接口规范如下：

```solidity
interface IERC1155 /* is IERC165 */ {
    event TransferSingle(address indexed operator, address indexed from, address indexed to,
uint256 id, uint256 value);
    event TransferBatch(
        address indexed operator,
        address indexed from,
        address indexed to,
        uint256[] ids,
        uint256[] values
    );
    event ApprovalForAll(address indexed account, address indexed operator, bool approved);
    event URI(string value, uint256 indexed id);
    function balanceOf(address account, uint256 id) external view returns (uint256);
    function balanceOfBatch(
        address[] calldata accounts,
        uint256[] calldata ids
    ) external view returns (uint256[] memoryToken 标准是实现的*最低*规范。这意味着，要符合比如说 ERC-20，你至少需要实现 ERC-20 标准指定的功能和行为。你也可以通过实现不属于标准一部分的功能来*添加*功能。

这些标准的主要目的是鼓励合约之间的*互操作性*。因此，所有钱包、交易所、用户界面和其他基础设施组件都可以以可预测的方式与任何遵循规范的合约进行*交互*。换句话说，如果你部署一个遵循 ERC-20 标准的合约，所有现有的钱包用户都可以无缝地开始交易你的代币，而无需任何钱包升级或你的任何努力。

这些标准旨在具有*描述性*而不是*规定性*。你如何选择实现这些功能取决于你；合约的内部运作与标准无关。它们有一些功能性要求，这些要求约束特定情况下的行为，但它们不规定实现方式。一个例子是当值设置为零时，转移函数的行为。ERC-20 标准没有规定在这种情况下交易是否应该回滚。

### 你应该使用这些标准吗？

鉴于所有这些标准，每个开发者都面临一个两难境地：使用现有的标准，还是突破它们施加的限制进行创新？

这个两难境地不容易解决。标准必然会限制你的创新能力，创建一个你必须遵循的狭窄的“车辙”。另一方面，基本标准是从数百个应用程序的经验中产生的，并且通常非常适合绝大多数用例。

作为这种考虑的一部分，还有一个更大的问题：互操作性和广泛采用的价值。如果你选择使用现有的标准，你将获得所有为与该标准一起工作而设计的系统的价值。如果你选择偏离标准，你必须考虑自己构建所有支持基础设施或说服其他人支持你的实现作为新标准的成本。倾向于开辟自己的道路并忽略现有标准的行为被称为“非我发明”综合症，与开源文化背道而驰。另一方面，进步和创新有时取决于偏离传统。这是一个棘手的选择，所以请仔细考虑！

> **注意**
>
> 根据 [Wikipedia](https://en.wikipedia.org/wiki/Not_invented_here)，不是“非我发明”是一种社会、公司或机构文化所采取的立场，它们避免使用或购买已经存在的产品、研究、标准或知识，因为它们的外部来源和成本，例如特许权使用费。

### 检测标准：EIP-165

正如我们所看到的，像 ERC-20 这样的标准简化了代币和钱包之间的交互。但是我们如何识别智能合约支持哪些接口呢？这就是 EIP-165 的用武之地，它提供了一种标准化的方式，让合约声明和检测接口。

EIP-165 定义了一种方法，让合约可以声明它们实现的接口。合约使用 `supportsInterface` 函数来为给定的接口 ID 返回一个 `true` 或 `false` 值（接口 ID 是一个唯一的标识符，计算方式是接口中所有函数选择器的 XOR）。例如，如果一个接口包括 `foo()` 和 `bar(int256)`，那么它的 ID 可以这样得出：

```
foo.selector ^ bar.selector
```

这种方法使其他合约和工具能够在交互之前验证兼容性。例如，一个市场可以确认一个 NFT 合约支持 ERC-721 接口，然后再列出它的代币。

要实现 EIP-165，一个合约需要继承一个基类，例如 OpenZeppelin 的 ERC-165，并重写 `supportsInterface` 方法来包括合约支持的接口：

```solidity
contract MyContract is IMyContract, ERC165 {
    function supportsInterface(bytes4 interfaceId) public view override returns (bool) {
        return interfaceId == type(IMyContract).interfaceId ||
super.supportsInterface(interfaceId);
    }
}
```

为了更好地理解 EIP-165 在实践中是如何工作的，让我们看看 ERC-1155，这是一个用途广泛且被广泛使用的多代币合约标准：

```solidity
abstract contract ERC1155 is Context, ERC165, IERC1155, IERC1155MetadataURI,
    IERC1155Errors {
[...]
    /**
     * @dev See {IERC165-supportsInterface}.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC165,
IERC165) returns (bool) {
        return
            interfaceId == type(IERC1155).interfaceId ||
            interfaceId == type(IERC1155MetadataURI).interfaceId ||
            super.supportsInterface(interfaceId);
    }
[...]
}
```

> **警告**
>
> EIP-165 依赖于合约诚实地报告它们的功能。一个恶意或实现不佳的合约可能会虚假地声称支持一个接口，从而导致潜在的问题。虽然 EIP-165 改善了开发者体验并减少了摩擦，但它不应被视为安全保证。

对于更高级的场景，例如当合约代表其他合约实现接口时，开发者可以探索 ERC-1820，它使用一个全局注册表来跟踪接口支持。虽然 ERC-1820 比 EIP-165 更复杂，但它为去中心化系统提供了更大的灵活性。

### 成熟带来的安全

除了标准的选择，还有*实现*的并行选择。当你决定使用像 ERC-20 这样的标准时，你必须决定如何实现兼容的设计。[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)生态系统中存在许多现有的“参考”实现，这些实现被广泛使用，或者你可以从头开始编写自己的实现。同样，这种选择代表了一个可能具有严重安全影响的两难境地。

现有的实现都经过了“实战考验”。虽然不可能证明它们是安全的，但其中许多都支撑着价值数百万美元的代币——在某些情况下，价值数十亿美元。它们受到了反复而猛烈的攻击。到目前为止，还没有发现任何重大的漏洞。编写你自己的实现并不容易；合约可以通过许多微妙的方式被破坏。使用经过良好测试、广泛使用的实现要安全得多。在我们的例子中，我们使用了 OpenZeppelin 的 ERC-20 标准实现，因为这个实现从根本上来说是注重安全的。

如果你使用现有的实现，你也可以扩展它。同样，要小心这种冲动。复杂性是安全的敌人。你添加的每一行代码都会扩大合约的攻击面，并且可能代表一个潜伏的漏洞。在你将大量价值放在合约之上并且有人破坏它之前，你可能不会注意到问题。

> **提示**
>
> 标准和实现选择是整体安全[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)设计的重要组成部分，但它们不是唯一的考虑因素（请参阅第 9 章）。

## 代币接口标准的扩展

到目前为止，我们讨论的代币标准为创建和管理代币提供了基本功能。然而，它们有意地保持最小化，为项目扩展和调整它们以适应特定需求留下了空间。随着时间的推移，许多项目都建立在这些标准之上，引入了增强可用性、安全性和灵活性的功能。OpenZeppelin 是[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)的领先库，已成为此类扩展的首选来源。让我们来探索一些 ERC-20、ERC-721 和 ERC-1155 代币最值得注意的扩展。

例如，在 ERC-20 中，我们看到了燃烧机制的添加。燃烧允许代币从流通中永久移除，从而减少供应，这对于通货紧缩模型或需要有意识地控制供应的代币经济学来说非常有用。另一方面，一些项目会加入上限来设置总供应量的硬性限制，确保永远不会铸造超过预定阈值的代币。

[ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM) 的另一个有趣的补充是投票功能。这允许代币持有者直接通过他们的代币参与治理决策。实现此功能的项目创建了去中心化的决策流程，使利益相关者可以在协议的演变过程中发表意见。

[ERC-721](https://learnblockchain.cn/tags/ERC721?map=EVM) 在其扩展中也看到了类似的创造力。像版税支付这样的功能让创作者在他们的 [NFT](https://learnblockchain.cn/tags/NFT) 被交易时可以赚取一定比例的销售额。URI 存储是另一种常见的添加，它允许元数据被动态地存储和检索，这对于具有不断变化的属性的 [NFT](https://learnblockchain.cn/tags/NFT) 尤其有用。可枚举的扩展允许开发者有效地列出地址持有的所有代币，从而更容易构建市场或[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)。

ERC-1155，多代币标准，也没有被抛在后面。[ERC-1155](https://learnblockchain.cn/tags/ERC1155?map=EVM) 的扩展包括可燃烧代币和可暂停合约，从而在使用案例（如游戏或代币化供应链）中增加了灵活性。一些实现还增强了元数据处理，确保代币详细信息保持可访问且易于更新。

除了这些之外，还存在无数其他的扩展，用于满足众筹、黑名单、白名单以及在转账中实施费用等需求。开发者经常将这些功能与其他标准库（如 [OpenZeppelin](https://learnblockchain.cn/tags/OpenZeppelin?map=EVM) 的 Ownable 或访问控制）结合使用，从而利用更多经过实战考验的资源。

灵活性伴随着责任。扩展代币标准涉及在创新与互操作性之间取得平衡。编写自定义功能可能看起来很有吸引力，但它通常会引入不必要的复杂性和风险。相反，利用完善的库和扩展（如 [OpenZeppelin](https://learnblockchain.cn/tags/OpenZeppelin?map=EVM) 的库和扩展）可以确保安全性和代码质量，并显着降低开发成本。当已经存在强大、经过测试的解决方案时，没有必要重新发明轮子。

## 结论

代币不仅仅是数字货币；它们可以代表治理权利、访问凭证、身份和现实世界的资产。它们的通用性之所以成为可能，要归功于像 [ERC-20](https://learnblockchain.cn/tags/ERC20?map=EVM)、[ERC-721](https://learnblockchain.cn/tags/ERC721?map=EVM) 和 [ERC-1155](https://learnblockchain.cn/tags/ERC1155?map=EVM) 这样的标准，这些标准确保了[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)、交易所和 [DApp](https://learnblockchain.cn/tags/DApp) 之间的无缝互操作性，从而创建了一个更高效、互联的区块链生态系统。在本章中，我们研究了不同类型的代币和代币标准，并且你构建了你的第一个代币和相关应用程序。
