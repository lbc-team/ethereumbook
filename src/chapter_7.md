# 第 7 章. 智能合约和Solidity

正如我们在第 2 章中讨论的，以太坊中有两种不同类型的账户：EOA 和合约账户。EOA 由用户控制，通常通过[钱包](https://learnblockchain.cn/tags/%E9%92%B1%E5%8C%85)应用程序等以太坊平台外部的软件控制。相比之下，合约账户由程序代码（也通常被称为*智能合约*）控制，这些代码由 EVM 执行。

简而言之，EOA 是没有任何关联代码或数据存储的简单账户，而合约账户则既有关联的代码又有数据存储。EOA 由交易控制，这些交易由私钥以密码学方式签名，并在独立于协议的“现实世界”中创建，而合约账户没有私钥，因此以智能合约代码预定的方式“自我控制”。两种类型的账户都由一个以太坊地址标识。在本章中，我们将讨论合约[账户](https://learnblockchain.cn/tags/账户?map=EVM)和控制它们的程序代码。

## 什么是智能合约？

多年来，术语*智能合约*被用来描述各种各样的事物。在 20 世纪 90 年代，密码学家 Nick Szabo 创造了这个术语，并将其定义为“一套以数字形式指定的承诺，包括各方履行彼此承诺的协议”。从那以后，智能合约的概念不断发展，尤其是在 2009 年[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)推出后，随着去中心化区块链平台的引入。

在以太坊的背景下，这个术语实际上有点用词不当，因为以太坊智能合约既不智能也不是法律意义上的合约，但这个术语已经沿用下来。在本书中，我们使用术语*智能合约*来指代不可变的计算机程序，这些程序作为以太坊网络协议的一部分，在 EVM 的上下文中确定性地运行——也就是说，在去中心化的以太坊世界计算机上运行。

让我们来解读一下这个定义：

**计算机程序**

智能合约仅仅是计算机程序。*合约*一词在这种语境下没有法律意义。

**不可变**

一旦部署，智能合约的代码就无法更改。与传统软件不同，修改智能合约的唯一方法是部署一个新的实例。

**确定性**

考虑到启动其执行的交易的上下文以及执行时以太坊区块链的状态，智能合约执行的结果对于每个运行它的人来说都是相同的。

**EVM 上下文**

智能合约在非常有限的执行上下文中运行。它们可以访问自己的状态、调用它们的交易的上下文以及有关最新区块的一些信息。

**去中心化的世界计算机**

EVM 作为本地实例在每个以太坊节点上运行，但由于 EVM 的所有实例都在相同的初始状态下运行并产生相同的最终状态，因此整个系统作为一个单一的“世界计算机”运行。

## 智能合约的生命周期

智能合约通常用高级语言编写，例如 Solidity。但是为了运行，它们必须被编译成低级字节码，该字节码才能在 EVM 中运行。一旦编译完成，它们就会使用特殊的合约创建交易部署在以太坊平台上，该交易通过被发送到合约创建地址来标识，即 `0x0` (参见 “特殊交易：合约创建")。每个合约都由一个以太坊地址标识，该地址是从合约创建交易中派生出来的，它是原始账户和 nonce 的函数。合约的以太坊地址可以用在交易中作为接收者，将资金发送到合约或调用合约的函数之一。请注意，与 EOA 不同的是，没有与为新智能合约创建的账户关联的密钥。作为合约创建者，您在协议级别上没有任何特殊权限（尽管您可以在智能合约中明确编码它们）。您当然不会收到合约账户的私钥，实际上它并不存在——我们可以说智能合约账户拥有自己。

重要的是，合约*只有在被交易调用时才会运行*。以太坊中的所有智能合约最终都是由于 EOA 发起的交易而执行的。一个合约可以调用另一个合约，该合约可以调用另一个合约，依此类推，但是这种执行链中的第一个合约将始终由 EOA 的交易调用。合约永远不会“自己”或“在后台”运行。合约实际上处于休眠状态，直到交易触发执行，无论是直接的还是间接的，作为一系列合约调用的一部分。还值得注意的是，智能合约不会以任何方式“并行”执行——以太坊世界计算机可以被认为是一台单线程机器。

交易是*原子性*的，无论它们调用多少合约，或者这些合约在被调用时做什么。交易完整地执行，只有当所有执行都成功终止时，才会记录全局状态（合约、账户等）的任何更改。*成功终止*意味着程序执行没有错误并到达执行结束。如果由于错误导致执行失败，则其所有影响（状态的更改）都将“回滚”，就好像交易从未运行过一样。失败的交易仍然会被记录为已尝试，并且在执行 gas 上花费的以太币将从原始账户中扣除，但在其他方面对合约或账户状态没有影响。

如前所述，合约的代码一旦部署就无法更改。历史上，合约可以被删除，从其地址中删除其代码和内部状态（存储），并留下一个空白账户。在此类删除之后，发送到该地址的任何交易都不会导致代码执行，因为不会留下任何代码。此删除是使用名为 `SELFDESTRUCT` 的 EVM 操作码完成的，该操作码提供 gas 退款，通过删除存储状态来激励网络资源的释放。但是，由于它需要对账户状态进行重大更改，特别是删除所有代码和存储，因此 `SELFDESTRUCT` 操作已在 2023 年被 [EIP-6780](https://eips.ethereum.org/EIPS/eip-6780) 弃用。随着以太坊路线图中即将到来的升级，此操作将不再可行。

## 以太坊高级语言简介

EVM 是一种运行特殊代码的虚拟机，称为 *EVM 字节码*，类似于您计算机的 CPU，它运行机器代码，例如 x86_64。我们将在第 14 章中更详细地研究 EVM 的操作和语言。在本节中，我们将了解如何编写智能合约以在 EVM 上运行。

虽然可以直接用字节码编写智能合约，但是 EVM 字节码相当笨拙，并且程序员很难阅读和理解。相反，大多数以太坊开发人员使用高级语言编写程序，并使用编译器将其转换为字节码。

虽然任何高级语言都可以适用于编写智能合约，但是将任意语言改编为可编译为 EVM 字节码是一个相当繁琐的练习，并且通常会导致一定程度的混乱。智能合约在高度受限和最小化的执行环境（EVM）中运行。此外，还需要一组特定的 EVM 特定系统变量和函数。因此，从头开始构建智能合约语言比使通用语言适合编写智能合约更容易。因此，已经出现了许多用于编程智能合约的专用语言。以太坊有几种这样的语言，以及生成 EVM 可执行字节码所需的编译器。

一般来说，编程语言可以分为两大编程范式：*声明式* 和 *命令式*，也分别称为 *函数式* 和 *过程式*。在声明式编程中，我们编写表达程序*逻辑*但不表达其*流程*的函数。声明式编程用于创建没有*副作用*的程序，这意味着函数外部的状态没有变化。声明式编程语言包括 Haskell 和 SQL。相比之下，命令式编程是程序员编写一组组合程序逻辑和流程的过程的地方。命令式编程语言包括 C++ 和 Java。有些语言是“混合的”，这意味着它们鼓励声明式编程，但也可以用来表达命令式编程范式。这种混合语言包括 Lisp、[JavaScript](https://learnblockchain.cn/tags/JavaScript) 和 Python。一般来说，任何命令式语言都可以用来以声明式范式编写，但这通常会导致不优雅的代码。相比之下，纯声明式语言不能用来以命令式范式编写。在纯声明式语言中，没有“变量”。

虽然命令式编程更常被程序员使用，但编写完全按照预期执行的程序可能非常困难。程序的任何部分都可以更改任何其他部分的状态，这使得很难推理程序的执行并为错误引入许多机会。相比之下，声明式编程更容易理解程序的行为方式：由于它没有副作用，因此可以孤立地理解程序的任何部分。

在智能合约中，错误实际上会花钱。因此，编写没有意外影响的智能合约至关重要。为此，您必须能够清楚地推理程序的预期行为。因此，声明式语言在智能合约中比在通用软件中发挥更大的作用。然而，正如你将看到的，最广泛使用的智能合约语言（Solidity）是命令式的。像大多数人一样，程序员抵制改变!

当前支持的智能合约高级编程语言包括以下几种（按受欢迎程度排序）：

**Solidity**

一种过程式（命令式）编程语言，其语法类似于 [JavaScript](https://learnblockchain.cn/tags/JavaScript)、C++ 或 Java。以太坊智能合约最流行和最常用的语言。

**Yul**

一种中间语言，可以在独立模式下或以内联方式在 Solidity 中使用，非常适合跨平台的高级优化。初学者应该先从 Solidity 或 Vyper 开始，然后再探索 Yul，因为它需要智能合约安全性和 EVM 的高级知识。

**Vyper**

一种面向合约的编程语言，具有类似 Python 的语法，优先考虑用户安全，并通过语言设计和高效执行来鼓励清晰的编码实践。

**Huff**

一种低级编程语言，主要由需要高效且最小化合约代码的开发人员使用，允许超出 Solidity 等高级语言提供的更高级的优化。与 Yul 一样，不建议初学者使用。

**Fe**

一种用于 EVM 的静态类型智能合约语言，灵感来自 Python 和 [Rust](https://learnblockchain.cn/tags/Rust)。它的目标是易于学习，即使对于以太坊的新手开发人员也是如此，自 2021 年 1 月发布 alpha 版本以来，其开发仍处于早期阶段。

过去开发的其他语言，例如 LLL、Serpent 和 Bamboo，现在已经不再维护。

正如你所看到的，有很多语言可供选择。然而，在所有这些语言中，Solidity 无疑是最受欢迎的，以至于成为以太坊甚至其他类似 EVM 的区块链的事实上的高级语言。

## 使用 Solidity 构建智能合约

Solidity 由 Gavin Wood（本书第一版的第一作者）创建，作为一种专门用于编写智能合约的语言，其特性直接支持在以太坊世界计算机的去中心化环境中执行。由此产生的属性非常通用，因此最终被用于在其他几个区块链平台上编码智能合约。它由 Christian Reitwiessner 开发，然后由 Alex Beregszaszi、Liana Husikyan、Yoichi Hirai 和几位前以太坊核心贡献者开发。Solidity 现在作为一个独立的项目在 [GitHub](https://github.com/argotorg/solidity) 上开发和维护。

Solidity 项目的主要“产品”是 Solidity 编译器 solc，它将用 Solidity 语言编写的程序转换为 EVM 字节码。该项目还管理着以太坊智能合约的重要 ABI 标准，我们将在本章中详细探讨。Solidity 编译器的每个版本都对应并编译特定版本的 Solidity 语言。

要开始使用，我们将下载 Solidity 编译器的二进制可执行文件。然后，我们将开发和编译一个简单的合约，延续我们在第 2 章中开始的示例。

### 选择一个 Solidity 版本

Solidity 遵循一个名为 [*语义化版本*](https://semver.org) 的版本控制模型，该模型指定版本号的结构为三个由点分隔的数字：MAJOR.MINOR.PATCH。“major” 数字用于主要和向后不兼容的更改，“minor” 数字用于在主要版本之间添加向后兼容的功能，“patch” 数字用于向后兼容的 bug 修复。

在编写本文时，Solidity 的版本是 0.8.26。主要版本 0 的规则，该版本用于项目的初始开发，是不同的：任何事情都可能随时更改。在实践中，Solidity 将 “minor” 数字视为主要版本，将 “patch” 数字视为 minor 版本。因此，在 0.8.26 中，8 被认为是主要版本，26 被认为是 minor 版本。正如你在第 2 章中看到的，你的 Solidity 程序可以包含一个 pragma 指令，该指令指定了它兼容的 Solidity 的最小和最大版本，并且可以用来编译你的合约。由于 Solidity 发展迅速，因此最好安装最新版本。

> **注意**
>
> Solidity 快速发展的另一个结果是文档过时的速度。目前，我们使用的是 Solidity 版本 0.8.26，本书中的所有内容都基于该版本。虽然本书将始终为你学习 Solidity 提供坚实的基础，但未来的版本可能会更改一些语法和功能。因此，无论何时你有疑问或遇到新的内容，最好查看 [官方 Solidity 文档](https://docs.soliditylang.org/en/latest/) 以保持最新状态。

### 下载和安装 Solidity

根据您的操作系统和要求，您可以使用多种方法来下载和安装 Solidity：可以作为二进制发行版，也可以从源代码编译。您可以在 [Solidity 文档](https://docs.soliditylang.org/en/latest/installing-solidity.html) 中找到详细且更新的说明。

以下是如何在 Ubuntu/Debian 操作系统上使用 apt 包管理器安装最新的 Solidity 二进制发行版：

```bash
$ sudo add-apt-repository ppa:ethereum/ethereum
$ sudo apt update
$ sudo apt install solc
```

安装完 solc 后，运行以下命令检查版本：

```bash
$ solc --version
solc, the solidity compiler commandline interface
Version: 0.8.26+commit.8a97fa7a.Linux.g++
```

### 开发环境

虽然完全可以使用简单的文本编辑器来开发 Solidity 智能合约，但是利用像 [Hardhat](https://hardhat.org) 或 [Foundry](https://getfoundry.sh/) 这样的开发框架可以显著提高你作为开发人员的效率和有效性。这些框架提供了一套全面的工具，可以简化和改进开发过程。例如，它们提供强大的测试环境，允许你编写和运行单元测试来验证合约的行为，并且它们提供分叉功能，以创建 mainnet 的本地实例以进行真实的测试场景。借助高级调试和跟踪功能，你可以轻松地单步执行代码执行并快速识别和解决问题，从而节省时间并减少错误。此外，这些框架还支持脚本编写和部署自动化、扩展功能的插件生态系统以及跨不同环境的无缝网络管理。将这些功能集成到你的工作流程中可确保更高水平的代码质量和安全性，这很难通过简单的文本编辑器来实现。

除了框架之外，采用像 VS Code 这样的现代 IDE 还可以进一步提高生产力。VS Code 为 Solidity 提供了各种扩展，包括语法突出显示，这使你的代码更易于阅读；高级注释和书签工具，可帮助组织和浏览复杂的项目；以及可视化分析工具，可提供有关代码结构和潜在问题的见解。还有基于 web 的开发环境，例如 [Remix IDE](https://remix.ethereum.org)。

总之，这些工具不仅可以提高代码质量，还可以加快开发过程，从而使我们能够更快、更安全地构建和部署智能合约。

### 编写一个简单的 Solidity 程序

在第 2 章中，我们编写了我们的第一个 Solidity 程序。当我们第一次构建 `Faucet` 合约时，我们使用 Remix IDE 来编译和部署合约。在本节中，我们将重温、改进和润色 `Faucet`。

我们的第一次尝试如示例 7-1 所示。

**示例 7-1. Faucet.sol：一个实现水龙头的 Solidity 合约**

```solidity
// SPDX-License-Identifier: GPL-3.0
// 我们的第一个合约是一个水龙头！
contract Faucet {
    // 向任何提出要求的人提供以太币
    function withdraw(uint _withdrawAmount, address payable _to) public {
        // 限制提款金额
        require(_withdrawAmount <= 100000000000000000);
        // 将金额发送到请求它的地址
        _to.transfer(_withdrawAmount);
    }
    // 接受任何传入金额
    receive() external payable {}
}
```

正如我们在第 2 章中看到的，注释中的 SPDX 许可证标识符指示智能合约已获得 GPL-3.0 许可，告知用户和开发人员使用和分发代码的合法权利和义务。

### 使用 Solidity 编译器 (solc) 进行编译

现在，我们将在命令行上使用 Solidity 编译器直接编译我们的合约。Solidity 编译器 solc 提供了各种选项，您可以通过传递 `--help` 参数来查看这些选项。

我们使用 solc 的 `--bin` 和 `--optimize` 参数来生成示例合约的优化二进制文件：

```bash
$ solc --optimize --bin Faucet.sol
======= Faucet.sol:Faucet =======
Binary:
6080604052348015600e575f5ffd5b5060fa8061001b5f395ff3fe608060405260043610601d575f3560e01c806
2f714ce146027575f5ffd5b36602357005b5f5ffd5b3480156031575f5ffd5b506041603d366004608d565b6043
565b005b67016345785d8a00008211156056575f5ffd5b6040516001600160a01b0382169083156108fc0290849
05f818181858888f193505050501580156088573d5f5f3e3d5ffd5b505050565b5f5f60408385031215609d575f
5ffd5b8235915060208301356001600160a01b038116811460b9575f5ffd5b80915050925092905056fea264697
06673582212208935b6cf5d9070b7609ad59ac4b727e512522c674cacf09a2eff88dafa3242ee64736f6c634300
081b0033
```

solc 生成的结果是一个十六进制序列化的二进制文件，可以提交给以太坊区块链。

## 以太坊合约 ABI

在计算机软件中，*应用程序二进制接口* 是两个程序模块之间的接口，通常是操作系统和用户程序之间。ABI 定义了如何在 *机器码* 中访问数据结构和函数；这不要与 API 混淆，后者以高级的、通常是人类可读的格式（作为*源代码*）定义这种访问。因此，ABI 是将数据编码和解码为机器码以及从机器码中编码和解码的主要方式。

在以太坊中，ABI 用于编码 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 的合约调用以及从交易中读取数据。ABI 的目的是定义合约中可以调用的函数，并描述每个函数将如何接受参数并返回其结果。

合约的 ABI 被指定为一个 JSON 函数描述数组（请参阅“函数”）和事件（请参阅“事件”）。函数描述是一个 JSON 对象，其中包含字段 `type`、`name`、`inputs`、`outputs`、`constant` 和 `payable`。事件描述对象具有字段 `type`、`name`、`inputs` 和 `anonymous`。

我们使用 solc 命令行 Solidity 编译器来生成 *Faucet.sol* 示例合约的 ABI：

```bash
$ solc --abi Faucet.sol
======= Faucet.sol:Faucet =======
Contract JSON ABI
[{"inputs":[{"internalType":"uint256","name":"withdrawAmount","type":"uint256"}],
"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},
{"stateMutability":"payable","type":"receive"}]
```

正如你所看到的，编译器生成一个 JSON 数组，描述了 *Faucet.sol* 定义的两个函数。任何想要在 `Faucet` 合约部署后访问它的应用程序都可以使用此 JSON。使用 ABI，钱包或 DApp 浏览器等应用程序可以构建调用 `Faucet` 中函数的交易，并使用正确的参数和参数类型。例如，钱包会知道要调用函数 `withdraw`，它必须提供一个名为 `withdrawAmount` 的 `uint256` 参数。钱包可以提示用户提供该值，然后创建一个编码该值并执行 `withdraw` 函数的交易。

应用程序与合约交互所需的只是一个 ABI 和合约部署的地址。

## 选择一个 Solidity 编译器和语言版本

正如我们在前面的代码中看到的，我们的 `Faucet` 合约使用 Solidity 版本 0.8.26 成功编译。但是，如果我们使用了不同版本的 Solidity 编译器会怎样？语言仍在不断变化，并且事情可能会以意想不到的方式发生变化。我们的合约相当简单，但是如果我们的程序使用了仅在 Solidity 版本 0.8.26 中添加的功能，并且我们尝试使用 0.8.25 来编译它会怎样？

为了解决此类问题，Solidity 提供了一个称为 *版本 pragma* 的编译器指令，该指令指示编译器该程序需要特定的编译器（和语言）版本。让我们看一个例子：

```solidity
pragma solidity 0.8.26;
```

Solidity 编译器读取版本 pragma，如果编译器版本与版本 pragma 不兼容，则会生成错误。在这种情况下，我们的版本 pragma 表明该程序可以由版本为 0.8.26 的 Solidity 编译器编译。Pragma 指令不会编译到 [EVM](https://learnblockchain.cn/tags/EVM?map=EVM) 字节码中；它们是仅由编译器用于检查兼容性的编译时指令。

> **注意**
>
> 在 pragma 指令中，符号 ^ 表示我们允许使用等于或高于指定版本的任何 *minor 修订版* 进行编译。例如，pragma 指令 `pragma solidity ^0.7.1;` 表示该合约可以使用 0.7.1、0.7.2 和 0.7.3 的 solc 版本进行编译，但不能使用 0.8.0（这是一个 major 修订版，而不是 minor 修订版）。

让我们将 pragma 指令添加到我们的 `Faucet` 合约中。我们将把新文件命名为 *Faucet2.sol*，以便在完成这些示例时跟踪我们的更改，从示例 7-2 开始。

**示例 7-2. Faucet2.sol：将版本 pragma 添加到 Faucet**

```solidity
pragma solidity 0.8.26;
// SPDX-License-Identifier: GPL-3.0
// 我们的第一个合约是一个水龙头！
contract Faucet {
    // 向任何提出要求的人提供以太币
    function withdraw(uint _withdrawAmount, address payable _to) public {
        // 限制提款金额
        require(_withdrawAmount <= 100000000000000000);
        // 将金额发送到请求它的地址
        _to.transfer(_withdrawAmount);
    }
    // 接受任何传入金额
    receive() external payable {}
}
```

添加版本 pragma 是一种最佳实践，因为它避免了编译器和语言版本不匹配的问题。我们将在本章中探讨其他最佳实践，并继续改进 `Faucet` 合约。

## 使用 Solidity 进行编程

在本节中，我们将了解 Solidity 语言的一些功能。正如我们在第 2 章中提到的，我们的第一个合约示例非常简单，并且在各种方面也存在缺陷。我们将在探索如何使用 Solidity 的同时逐步改进它。但是，这不会是一个全面的 Solidity 教程，因为 Solidity 非常复杂且发展迅速。我们将介绍基础知识，并为您提供足够的基础，以便您能够自己探索其余部分。

### 数据类型

首先，让我们看一下 Solidity 中提供的一些基本数据类型：

**布尔值 (bool)**

布尔值，`true` 或 `false`，具有逻辑运算符 !（非），&&（与），||（或），==（等于）和 !=（不等于）。

**整数 (int, uint)**

有符号 (`int`) 和无符号 (`uint`) 整数，以 8 位增量声明，从 `int8` 到 `uint256`。如果没有大小后缀，则使用 256 位数量来匹配 EVM 的字大小。

**定点数 (fixed, ufixed)**

定点数，使用 `(u)fixedMxN` 声明，其中 *M* 是以位为单位的大小（以 8 为增量，最大为 256），*N* 是小数点后的位数（最大为 18） - 例如，`ufixed32x2`。

> **注意**
>
> Solidity 尚未完全支持定点数。可以声明它们，但不能分配给它们或从它们分配。

**地址 (address)**

一个 20 字节的以太坊地址。`address` 对象有许多有用的成员函数，主要的函数是 `balance`（返回账户余额）和 `transfer`（将以太币转移到账户）。

**字节数组（固定）**

字节的固定大小数组，使用 `bytes1` 到 `bytes32` 声明。

**字节数组（动态）**

字节的可变大小数组，使用 `bytes` 或 `string` 声明。

**枚举 (Enum)**

用于枚举离散值的用户定义类型：`enum NAME {LABEL1, LABEL 2, ...}`。枚举的基础类型是 `uint8`；因此，它不能超过 256 个成员，并且可以显式转换为所有整数类型。

**数组 (Arrays)**

任何类型的数组，无论是固定大小的还是动态大小的：`uint32[][5]` 是五个无符号整数的动态数组的固定大小数组。

**结构体 (Struct)**

用于对变量进行分组的用户定义数据容器：`struct NAME {TYPE1 VARIABLE1; TYPE2 VARIABLE2; ...}`。

**映射 (Mapping)**

用于 *key* ⇒ *value* 对的哈希查找表：`mapping(KEY_TYPE` `⇒` `VALUE_TYPE) NAME`。

除了这些数据类型之外，Solidity 还提供了各种值字面量，可用于计算不同的单位：

**时间单位**

全局变量 `block.timestamp` 表示将块发布并添加到区块链的时间（以秒为单位），从 Unix Epoch（1970 年 1 月 1 日）开始计数。单位 `seconds`、`minutes`、`hours` 和 `days` 可以用作后缀，转换为基本单位 `seconds` 的倍数。

> **注意**
>
> 由于一个块可以包含多个交易，因此一个块中的所有交易共享相同的 `block.timestamp`，它反映了块发布的时间，而不是每个交易发起的准确时间。

**以太币单位**

单位 `wei` 和 `ether` 可以用作后缀，转换为基本单位 `wei` 的倍数。以前，也提供了面额 `finney` 和 `szabo`，但在 Solidity 版本 0.7.0 中已删除它们。

在我们的 `Faucet` 合约示例中，我们对 `withdrawAmount` 变量使用了 `uint`（它是 `uint256` 的别名）。我们还间接使用了 `address` 变量，我们使用 `msg.sender` 设置了该变量。我们将在本章的其余示例中使用更多这些数据类型。

让我们使用单位乘数之一来提高示例合约的可读性。在 `withdraw` 函数中，我们限制了最大提款，以 wei 为单位表示限制，即以太币的基本单位：

```solidity
require(withdrawAmount <= 100000000000000000);
```

这不太容易阅读。我们可以通过使用单位乘数 `ether` 来改进我们的代码，以以太币而不是 wei 为单位表示该值：

```solidity
require(withdrawAmount <= 0.1 ether);
```

### 变量：定义和作用域

在 Solidity 中，定义变量和函数的语法与其他静态类型语言类似：我们为每个变量分配一个类型、一个名称和一个可选值。对于状态变量，我们还可以指定它们的可见性。默认可见性是 `internal`，这意味着该变量只能在合约及其派生合约中访问。要使它们可以从其他智能合约访问，我们需要使用 `public` 可见性。

Solidity 智能合约具有三种类型的变量作用域：

**状态变量**

这些变量通过在区块链上记录值来存储智能合约中的永久数据，称为*持久状态*。状态变量在智能合约中定义，但在任何函数之外定义。示例：`uint public count;`

**局部变量**

这些是在计算期间使用的临时数据，用于短期保存信息。局部变量不存储在区块链上；它们存在于函数中，并且无法在其定义的作用域之外访问。示例：`uint count = 1;`

**全局变量**

这些变量由 Solidity 自动提供，无需显式声明或导入即可使用。它们提供有关区块链环境的信息，并包括可在程序中使用的实用程序功能。预定义的全局变量详尽地列在以下各节中。

正如我们简要提到的，可以声明状态变量并指定其可见性。Solidity 提供三个不同的可见性级别：*公共变量* 生成自动 getter 函数，允许外部合约读取它们的值，尽管它们不能修改它们；*内部变量* 只能在合约及其派生合约中访问；*私有变量* 类似于内部变量，但即使是派生合约也无法访问。

### 预定义的全局变量和函数

当在 EVM 中执行合约时，它可以访问一小组全局对象。这些对象包括 `block`、`msg` 和 `tx` 对象。此外，Solidity 将许多 EVM 操作码公开为预定义的函数。在本节中，我们将检查您可以从 Solidity 智能合约中访问的变量和函数。

#### 交易/消息调用上下文

`msg` 对象是启动此合约执行的交易调用(EOA 发起)或消息调用(合约发起)。它包含许多有用的属性：

**msg.sender**

我们已经使用过这个属性。它表示启动此合约调用的地址，不一定是发送交易的原始 EOA。如果我们的合约是由 EOA 交易直接调用的，那么这就是签署交易的地址，否则，它将是一个合约地址。

**msg.value**

随此调用一起发送的以太币值（以 wei 为单位）。

**msg.data**

调用到我们合约的数据有效负载。

**msg.sig**

数据有效负载的前四个字节，即函数选择器。

> **注意**
>
> 每当合约调用另一个合约时，`msg` 的所有属性的值都会更改以反映新调用者的信息。唯一的例外是 `delegatecall` 函数，它在原始 `msg` 上下文中运行另一个合约或库的代码。

#### 交易上下文

`tx` 对象提供了一种访问与交易相关的信息的方法：

**tx.gasprice**

调用交易中的 gas 价格

**tx.origin**

此交易的原始 EOA 的地址

#### 区块上下文

`block` 对象包含有关当前区块的以下信息：

**block.basefee**

当前区块的基本费用，一个动态调整的值，表示包含在区块中的交易所需的最小 gas 费用。

**block.blobbasefee**

与 blob 交易动态调整的基本费用，引入该费用是为了高效地处理大数据，作为以太坊使用 EIP-4844 提高可扩展性的一部分。

**block.chainid**

当前构建区块的区块链的唯一标识符。

**block.prevrandao**

从信标链的前一个区块的随机信标派生的伪随机值。这对于需要随机数的智能合约非常有用——仅适用于非敏感的操作，因为它可以在一定程度上被操纵。

**block.coinbase**

当前区块的费用和区块奖励的接收者的地址。

**block.difficulty**

巴黎（The Merge）之前的 EVM 版本的当前区块的难度 (PoW)。对于采用 PoS 共识模型的后续 EVM 版本，它的行为类似于 `block.prevrandao` 的已弃用别名。

**block.gaslimit**

可以在当前区块中包含的所有交易中花费的最大 gas 量。

**block.number**

当前区块号（区块链高度）。

**block.timestamp**

矿工放置在当前区块中的时间戳（自 Unix epoch 以来的秒数）。

#### 地址对象

任何地址，无论是作为输入传递还是从合约对象强制转换，都具有许多属性和方法。

**address.balance**

以 wei 为单位的地址余额。例如，当前合约余额为 `address(this).balance`。

**address.code**

存储在该地址的合约字节码。对于 EOA 地址，返回一个空字节数组。

**address.codehash**

存储在该地址的合约字节码的 Keccak-256 哈希值。

**address.transfer(amount)**

将金额（以 wei 为单位）转移到此地址，并在任何错误时抛出异常。我们在 `Faucet` 示例中将此函数用作 `msg.sender` 地址上的方法，即 `msg.sender.transfer`。

**address.send(amount)**

类似于 `transfer`，只是它返回 `false` 而不是抛出异常。请务必始终检查 `send` 的返回值。

**address.call(payload)**

低级 `CALL` 函数，可以使用数据有效负载构造任意消息调用。错误时返回 `false`。请注意：接收者可能（意外或恶意地）用完您所有的 gas，导致您的合约因 OOG（gas 不足）异常而停止；始终检查 `call` 的返回值。

**address.delegatecall(payload)**

低级 `DELEGATECALL` 函数，类似于 `address(this).call(...)`，但此合约的代码被 `address` 的代码替换。对于实现代理模式特别有用。错误时返回 `false`。警告：仅限高级使用！

**address.staticcall(payload)**

低级 `STATICCALL` 函数，类似于 `address(this).call(...)`，但在只读模式下，这意味着被调用的函数无法修改任何状态或发送以太币。错误时返回 `false`。

> **注意**
>
> `address.send()` 和 `address.transfer()` 都转发固定数量的 2,300 个 gas 单位，这可能不足以执行回退逻辑。随着 EIP-7702 上线，不鼓励使用它们，而推荐使用更灵活的 `address.call()`。有关更多信息，请参见第9章。

#### 内置函数

其他值得注意的函数是：

**addmod, mulmod**

用于模加法和乘法。例如，`addmod(x,y,k)` 计算 (x + y) % k。

**keccak256, sha256, ripemd160**

使用各种标准哈希算法计算哈希值的函数。

**ecrecover**

从签名中恢复用于签署消息的地址。

**selfdestruct(recipient_address)**

已弃用。用于删除当前合约并将帐户中剩余的所有以太币发送到接收者地址。在 EIP-6780 之后，只有在自毁指令与创建位于同一交易中被调用时，才会发生这种情况。在所有其他情况下，资金将被转移，但合约及其状态不会被清除。

**this**

当前合约，可以显式转换为 `Address` 类型以检索当前执行的合约帐户的地址：`address(this)`。

**super**

在继承层次结构中高一个级别的合约。

**gasleft**

当前执行上下文剩余的 gas 量。

**blockhash(block_number)**

给定区块的哈希值，由其区块号标识；仅适用于最新的 256 个区块。

**blobhash(index)**

与当前交易关联的第 `index` 个 blob 的哈希值。

### 合接口定义与合约的结构完全相同，除了没有定义任何函数——它们只是被声明。这种类型的声明通常被称为*桩*；它告诉你函数的参数和返回类型，而没有任何实现。接口指定了合约的“形状”；当被继承时，接口声明的每个函数都必须由子合约定义。

**library**

库合约是指只部署一次，并被其他合约使用 `delegatecall` 方法（参见“地址对象”）的合约。

### 函数

在合约中，我们定义可以被 EOA 交易或其他合约调用的函数。在我们的 `Faucet` 示例中，我们有两个函数：`withdraw` 和 `receive`。

我们在 Solidity 中声明函数的语法如下：

```solidity
function FunctionName([parameters]) {public|private|internal|external} [virtual|override]
[pure|view|payable] [modifiers] [returns (return types)]
```

让我们看看这些组成部分：

**FunctionName**

函数的名称，用于从 EOA、另一个合约甚至同一个合约中调用该函数。

**parameters**

在名称之后，我们指定必须传递给函数的参数，包括它们的名称和类型。在我们的 `Faucet` 示例中，我们定义了 `uint withdrawAmount` 作为 `withdraw` 函数的唯一参数。

下一组关键字（`public`、`private`、`internal`、`external`）指定了函数的可见性：

**public**

Public 是默认值；此类函数可以被其他合约或 EOA 交易调用，也可以从合约内部调用。在我们的 `Faucet` 示例中，两个函数都被定义为 public。

**private**

Private 函数类似于 internal 函数，但不能被派生合约调用。

**internal**

Internal 函数只能从合约内部访问——它们不能被另一个合约或 EOA 交易调用。它们可以被派生合约（继承该合约的合约）调用。

**external**

External 函数类似于 public 函数，但除非显式地以关键字 `this` 作为前缀，否则无法从合约内部调用。

请记住，术语 *internal* 和 *private* 有些误导性。合约中的任何函数或数据始终在公共区块链上 *可见*，这意味着任何人都可以看到代码或数据。这里描述的关键字只影响函数可以被 *调用* 的方式和时间。

> **注意**
>
> 函数可见性不应与状态变量可见性混淆！它们共享关键字和语义，但它们是两个不同的东西。虽然状态变量可见性是可选的，但函数可见性必须显式定义。

第二组关键字（`pure`、`view`、`payable`）影响函数的行为：

**pure**

`pure` 函数是指既不读取也不写入存储中的任何变量的函数。它只能操作参数和返回数据，而不引用任何存储的数据或区块链状态。`pure` 函数旨在鼓励声明式编程，而没有副作用或状态。

**view**

标记为 `view` 的函数承诺不修改任何状态。编译器不强制执行 `view` 修饰符；它只在可以应用时产生警告。

**payable**

`payable` 函数是可以接受传入付款的函数。未声明为 `payable` 的函数将拒绝传入付款。由于 EVM 中的设计决策，有两个例外：coinbase 付款和 `SELFDESTRUCT` 继承即使在回退函数未声明为 `payable` 的情况下也会被支付，但这很有意义，因为代码执行无论如何也不是这些付款的一部分。

现在让我们探讨两个特殊函数 `receive` 和 `fallback` 的行为：

**receive()**

`receive` 函数允许我们的合约接收以太币。当合约收到一个带有空 calldata 的调用时，它会被触发，通常是在简单的以太币转移过程中（例如使用 `.send()` 或 `.transfer()` 进行的转移）。它被声明为 `receive() external payable { ... }`, 虽然它不能有任何参数或返回值，但它可以是 virtual、可以 override，并且可以有修饰符。

**fallback()**

当使用与任何其他函数签名都不匹配的数据调用合约时，将执行 `fallback` 函数。我们可以使用 `fallback() external [payable]` 或 `fallback(bytes calldata input) external [payable] returns (bytes memory output)` 声明它。如果 `fallback` 函数包含输入参数，它将包含发送到合约的整个数据（相当于 `msg.data`）。与 `receive` 函数类似，`fallback` 函数可以是 payable 和 virtual 的，可以 override，并且可以包含修饰符。如今，它主要用于实现*代理模式*：一种支持智能合约可升级性的设计模式。

> **注意**
>
> 如果合约缺少 `receive` 函数，但有一个 payable 的 `fallback` 函数，则在这种转移过程中将执行 `fallback` 函数。如果合约既没有 `receive` 函数，也没有 payable 的 `fallback` 函数，则它无法接受以太币，并且交易将回退并出现异常。

### 合约构造函数

有一个特殊的函数只使用一次。当创建一个合约时，它也会运行*构造函数*（如果存在），以初始化合约的状态。构造函数与合约创建在同一个交易中运行。构造函数是可选的；你会注意到我们的 `Faucet` 示例没有构造函数。

可以通过 `constructor` 关键字指定构造函数。它看起来像这样：

```solidity
pragma 0.8.26
// SPDX-License-Identifier: GPL-3.0
contract MEContract {
 address owner;
 constructor () { // This is the constructor
  owner = msg.sender;
 }
}
```

合约的生命周期始于来自 EOA 或合约[账户](https://learnblockchain.cn/tags/账户?map=EVM)的创建交易。如果存在构造函数，则它作为合约创建的一部分执行，以初始化正在创建的合约的状态，然后将其丢弃。

> **注意**
>
> 构造函数也可以标记为 payable。如果你想在合约创建交易中一起发送 ETH，这是必要的。如果构造函数不是 payable 的，则在部署期间发送的任何 ETH 都会导致交易回退。

### 函数修饰符

Solidity 提供了一种称为*函数修饰符*的特殊函数类型。通过在函数声明中添加修饰符名称，可以将修饰符应用于函数。修饰符最常用于创建适用于合约中许多函数的条件。在我们的 `destroy` 函数中，我们已经有一个访问控制语句。让我们创建一个表达该条件的函数修饰符：

```solidity
modifier onlyOwner {
 require(msg.sender == owner);
 _;
}
```

这个名为 `onlyOwner` 的函数修饰符为它修改的任何函数设置了一个条件，要求存储为合约 `owner` 的地址与交易的 `msg.sender` 的地址相同。这是访问控制的基本设计模式，只允许合约的所有者执行任何具有 `onlyOwner` 修饰符的函数。

你可能已经注意到我们的函数修饰符中有一个特殊的语法“占位符”：一个下划线后跟一个分号 (`_;`)。这个占位符被被修改的函数的代码替换。本质上，修饰符“包装”了修改后的函数，将其代码放置在由下划线字符标识的位置。

要应用修饰符，请将其名称添加到函数声明中。可以将多个修饰符应用于一个函数；它们按照声明的顺序应用，作为一个逗号分隔的列表。

让我们定义一个 `changeOwner` 函数来使用 `onlyOwner` 修饰符：

```solidity
function changeOwner(address newOwner) public onlyOwner {
 require(newOwner != address(0), "New owner address not set");
 owner = newOwner;
}
```

函数修饰符的名称 (`onlyOwner`) 在关键字 `public` 之后，它告诉我们 `changeOwner` 函数被 `onlyOwner` 修饰符修改。本质上，你可以将其理解为“只有所有者才能设置新的所有者地址。” 实际上，结果代码等效于将 `onlyOwner` 中的代码“包装”到 `changeOwner` 周围。

函数修饰符是一个非常有用的工具，因为它们允许我们编写函数的前提条件并一致地应用它们，从而使代码更易于阅读，因此也更易于进行安全审计。它们最常用于访问控制，但它们非常通用，可以用于各种其他目的。

### 合约继承

Solidity 的 `contract` 对象支持*继承*，这是一种使用附加功能扩展基本合约的机制。要使用继承，请使用关键字 `is` 指定父合约：

```solidity
contract Child is Parent {
 ...
}
```

使用此构造，`Child` 合约继承 `Parent` 的所有方法、功能和变量。Solidity 还支持多重继承，可以通过在关键字 `is` 后面使用逗号分隔的合约名称来指定：

```solidity
contract Child is Parent1, Parent2 {
 ...
}
```

我们可以通过显式指定合约（如 `Parent1.functionName()`）或使用 `super.functionName()`（如果我们想在扁平化的继承层次结构中仅调用高一级别的函数）来调用继承链中更高的函数。

合约继承允许我们编写合约，以实现模块化、可扩展性和重用。我们从简单且实现最通用功能的合约开始，然后通过在更专业的合约中继承这些功能来扩展它们。

在我们的 `Faucet` 合约中，我们引入了对所有者的访问控制，该所有者在构造时被分配。此功能非常通用：许多合约都将具有此功能。我们可以将其定义为通用合约，然后使用继承将其扩展到 `Faucet` 合约。为了丰富示例，让我们将可暂停功能与访问控制功能一起添加。

我们首先定义一个基本合约 `Owned`，它具有一个 `owner` 变量，并在合约的构造函数中设置它：

```solidity
contract Owned {
  address owner;
  // Contract constructor: set owner
  constructor() {
   owner = msg.sender;
  }
  // Access control modifier
  modifier onlyOwner {
   require(msg.sender == owner);
   _;
  }
}
```

接下来，我们定义一个基本合约 `Pausable`，它继承 `Owned`：

```solidity
contract Pausable is Owned {
  bool paused;
  // Status check modifier
  modifier whenNotPaused {
   require(paused == false);
   _;
  }
  // Functions to pause/unpause user operations
  function pause() public onlyOwner {
   paused = true;
  }
  function unpause() public onlyOwner {
   paused = false;
  }
}
```

正如你所看到的，`Pausable` 合约可以使用 `Owned` 中定义的 `onlyOwner` 函数修饰符。它间接使用了 `owner` 地址变量和 `Owned` 中定义的构造函数。继承使每个合约更简单，并专注于其特定功能，从而使我们能够以模块化的方式管理细节。

现在我们可以进一步扩展 `Owned` 合约，在 `Faucet` 中继承其功能：

```solidity
contract Faucet is Pausable {
  // Give out ether to anyone who asks
  function withdraw(uint _withdrawAmount, address payable _to) public whenNotPaused {
   // Limit withdrawal amount
   require(_withdrawAmount <= 0.1 ether);
   // Send the amount to the address that requested it
   _to.transfer(_withdrawAmount);
  }
  // Accept any incoming amount
  receive() external payable {}
}
```

通过继承 `Pausable`，而 `Pausable` 又继承 `Owned`，`Faucet` 合约现在可以使用 `whenNotPaused` 修饰符，其输出可以通过 `Owned` 合约构造函数定义的所有者来控制。该功能与这些函数在 `Faucet` 中时相同，但由于这种模块化架构，我们可以在其他合约中重用函数和修饰符，而无需再次编写它们。代码重用和模块化使我们的代码更简洁、更易于阅读和更易于审计。

有时我们可能需要更改继承合约的某些功能。幸运的是，Solidity 带有适合我们的功能：函数覆盖。声明为 `virtual` 的函数可以被继承链中更高的合约覆盖，从而保持继承方法的高度灵活性。

让我们看一个例子。假设我们想使可暂停功能成为单向的：一旦暂停，合约就不能再取消暂停。为了做到这一点，我们需要将 `Pausable` 合约中的 `unpause` 函数标记为 `virtual`，并在 `Faucet` 合约中使用 `override` 属性重新声明 `unpause` 函数，从而定义新的所需行为，即回退：

```solidity
contract Pausable is Owned {
  bool paused;
  // Status check modifier
  modifier whenNotPaused {
   require(paused == false);
   _;
  }
  // Functions to pause/unpause user operations
  function pause() public virtual onlyOwner {
   paused = true;
  }
  function unpause() public virtual onlyOwner {
   paused = false;
  }
}
contract Faucet is Pausable {
  // Give out ether to anyone who asks
  function withdraw(uint _withdrawAmount, address payable _to) public whenNotPaused {
   // Limit withdrawal amount
   require(_withdrawAmount <= 0.1 ether);
   // Send the amount to the address that requested it
   _to.transfer(_withdrawAmount);
  }
  function unpause() public view override onlyOwner {
   revert("Disabled feature”);
  }
  // Accept any incoming amount
  receive() external payable {}
}
```

正如你所看到的，`Faucet` 中的 `unpause()` 函数必须使用 `override` 关键字声明。在 `Pausable` 合约中，为了保持一致性，我们将 `pause` 和 `unpause` 函数都标记为 virtual，而在我们的例子中，我们只需要更改 `unpause`。

> **注意**
>
> 当我们在 Solidity 中覆盖一个函数时，我们只能使可见性更易于访问——具体来说，我们可以将其从 external 更改为 public，但不能反过来。对于可变性，我们可以收紧它，例如从 nonpayable 移动到 view 或 pure（正如我们对 `unpause` 所做的那样），以及从 view 移动到 pure。但有一个很大的例外：如果一个函数被标记为 payable，它必须保持这种状态——我们不能将其更改为任何其他状态。

### 多重继承

当我们在 Solidity 中使用多重继承时，它依赖于一种称为 C3 线性化算法的东西来确定合约的继承顺序。该算法确保继承顺序是严格且可预测的，这有助于避免循环继承等问题。以最简单的形式，我们可以说它确定了在查找函数时检查基本合约的顺序，并且该顺序从右到左。这意味着右侧的合约被认为是“派生最多的”。例如，在合约声明 `contract C is A, B { }` 中，合约 B 比合约 A 更派生。

现在，除了使用 C3 线性化之外，Solidity 还有额外的保护措施。一个关键规则是，如果多个合约具有相同的函数，我们必须明确声明哪些合约被覆盖。让我们来看一个例子：

```solidity
contract A {
  function foo() public virtual returns(string memory){
   return "A";
  }
}
contract B {
  function foo() public virtual returns(string memory){
   return "B";
  }
}
contract C is A, B {
}
```

乍一看，这看起来应该可以正常工作，因为 C3 线性化应该处理所有事情。但实际上，它不会编译。Solidity 会抛出一个错误，提示：“TypeError: Derived contract must override function `foo`. Two or more base classes define a function with the same name and parameter types.”要解决这个问题，我们需要像这样显式地覆盖来自 A 和 B 的 `foo()` 函数：

```solidity
contract C is A, B {
  function foo() public override(A, B) returns(string memory){
   return "C";
  }
}
```

因此，即使 Solidity 使用 C3 线性化，我们在编码时也无需过多担心它，因为 Solidity 强制我们显式处理函数覆盖。

但是，C3 线性化很重要的地方之一是 Solidity 决定构造函数执行顺序的时候。构造函数遵循 C3 线性化顺序，但有一个奇怪的地方：它们以相反的顺序执行。如果你考虑一下，这是有道理的：派生最多的合约的构造函数应该最后运行，因为它可能会覆盖早期构造函数设置的内容。让我们看一个例子：

```solidity
contract Base{
  uint x;
}
contract Derived1 is Base{
  constructor(){
   x = 1;
  }
}
contract Derived2 is Base{
  constructor(){
   x = 2;
  }
}
contract Derived3 is Derived1, Derived2 {
  uint public y;
  constructor() Derived1() Derived2() {
   y = x;
  }
}
```

在这种情况下，`y` 的值最终将为 2，正如预期的那样，因为 `Derived2` 的构造函数最后运行并将 `x` 设置为 2。

需要记住的重要一点是，你提供构造函数参数的顺序不会影响执行顺序。例如，我们可以像这样翻转构造函数调用：

```solidity
contract Derived3 is Derived1, Derived2 {
  uint public y;
  constructor() Derived2() Derived1() { // we switched the order here
   y = x;
  }
}
```

即使我们更改了构造函数中的顺序，结果仍然相同。 `y` 的值将为 2，因为构造函数执行顺序由 C3 线性化确定，而不是我们调用构造函数的顺序。

最后的提醒：Solidity 使用 C3 线性化进行多重继承可能会使 `super` 关键字的行为方式与你预期的不同。有时，调用 `super` 可能会触发来自同级类的函数，而不是直接父类。这可能会导致一些令人惊讶的结果，即从你甚至没有在继承链中列出的类中调用一个方法。这有点像边缘情况，所以我们不会深入研究它，但在使用具有复杂继承设置的合约中的 `super` 关键字时，一定要记住这一点。

### 错误处理

合约调用可以终止并返回错误。Solidity 中的错误处理由三个函数处理：`assert`、`require` 和 `revert`。

当合约因错误而终止时，所有状态更改（对变量、余额等的更改）都会回退，如果调用了多个合约，则会一直回退到合约调用链的顶部。这确保了事务是*原子*的，这意味着它们要么成功完成，要么对状态没有影响并完全回退。

`assert` 和 `require` 函数以相同的方式运行，评估一个条件，如果条件为假，则停止执行并显示错误。按照惯例，`assert` 用于结果预计为真的情况，这意味着我们使用 `assert` 来测试内部条件。相比之下，`require` 用于测试输入（例如函数参数或事务字段），从而设置我们对这些条件的期望。还值得注意的是，`assert` 在失败时的行为与 `require` 不同：它会消耗所有剩余的 gas。这使得它在被触发时更昂贵，这也是我们通常将其保留给永远不应破坏的不变条件的原因之一。

我们已经在函数修饰符 `onlyOwner` 中使用 `require` 来测试消息发送者是否为合约的所有者：

```solidity
require(msg.sender == owner);
```

`require` 函数充当*门控条件*，阻止执行函数的其余部分，并在不满足条件时产生错误。它还可以包含有用的文本消息，可用于显示错误原因。错误消息记录在事务日志中，并且建议采用它以通过让用户知道错误是什么以及如何修复错误来改善用户体验。因此，我们可以通过在 `require` 函数中添加错误消息来改进我们的代码：

```solidity
require(msg.sender == owner, "Only the contract owner can call this function");
```

`revert` 函数会停止合约的执行并回退任何状态更改。它可以通过两种方式使用：可以直接以不带括号的自定义错误作为语句传递，也可以作为带有括号的函数传递，该函数接受一个字符串参数。自定义错误在 gas 成本方面会便宜得多，而错误字符串和自定义错误都会记录在事务日志中：

```solidity
revert();
revert("Error string");
revert CustomError(arg1, arg2);
```

合约中的某些条件会生成错误，而不管我们是否明确检查它们。例如，在我们的 `Faucet` 合约中，我们不检查是否有足够的以太币来满足提款请求。这是因为如果余额不足以进行转移，`transfer` 函数将失败并显示错误并回退事务：

```solidity
payable(msg.sender).transfer(withdrawAmount);
```

但是，最好明确检查并在失败时提供明确的错误消息。我们可以通过在转移之前添加 `require` 语句来做到这一点：

```solidity
require(this.balance >= withdrawAmount,
 "Insufficient balance in faucet for withdrawal request");
payable(msg.sender).transfer(withdrawAmount);
```

像这样的额外错误检查代码会稍微增加 gas 消耗，但它比省略时提供更好的错误报告。虽然由于以太坊主网上高昂的成本，最大限度地减少 gas 消耗曾经是一项强制性活动，但 EIP-4844 的引入已大大降低了该成本，使得 gas 消耗不再是今天一个紧迫的问题。但是，在 gas 效率和彻底的错误检查之间取得适当的平衡仍然很重要。

Solidity 通过 try/catch 功能为我们提供了对错误处理的更多控制权。这是一个非常方便的功能，允许我们在调用外部合约时更优雅地处理错误。当出现问题时，我们可以捕获错误并决定下一步该怎么做，而不是让我们的整个事务失败并回退。当我们使用 try/catch 时，我们基本上将外部调用包装在 `try` 块中。如果调用成功，则 `try` 块中的代码会像往常一样执行。但是，如果出现问题（例如，被调用的合约耗尽 gas，遇到 `require` 语句或抛出异常），代码将跳转到 `catch` 块，我们可以在其中处理错误。

这是一个简单的例子：

```solidity
function sampleExternalCall(address target, uint amount) public {
  try ITargetContract(target).someFunction(amount) {
   // This runs if the call is successful
   emit Success("Call succeeded!");
  } catch {
   // This runs if the call fails
   emit Error("Call failed!");
  }
}
```

我们可以根据错误的类型以不同的方式捕获错误。基本的 `catch` 块捕获所有错误，但我们也可以捕获特定错误。例如，我们可以使用 `catch Error(string memory reason)` 捕获返回错误字符串的错误，或者我们可以使用 `catch (bytes memory lowLevelData)` 处理不返回数据的低级错误。此外，我们可以使用 `catch Panic(uint errorCode)` 捕获更严重的 panic 错误，例如溢出或除以零。

Try/catch 仅适用于外部调用。它对同一合约中的内部函数调用没有帮助。如果同一合约中的函数失败，它仍会像往常一样回退，我们无法使用 try/catch 捕获该错误。

### 事件

当事务完成时（无论成功与否），它都会生成事务收据。事务收据包含日志条目，这些条目提供有关在事务执行期间发生的动作的信息。*事件* 是 Solidity 高级对象，用于构造这些日志。

事件对于轻客户端和 DApp 服务特别有用，它们可以“监视”特定事件并将其报告给用户界面，或者更改应用程序的状态以反映底层合约中的事件。

事件对象采用参数，这些参数被序列化并记录在区块链的事务日志中。你可以在参数前提供关键字 `indexed`，以使该值成为索引表（哈希表）的一部分，应用程序可以搜索或过滤该表。

#### 添加事件

到目前为止，我们还没有在 `Faucet` 示例中添加任何事件，所以让我们这样做。我们将添加两个事件：一个用于记录任何提款，另一个用于记录任何存款。我们将分别调用这些事件 `Withdrawal` 和 `Deposit`。首先，我们在 `Faucet` 合约中定义事件：

```solidity
contract Faucet is Pausable {
 event Withdrawal(address indexed to, uint amount);
 event Deposit(address indexed from, uint amount);
 [...]
}
```

我们选择使地址成为 `indexed`，以便在构建用于访问我们的 `Faucet` 的任何用户界面中进行搜索和过滤。

接下来，我们使用 `emit` 关键字将事件数据合并到事务日志中：

```solidity
// Give out ether to anyone who asks
function withdraw(uint withdrawAmount) public {
 [...]
 payable(msg.sender).transfer(withdrawAmount);
 emit Withdrawal(msg.sender, withdrawAmount);
}
// Accept any incoming amount
receive() external payable {
 emit Deposit(msg.sender, msg.value);
}
```

生成的 *Faucet.sol* 合约如示例 7-3 所示。

**示例 7-3. Faucet.sol：修订后的 Faucet 合约，带有事件**

```solidity
// Version of Solidity compiler this program was written for
pragma solidity 0.8.26;
// SPDX-License-Identifier: GPL-3.0
contract Owned {
  address owner;
  // Contract constructor: set owner
  constructor() {
   owner = msg.sender;
  }
  // Access control modifier
  modifier onlyOwner {
   require(msg.sender == owner);
   _;
  }
}
contract Pausable is Owned {
  event Paused();
  event Unpaused();
  bool paused;
  // Status check modifier
  modifier whenNotPaused {
   require(paused == false);
   _;
  }
  // Functions to pause/unpause user operations
  function pause() public onlyOwner {
   paused = true;
   emit Paused();
  }
  function unpause() public onlyOwner {
   paused = false;
   emit Unpaused();
  }
}
contract Faucet is Pausable {
  event Withdrawal(address indexed to, uint amount);
  event Deposit(address indexed from, uint amount);
  // Give out ether to anyone who asks
  function withdraw(uint withdrawAmount) public whenNotPaused {
   // Limit withdrawal amount
   require(withdrawAmount <= 0.1 ether);
   // Send the amount to the address that requested it
   payable(msg.sender).transfer(withdrawAmount);
   emit Withdrawal(msg.sender, withdrawAmount);
  }
  // Accept any incoming amount
  receive() external payable {
   emit Deposit(msg.sender, msg.value);
  }
}
```

#### 捕获事件

让我们逐步了解如何使用代码捕获链上事件。具体来说，我们将编写一个脚本来监视以太坊主网上的 USDT 代币转移。为此，我们需要一个 Web3 库，虽然 web3.js 是第一个流行的库，但 [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM) 近年来已经超越了它。作为开发人员，我们更喜欢 [ethers.js](https://learnblockchain.cn/tags/ethers.js?map=EVM)，所以我们将在此处使用它。

首先，让我们设置我们的项目。首先创建一个新的项目文件夹，然后运行以下命令安装 ethers 库：

```bash
npm i ethers
```

接下来，我们需要 USDT 合约的 ABI。你可以从 [Etherscan](https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7#code) 获取它，就在合约源代码下方（参见图 7-1），并将其保存在你的项目文件夹中。

![Etherscan’s USDT ABI section](https://img.learnblockchain.cn/masterethereumbook/images/ch1/maet_0701.png)

**图 7-1.** Etherscan 的 USDT [ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 部分

现在，让我们谈谈我们将如何连接到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)网络。我们需要一个 WebSocket 提供程序，因为我们正在侦听事件，这需要持续连接。你可以在付费提供程序（它们更可靠且更快）或你可以在 [ChainList](https://chainlist.org) 等网站上找到的免费公共提供程序之间进行选择。对于我们的示例，公共提供程序就可以了，即使它们可能受到速率限制。

> **注意**
>
> 要侦听事件，我们需要一个 WebSocket，而不是 RPC 端点。RPC 端点非常适合单个请求，例如调用函数或获取数据，但对于捕获事件，WebSocket 连接允许我们保持客户端和服务器之间的开放通信线路。

现在，让我们深入研究代码：

```javascript
const ethers = require("ethers");
const ABI = require("./USDTabi.json"); // the ABI we fetched from etherscan
const usdtAddress = "0xdac17f958d2ee523a2206206994597c13d831ec7"; // USDT Contract
const wssProviderURL = "wss://ethereum-rpc.publicnode.com"; // a public websocket provider
const wssProvider = new ethers.providers.WebSocketProvider(wssProviderURL);
const usdtContract = new ethers.Contract(usdtAddress, ABI, wssProvider);
async function getTransfer(){
  usdtContract.on("Transfer", (from, to, value, event)=>{
   let transferEvent ={
    from: from,
    to: to,
    value: value,
    eventData: event,
   }
   console.log(JSON.stringify(transferEvent, null, 2))
  })
}
getTransfer()
```

在我们声明 USDT 地址和 WebSocket 提供程序 URL 后，脚本首先使用 ethers 库创建一个新的 WebSocketProvider 实例。此提供程序通过我们指定的 WebSocket URL 将我们连接到[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)网络。接下来，我们使用 ethers.Contract 类创建一个 USDT 智能合约的实例。我们传入 USDT 地址、[ABI](https://learnblockchain.cn/tags/ABI?map=EVM) 和我们的 WebSocket 提供程序。

现在我们进入脚本的核心。我们在合约实例上设置一个事件侦听器，以捕获 USDT 合约发出的 `Transfer` 事件。每当发生 `Transfer` 事件时，此侦听器都会触发一个回调函数，该函数接收四个与转移相关的参数。在回调中，我们获取转移详细信息，将其包装在一个对象中，然后将此对象格式化为 JSON 字符串。最后，我们使用 `console.log` 将该 JSON 字符串打印到控制台，以便我们可以实时查看每次转移的实际情况。

这是我们脚本的示例输出：

```json
{
  "from": "0xc169e35abb35f8e712eCF9F6d9465C96962CA383",
  "to": "0x7E73F680243A93a9D98C5Ce4b349451805fc37ca",
  "value": {
   "type": "BigNumber",
   "hex": "0x55b27b90"
  },
  "eventData": {
   "blockNumber": 20687220,
   "blockHash": "0xa5c3c518d7246e516e076ef8d43c387dcb54d06702e9e059c583ce28a7a271b8",
   "transactionIndex": 166,
   "removed": false,
   "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
   "data": "0x0000000000000000000000000000000000000000000000000000000055b27b90",
   "topics": [
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "0x000000000000000000000000c169e35abb35f8e712ecf9f6d9465c96962ca383",
    "0x0000000000000000000000007e73f680243a93a9d98c5ce4b349451805fc37ca"
   ],
   "transactionHash":
    "0xb527a5a18f10ed9b65dda7a914715a0b0bbfd6db053d8f6b35805ad49a588cfd",
   "logIndex": 300,
   "event": "Transfer",
   "eventSignature": "Transfer(address,address,uint256)",
   "args": [
    "0xc169e35abb35f8e712ecf9f6d9465C96962CA383",
    "0x7E73F680243A93a9D98C5Ce4b349451805fc37ca",
    {
     "type": "BigNumber",
     "hex": "0x55b27b90"
    }
   ]
  }
}
```

像这样的事件非常有用，不仅适用于链下通信，还适用于调试。在开发时，你可以在事务收据中的“日志”条目下找到这些事件，这在事情未按预期运行时可以挽救你的生命。

### 调用其他合约

从你的合约中调用其他合约是一个非常有用但可能危险的操作。我们将检查你可以实现此目的的各种方式，并评估每种方法的风险。简而言之，风险源于你可能不太了解你正在调用的合约或正在调用你的合约这一事实。在编写智能合约时，你必须记住，虽然你可能主要希望与 EOA 打交道，但没有任何东西可以阻止任意复杂且可能恶意的合约调用你的代码和被你的代码调用。

#### 创建新实例

调用另一个合约的最安全方法是如果你自己创建该合约。这样，你就可以确定其接口和行为。为此，你可以像在其他面向对象的语言中一样，只使用关键字 `new` 实例化它。在 Solidity 中，关键字 `new` 将在区块链上创建合约，并返回一个对象，你可以使用该对象来引用它。假设你想从另一个名为 `Token` 的合约中创建并调用一个 `Faucet` 合约：

```solidity
contract Token is Pausable {
  Faucet _faucet;
  constructor() {
   _faucet = new Faucet();
  }
}
```

这种构造合约的机制确保你确切地知道合约的类型及其接口。合约 `Faucet` 必须在 `Token` 的范围内定义，如果定义在另一个文件中，你可以使用 `import` 语句来完成：

```solidity
import "Faucet.sol";
contract Token is Pausable {
  Faucet _faucet;
  constructor() {
   _faucet = new Faucet();
  }
}
```

你可以选择指定创建时以太币转移的值，并将参数传递给新合约的构造函数：
```markdown
import "Faucet.sol";
contract Token is Pausable {
    Faucet _faucet;
    constructor() {
        _faucet = new Faucet{value: 0.5 ether}();
    }
}
```

请注意，这将需要 `Faucet` 构造函数是 payable 的！

然后你也可以调用 `Faucet` 函数。在这个例子中，我们从 `Token` 的 `changeOwner` 函数中调用 `Faucet` 的 `changeOwner` 函数：

```solidity
import "Faucet.sol";
contract Token is Pausable {
    Faucet _faucet;
    constructor() {
         _faucet = new Faucet{value: 0.5 ether}();
    }
    function changeOwner(address newOwner) onlyOwner {
        _faucet.changeOwner(newOwner);
    }
}
```

重要的是要理解，虽然你是 `Token` 合约的拥有者，但 `Token` 合约本身拥有新的 `Faucet` 合约，而不是你！正如我们在本章前面所看到的，在外部调用期间， `msg.sender` 将会改变；在我们的例子中，在 `Faucet` 的执行上下文中，它将会是 `Token` 的地址。

#### 寻址已存在的实例

调用合约的另一种方式是通过强制转换合约的现有实例的地址。通过这种方法，你可以将已知的接口应用于现有的实例。因此，至关重要的是，你要确定你正在寻址的实例实际上是你假设的类型。让我们来看一个例子：

```solidity
import "Faucet.sol";
contract Token is Pausable {
    Faucet _faucet;
    constructor(address _f) {
        _faucet = Faucet(_f);
        _faucet.withdraw(0.1 ether)
    }
}
```

在这里，我们获取一个作为构造函数参数提供的地址 `_f`，并将其强制转换为 `Faucet` 对象。这比前面的机制风险更大，因为我们不能确定该地址实际上是否是一个 `Faucet` 对象。当我们调用 `withdraw` 时，我们假设它接受相同的参数并执行与我们的 `Faucet` 声明相同的代码，但我们不能确定。我们所知道的是，即使名称相同，此地址上的 `withdraw` 函数也可能执行与我们预期的完全不同的操作。因此，使用作为输入传递的地址并将它们强制转换为特定对象比自己创建合约要危险得多。

#### Raw call, delegatecall, 和 staticcall

Solidity 提供了一些更“底层”的函数来调用其他合约。这些函数直接对应于具有相同名称的 EVM 操作码，并允许我们手动构建合约到合约的调用。因此，它们代表了调用其他合约的最灵活 *和* 最危险的机制。它们返回两个值：`bool success`，指示操作是否成功；以及 `bytes memory data`，包含返回数据。

以下是使用 `call` 方法的相同示例：

```solidity
contract Token is Pausable {
    constructor(address _faucet) {
        _faucet.call(abi.encodeWithSignature("withdraw(uint256)", 0.1 ether));
    }
}
```

正如你所看到的，这种类型的 `call` 是一种 *盲* 调用函数的方式，非常像构造一个原始交易，只是从合约的上下文中进行。如果出现问题， `call` 函数将返回 `false`，因此你可以评估返回值以进行错误处理：

```solidity
contract Token2 is Pausable {
    constructor(address _faucet) {
        (bool res, ) = _faucet.call(
            abi.encodeWithSignature("withdraw(uint256)", 0.1 ether)
        );
        if (!res) {
            revert("Withdrawal from faucet failed");
        }
    }
}
```

`call` 的变体是 `staticcall` 和 `delegatecall`。正如在“地址对象”一节中提到的， `staticcall` 以保证没有状态变化的方式在另一个合约上调用一个函数。这意味着被调用的函数不能修改任何状态变量，不能与区块链的状态交互，也不能发送以太币。

`delegatecall` 与 `call` 的不同之处在于 `msg` 上下文不会更改。例如， `call` 会将 `msg.sender` 的值更改为调用合约，而 `delegatecall` 会保持与调用合约中相同的 `msg.sender`。本质上， `delegatecall` 在当前合约的执行上下文中运行另一个合约的代码。它最常用于调用库中的代码。它还允许你利用使用存储在其他地方的库函数的模式，并使该代码与你合约的存储数据一起工作；一个明显的例子是代理模式。应非常谨慎地使用 `delegatecall`。它可能会产生一些意想不到的效果，特别是如果你调用的合约不是作为库设计的。

让我们使用一个示例合约来演示 `call` 和 `delegatecall` 用于调用库和合约的各种调用语义。在示例 7-4 中，我们使用一个事件来记录每次调用的详细信息，并查看调用上下文如何根据调用类型而变化。

**示例 7-4. CallExamples.sol: 不同调用语义的示例**

```solidity
pragma solidity 0.8.26;
contract CalledContract {
    event callEvent(address sender, address origin, address from);
    function calledFunction() public {
        emit callEvent(msg.sender, tx.origin, address(this));
    }
}
library CalledLibrary {
    event callEvent(address sender, address origin, address from);
    function calledFunction() public {
        emit callEvent(msg.sender, tx.origin, address(this));
    }
}
contract Caller {
    function makeCalls(CalledContract _calledContract) public {
        // 直接调用 CalledContract 和 CalledLibrary
        _calledContract.calledFunction();
        CalledLibrary.calledFunction();
        // 使用地址对象的低级别调用 CalledContract
        (bool res, ) = address(_calledContract).
            call(abi.encodeWithSignature("calledFunction()"));
        require(res);
        (res, ) = address(_calledContract).
            delegatecall(abi.encodeWithSignature("calledFunction()"));
        require(res);
    }
}
```

正如你在这个例子中所看到的，我们的主要合约是 `Caller` ，它调用了一个库 `CalledLibrary` 和一个合约 `CalledContract` 。被调用的库和合约都有相同的 `calledFunction` 函数，该函数触发一个事件 `calledEvent` 。事件 `calledEvent` 记录三个数据： `msg.sender` ， `tx.origin` 和 `this` 。每次 `calledFunction` 被调用时，它可能具有不同的执行上下文（对于潜在的所有上下文变量具有不同的值），这取决于它是直接调用还是通过 `delegatecall` 调用。

在 `Caller` 中，我们首先通过在每个合约中调用 `calledFunction` 来直接调用合约和库。然后，我们明确地使用低级别函数 `call` 和 `delegatecall` 来调用 `CalledContract.calledFunction` 。通过这种方式，我们可以看到各种调用机制的行为。

让我们部署合约，运行 `makeCalls` 函数，然后捕获事件。为了清楚起见，我们将用它们的标签替换地址（例如， `CALLER_CONTRACT_ADDRESS` ）。

我们调用了 `makeCalls` 函数并传递了 `CalledContract` 的地址，然后捕获了由每个不同调用触发的四个事件。让我们看一下 `makeCalls` 函数并逐步执行每个步骤。

第一个调用是：

```solidity
_calledContract.calledFunction();
```

在这里，我们使用 `calledFunction` 的高级 ABI 直接调用 `CalledContract.calledFunction` 。触发的事件的参数是：

```json
{
    sender: 'CALLER_CONTRACT_ADDRESS',
    origin: 'EOA_ADDRESS',
    from: 'CALLED_CONTRACT_ADDRESS'
}
```

正如你所看到的， `msg.sender` 是 `Caller` 合约的地址。 `tx.origin` 是我们账户的地址， `web3.eth.accounts[0]` ，它将交易发送到 `Caller` 。该事件由 `CalledContract` 触发，我们可以从事件中的最后一个参数中看到。

`makeCalls` 中的下一个调用是库：

```solidity
CalledLibrary.calledFunction();
```

它看起来与我们调用合约的方式相同，但行为却大相径庭。让我们看一下触发的第二个事件：

```json
{
    sender: 'EOA_ADDRESS',
    origin: 'EOA_ADDRESS',
    from: 'CALLER_CONTRACT_ADDRESS'
}
```

这一次， `msg.sender` 不是 `Caller` 的地址。相反，它是我们账户的地址，并且与交易发起方的地址相同。那是因为当你调用库时，调用始终是 `delegatecall` 并且在调用者的上下文中运行。因此，当 `CalledLibrary` 代码正在运行时，它继承了 `Caller` 的执行上下文，就好像它的代码在 `Caller` 内部运行一样。变量 `this` (在触发的事件中显示为 `from` ) 是 `Caller` 的地址，即使它是从 `CalledLibrary` 内部访问的。

接下来的两个使用低级别 `call` 和 `delegatecall` 的调用验证了我们的期望，触发的事件反映了我们刚刚看到的事件。

## Gas 考虑因素

Gas 在第 14 章中会更详细地描述，它是智能合约编程中一个非常重要的考虑因素。Gas 是一种资源，它限制了以太坊允许交易消耗的最大计算量。如果在计算过程中超过了 gas 限制，则会发生以下一系列事件：

- 抛出“out of gas”异常。
- 执行前的合约状态被恢复（回滚）。
- 用于支付 gas 的所有以太币都作为交易费用被收取；它 *不会* 被退还。

### 最佳实践

由于 gas 由发起交易的用户支付，因此不鼓励用户调用 gas 成本高的函数。因此，尽量减少合约函数中的 gas 成本符合程序员的最佳利益。为此，在构建智能合约时，建议采用某些实践来尽量减少函数调用的 gas 成本：

**避免动态大小的数组**

在动态大小的数组中进行任何循环，其中函数对每个元素执行操作或搜索特定元素都会带来使用过多 gas 的风险。实际上，合约可能在找到期望的结果之前或在对每个元素执行操作之前耗尽 gas，从而浪费时间和以太币而没有给出任何结果。

**避免调用其他合约**

调用其他合约，特别是当其函数的 gas 成本未知时，会带来耗尽 gas 的风险。避免使用未经充分测试和广泛使用的库。其他程序员对库的审查越少，使用它的风险就越大。

**避免冗余存储访问**

访问存储变量（无论是读取还是写入）比使用内存变量花费更多的 gas。因此，只要有可能，最好避免直接使用存储。例如，如果我们需要在某些计算过程中多次读取存储变量，最好首先将其值复制到内存变量中。这样，我们可以重复访问更便宜的内存变量，而无需每次都访问存储，从而节省 gas 成本。

> **注意**
>
> 为了将这一点放在上下文中，Solidity 使用多个地方来保存数据：存储，它是持久且昂贵的；内存，它是临时的且在执行期间更便宜；calldata，它是一个只读区域，主要用于外部函数输入；以及堆栈，它用于非常短时间的值，并且访问成本最低。选择正确的对象取决于数据的使用方式、是否需要持久化、是否可变以及是否从外部传递。我们将在第 14 章中更深入地探讨这些区别，但尽早开始思考它们如何影响性能和成本是有帮助的。

### 估算 Gas 成本

当以太坊首次启动时，估算 gas 成本有点像试图猜测拍卖中的中标价。这类似于比特币处理交易费用的方式：我们将设置自己的 gas 价格，矿工将优先处理出价最高的交易。这意味着在繁忙时段，我们经常需要出价更多，以确保我们的交易能够快速通过。这种方式可行，但也意味着 gas 价格可能会波动很大，有时会在网络拥堵时飙升。

然后在 2021 年，出现了 EIP-1559，它改变了游戏规则。以太坊并没有让我们猜测正确的 gas 价格，而是引入了一个基本费用，该费用会根据网络活动自动调整。这使得 gas 费用更具可预测性。此外，如果我们在赶时间，我们仍然可以添加小费（称为*优先级费用*）来加快速度。现在估算 gas 成本更加简单，我们不太可能仅仅为了让我们的交易得到处理而支付过多的费用。

让我们详细探讨如何估算我们的交易的 gas 成本。首先，每笔交易都有两个主要的 gas 成本组成部分：基本费用和优先级费用：

**基本费用**

这是我们需要支付的最低 gas 金额，以便我们的交易被包含在一个区块中。基本费用由网络自动确定，并根据网络的繁忙程度动态调整。如果区块已满，则基本费用会上涨；如果区块未被充分利用，则会下降。

**优先级费用（小费）**

这是我们添加的额外费用，用于激励矿工（或 PoS 上下文中的验证者）优先处理我们的交易。这就像我们为了更快地处理我们的交易而支付的小费。我们可以自己设置此费用，但钱包应用程序会根据所需的交易包含速度建议适当的值。

现在，我们的交易的总 gas 成本是通过将 gas 使用量（取决于我们交易的复杂性）乘以有效 gas 价格来计算的。有效 gas 价格是基本费用和优先级费用的总和。

因此，要估算我们的 gas 成本，我们按照以下步骤操作：

1. 查看当前的基本费用，我们可以使用 gas 跟踪工具（如 [Etherscan Gas Tracker](https://etherscan.io/gastracker)）或通过 Web3 库（例如， [ethers’`maxFeePerGas()`](https://docs.ethers.org/v6/api/providers/#FeeData-maxFeePerGas)）来查找。
2. 根据我们希望交易的速度选择优先级费用（或小费）。如果我们赶时间，我们可以提高小费。Gas 跟踪工具可以帮助我们根据当前网络状况和我们需要发生事情的速度来确定正确的小费金额。
3. 将总 gas 价格（基本费用 + 小费）乘以估计的 gas 使用量。如果我们是开发人员，我们可以使用 Web3 库（例如， [ethers’`estimateGas()`](https://docs.ethers.org/v6/api/contract/#BaseContractMethod-estimateGas)）来计算此估计的 gas 使用量。但如果我们只是普通用户，则无需担心——任何钱包应用程序都会在我们在发送交易时自动处理此事。

例如，如果基本费用为 20 gwei，我们设置的小费为 2 gwei，并且我们的交易使用 50,000 gas，则我们的估计 gas 成本将为：

(20 gwei + 2 gwei) × 50,000 = 1,100,000 gwei

因此，这是 110 万 gwei，或 0.0011 ETH。

建议您在开发工作流程中评估函数的 gas 成本，以避免在将合约部署到主网时出现任何意外。

## 结论

在本章中，我们开始详细地使用[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)，并探索了 Solidity 合约编程语言。我们采用了一个简单的示例合约 *Faucet.sol*，并逐步改进它并使其更加复杂，使用它来探索 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM) 语言的各个方面。在第 8 章中，我们将使用 [Vyper](https://learnblockchain.cn/tags/Vyper?map=EVM)，另一种面向合约的编程语言。我们将比较 [Vyper](https://learnblockchain.cn/tags/Vyper?map=EVM) 和 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM)，展示这两种语言设计上的一些差异，并加深我们对[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)编程的理解。
