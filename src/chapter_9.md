# 第 9 章. 智能合约安全

安全是编写智能合约时最重要的考虑因素之一。在智能合约编程领域，错误代价高昂且容易被利用。在本章中，我们将探讨安全最佳实践和设计模式以及*安全反模式*，这些实践和模式可能会将漏洞引入智能合约中。

与其他程序一样，智能合约将完全按照编写的内容执行，但这并不总是程序员想要的结果。此外，所有智能合约都是公开的，任何用户都可以通过创建交易来与它们交互。任何漏洞都可能被利用，而且损失几乎总是无法弥补的。因此，遵循最佳实践并使用经过充分测试的设计模式至关重要。

将稳健的开发视为安全“瑞士奶酪模型”中的第一层。每一层保护都像一片瑞士奶酪：单独来看都不完美，但结合在一起可以形成更强大的防御。最首要的一层是遵循可靠的开发实践：使用可靠的设计模式、编写清晰且有目的的代码，并积极避免已知的陷阱。这个基础层为我们安全地保护合约免受漏洞攻击提供了最佳开端。除此之外，测试、代码审查和漏洞赏金等其他层增加了额外的保护，但这一切都始于我们的开发实践。

## 安全最佳实践

*防御性编程*是一种特别适合智能合约的编程风格。它强调以下几点，所有这些都是最佳实践：

**最小化/简洁**

甚至在编写代码之前，都值得退一步思考是否真的需要每个组件。设计可以简化吗？某些数据结构是否引入了不必要的攻击面？一旦架构确定下来，我们仍然应该带着批判的眼光检查代码，寻找减少行数、消除边缘情况或删除非必要功能的机会。更简单的合约更容易推理、测试和审计。虽然一些 DeFi 协议确实会增长到几千行代码，但当有人吹嘘其代码库的大小的时候，仍然值得怀疑。更多的代码通常意味着更多的错误，而不是更多的价值。

**代码重用**

尽量不要重复发明轮子。如果已经存在一个库或合约可以完成您需要的大部分工作，请重用它。例如，[OpenZeppelin](https://www.openzeppelin.com) 提供了一套被广泛采用、经过全面测试并持续被社区审查的合约。在您自己的代码中，遵循 DRY 原则：不要重复自己。如果您看到任何代码片段重复出现多次，请问自己是否可以将其编写为函数或库并重复使用。在许多部署中经过实战测试的代码几乎总是比您刚刚编写的代码更安全，无论您对它有多么自信。警惕“非我发明”综合征，在这种情况下，您可能会试图通过从头开始构建某个特性或组件来“改进”它。安全风险通常大于改进的价值。重用不是懒惰。这是一种明智的防御性工程。

**代码质量**

智能合约代码是无情的。每个错误都可能导致金钱损失。您不应该像对待通用编程那样对待智能合约编程。用 Solidity 编写 DApp 与用 JavaScript 创建 Web 小部件不同。相反，您应该像在航空航天工程或任何类似无情的学科中那样，应用严格的工程和软件开发方法。一旦您“启动”了您的代码，您几乎无法修复任何问题。即使代码是可升级的，如果出现任何问题，您通常也没有多少时间做出响应。如果有人在您之前发现了您项目中的错误，漏洞利用可能会在单个交易或几个交易中展开，这意味着损害会在几秒钟内完成，远在您可以干预之前。

**可读性/可审计性**

您的代码应该清晰易懂。越容易阅读，就越容易审计。智能合约是公开的：每个人都可以读取字节码，任何有足够技能的人都可以对其进行逆向工程。因此，最好以公开的方式开发您的工作，使用协作和开源方法，以利用开发者社区的集体智慧，并从开源开发的最高公分母中受益。您应该编写有良好文档记录且易于阅读的代码，遵循以太坊社区的一部分的风格和命名约定。

**测试覆盖率**

测试所有你能测试的东西。智能合约在公共执行环境中运行，任何人都可以使用他们想要的任何输入来执行它们。您永远不应假设输入（例如函数参数）格式良好或边界正确，或者具有良性目的。测试所有参数，确保它们在预期范围内并且格式正确，然后再允许继续执行您的代码。

## 安全风险和反模式

作为一名智能合约程序员，您应该熟悉最常见的安全风险，以便检测和避免使您的合约暴露于这些风险的编程模式。在接下来的几个章节中，我们将研究不同的安全风险、漏洞如何产生的示例，以及可用于解决这些问题的对策或预防性解决方案。

以下反模式通常被组合起来以执行漏洞利用，就像在 Web2 安全中一样。现实世界中的漏洞利用通常比本章中的示例更复杂。

### 重入

以太坊智能合约的一个特性是它们能够调用和利用来自其他外部合约的代码。合约通常也处理以太币，因此经常将以太币发送到各种外部用户地址。这些操作需要合约提交外部调用。这些外部调用可能会被攻击者劫持，他们可以强制合约执行进一步的代码（通过回调：可以是回退函数或一些钩子，通常是 `transfer`），包括回调到它们自身。这种攻击在 2016 年臭名昭著且仍然令人记忆犹新的 DAO 黑客事件中被使用。即使过了这么多年，[我们仍然看到很多攻击利用这个漏洞](https://github.com/pcaversaccio/reentrancy-attacks)，尽管它很容易被发现并且修复成本不高。

#### 漏洞

当攻击者在另一个合约完成更新其状态之前设法控制该合约的执行时，就会发生这种类型的攻击。由于合约仍处于其过程的中间，它尚未更新其状态（例如，关键变量）。然后，攻击者可以在这个脆弱的时刻“重新进入”合约，利用不一致的状态来触发未预期或不期望的操作。这种重新进入允许攻击者绕过保护措施、操纵数据或耗尽资金，所有这些都是因为合约尚未完全稳定到安全、一致的状态。

如果没有实际的例子，重入可能很难掌握。请看示例 9-1 中这个简单的易受攻击的合约，它充当以太坊金库，允许存款人每周只提取 1 个以太币。

**示例 9-1. EtherStore：一个容易受到重入攻击的合约**

```solidity
1 contract EtherStore {
2      uint256 public withdrawalLimit = 1 ether;
3      mapping(address => uint256) public lastWithdrawTime;
4    mapping(address => uint256) balances;
5
6    function depositFunds() public payable{
7      balances[msg.sender] += msg.value;
8    }
9
10    function withdrawFunds() public {
11        require(block.timestamp >= lastWithdrawTime[msg.sender] + 1 weeks);
12        uint256 _amt = balances[msg.sender];
13        if(_amt > withdrawalLimit){
14            _amt = withdrawalLimit;
15        }
16      (bool res, ) = address(msg.sender).call{value: _amt}("");
17        require(res, "Transfer failed");
18      balances[msg.sender] = 0;
19        lastWithdrawTime[msg.sender] = block.timestamp;
20    }
21 }
```

此合约有两个公共函数 `depositFunds` 和 `withdrawFunds`。`depositFunds` 函数简单地增加发送者的余额。`withdrawFunds` 函数允许发送者提取他们的余额。只有在过去一周没有发生提款的情况下，此函数才能成功执行。

漏洞位于第 17 行，合约在此处将用户请求的以太币数量发送给他们。考虑一个攻击者创建了示例 9-2 中的合约。

**示例 9-2. Attack.sol：一个用于利用 EtherStore 合约中的重入漏洞的合约**

```solidity
1 contract Attack {
2  EtherStore public etherStore;
3
4  // 使用合约地址初始化 etherStore 变量
5  constructor(address _etherStoreAddress) {
6      etherStore = EtherStore(_etherStoreAddress);
7  }
8
9  function attackEtherStore() public payable {
10      // 攻击到最接近的以太币
11      require(msg.value >= 1 ether, "no bal");
12      // 将 eth 发送到 depositFunds() 函数
13      etherStore.depositFunds{value: 1 ether}();
14      // 开始魔法
15      etherStore.withdrawFunds();
16  }
17
18  function collectEther() public {
19      payable(msg.sender).transfer(address(this).balance);
20  }
21
22  // 接收函数 - fallback() 函数也可以工作
23  receive() external payable {
24      if (address(etherStore).balance >= 1 ether) {
25          // 对受害者合约的重入调用
26          etherStore.withdrawFunds();
27      }
28  }
29 }
```

漏洞是如何发生的？首先，攻击者会创建恶意合约（假设地址为 `0x0...123`），并将 `EtherStore` 的合约地址作为唯一的构造函数参数。这将初始化公共变量 `etherStore` 并将其指向要攻击的合约。

然后，攻击者将调用 `attackEtherStore` 函数，其以太币数量大于或等于 1——暂时假设为 1 个以太币。在此示例中，我们还将假设许多其他用户已将以太币存入此合约，因此其当前余额为 10 个以太币。然后将发生以下情况：

- *Attack.sol*，第 13 行：将使用 `msg.value` 为 `1 ether`（以及大量的 gas）调用 `EtherStore` 合约的 `depositFunds` 函数。发送者 (`msg.sender`) 将是恶意合约 (`0x0...123`)。因此，`balances[0x0..123] = 1 ether`。
- *Attack.sol*，第 15 行：恶意合约将调用 `EtherStore` 合约的 `withdrawFunds` 函数。这将通过要求（`EtherStore` 合约的第 11 行），因为之前没有进行过提款。
- *EtherStore.sol*，第 16 行：合约将 `1 ether` 发送回恶意合约。
- *Attack.sol*，第 23 行：对恶意合约的付款将执行 `receive` 函数。
- *Attack.sol*，第 24 行：`EtherStore` 合约的总余额为 10 个以太币，现在为 9 个以太币，因此此 `if` 语句通过。
- *Attack.sol*，第 26 行：回退函数再次调用 `EtherStore` 的 `withdrawFunds` 函数并*重新进入* `EtherStore` 合约。
- *EtherStore.sol*，第 10 行：在第二次调用 `withdrawFunds` 时，攻击合约的余额仍然是 1 个以太币，因为第 18 行尚未执行。因此，我们仍然有 `balances[0x0..123] = 1 ether`。`lastWithdrawTime` 变量也是如此。同样，我们通过了要求。
- *EtherStore.sol*，第 16 行：攻击合约提取了另一个 `1 ether`。
- 重新进入 EtherStore 合约，直到不再有 `EtherStore.balance >= 1` 的情况，如 *Attack.sol* 中的第 24 行所述。
- *Attack.sol*，第 24 行：一旦 `EtherStore` 合约中剩余的以太币少于 1 个，此 `if` 语句将失败。然后，这将允许执行 `EtherStore` 合约的第 17-19 行（对于每次调用 `withdrawFunds` 函数）。
- *EtherStore.sol*，第 18 行和 19 行：将设置 `balances` 和 `lastWithdrawTime` 映射，并且执行将结束。

最终结果是，攻击者在单个交易中从 `EtherStore` 合约中提取了所有以太币。

虽然回退函数拦截的本地以太币转移是重入攻击的常见媒介，但它们并不是唯一可以引入这种风险的机制。一些代币标准，如 ERC-721 和 ERC-777，包括也可以启用重入攻击的回调机制。例如，ERC-721 的 `safeTransfer` 函数确保代币转移到合约会调用接收方的 `onERC721Received` 函数。类似地，ERC-777 代币允许在转移期间通过 `tokensReceived` 函数调用钩子。

#### 超越经典重入模式

重入攻击不限于单个函数或合约。虽然经典重入涉及在同一函数完成之前重新进入该函数，但有些变体更难发现，例如跨函数重入、跨合约重入，以及最棘手的只读重入。
只读重入利用了依赖于其他合约的 view 函数的合约。这些函数不修改状态，但返回其他合约依赖的数据，通常没有重入保护。当重入调用允许攻击者暂时将目标合约置于不一致状态时，问题就出现了，允许他们使用另一个合约（受害者）通过 view 函数查询这种不稳定状态。
让我们看看它是如何运作的：
1. 攻击者的合约与易受攻击的合约（我们称之为合约 A）交互，该合约可以被重入。此合约保存其他协议依赖的数据。
2. 合约 A 触发对攻击者合约的回调，允许攻击者合约逻辑运行。
3. 在回退中，攻击者的合约调用不同的协议，合约 B，该合约连接到合约 A 并依赖于它提供的数据。
4. 合约 B 没有意识到任何问题，从合约 A 读取数据。但是，合约 A 的状态已过时，因为它尚未完成更新。
在这个周期结束时，攻击者已经利用了合约 B，利用了合约 A 的过时数据，然后让合约 A 中的回调和原始调用正常完成。该过程如图 9-1 所示。
图 9-1. 只读重入

![只读重入](https://img.learnblockchain.cn/masterethereumbook/images/ch9/maet_0901.png)

**图 1-1.** 只读重入

这里的关键是合约 B 信任来自合约 A 的数据，但合约 A 的状态尚未赶上，允许攻击者利用这种延迟。这种类型的攻击更难防御，因为开发者通常不会用重入锁保护 view 函数，认为它们是安全的，因为它们不修改状态。
只读重入告诉我们，即使只读函数，当它们被外部合约依赖时，也可能是危险的。

#### 预防技术

为了防止重入问题，首先要遵循的最佳实践是在编写智能合约时坚持 check-effect-interaction 模式。这种模式是关于确保在与外部合约交互之前发生对状态变量的所有更改。例如，在 *EtherStore.sol* 合约中，修改状态变量的行应该出现在任何外部调用之前。目标是确保与外部地址交互的任何代码都是函数中执行的最后一件事。这可以防止外部合约在重新进入时干扰内部状态，因为必要的更新已经完成。

另一个有用的技术是应用重入锁。*重入锁*是一个简单的状态变量，它在合约执行函数时“锁定”合约，防止其他外部调用中断。这可以使用如下所示的修饰符来实现：

```solidity
contract EtherStore {
    bool lock;
      uint256 public withdrawalLimit = 1 ether;
      mapping(address => uint256) public lastWithdrawTime;
    mapping(address => uint256) balances;

      modifier nonReentrant {
      require(!lock, "Can't reenter");
      lock = true;
      _;
      lock = false;
    }

    function withdrawFunds() public nonReentrant{
        [...]
    }
}
```

在此示例中，`nonReentrant` 修饰符使用锁变量来防止 `withdrawFunds` 函数在仍在运行时被重新进入。`nonReentrant` 修饰符在函数开始时锁定合约，并在函数完成后解锁合约。但是，我们不应该重新发明轮子。与其制作我们自己的重入锁，不如依赖像 OpenZeppelin 的 ReentrancyGuard 这样的经过充分测试的库。这些库提供安全、gas 优化的解决方案。

> **注意**
>
> 随着 Solidity 0.8.24 中以太坊上瞬态存储的出现，OpenZeppelin 引入了 ReentrancyGuardTransient，这是 ReentrancyGuard 的一种新变体，它利用瞬态存储来显着降低 gas 成本。由 [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153) 启用的瞬态存储提供了一种更便宜的方式来存储仅在单个交易期间需要的数据，使其成为重入守卫和类似临时逻辑的理想选择。但是，ReentrancyGuardTransient 只能在 EIP-1153 可用的链上使用，因此在实施之前，请确保您的目标链支持此功能。

另一种方法是使用 Solidity 的内置 `transfer` 和 `send` 函数来发送以太币。这些函数仅转发有限数量的 gas（2,300 个单位），这通常不足以让接收合约执行重入调用，因此它们是防止重入的一种简单方法。但是，它们存在明显的缺点。如果接收者是一个智能合约，其回退或接收函数中包含非恶意逻辑，则转移可能会失败，从而可能锁定资金。随着 EIP-7702 的引入，这种风险变得越来越重要，EIP-7702 允许 EOA 具有附加的代码，包括回退逻辑。随着越来越多的 EOA 采用此功能，由于 gas 不足，使用 `transfer` 或 `send` 的交易更有可能在交易的常规执行期间恢复。从安全的角度来看，这种方法不是面向未来的：如果未来的硬分叉降低了某些操作的 gas 成本，则 2,300 个单位可能足以重新进入，从而打破了以前安全的假设。因此，虽然 `transfer` 和 `send` 在狭窄的情况下仍然有用，但我们需要谨慎使用它们，并且不要将它们作为我们的主要防御手段。

只读重入和跨合约重入值得特别关注：这些利用可能很棘手，因为它们可能涉及两个单独的协议，使得协调预防成为一项挑战。当我们的项目依赖于外部协议获取数据时，我们需要深入研究组合逻辑的工作方式。即使每个项目本身都是安全的，漏洞也可能在集成过程中出现。

#### 现实世界的例子：The DAO 攻击

重入在 2016 年发生的 DAO 攻击中发挥了重要作用，并且是以太坊早期开发过程中的主要黑客攻击之一。当时，该合约持有超过 1.5 亿美元，占以太币流通供应量的 15%。为了恢复黑客攻击的影响，以太坊社区最终选择了一个硬分叉，分裂了以太坊区块链。结果，以太坊经典 (ETC) 作为原始链继续存在，而使用更新的规则来扭转黑客攻击的分叉版本成为我们今天所知的以太坊。

#### 现实世界的例子：Libertify

最近一个重入是唯一的攻击向量的漏洞利用是 2023 年 7 月发生的 Libertify 事件，这是一个被盗取了 40 万美元的 DeFi 协议。让我们检查一下被利用的函数的代码，看看它是如何发生的：

```solidity
function _deposit(
    uint256 assets,
    address receiver,
    bytes calldata data,
    uint256 nav
) private returns (uint256 shares) {
        /*
        validations
    */
    uint256 returnAmount = 0;
    uint256 swapAmount = 0;
    if (BASIS_POINT_MAX > invariant) {
        swapAmount = assetsToToken1(assets);
        returnAmount = userSwap( // 外部调用
            data,
            address(this),
            swapAmount,
            address(asset),
            address(other)
        );
    }
    uint256 supply = totalSupply(); // 状态更新
    if (0 < supply) {
        uint256 valueToken0 = getValueInNumeraire(
            asset,
            assets - swapAmount,
            MathUpgradeable.Rounding.Down
        );
        uint256 valueToken1 = getValueInNumeraire(
            other,
            returnAmount,
            MathUpgradeable.Rounding.Down
        );
        shares = supply.mulDiv(
            valueToken0 + valueToken1,
            nav,
            MathUpgradeable.Rounding.Down
        );
    } else {
        shares = INITIAL_SHARE;
    }
    uint256 feeAmount = shares.mulDiv(
        entryFee, BASIS_POINT_MAX, MathUpgradeable.Rounding.Down
    );
    _mint(receiver, shares - feeAmount);
    _mint(owner(), feeAmount);
}
```

这是一个重入问题的经典例子——现在你很少看到这么直接的例子了！这里的核心问题是缺乏重入保护。`userSwap()` 函数允许攻击者在原始调用更新 `totalSupply` 之前重新进入 `deposit()` 函数。这意味着攻击者可以比实际应得的铸造更多的份额，从而利用合约获利。

### DELEGATECALL

`CALL` 和 `DELEGATECALL` 操作码对于允许以太坊开发者模块化他们的代码非常有用。对合约的标准外部消息调用由 `CALL` 操作码处理，该操作码在*被调用*合约的上下文中执行代码。相比之下，`DELEGATECALL` 运行来自另一个合约的代码，但在*调用*合约的上下文中运行。这意味着存储、`msg.sender` 和 `msg.value` 都保持不变。一个有用的思考 `DELEGATECALL` 的方式是，调用合约暂时借用被调用合约的字节码，并像执行自己的字节码一样执行它。这实现了强大的模式，如代理合约和库，您可以部署一次可重用逻辑，并在多个合约中重用它。尽管这两个操作码之间的差异简单直观，但 `DELEGATECALL` 的使用可能会导致微妙和意想不到的行为，尤其是在存储布局方面。有关更多阅读，请参阅 Loi.Luu 在 [Ethereum Stack Exchange 上关于此主题的问题](https://ethereum.stackexchange.com/questions/3667/difference-between-call-callcode-and-delegatecall) 和 [Solidity 文档](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html#delegatecall-callcode-and-libraries)。

#### 漏洞

由于 `DELEGATECALL` 的上下文保存性质，构建无漏洞的自定义库并不像您想象的那么容易。库中的代码本身可以是安全且无漏洞的；但是，当它在其他应用程序的上下文中运行时，可能会出现新的漏洞。让我们看一个相当复杂的例子，使用斐波那契数列。考虑示例 9-3 中的库，它可以生成斐波那契数列和类似形式的数列。（注意：此代码已从 [*https://github.com/LFDT-web3j/web3j/blob/main/codegen/src/test/resources/solidity/fibonacci/Fibonacci.sol**https://github.com/LFDT-web3j/web3j/blob/main/codegen/src/test/resources/solidity/fibonacci/Fibonacci.sol*](https://github.com/LFDT-web3j/web3j/blob/main/codegen/src/test/resources/solidity/fibonacci/Fibonacci.sol) 修改。）

**示例 9-3. FibonacciLib：自定义库的错误实现**

```solidity
1 // 库合约 - 计算类似于斐波那契数列的数字
2 contract FibonacciLib {
3     // 初始化标准斐波那契数列
4     uint256 public start;
5     uint256 public calculatedFibNumber;
6
7     // 修改序列中的第零个数字
8     function setStart(uint256 _start) public {
9         start = _start;
10     }
11
12     function setFibonacci(uint256 n) public {
13         calculatedFibNumber = fibonacci(n);
14     }
15
16     function fibonacci(uint256 n) internal view returns (uint) {
17         if (n == 0) return start;
18         else if (n == 1) return start + 1;
19         else return fibonacci(n - 1) + fibonacci(n - 2);
20     }
21 }
```

此库提供了一个函数，可以生成序列中的第 *n* 个斐波那契数。它允许用户更改序列的起始编号 (`start`) 并计算此新序列中的第 *n* 个斐波那契数。

现在让我们考虑一个使用此库的合约：

```solidity
contract FibonacciBalance {
    address public fibonacciLibrary;
    // 要提取的当前斐波那契数
    uint256 public calculatedFibNumber;
    // 起始斐波那契数列数
    uint256 public start = 3;
    uint256 public withdrawalCounter;
    // 斐波那契函数选择器
    bytes4 constant fibSig = bytes4(keccak256("setFibonacci(uint256)"));
    // 构造函数 - 用以太币加载合约
    constructor(address _fibonacciLibrary) payable {
        fibonacciLibrary = _fibonacciLibrary;
    }
    function withdraw() public {
        withdrawalCounter += 1;
        // 计算当前提款user-的斐波那契数
        // 这将设置 calculatedFibNumber
        (bool success, ) = fibonacciLibrary.delegatecall(
            abi.encodeWithSelector(fibSig, withdrawalCounter)
        );
        require(success, "Delegatecall failed");
        payable(msg.sender).transfer(calculatedFibNumber * 1 ether);
    }
    // 允许用户调用斐波那契库函数
    fallback() external {
        (bool success, ) = fibonacciLibrary.delegatecall(msg.data);
        require(success, "Delegatecall failed");
    }
}
```

此合约允许参与者从合约中提取以太币，以太币数量等于与参与者的提取顺序相对应的斐波那契数，即，第一个参与者获得 1 个以太币，第二个参与者也获得 1 个以太币，第三个参与者获得 2 个以太币，第四个参与者获得 3 个以太币，第五个获得 5 个，依此类推（直到合约的余额小于提取的斐波那契数）。

此合约中有许多元素可能需要一些解释。首先，有一个看起来很有趣的变量：`fibSig`。这保存着字符串 `"setFibonacci(uint256)"` 的 Keccak-256 哈希的前 4 个字节。这被称为[*函数选择器**函数选择器*](https://docs.soliditylang.org/en/latest/abi-spec.html#function-selector)，并放入 calldata 中以指定将调用智能合约的哪个函数。它在第 21 行的 `delegatecall` 函数中使用，以指定我们希望运行 `fibonacci(uint256)` 函数。`delegatecall` 中的第二个参数是我们传递给函数的参数。其次，我们假设 FibonacciLib 库的地址在构造函数中被正确引用。

您能发现此合约中的任何错误吗？如果您要部署此合约，用以太币填充它并调用 `withdraw`，它可能会恢复。

您可能已经注意到，状态变量 `start` 在库和主调用合约中都使用。在库合约中，`start` 用于指定斐波那契数列的开头，并设置为 `0`，而在调用合约中，它设置为 `3`。您可能还注意到，`FibonacciBalance` 合约中的回退函数允许将所有调用传递到库合约，这允许调用库合约的 `setStart` 函数。回想一下，我们保留合约的状态，因此似乎此函数允许您更改本地 `FibonacciBalance` 合约中 `start` 变量的状态。如果是这样，这将允许您提取更多的以太币，因为生成的 `calculatedFibNumber` 依赖于 `start` 变量（如库合约中所见）。实际上，`setStart` 函数不会（也不能）修改 `FibonacciBalance` 合约中的 `start` 变量。此合约中的潜在漏洞远比仅修改 `start` 变量更严重。

在讨论实际问题之前，让我们快速绕道了解状态变量实际上是如何存储在合约中的。*状态*或*存储变量*（在单个交易中持续存在的变量）在合约中引入时按顺序放置到*插槽*中。（这里有一些复杂性；请参阅 [Solidity 文档](https://docs.soliditylang.org/en/latest/) 以获得更彻底的理解。）

例如，让我们看一下库合约。它有两个状态变量：`start` 和 `calculatedFibNumber`。第一个变量 `start` 存储在合约的存储中的 `slot[0]`（即，第一个插槽）。第二个变量 `calculatedFibNumber` 放置在下一个可用的存储插槽 `slot[1]` 中。函数 `setStart` 接受一个输入并将 `start` 设置为输入的内容。因此，此函数将 `slot[0]` 设置为我们在 `setStart` 函数中提供的任何输入。类似地，`setFibonacci` 函数将 `calculatedFibNumber` 设置为 `fibonacci(n)` 的结果。同样，这只是将存储 `slot[1]` 设置为 `fibonacci(n)` 的值。

现在，让我们看一下 `FibonacciBalance` 合约。存储 `slot[0]` 现在对应于 `fibonacciLibrary` 地址，而 `slot[1]` 对应于 `calculatedFibNumber`。正是在这种不正确的映射中发生了漏洞：`delegatecall` *保留合约上下文*。这意味着通过 `delegatecall` 执行的代码将作用于调用合约的状态（即，存储）。

现在请注意，在第 21 行的 `withdraw` 中，我们执行 `fibonacciLibrary.delegatecall(fibSig,withdrawalCounter)`。这将调用 `setFibonacci` 函数，如我们所讨论的，该函数修改存储 `slot[1]`，在当前上下文中是 `calculatedFibNumber`。这正如预期的那样（即，执行后，`calculatedFibNumber` 被修改）。但是，回想一下 `FibonacciLib` 合约中的 `start` 变量位于存储 `slot[0]` 中，在当前合约中是 `fibonacciLibrary` 地址。这意味着函数 `fibonacci` 将给出意想不到的结果。这是因为它引用了 `start` (`slot[0]`)，在当前的调用上下文中是 `fibonacciLibrary` 地址（当被解释为 `uint` 时，这通常会非常大）。因此，`withdraw` 函数很可能会恢复，因为它将不包含 `uint(fibonacciLibrary)` 个以太币，这将是 `calculatedFibNumber` 返回的值。

更糟糕的是，`FibonacciBalance` 合约允许用户通过第 27 行的回退函数调用所有 `fibonacciLibrary` 函数。正如我们前面所讨论的，这包括 `setStart` 函数。我们讨论了此函数允许任何人修改或设置存储 `slot[0]`。在这种情况下，存储 `slot[0]` 是 `fibonacciLibrary` 地址。因此，攻击者可以创建一个恶意合约，将地址转换为 `uint256`（这可以在 Python 中使用 `int('<address>',16)` 轻松完成），然后调用 `setStart(<attack_contract_address_as_uint>)`。这将更改 `fibonacciLibrary` 为攻击合约的地址。然后，每当用户调用 `withdraw` 或回退函数时，恶意合约将运行（可以窃取合约的全部余额），因为我们已经修改了 `fibonacciLibrary` 的实际地址。此类攻击合约的示例是：

```solidity
contract Attack {
    uint256 private storageSlot0; // corresponds to fibonacciLibrary
   请注意，`Wallet`合约实际上是通过委托调用将所有调用传递给`WalletLibrary`合约。此代码片段中的常量`_walletLibrary`地址充当实际部署的`WalletLibrary`合约的占位符（地址为`0x863DF6BFa4469f3ead0bE8f9F2AAE51c91A907b4`）。

这些合约的预期操作是拥有一个简单的、低成本的、可部署的`Wallet`合约，其代码库和主要功能都在`WalletLibrary`合约中。不幸的是，`WalletLibrary`合约本身也是一个合约，并维护自己的状态。你能看出这可能存在什么问题吗？

可以将调用发送到`WalletLibrary`合约本身。具体来说，`WalletLibrary`合约可以被初始化并被拥有。事实上，一个用户这样做了，调用了`WalletLibrary`合约上的`initWallet`函数，并成为该库合约的所有者。该用户随后调用了`kill`函数。因为该用户是该库合约的所有者，所以修饰器通过了，并且该库合约自毁了。由于所有现有的`Wallet`合约都引用这个库合约，并且没有方法来改变这个引用，所以它们的所有功能，包括提取以太币的能力，都随着`WalletLibrary`合约的消失而丧失。结果，所有此类Parity多重签名钱包中的所有以太币立即丢失或永久无法恢复。

> **注意**
>
> 利用者后来[出现在GitHub上](https://github.com/openethereum/parity-ethereum/issues/6995)，留下了令人难忘的评论：“我不小心杀死了它。” 他声称自己是以太坊的新手，一直在试验智能合约。

### 熵的错觉

以太坊区块链上的所有交易都是*确定性的状态转换*操作。这意味着每笔交易都以可计算的方式修改以太坊生态系统的全局状态，没有任何不确定性。这从根本上意味着以太坊中没有熵或随机性的来源。早期，找到一种去中心化的方法来创建随机性是一个很大的挑战。但多年来，我们已经开发出一些可靠的解决方案来解决这个问题。

#### 漏洞

当开发者在以太坊上构建智能合约时，他们经常需要一个随机性来源，无论是为了游戏、彩票还是其他需要不可预测性的功能。挑战在于，以太坊作为一个区块链，本质上是确定性的：每个节点必须达成相同的结果才能维持共识。因此，引入真正的随机性需要一些创造力。

许多开发者采用的一种方法是使用区块变量（例如区块哈希、时间戳或区块号）作为种子来生成随机数。这些值可能看起来是随机的，但实际上是由提议当前区块的验证者控制的。例如，想象一个DApp，其中游戏的结果基于下一个区块哈希是否以偶数结尾。验证者可以操纵这个过程：如果他们即将提议一个区块，并且哈希不符合他们想要的结果，他们可以，例如，更改交易顺序，以一种有利的方式更改区块哈希。

当从区块变量中获取随机性时，验证者操纵并不是唯一的风险。其他智能合约知道这些区块变量的值，使他们能够在结果有利时才与易受攻击的合约交互。

#### 预防技术

与过去相比，以太坊开发者现在拥有可靠的生成随机数的方法：`PREVRANDAO`和*可验证随机函数*（VRF）。

VRF是加密证明，确保生成的随机数是公平和公正的。VRF由多个提供商支持，例如Chainlink。VRF生成一个随机数以及一个验证其公平性的证明。任何人都可以验证此证明，确保随机性是安全的。VRF已成为在智能合约中安全获取随机性的标准去中心化解决方案。

另一个可靠的选择是`PREVRANDAO`操作码，随着向PoS的过渡而引入以太坊。此操作码用于获取`PREVRANDAO`值，该值源自Randao过程，Randao过程是PoS区块生产的组成部分。本质上，Randao是验证者通过每个人贡献一块数据来生成随机性的集体努力。`PREVRANDAO`是来自先前区块的此过程的结果，并且它是可靠的随机性来源。它是值得信赖的，因为操纵`PREVRANDAO`值需要损害大量验证者，使得这种利用在实践中不可行且在经济上不可行。开发者可以在他们的合约中使用此值，但他们应该记住，`PREVRANDAO`代表来自先前区块的值，该值已经是已知的。为了避免此值在提交时是可预测的，智能合约应该改为提交到未来区块的`PREVRANDAO`值。这样，当进行提交时，该值将是未知的。

> **警告**
>
> 如果攻击者控制了分配给一个epoch中最后几个slot的提议者，则Randao可能会被操纵。 要确定`PREVRANDAO`是否是智能合约中生成随机数的可靠选择，您应该仔细衡量操纵它的成本和收益。 虽然篡改Randao的成本可能很高，但如果您的合约涉及有价值的资产，则使用去中心化预言机解决方案会更安全。

由于`PREVRANDAO`和VRF等解决方案已被广泛记录和访问，如今很少见到开发者使用不安全的区块变量作为随机性来源。但是，当采取捷径或当开发者不了解这些工具时，仍然会发生错误。

#### 现实案例：Fomo3D

Fomo3D是一个以太坊彩票游戏，玩家购买“钥匙”来延长计时器，竞争成为计时器归零时的最后一位买家以赢得奖金池。它包括一个随机性很差的空投功能，如下面的代码所示：

```solidity
function airdrop()
        private
        view
        returns(bool)
    {
        uint256 seed = uint256(keccak256(abi.encodePacked(

            (block.timestamp).add
            (block.difficulty).add
            ((uint256(keccak256(abi.encodePacked
            (block.coinbase)))) / (block.timestamp)).add
            (block.gaslimit).add
            ((uint256(keccak256(abi.encodePacked
            (msg.sender)))) / (block.timestamp)).add
            (block.number)
        )));
        if((seed - ((seed / 1000) * 1000)) < airDropTracker_) {
            return(true);
        } else {
            return(false);
        }
    }
```

恶意合约会提前知道用于计算种子的值，从而只会在导致获胜时才触发`airdrop`函数。 毫不奇怪，该合约遭到了利用。

### 未检查的CALL返回值

在Solidity中有多种执行外部调用的方法。将以太币发送到外部帐户通常通过`transfer`方法执行。但是，也可以使用`send`函数，对于更通用的外部调用，可以直接在Solidity中使用`CALL`操作码。`call`和`send`函数返回一个布尔值，指示调用是成功还是失败。因此，这些函数有一个简单的警告，即如果外部调用（由`call`或`send`初始化）失败，则执行这些函数的交易不会回滚；相反，这些函数只会返回`false`。一个常见的错误是开发者期望如果外部调用失败会发生回滚，但不检查返回值。

#### 漏洞

考虑示例9-4中的合约。

**示例9-4。易受攻击的Lotto合约**

```solidity
1 contract Lotto {
2
3     bool public payedOut;
4     address public winner;
5     uint256 public winAmount;
6
7     // ... 这里有额外的功能
8
9     function sendToWinner() public {
10         require(!payedOut);
11         payable(winner).send(winAmount);
12         payedOut = true;
13     }
14
15     function withdrawLeftOver() public {
16         require(payedOut);
17         payable(msg.sender).send(address(this).balance);
18     }
19 }
```

这代表一个类似Lotto的合约，其中`winner`收到`winAmount`的以太币，这通常会留下一点剩余给任何人提取。漏洞存在于第11行，其中使用`send`而没有检查响应。在这个简单的例子中，一个`winner`的交易失败（要么因为耗尽gas，要么因为是一个故意在回退函数中抛出的合约）允许`payedOut`设置为`true`，而不管是否发送了以太币。在这种情况下，任何人都可以通过`withdrawLeftOver`函数提取`winner`的奖金。

#### 预防技术

第一道防线始终是检查`send`函数和底层调用的返回值，没有例外。如今，任何静态分析工具都会标记此问题，使其难以忽略。

在发送以太币时，我们需要仔细考虑使用哪种方法。如果我们希望交易在失败时自动回滚，那么`transfer`似乎很有吸引力，因为它默认会处理失败。但是，由于`send`和`transfer`仅转发 2,300 个 gas 单位，当收件人（无论是合约还是现在的 EIP-7702，甚至是 EOA）有任何回退逻辑时，它们很容易失败。鉴于这种不断变化的情况，更安全、更灵活的方法是改为使用`call`，显式检查其返回值，并相应地管理错误。这使我们能够完全控制 gas 转发，并使我们的合约与更广泛的收件人兼容。

#### 现实案例：Etherpot和King of the Ether

[Etherpot](https://web.archive.org/web/20180723043801/https:/github.com/etherpot/contract/blob/master/app/contracts/lotto.sol)是一个智能合约彩票，与示例9-4中的合约非常相似。 此合约的失败主要是由于不正确地使用block hash（只有最后256个block hash可用；请参阅“预定义的全局变量和函数”）。 但是，此合约也遭受了未检查的`call`值的影响。

考虑示例9-5中的函数`cash`：同样，以下代码段已更新以反映最新Solidity版本的语法。

**示例9-5。Lotto.sol：代码段**

```solidity
1 function cash(uint256 roundIndex, uint256 subpotIndex) public {
2    uint256 subpotsCount = getSubpotsCount(roundIndex);
3    if(subpotIndex>=subpotsCount)
4        return;
5    uint256 decisionBlockNumber = getDecisionBlockNumber(roundIndex,subpotIndex);
6    if(decisionBlockNumber>block.number)
7        return;
8    if(rounds[roundIndex].isCashed[subpotIndex])
9        return;
10    //子奖池只能兑现一次。这是为了防止双重支付
11    address winner = calculateWinner(roundIndex,subpotIndex);
12    uint256 subpot = getSubpot(roundIndex);
13    payable(winner).send(subpot);
14    rounds[roundIndex].isCashed[subpotIndex] = true;
15    //将回合标记为已兑现
16 }
```

请注意，在第13行，未检查`send`函数的返回值，并且下一行然后设置一个布尔值，指示已将资金发送给获胜者。此错误可能允许一种状态，即获胜者没有收到他们的以太币，但合约的状态可以指示已经支付了获胜者。

在[King of the Ether](https://www.kingoftheether.com/thrones/kingoftheether/index.html)合约中发生了此错误的更严重版本。已经编写了针对此合约的出色的[事后分析](https://www.kingoftheether.com/postmortem.html)，详细说明了如何使用未经检查的失败的`send`来攻击合约。

#### ERC-20 案例

在 Solidity 中处理 ERC-20 代币时，仅检查代币转移的返回值不足以确保安全交互。 这是因为并非所有 ERC-20 代币都严格遵循 ERC-20 标准，尤其是较旧的代币。 有些代币在完成转移后会返回一个布尔值，而不是在操作失败时直接回滚或抛出异常。 其他代币可能根本不返回任何值，导致在使用标准方法与它们交互时出现模糊行为。 Tether (USDT) 是一个没有完全符合 ERC-20 标准的广泛使用的代币的突出例子。

为了缓解这个问题，我们使用像 OpenZeppelin 的 SafeERC20 这样的库。 这个库以一种优雅地处理这些变化的方式包装了标准的 ERC-20 操作（如 `transfer`、`transferFrom` 和 `approve`）。 如果一个代币返回 `false`，该库确保交易被回滚，如果一个代币不返回值，该库假定如果没有发生回滚，操作就成功了。

### 竞争条件和抢跑交易

为了真正理解此漏洞，让我们简要回顾一下交易在以太坊中如何运作。 当我们发送交易时，它会被广播到节点网络并放置在 mempool 中，这是一种待处理交易的等待室。 然后，验证者从 mempool 中提取这些交易以构建块。 块内的交易按特定顺序依次执行，并且由于每个交易都更改了区块链的全局状态，因此交易的结果可能会因其在块中的位置而异。 此交易排序很重要，因为它会显着影响交易执行的结果。

> **注意**
>
> 实际上，控制交易在区块中的位置主要归结为支付。 最初，您可以通过提供更高的 gas 价格来简单地影响订单管理。 今天，由于实施构建者-提议者分离的 Flashbots 基础设施（这尚未成为以太坊原生的一部分），用户可以按特定顺序提交交易捆绑，并通过链下中继系统竞标将其包含在内。 这些过程——无论是传统的基于 mempool 的系统还是新的基于构建者的系统——都在第 6 章中进行了更详细的介绍。

#### 漏洞

*抢跑交易*是一种通过将其他交易插入块中，以使抢跑者受益的方式来利用此顺序执行的做法。 本质上，有人会监视可能影响市场或特定合约的待处理交易，然后提交自己的交易以在原始交易之前进行处理。 通过这样做，他们可以利用来自待处理交易的信息来获利，这通常会对原始发送者不利。 重要的是，我们的代码要考虑到这种动态，并设计为能够抵御块内交易顺序的变化。

让我们看一个简单的例子，说明这如何运作。 考虑示例 9-6 中所示的合约。

**示例 9-6。FindThisHash：容易受到抢跑交易攻击的合约**

```solidity
contract FindThisHash {
    bytes32 constant public hash =
      0xb5b5b97fafd9855eec9b41f74dfb6c38f5951141f9a3ecd7f44d​5479b630ee0a;
    constructor() payable {} // 加载以太币
    function solve(string memory solution) public {
        // 如果您可以找到哈希的预映像，则可以收到 1000 个以太币
        require(hash == keccak256(abi.encodePacked(solution)));
        payable(msg.sender).transfer(1000 ether);
    }
}
```

假设此合约有 1,000 个以太币。 可以找到 SHA-3 哈希 `0xb5b5b97fafd9855eec9b41f74dfb6c38f5951141f9a3ecd7f44d​5479b630ee0a` 的预映像的用户可以提交解决方案并检索 1,000 个以太币。 假设一个用户发现解决方案是 `Ethereum!`。 他们使用 `Ethereum!` 作为参数调用 `solve`。 不幸的是，攻击者在 mempool 中发现了该交易，检查了其有效性，然后提交了具有更高块优先级的等效交易。 原始交易将回滚，因为攻击者的交易将首先被处理。

#### 预防技术

抢跑漏洞会以各种形式出现，具体取决于智能合约或协议的特定逻辑。 只要可以通过交易排序来利用操作，我们就会遇到抢跑漏洞。 因此，解决方案通常是针对特定问题量身定制的。 例如，自动做市商 (AMM) 协议通过允许用户设置他们在交换期间必须收到的最少代币数量来解决此问题。 虽然这不能完全防止抢跑，但它会严重限制攻击者可以提取的潜在利润，从而减少损害并保护用户免受极端滑点的影响。

另一种通用技术是使用提交-披露方案。 在此方法中，用户首先提交一个包含隐藏信息的交易，通常表示为哈希（提交阶段）。 一旦此交易被包含在块中，用户将继续进行第二次交易，以披露实际数据（披露阶段）。 此方法可有效防止抢跑，因为攻击者无法看到初始交易的详细信息，直到采取行动为时已晚。 但是，权衡是它需要两个单独的交易，这意味着更高的成本和增加的延迟。 除了较差的用户体验外，交易之间所需的延迟可能是在时间敏感型应用中的实际限制。

#### 现实案例：AMM 和 minAmountOut

让我们探讨一个常见的现实世界中的抢跑漏洞。 当集成 AMM 协议的智能合约执行未设置要接收的最少代币数量的交换时，就会发生这种情况，从而使所述交换容易受到抢跑攻击。 如果未正确设置要接收的最少代币数量（或将其设置得太低），则交换交易将容易受到三明治攻击的影响，三明治攻击是一种特定类型的抢跑。

以下是三明治攻击的展开方式：抢跑者监视 mempool 中的待处理交易，并发现我们的交换交易没有强制执行最少数量的输出。 攻击者在我们的交换之前提交购买交易，以人为地抬高代币价格。 然后，我们的交易以这个虚高的价格继续进行，导致我们收到的代币比我们预期的要少。 最重要的是，我们的交易进一步抬高了价格。 紧随其后，攻击者以更高的价格出售他们的代币，从而使价格回落并从我们的交易产生的价格差异中获利。 此策略会将我们的交易“夹在”他们的两个交易之间，因此得名 *三明治攻击*。 为了解决此问题，集成 AMM 的智能合约需要从受信任的来源（如预言机，甚至是基于时间的加权平均价格）获取实际资产价格，然后在执行交换时计算并强制执行精确的最低输出量。

### 拒绝服务

此类别非常广泛，但从根本上讲，它包含攻击者可以在一段时间内或在某些情况下永久地使合约或其一部分无法运行的攻击。 这会永远将资金困在这些合约中，如“实际案例：Parity 多重签名钱包（第二次黑客攻击）”中所述。

#### 漏洞

合约可能以多种方式变得无法运行。 在这里，我们仅重点介绍一些不太明显的 Solidity 编码模式，这些模式可能会导致 DoS 漏洞。

#### 循环遍历外部操纵的映射或数组

当所有者希望使用类似 `distribute` 的函数将代币分配给投资者时，通常会出现这种模式，如示例 9-7 中的合约所示。

**示例 9-7。DistributeTokens 合约**

```solidity
1 contract DistributeTokens {
2     address public owner; // 在某处设置
3     address[] investors; // 投资者数组
4     uint[] investorTokens; // 每个投资者获得的代币数量
5
6     // ... 额外的功能，包括 transfertoken()
7
8     function invest() public payable {
9         investors.push(msg.sender);
10         investorTokens.push(msg.value * 5); // 发送的 wei 的 5 倍
11         }
12
13     function distribute() public {
14         require(msg.sender == owner); // 只有所有者
15         for(uint256 i = 0; i < investors.length; i++) {
16             // 在这里 transferToken(to,amount) 转移
17             // “amount” 的代币到地址 “to”
18             transferToken(investors[i],investorTokens[i]);
19         }
20     }
21 }
```

请注意，此合约中的循环遍历一个可以被人为膨胀的数组。 攻击者可以创建许多用户帐户，从而使 `investors` 数组非常大。 风险不仅在于循环本身，还在于其中操作的累积 gas 成本，例如 `transferToken` 或任何其他逻辑。 每个额外的迭代都会增加使用的总 gas，如果数组变得足够大，则完成循环所需的 gas 可能超过块 gas 限制。 此时，`distribute` 函数实际上变得无法使用。

> **注意**
>
> 这种 DoS 不限于更改状态的函数。 如果只读视图函数循环遍历大型数组，即使它们也可以变得无法访问。 虽然调用它们不会消耗链上的 gas，但 RPC 端点对 `eth_call` 执行强制执行它们自己的任意 gas 上限。 因此，如果视图函数运行足够的逻辑以超过这些限制，则 RPC 调用将失败。

#### 基于外部调用推进状态

有时会编写合约，以便推进到新状态需要向地址发送以太币或等待来自外部来源的一些输入。 当外部调用失败或由于外部原因而阻止时，这些模式可能会导致 DoS。 在发送以太币的示例中，用户可以创建一个不接受以太币的合约。 如果合约需要发送以太币才能推进到新状态，则合约将永远无法达到新状态，因为永远无法将以太币发送到不接受以太币的用户合约。

#### 意外问题

DoS 问题可能会以意想不到的方式出现，并且它们并不总是涉及恶意攻击。 有时，合约的功能可能会因无法预见的事件而中断。 例如，如果智能合约依赖所有者的私钥来调用特定的特权函数，并且该密钥丢失或泄露，我们将遇到麻烦。 如果没有该密钥，这些关键函数将永久无法访问，这可能会阻止整个合约的运行。 想象一个初始代币发行 (ICO) 合约，其中所有者必须调用一个函数才能完成销售。 如果密钥丢失，则没有人可以调用它，并且代币将永远锁定。

另一个意外中断的例子来自发送到合约的以太币，而合约对此不知情或无意。 可以使用称为 `selfdestruct`（现在已弃用）的方法，甚至通过在将合约部署到其预定地址之前发送以太币来将以太币“强制”到合约中。 如果合约假设它通过自己的函数控制它收到的所有以太币的会计，则它可能不知道如何处理这些不请自来的资金，从而导致意外行为。 这就像在您的银行帐户中收到您不期望的钱一样——有时这很好，但这也可能意味着您的帐户余额不正确，并且任何依赖于该精确数量的系统都可能开始出现问题。

#### 预防技术

由于 DoS 问题以不同的形式出现，因此解决方案通常也是特定于情况的。

存在达到 gas 限制风险的长列表是一个相当常见的情况，因此我们可以为处理这种情况提供一些建议。 在第一个示例中，合约不应循环遍历可以由外部用户人为操纵的数据结构。 建议采用提款模式，即每个投资者都调用 `withdraw` 函数以独立声明代币（pull-over-push 模式）。 对于迭代长列表的函数，一个好的解决方案是实现分页功能。

DoS 的通用解决方案是尽可能多地研究可能出现的问题并实施安全措施。

#### 实际案例：ZKsync Era Gemholic 资金锁定

正如我们刚才所说，最意想不到的错误可能导致智能合约中的 DoS 问题。 最近的一个例子涉及 Gemholic，这是一个在以太坊 L2 解决方案 ZKsync Era 上部署智能合约的项目。 当 Gemholic 无法访问代币销售中筹集的 921 ETH（约 170 万美元）时，它面临一个主要问题。 根本原因？ 智能合约依赖于 `transfer()` 函数，ZKsync Era 不支持该函数。 尽管 ZKsync Era 与 EVM 的大部分功能兼容，但它并非完全等同于 EVM，这意味着某些功能（如 `transfer()`）的运行方式与以太坊主网上不同。 这种不兼容导致 Gemholic 的资金被卡住，因为智能合约无法按预期提取以太币。 幸运的是，ZKsync 的团队能够介入并开发他们所谓的“优雅解决方案”来解锁资金，从而使 Gemholic 能够再次访问它们。 不幸的是，这个“优雅解决方案”的具体细节仍然未公开。

### 浮点数和精度

截至撰写本文时，Solidity的 v0.8.29 尚未完全支持定点数和浮点数。 这种设计选择源于区块链对确定性的根本需求：网络中的每个节点必须从相同的输入获得相同的结果，以维持共识。 不幸的是，浮点运算在不同的硬件架构中本质上是不确定的，可能会从相同的计算中产生略有不同的结果。

由于区块链应用程序需要绝对确定性以防止网络分叉并保持安全性，Solidity 强制开发者使用整数类型实现浮点表示。 虽然如果不正确地实现，这种方法会更加繁琐且容易出错，但它可以确保财务计算和智能合约逻辑在网络中的所有节点上产生相同的结果。

#### 漏洞

Solidity 尚未完全支持定点数。 它们可以被声明，但不能被赋值或从中赋值，这意味着开发者需要使用标准整数数据类型来实现自己的定点数。 在此过程中，开发者可能会遇到许多陷阱。 我们将尝试在本节中重点介绍其中的一些内容。 让我们从一个代码示例开始（示例 9-8）。

**示例 9-8。FunWithNumbers**

```solidity
1 contract FunWithNumbers {
2    uint256 constant public tokensPerEth = 10;
3    uint256 constant public weiPerEth = 1e18;
4    mapping(address => uint) public balances;
5
6    function buyTokens() public payable {
7        // 将 wei 转换为 eth，然后乘以代币费率
8        uint256 tokens = msg.value/weiPerEth*tokensPerEth;
9        balances[msg.sender] += tokens;
10    }
11
12    function sellTokens(uint256 tokens) public {
13        require(balances[msg.sender] >= tokens);
14        uint256 eth = tokens/tokensPerEth;
15        balances[msg.sender] -= tokens;
16        payable(msg.sender).transfer(eth*weiPerEth);
17    }
18 }
```

这个简单的代币买卖合约存在一些明显的问题。 尽管买卖代币的数学计算是正确的，但缺乏浮点数会给出错误的结果。 例如，在第 8 行购买代币时，如果该值小于 1 个以太币，则初始除法将导致 0，从而使最终乘法的结果为 `0`（例如，200 wei 除以 `1e18` `weiPerEth` 等于 0）。 同样，在出售代币时，任何小于 10 的代币数量也将导致 0 个以太币。 事实上，这里的舍入总是向下舍入，因此出售 29 个代币将导致 2 个以太币（29 个代币 / 10 `tokensPerEth` = 2.9，向下舍入得到 2）。

此合约的问题在于精度仅为最接近的以太币（即 1e18 wei）。 当您需要在 [ERC-20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md) 代币中使用小数时，这可能会变得棘手，因为您需要更高的精度。 在实际情况下，精度损失可能看起来很小，但它们很容易被放大和利用。 例如，闪电贷允许攻击者以零前期成本借入大量资金，从而可以利用即使是微小的差异。

#### 预防技术

在智能合约中保持正确的精度非常重要，尤其是在处理反映经济决策的比率和费率时。 您应确保您使用的任何比率或费率都允许分母中的大分子。 例如，我们在示例中使用了费率 `tokensPerEth`。 最好使用 `weiPerTokens`，这将是一个很大的数字。 为了计算相应的代币数量，我们可以执行 `msg.sender/weiPerTokens`。 这将给出更精确的结果。

另一种策略是注意运算顺序。 在我们的示例中，购买代币的计算是 `msg.value/weiPerEth*tokenPerEth`。 请注意，除法发生在乘法之前。 与某些语言不同，Solidity 保证按照书写顺序执行运算。 如果通过先执行乘法，然后执行除法来执行计算，则此示例将获得更高的精度：`msg.value*tokenPerEth/weiPerEth`。

最后，当为数字定义任意精度时，最好将值转换为更高的精度，执行所有数学运算，然后转换回输出所需的精度。 通常，使用 `uint256`，因为它们是 gas 使用的最佳选择； 这些在它们的范围内给了我们大约 60 个数量级，其中一些可以专用于数学运算的精度。 最好将 Solidity 中的所有变量保持高精度，并在外部应用程序中转换回较低的精度。 这基本上就是 ERC-20 代币合约中 `decimals` 变量的工作方式：当我们在 MetaMask 上发送 1,000 个 USDT 时，我们实际上发送的是 1,000,000,000 个 USDT 单位，这是 1,000 乘以 USDT 的小数位数 (1e6)。

要查看如何使用更高的精度处理数学运算的示例，让我们引入 Wad 和 Ray 数学。 *Wad* 表示一个精度为 18 位的十进制数，与以太币等 ERC-20 代币的 18 个小数位完美对齐。 这使其非常适合表示代币余额，确保我们在计算期间具有足够的准确性。 另一方面，*Ray* 的精度甚至更高，为 27 位，可用于计算非常接近于零的比率。 第一个 Solidity 定点数学库（称为 DS-Math）提供了一种处理这些高精度数字的结构。

MakerDAO 的开发者最初专门为他们的项目需求创建了 Wad 和 Ray。 鉴于以太币的 18 位小数标准——也由于大多数 ERC-20 代币也遵循这种约定（尽管存在很多例外）——Wad 非常适合主要的金融单位，而 Ray 则保留用于需要精确小数调整的情况。 虽然 DS-Math 开创了这种方法，但现在有更多的库可用于精确的 Solidity 数学运算。 Aave 的 WadRayMath、Solmate 的 FixedPointMathLib 和 OpenZeppelin 的 Math 库只是当今可用的几个选项。

#### 实际案例：ERC-4626 通货膨胀攻击

我们现在将看到一个在野外常见的精度损失漏洞，使用 OpenZeppelin 的 ERC-4626 实现的简化版本。 ERC-4626 是一个代币化的金库标准，允许用户将资产（如 USDT）存入金库并接收代表他们金库资产份额的份额。 示例 9-9 是我们正在使用的合约的简化版本。

**示例 9-9。原始 ERC4626 OpenZeppelin 实现的简化版本**

```solidity
1 abstract contract ERC4626 is ERC20, IERC4626 {
2    using Math for uint256;
3    IERC20 private immutable _asset;
4
5    constructor(IERC20 asset_) {
6        _asset = asset_;
7    }
8
9    function totalAssets() public view returns (uint256) {
10        return _asset.balanceOf(address(this));
11    }
12    function deposit(address receiver, uint256 assets) public {
13        SafeERC20.safeTransferFrom(_asset, msg.sender, address(this), assets);
14        uint256 shares = _convertToShares(assets, Math.Rounding.Down);
15        _mint(receiver, shares);
16        emit Deposit(msg.sender, receiver, assets, shares);
17    }
18    function _withdraw(address receiver, uint256 assets) public {
19        uint256 shares = _convertToShares(assets, Math.Rounding.Up);
20        _burn(msg.sender, shares);
21        SafeERC20.safeTransfer(_asset, receiver, assets);
22 #### 漏洞

想象一下这个简单的场景：攻击者发现一个借贷协议，该协议依赖于不安全的预言机来定价。通过操纵资产的价格，使其看起来低于实际价格，攻击者可以借入超过他们应有的该资产。然后他们以真实的市場價格出售借入的资产，从而获利。这种漏洞的根源在于依赖于链上价格指标来确定资产价格，而这些指标是可以被操纵的。这种操纵通常通过 *闪电贷* 来放大：即时且无需抵押的贷款，必须在同一交易区块内偿还。

#### 预防措施

当我们需要确定价格时，最好的选择是使用像 Chainlink、RedStone、Pyth 等去中心化预言机。由于这些预言机是去中心化的，因此它们更难被攻击，因为攻击者需要控制网络中超过 50% 的节点。但它们也有局限性。例如，它们可能不适用于所有资产。在这种情况下，我们可以转向时间加权平均价格（TWAP）预言机。

TWAP 预言机从链上数据推导出资产价格，并增加了一些安全性。它们通过计算资产在定义的时间范围内的平均价格来运作，例如过去五分钟。通过从计算中排除当前区块，TWAP 预言机有效地防止了闪电贷攻击。然而，TWAP 预言机并非完全免疫于资金充足的攻击者的操纵。这里的关键是调整周期长度：周期越长，攻击者操纵价格所需的资金就越多。但较长的周期也意味着 TWAP 价格可能与实际市场价格有更大的偏差。因此，根据项目的具体需求和风险状况微调 TWAP 非常重要。

无论我们使用哪种预言机，我们都不应该盲目信任它提供的数据。定期将预言机数据与其他来源进行验证是一个好习惯。例如，我们可以编写一个脚本，将预言机价格与其他来源的价格进行比较，并标记任何重大差异。如果发现此类差异，可以暂停协议以防止进一步的问题。

#### 原型示例：依赖于 AMM 链上数据

通常，易受攻击的预言机模块是协议本身的一部分，正如我们将在本例中看到的那样。当智能合约直接从 Uniswap 等链上 AMM 协议获取资产价格时，就会发生常见的漏洞利用场景。想象一个 Uniswap V2 池，其中有 4,000 USDC 和 1 ETH 的储备。智能合约可能会假设 1 ETH 价值 4,000 USDC。但是，如果推断出的价格用于进一步的状态改变操作，这种假设可能非常危险。在这种情况下，攻击者可以进行闪电贷执行大规模的兑换，改变池的余额，从而改变 ETH 的推断价格。易受攻击的协议依赖于这种被操纵的价格，然后会被攻击者利用。

幸运的是，这种特定的攻击向量是众所周知的。虽然它不像以前那样频繁地被利用，但它仍然出现在备受瞩目的事件中。例如，在 2025 年 5 月，Mobius Token 被攻击，损失了 210 万美元。尽管直接触发因素是 `mint` 函数中错误的乘以 1018，但该合约还包含一个单独的但同样关键的漏洞：它依赖于链上指标来计算 BNB/USDT 价格，使其容易受到操纵。即使没有数学错误，该合约仍然会在短时间内被利用。你可能想知道这样的代码是如何进入生产环境的，最终保障了如此多的总锁定价值 (TVL)。该团队选择不发布合约的源代码，假设保持隐藏可以提供安全保障——这再次提醒我们，通过模糊性来确保安全性是行不通的，尤其是在风险如此之高的情况下。

> **注意**
>
> 只有当从链上数据推断出的价格应用于状态改变操作时，使用这些价格才是危险的。如果这些价格仅用于信息目的，例如前端用于获取数据的 view 函数中，那么攻击是不可行的。但是，如果外部合约从这样的 view 函数中检索价格，然后将其用于状态改变操作，那么它就容易受到操纵。

#### 真实案例：Mango Markets

在 Mango Markets 被攻击事件中，一名交易员利用该平台价格操纵漏洞提取了超过 1.16 亿美元。攻击者通过在两个钱包中使用 1000 万美元，以每股 3.8 美分的价格开设了 4.83 亿 Mango 永续期货 (MNGO-PERPs)。然后，他们在三个不同的交易所购买了价值 400 万美元的 MNGO，使预言机报告的价格上涨了 2,300%。攻击者利用这种被抬高的 perp 头寸作为抵押品，从 Mango Markets 借了 1.16 亿美元，留下了大量的坏账，然后带着资金逃之夭夭。正如价格操纵攻击中常见的情况一样，这并非黑客行为，而是对系统机制的操纵，在不破坏任何底层代码的情况下利用了 Mango 的流动性。

#### 与攻击者谈判
攻击者和协议经常在链上直接谈判，以决定攻击者应该归还多少被盗资金，以换取协议同意撤销任何指控。虽然这些交易很常见，但它们在法庭上可能几乎没有法律效力。通常，协议会向攻击者提供约 10% 的赏金，这意味着如果攻击者归还 90% 的被盗资金，协议将同意停止追究他们。尽管这些类型的谈判很常见，但本案中发生的事情尤其引人注目。
攻击发生后，攻击者向 Mango Markets 的 DAO 提出了一个交易：如果社区同意承担之前为拯救另一个 Solana 项目 Solend 而承担的一些坏账，他们将归还大部分被盗资金。作为回应，Mango 团队提出了第二个提案，该提案将使攻击者归还高达 6700 万美元，同时保留 4700 万美元作为一种漏洞赏金。该协议包括放弃与坏账相关的任何索赔，并承诺在代币归还后不追究刑事指控或冻结攻击者的资金。第一个提案被否决，而第二个提案获得通过。这导致 Mango Markets 在 10 月 15 日发推文称，6700 万美元的资产确实已归还。
当其中一名攻击者在 Twitter 上透露自己的身份时，事情出现了法律转折，他称这种攻击是一种“利润丰厚的交易策略”，并声称这一切都是在协议的预期设计范围内完成的。但美国当局对此有不同的看法，并以市场操纵罪逮捕了他。Mango Markets 随后提起了民事诉讼，认为该协议是在胁迫下达成的，因此应无效，并寻求 4700 万美元的赔偿。由于 DAO 在法律上是一个相对较新的概念，因此该案件引起了很多关注，并且可能为去中心化组织如何处理法律纠纷树立先例。
2025 年 5 月，攻击者实际上赢得了他的欺诈案件，这完美地捕捉了加密货币领域疯狂的法律格局：法官裁定，你不能通过没有服务条款的无需许可的协议进行欺诈。但这里有一个关键：当当局在最初的 Mango Markets 调查期间搜查他的设备时，他们发现了 1,200 多张儿童性虐待材料的图片和视频，他现在因此服刑四年多，这证明即使是才华横溢的 DeFi 攻击也无法将你从违反基本人类尊严的行为中拯救出来。

### 不正确的输入验证

一个经常被忽视的主要漏洞是不正确的输入验证。当来自用户或外部来源的输入未得到正确验证时，对智能合约的后果可能会有很大差异，从轻微问题到重大资金损失。正确的输入验证有助于防范可能操纵合约行为的恶意行为者以及用户或管理员犯下的真正错误，否则可能导致资金损失。如果我们不采取正确的预防措施，看似无辜的疏忽可能会导致合约执行中的重大问题。

#### 漏洞

在其核心，不正确的输入验证发生在智能合约在处理数据或参数之前没有彻底检查它们的情况。如果我们不确保某些值满足特定条件，我们就会为真正的用户错误和潜在攻击打开大门。用户可能会意外输入不正确的数据，而攻击者可能会故意向我们的合约提供意外数据。这可能会绕过预期的逻辑并导致意外的状态更改，从而导致我们的合约以不可预测的方式运行。

当 setter 函数在将地址设置为资金接收者之前未验证该地址是否为零地址时，就会发生此漏洞的一个简单实例。如果我们错误地将零地址设置为接收者，则发送到零地址的资金将被永久锁定，使其无法追回。

智能合约开发中一个常见且危险的误解是认为保持源代码私有化将在某种程度上保护它免受漏洞利用。我们之前在本章中讨论过为什么通过模糊性来确保安全性是行不通的，并且此原则也适用于输入验证。开发人员有时会保留不受保护的函数，假设如果代码未发布，它们就不会被发现。但是，攻击者可以并且确实会对合约字节码进行逆向工程，以识别敏感且不受保护的函数。例如，几个封闭源代码的 MEV 机器人已通过不受保护的闪电贷回调被利用，导致数百万美元的损失。隐藏代码并不能隐藏风险。

#### 预防措施

那么，我们如何防范不正确的输入验证呢？第一步很简单：永远不要假设我们收到的输入是有效的。无论输入来自 EOA、另一个合约，甚至有时来自同一合约，都应严格检查。我们不仅需要验证输入长度，还需要验证极端情况和边界条件，例如最小值和最大值。我们不应忽视的一个经典极端情况是零值。

可重用的验证逻辑是编写安全且可维护的智能合约的关键部分。我们可以使用修饰符或内部函数来实现这些验证块，具体取决于最适合的方法。修饰符对于以一致且声明性的方式将先决条件或后置条件附加到多个函数特别有用。例如，我们可以使用修饰符来确保函数的输入不是零地址，或者在执行敏感操作之前检查调用者是否具有正确的权限。内部函数可以实现相同的目标，有时提供更大的灵活性，尤其是在验证取决于复杂逻辑或需要返回值时。

#### 访问控制
说到权限，实施强大的访问控制非常重要：`msg.sender` 是一个参数，应将其视为如此。虽然自定义逻辑是一种选择，但使用像 OpenZeppelin 这样的受信任的库可以帮助我们安全地管理访问，同时最大限度地降低复杂性。
对于需要一个实体完全控制的简单项目，开发人员可以使用 OpenZeppelin 的 Ownable 合约，该合约指定一个具有密钥函数权限的“所有者”。为了增加安全性，我们建议使用 Ownable2Step。此版本包括一个两步所有权转移过程，有助于防止意外丢失所有权。
对于更复杂的需求，OpenZeppelin 的 AccessControl 允许我们创建多个角色，每个角色具有不同的权限。基于角色的访问控制允许我们将特定任务分配给不同的用户，使其成为更大项目的理想选择。
在实施正确的访问控制之前，我们需要验证我们对谁可能调用外部函数和公共函数的所有假设。智能合约在公共和无需信任的环境中运行，因此我们不能假设只有我们预期的实体才会与合约交互。事实上，我们应该始终假设攻击者会尝试调用这些函数来触发意外行为。

#### 原型示例：任意调用

最常见的漏洞包括任意调用。在这里，一个易受攻击的智能合约允许攻击者提供要调用的地址。在这种情况下，合约将有效地执行攻击者想要的任何调用。一种可能的利用方式是通过返回被操纵的值来欺骗合约转移不应该转移的代币。

检查此易受攻击的收益聚合器协议的示例代码：

```solidity
contract Aggregator {
    function stake( ... ) external {
        ...
    }
    function claimMultipleStakingRewards(address[] calldata _claimContracts) external {
        uint256 totalRewards;
        for (uint256 i = 0; i < _claimContracts.length; i++) {
            totalRewards += IClaimContract(_claimContracts[i]).claimStakingRewards(
            msg.sender
            );
        }
        IERC20(stakingToken).transfer(msg.sender, totalRewards);
    }
}
```

它的目标很简单：`claimMultipleStakingRewards` 函数循环遍历用户提供的 staking 合约地址数组，调用每个合约上的 `claimStakingRewards` 函数，并统计总奖励。最后，它将累积的奖励发送到用户的地址。问题在于，合约没有检查 `_claimContracts` 中的地址是否真的指向受信任的 staking 合约。这为任意外部调用打开了大门。

例如，攻击者可以部署这样的合约：

```solidity
contract Attack {
    function claimStakingRewards(address ) external pure returns (uint256) {
        return 1_000_000 ether; // fabricated reward
    }
}
```

这个恶意合约假装是一个 staking 合约，只是返回一个 inflated 的奖励值。当 `Aggregator` 在其上调用 `claimStakingRewards` 时，它被欺骗，认为调用者被欠了大量的代币。如果没有额外的检查，`Aggregator` 会盲目地将其添加到总数中，并将真正的代币转移给攻击者。可以通过基本的允许列表来避免这种情况，以确保只有受信任的合约才能在 `claimMultipleStakingRewards` 中被允许。

### 签名重放攻击

以太坊上的签名非常有用，因为它们允许我们在链下授权操作，从而减少了对昂贵的链上交易的需求。例如，如果您授权某人代表您执行特定操作，例如转移代币或访问智能合约中的某个功能，您可以签署一个链下消息，授予他们许可。然后，合约验证签名并执行操作，而无需您直接在链上进行交互。这也实现了无 gas 交易，您可以在链下签名，然后由中继器在链上提交，并支付 gas 费用。智能合约可以验证这些签名，以确保在不需要持续的链上交互的情况下安全地授权操作。

然而，一旦一段数据被签名，它在逻辑上应该只使用一次。如果可以重用已签名的交易，那么它就为重放攻击打开了大门，攻击者可以重放签名以多次执行相同的操作，例如未经授权地转移资金或更改合约状态。智能合约必须设计为防止这种情况，方法是确保每个已签名的消息都是唯一的且不能被重放。

#### 漏洞

让我们看一个容易受到重放攻击的示例合约（示例 9-10）。

**示例 9-10. Token：容易受到签名重放攻击的合约**

```solidity
1 contract Token {
2    mapping(address => uint256) public balances;
3    struct Signature {
4        bytes32 r;
5        bytes32 s;
6        uint8 v;
7    }
8    event Transfer(address indexed from, address indexed to, uint256 amount);
9    function transfer(uint256[] memory _amount, address[] memory _from, address[]
     memory _to,  Signature memory _signature) public {
10        bytes32 messageHash = keccak256(abi.encodePacked(_from, _to, _amount));
11        address signer = ecrecover(messageHash, _signature.v, _signature.r, _signature.s);
12        for(uint256 i = 0; i < _from.length; i++){
13            address __from = _from[i];
14            address __to = _to[i];
15            uint256 __amount = _amount[i];
16            require(balances[__from] >= _amount[i], "Insufficient balance");
17            require(signer == _from[i], "Invalid signature");
18            balances[__from] -= __amount;
19            balances[__to] += __amount;
20            emit Transfer(__from, __to, __amount);
21        }
22    }
23 }
```

乍一看，这看起来像一个方便的合约函数。它允许任何拥有有效签名的人执行多次转账，而无需签名者支付 gas 费用。管理员可以在链下签署数据，而其他人（可能是服务）可以在链上为他们提交交易。无论如何，处理签名并非易事，并且这段非常简短的代码包含大量问题。

最明显的问题是没有机制可以阻止某人一遍又一遍地重复使用相同的签名。在没有任何方法来跟踪签名是否已被使用的情况下，攻击者可以简单地重复该交易，直到受害者的余额耗尽。修复非常简单：我们需要将 *nonce*（一个只使用一次的值，通常是一个每次交易都会递增的计数器）添加到正在签名的数据中。验证签名的合约有责任检查提供的 nonce 是否以前被使用过。这确保了每个签名都是唯一的，从而防止了重放。以太坊交易已经出于这个原因使用了 nonce。

这里的另一个关键问题是签名可延展性。当可以更改加密签名以生成相同底层消息的不同但仍然有效的签名时，就会发生这种情况。合约中使用的内置 `ecrecover` 函数容易受到此问题的影响。攻击者可以调整有效签名并创建另一个也有效的签名，即使底层的已签名消息保持不变。为避免这种情况，开发人员应使用更安全的签名验证方法，例如 OpenZeppelin ECDSA 库提供的方法。可延展的签名是您不想将签名用作唯一标识符的原因，例如为了避免重放攻击——坚持使用 nonce。

我们已经解决了潜在的签名操纵问题，但是如果也可以操纵正在签名的数据会发生什么呢？在这个合约中，它可以。问题在于使用 `abi.encodePacked`，它通常因其紧凑的编码而选择，这种编码需要更少的内存。但是，这种效率是有代价的，我们将要探讨它们。具体来说，`abi.encodePacked` 连接原始字节而不添加长度信息或边界，这意味着不同的输入集最终可能产生相同的输出。以下是它如何发挥作用。

为了简单起见，让我们假设金额采用 8 位（两位十六进制数字），地址采用 12 位（三位十六进制数字）。让我们说参数如下：

```solidity
_amount = [0x64, 0x64]
_from = [0x001, 0x002]
_to = [0x003, 0x003]
```

当我们使用 `abi.encodePacked` 时，它将这些值组合成 `0x6464001002003003`。但是，这里的事情变得棘手了。如果我们从 `_from` 将 `0x002` 移动到 `_to`，我们仍然会从 `abi.encodePacked` 获得与之前完全相同的输出：

```solidity
_amount = [0x64, 0x64]
_from = [0x001]
_to = [0x002, 0x003, 0x003]
```

对于这组新值，`abi.encodePacked` 将返回相同的输出：`0x6464001002003003`。这意味着用户 `0x002` 可以使用有效的签名，但更改输入参数 `_from` 和 `_to`，从而欺骗合约认为要执行的唯一转账是从 `0x001` 到 `0x002`。示例中使用的代码在验证输入方面做得非常糟糕，从而允许了这种有问题的situation。无论如何，它表明在动态数据类型（如数组）上生成签名时应避免使用 `encodePacked`。在这些情况下，我们应该使用 `abi.encode`，即使在连接动态数据时，它也会产生明确的输出，从而有效地防止这种类型的攻击。

但是等等，还有一个问题。如果此合约部署在多个链上会发生什么？相同的签名将在所有这些链上都有效，从而创造了跨链重放攻击的机会。攻击者可以监视用户在一个链上的活动，然后在其他链上重复使用其签名。为防止这种情况，我们需要在已签名的消息中包含上下文数据——至少是 `chainId`。根据用例，您可能还会包括合约地址或其版本。幸运的是，我们不必从头开始提出新的解决方案：EIP-712 是一个通过允许上下文感知签名来解决此问题的标准。它还通过向用户显示有关他们正在签名的内容的可读信息，而不是令人困惑的字节字符串，从而改善了用户体验。

#### 预防措施

为防止重放攻击和其他漏洞，我们需要确保每个签名都是唯一的、安全的且只能使用一次。我们可以通过 nonce、安全签名处理和上下文感知签名轻松实现这一点。

Nonce 用于确保唯一性。通过向每个已签名的消息添加 nonce，我们可以防止攻击者重复使用签名。验证签名的合约要确保使用的 nonce 是唯一的。一旦签名被使用，其 nonce 将变为无效，从而阻止重放尝试。

在验证签名时，我们应该避免使用普通的内置 `ecrecover` 函数，而应使用 OpenZeppelin 的 ECDSA 库，该库可以防止签名可延展性。我们也不应将签名用作唯一标识符，因为它们可以被操纵。

对于签名动态数据，使用 `abi.encode` 而不是 `abi.encodePacked` 可以通过正确分离输入来防止操纵输入，从而确保它们不会被篡改或误解。

最后，每当我们处理签名时，我们都应实施 EIP-712。除了添加上下文感知（例如，`chainId` 以防止跨链重放）之外，EIP-712 还可以让用户看到清晰、有意义的他们正在签名的数据的可视化表示，而不是不透明的字节字符串，从而改善用户体验。这不仅使交易更容易理解，而且还通过使用户更容易识别可疑请求来增强用户安全，因为这使得网络钓鱼攻击更加困难。

#### 真实案例：TCH 代币

2024 年 5 月，TCH 代币由于常见的签名可延展性漏洞而被利用。问题出在合约的 `burnToken` 函数中，该函数验证签名以授权代币销毁。为防止签名重放攻击，合约将已使用的签名存储在映射中。但是，如果签名被篡改，则可以绕过此防御。

攻击者通过收集先前提交签名并修改 `v` 和 `s` 值来利用这一点，这些值是签名的一部分。尽管签名被更改了，但它仍然通过使用 `ecrecover` 进行了验证。由于修改后的签名与原始签名不同，因此未被识别为已使用，并且新版本存储在映射中。通过这种技巧，攻击者能够反复销毁 PancakeSwap 流动性池拥有的大量 TCH 代币。这允许攻击者操纵池中代币的价格，并从他们造成的价格波动中获利。

### 智能合约错误配置

错误配置是那些并不是技术上的漏洞，但仍然可能对智能合约产生严重后果的隐蔽问题之一。在您编写完智能合约并通过审计后，工作并没有完成；您仍然需要部署、维护，有时还需要升级它。正是在这些阶段，经常会发生错误配置。例如，DeFi 协议带有大量的参数，如果这些参数中的任何一个配置错误，都可能导致重大损失。不幸的是，即使在审计中，这些类型的问题也很难发现，因为审计员经常忽略部署和升级脚本。因此，虽然错误配置本身不是漏洞，但它们可能会为漏洞的出现创造机会，因此在部署和管理阶段格外小心至关重要。

错误配置问题很难分类，因为它们可能差异很大，因此与其尝试全部列出，不如直接跳到一些真实案例，以了解可能出错的情况。

#### 真实案例：yUSDT

让我们看一下最简单的错误配置案例：Yearn Finance 的 yUSDT 代币中配置错误的存储变量，这导致了 2023 年 4 月的利用。yUSDT 代币应该通过投资于基于 USDT 的衍生品来产生收益，但由于错误配置，它实际上使用了一个不同的代币 (IUSDC) 作为其底层资产。疯狂的是，这种情况持续了一千多天都没被注意到。错误配置允许攻击者操纵系统，从池中耗尽价值，并基本上免费铸造 yUSDT。因此，yUSDT 的价值降至零，攻击者带着 1,160 万美元的利润离开了。

#### 真实案例：Ronin Bridge

2024 年 8 月，Ronin Bridge 在合约升级后仅一小时就被黑客入侵。根本原因是升级过程中的一个失误：一个重要的变量 `_totalOperatorWeight` 没有被初始化。这个变量应该在 `initializeV3` 函数中设置，但在升级期间，只调用了 `initializeV4`，跳过了之前版本中必要的设置。这个疏忽使合约暴露了。在这种情况下，一个白帽 MEV 机器人能够在攻击之前抢先行动并归还被盗的 4,000 ETH，但这突出了彻底审查和测试升级程序的重要性。

> **注意**
>
> 如果您认为在合约升级后不久发生的黑客攻击纯粹是巧合，那么您就错了。黑帽和白帽都在密切监视合约升级：黑帽寻找可以利用的弱点，而白帽则试图防止攻击。团队经常低估即使是小的代码更改的安全风险，并跳过审计过程。不幸的是，破坏一份合约并不需要太多，正如本案所示，漏洞并不总是在智能合约本身中——有时它在于升级的执行方式。

#### 真实案例：Sonne Finance

Sonne Finance 在 2024 年 5 月被黑客入侵的根本原因不仅仅是一个典型的协议错误，而是其市场激活过程中的缺陷。像许多协议一样，Sonne 意识到了 Compound v2 中发现的“空市场”错误，即一个开放但未注资的市场可能被利用来耗尽整个协议。此错误的标准解决方法是确保在市场激活时原子地将资金存入市场，从而防止市场在任何时候都为空。

Sonne 制定了一个处理此问题的计划。它打算添加市场、存入资金，然后开放市场供使用——所有这三个操作都通过时间锁进行。如果以正确的顺序完成，此过程将起作用。问题出现的原因是 Sonne 将这些步骤中的每一个都安排为治理时间锁控制器中的单独交易，这意味着它们的执行顺序没有被强制执行。Sonne 团队使每个人都可以访问治理 `EXECUTOR_ROLE`，允许任何用户在时间锁到期后执行治理交易。虽然这种设置是不寻常的，但它本身并没有问题；然而，它在这种特定情况下被证明是毁灭性的。它为任何人在时间锁到期后以错误的顺序执行操作敞开了大门。

攻击者只是执行了所有排队的时间锁操作，而没有等待资金存入，从而使一个空的、易受攻击的市场开放。通过利用这个未注资的市场，他们从协议中耗尽了 2000 万美元。

这里的关键要点是，当治理操作需要以特定的顺序发生以确保安全时，它们应该被原子化。例如，如果他们使用 OpenZeppelin Timelock，则应使用 `scheduleBatch()` 而不是 `schedule()` 进行安排。Sonne 的错误是允许将这些操作单独排队，这使它们暴露了。

#### 预防措施

为避免错误配置问题以及我们讨论过的代价高昂的错误，我们需要在智能合约的整个生命周期中采取积极主动的方法，尤其是在部署、升级和任何关键的治理操作方面。我们应始终确保部署和升级脚本经过彻底的测试和审计。我们需要超越审计代码本身，并密切关注触及主网的脚本，确保流程的每个方面都在类似直播的环境中进行了测试。

## 合约库

有很多现有代码可供重用，无论是在链上部署为可调用的库，还是在链下部署为代码模板库。在以太坊中，最广泛使用的资源是 [OpenZeppelin 套件](https://github.com/OpenZeppelin/openzeppelin-contracts/tree/master/contracts)，这是一个包含大量合约的库，范围从各种代币的实现到不同的代理架构，再到合约中常见的简单行为，例如 `Ownable`、`Pausable` 或 `ReentrancyGuard`。此存储库中的合约已经过广泛的测试，并且在某些情况下，甚至可以作为事实上的标准实现。它们可以免费使用，并且由 [OpenZeppelin](https://www.openzeppelin.com) 与不断增长的外部贡献者列表共同构建和维护。

其他值得注意的合约库包括 Paradigm 的 [Solmate](https://github.com/transmissions11/solmate) 和 Vectorized 的 [Solady](https://github.com/Vectorized/solady)。Solmate 在设计方面更固执己见，而 Solady 主要侧重于 gas 优化。

## 附加资源

由于智能合约安全性涵盖了如此多的深度和细微差别，因此这里提供了一个资源列表，好奇的读者可以在其中了解有关这个非常高级主题的更多信息：

**Cyfrin Updraft 智能合约安全和审计**

一个全面的 24 小时课程（270 多个课程）

**Secureum 训练营**

一个为期三个月的强化训练营，专注于以太坊智能合约安全审计

**Ethernaut**

OpenZeppelin 的一个基于 Solidity 的战争游戏，玩家通过黑客智能合约级别来学习常见的漏洞

**Damn Vulnerable DeFi**

一个夺旗 (CTF) 平台，包含 18 个挑战，涵盖闪电贷、价格预言机、治理、NFT 等

**Capture the Ether**

一个经典的 CTF 风格的以太坊安全游戏

**QuillCTF**

QuillAudits 的以太坊安全谜题的集合

**Paradigm CTF**

由 Paradigm 组织的年度在线 CTF 竞赛，面向经验丰富的智能合约黑客，挑战非常高级，反映了最前沿的漏洞；官方解决方案和说明经常发布，使其也成为一种学习资源

## 结论

感谢它的更新，Solidity 编译器现在可以缓解诸如整数溢出和默认可见性问题之类的风险。这使我们能够删除本书第一版中提到的一些较旧的陷阱，并使用该空间来关注更多当前和相关的漏洞。无论如何，任何在智能合约领域工作的开发人员仍然需要知道和理解很多东西。通过遵循智能合约设计和代码编写中的最佳实践，您将避免许多严重的陷阱和陷阱。

也许最基本的软件安全原则是最大限度地重用受信任的代码。在密码学中，这非常重要，以至于它已被浓缩成一句格言：“不要自己编写密码。”在智能合约的情况下，这相当于从社区彻底审查过的免费库中获得尽可能多的收益。
