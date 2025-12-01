# 第 3 章. 以太坊节点

以太坊节点是一个实现以太坊规范并通过 P2P 网络与其他以太坊节点通信的软件应用程序。

最初，一个节点只需要运行一个客户端就可以完全实现成为以太坊生态系统一部分的所有要求。在 2022 年 9 月 15 日，发生了 The Merge 硬分叉，将共识协议从基于 PoW 的方案更改为 Gasper，新的基于 PoS 的共识协议。这也导致了关注点分离——共识和执行——以及一种新型以太坊客户端的创建：共识客户端。

因此，在撰写本文时，一个以太坊节点必须同时运行两个软件才能与最新的规范兼容，如图 3-1 所示，定义如下：

**共识客户端**

这个新软件现在负责共识协议，该协议使所有节点就区块链的单一历史达成一致。

**执行客户端**

该软件专注于接收网络上发生的所有区块和交易，在 EVM 内部执行它们，并验证其正确性。

![图 3-1. 以太坊节点的架构](https://img.learnblockchain.cn/masterethereumbook/./images/ch3/maet_0301.png)

如果不同的以太坊客户端——包括执行客户端和共识客户端——符合参考规范和标准化的通信协议，它们就可以互操作。虽然这些不同的客户端由不同的团队使用不同的编程语言实现，但它们都“说”相同的协议并遵循相同的规则。因此，它们都可以用于操作和与同一个以太坊网络交互。

以太坊是一个开源项目，所有主要客户端的源代码都可以在开源许可（例如，LGPL v3.0）下获得，可以免费下载并用于任何目的。然而，开源不仅仅意味着可以免费使用。它还意味着以太坊由一个开放的志愿者社区开发，并且可以被任何人修改。更多的眼睛意味着更可信的代码。

以太坊最初是由一个名为“黄皮书”的正式规范定义的，该规范由本书的原始合著者之一 Gavin Wood 编写。尽管该规范会随着以太坊的重大更改而定期更新，但对于两种不同的参考实现，即执行客户端和共识客户端，存在一条清晰的路径。这些参考实现是用 Python 编写的，并优先考虑可读性和简洁性。

> **注意**
>
> 这些规范并非旨在成为完整的节点实现。它们用作可执行的伪代码规范。

例如，这与比特币形成对比，比特币没有以任何正式方式定义。比特币的“规范”是参考实现 Bitcoin Core，而以太坊的执行规范记录在一篇结合了英语和数学（正式）规范的论文中。除了各种以太坊改进提案（EIP）和用 Python 编写的新共识规范之外，这个正式规范还定义了以太坊节点的标准行为。

由于以太坊清晰的正式规范，存在许多独立开发但可互操作的以太坊客户端软件实现。以太坊在网络上运行的实现的多样性比任何其他区块链都高，这通常被认为是一件好事。事实上，例如，这已被证明是防御网络攻击的一种绝佳方法，因为利用特定客户端的实现策略只会困扰开发人员，同时他们修补漏洞，而其他客户端几乎不受影响地保持网络运行。

## 以太坊网络

存在各种基于以太坊的网络，它们在很大程度上符合原始以太坊“黄皮书”中定义的正式规范，但可能不会彼此互操作。

几个 EVM 兼容链，如 Ethereum Classic、BNB Chain 和 Polygon，共享执行规范的大部分，尽管许多在共识和参数上有所不同。虽然它们在协议级别上大多兼容，但这些网络通常具有需要以太坊客户端软件的维护者进行少量更改以支持每个网络的功能或属性。因此，并非每个版本的以太坊客户端软件都运行每个基于以太坊的区块链。

截至 2025 年 6 月，以四种不同语言编写的以太坊执行协议有五个主要实现，以及以五种不同语言编写的以太坊共识协议有五个实现：

执行客户端包括：

- Geth，用 Go 编写
- Nethermind，用 C# 编写
- Besu，用 Java 编写
- Erigon，用 Go 编写
- Reth，用 Rust 编写

共识客户端包括：

- Lighthouse，用 Rust 编写
- Lodestar，用 TypeScript 编写
- Nimbus，用 Nim 编写
- Prysm，用 Go 编写
- Teku，用 Java 编写

在本节中，我们将研究以下两个执行客户端：

**Geth**

最古老和使用最广泛的执行客户端，由以太坊基金会维护

**Reth**

一个新的基于 Rust 的执行客户端，由 Paradigm 在 Parity/OpenEthereum 停止后创建

我们将研究以下两个共识客户端：

**Prysm**

第一个共识客户端，现在由 Offchain Labs 维护

**Lighthouse**

最常用的共识客户端，由 Sigma Prime 维护

我们将展示如何使用每个客户端设置节点。具体来说，我们将使用 Geth-Prysm 和 Reth-Lighthouse 组合，并将探索它们的一些命令行选项和 API。

> **注意**
>
> 这些对只是示例；您可以选择组合您最喜欢的任何执行和共识客户端来运行以太坊节点。

## 我应该运行一个完整节点吗？

区块链的健康、弹性和抗审查性取决于它们拥有许多独立运营且地理位置分散的完整节点——也就是说，下载整个区块链并无限期地保留数据的节点。每个完整节点都可以帮助其他新节点获取区块数据以引导其运营，并为运营商提供对所有交易和合约的权威且独立的验证。

> **注意**
>
> 为了真正精确，这些节点之间存在区别：
>
> **归档节点**
>
> 无限期保留所有数据的以太坊节点
>
> **完整节点**
>
> 丢弃历史状态和收据的以太坊节点——通常是您启动节点时的默认选项

然而，运行完整节点会产生硬件资源和带宽成本。一个完整节点必须下载至少 2 TB 的数据（截至 2025 年 6 月，取决于客户端配置）并将其存储在本地硬盘驱动器上。随着新的交易和区块的添加，这种数据负担每天都在迅速增加。我们将在后面的“完整节点的硬件要求”一节中更详细地讨论这个主题。

在实时主网上运行的完整节点对于以太坊开发来说不是必需的。您可以使用测试网节点（将您连接到较小的公共测试区块链之一）、像 Anvil 这样的本地私有区块链或由 Infura 或 Alchemy 等服务提供商托管的节点 API 来完成几乎所有您需要做的事情。

您还可以选择运行远程客户端，该客户端不存储区块链的本地副本或验证区块和交易。这些客户端提供钱包的功能，可以创建和广播交易。远程客户端可用于连接到现有网络，例如您自己的完整节点、公共区块链、公共或许可（权威证明）测试网或本地私有区块链。在实践中，您可能会使用远程客户端，例如 MetaMask、Rabby Wallet 或 Coinbase Wallet，作为在所有不同节点选项之间切换的便捷方式。

术语远程客户端和钱包可以互换使用，尽管存在一些差异。通常，远程客户端除了钱包的交易功能外，还提供 API（例如 web3.js API）。

不要将以太坊中的远程客户端概念与轻客户端（类似于比特币中的简易支付验证 [SPV] 客户端）混淆。轻客户端验证区块头并使用 Merkle 证明来验证交易是否包含在区块链中并确定其影响，从而使其具有与完整节点相似的安全级别。相反，以太坊远程客户端不验证区块头或交易。它们完全信任完整节点，让它们访问区块链，因此失去了重要的安全和匿名性保证。您可以通过使用自己运行的完整节点来缓解这些问题。

### 完整节点的优点和缺点

选择运行完整节点有助于您连接到的网络运行，但也会给您带来一些轻微到中等的成本。让我们看一下其中的一些优点和缺点。

**优点**：

- 支持基于以太坊的网络的弹性和抗审查性
- 权威地验证所有交易
- 可以与公共区块链上的任何合约交互，无需中间人
- 可以将合约直接部署到公共区块链中，无需中间人
- 可以离线查询（只读）区块链状态（帐户、合约等）
- 可以查询区块链，而无需让第三方知道您正在读取的信息

**缺点**：

- 需要大量且不断增长的硬件和带宽资源
- 首次启动时可能需要几天才能完全同步
- 必须维护、升级并保持在线才能保持同步

### 公共测试网的优点和缺点

无论您是否选择运行完整节点，您可能都想运行公共测试网节点。让我们看一下使用公共测试网的一些优点和缺点。

**优点：**

- 测试网节点需要的同步和存储的数据要少得多——根据网络的不同，大约需要 100–300 GB（截至 2025 年 6 月）。
- 测试网节点可以在几个小时内完全同步。
- 部署合约或进行交易需要测试以太币，它没有价值，可以从几个“水龙头”免费获得。
- 测试网是具有许多其他用户和合约的公共区块链，正在“实时”运行。

**缺点：**

- 您不能在测试网上使用“真”钱；它在测试以太币上运行。因此，您无法测试针对真实对手的安全性，因为没有任何风险。
- 公共区块链的某些方面您无法在测试网上进行逼真的测试。例如，交易费用虽然是发送交易所必需的，但在测试网上不是一个考虑因素，因为 gas 是免费的（这意味着测试网 ETH 没有任何实际经济价值）。此外，测试网不像公共主网那样有时会遇到网络拥塞。
- 某些测试网设计用于特定目的，它们可能与以太坊主网slightly不同的。

### 本地区块链模拟的优点和缺点

对于许多测试目的，最好的选择是启动一个单实例私有区块链。Anvil 是您可以运行和交互的最流行的本地区块链模拟之一，无需任何其他参与者。

**优点：**

- 无需同步，磁盘上几乎没有数据；您自己生成第一个区块。
- 无需获取测试以太币；您“奖励”自己可以用于测试的区块奖励。
- 没有其他用户，只有您。
- 没有其他合约，只有在启动后部署的合约。

**缺点：**

- 没有其他用户意味着您的本地链的行为与公共区块链不同。交易空间或交易排序没有竞争。
- 除了您之外没有其他区块生产者意味着区块生产更可预测；因此，您无法测试公共区块链上发生的一些场景。值得一提的是，Anvil（以及像 Hardhat 这样的其他工具）允许您配置区块生产模式以尝试重现类似于主网的行为，但仍然与在以太坊主网上不同。
- 没有其他合约意味着您必须部署所有要测试的内容，包括依赖项和合约库。幸运的是，像 Anvil 这样的工具允许您在任意区块分叉以太坊主网链，并在类似于主网的状态下试验您的智能合约。

## 运行以太坊节点

如果您有时间和资源，您应该尝试运行一个完整节点，即使只是为了更多地了解该过程。在本节中，我们将介绍如何下载、编译和运行以太坊客户端 Geth-Prysm 和 Reth-Lighthouse。这需要一些熟悉在您的操作系统上使用命令行界面 (CLI) 的知识。无论您选择将这些客户端作为完整节点、测试网节点还是本地私有区块链的客户端运行，都值得安装它们。

### 完整节点的硬件要求

在我们开始之前，您应该确保您的计算机具有足够的资源来运行以太坊完整节点。您需要至少 2 TB 的磁盘空间来存储以太坊区块链的完整副本。如果您还想在以太坊测试网上运行完整节点，您将需要至少额外 100–400 GB 的空间。下载 2 TB 的区块链数据可能需要很长时间，因此建议您在快速互联网连接上工作。

同步以太坊区块链非常消耗输入/输出 (I/O)。最好有一个固态驱动器 (SSD)。如果您有机械硬盘驱动器 (HDD)，您将需要至少 8 GB 的 RAM 用作缓存。否则，您可能会发现您的系统速度太慢而无法跟上并完全同步。

以下是同步以太坊区块链完整副本的最低要求摘要：

- 具有 2 个或更多内核的 CPU
- 至少 2 TB 的可用存储空间
- SSD 至少 8 GB RAM，或者如果您有 HDD 则至少 8+ GB（SSD 是强烈推荐的）
- 7+ Mbps 下载互联网服务

如果您想在合理的时间内同步并存储本书中讨论的所有开发工具、库、客户端和区块链，您将需要一台功能更强大的计算机。以下是我们推荐的规格：

- 具有 4+ 个内核的快速 CPU——更高的时钟速度比内核数量更重要
- 16+ GB RAM
- 具有至少 2 TB 可用空间的快速 NVMe SSD
- 24+ Mbps 下载互联网服务

很难预测区块链的大小会增加多快以及何时需要更多磁盘空间，因此建议您在开始同步之前检查区块链的最新大小。

> **注意**
>
> 此处列出的磁盘大小要求假设您将使用默认设置运行节点，其中区块链会“修剪”旧状态数据。如果您改为运行完整的“归档”节点，其中所有状态都保存在磁盘上，则可能需要超过 2 TB（最多 12–15 TB）的磁盘空间，具体取决于客户端。在运行节点之前，请始终查阅官方客户端网站上的最新硬件要求。

### 构建和运行客户端的软件要求

本节介绍 Geth-Prysm 和 Reth-Lighthouse 客户端软件。它还假设您使用的是类似 Unix 的命令行环境。这些示例显示了命令和输出在运行 Bash shell（命令行执行环境）的 macOS 上的外观。这些说明在大多数 Linux 发行版上都保持不变。Windows 用户可以使用适用于 Linux 的 Windows 子系统 (WSL2)。

> **提示**
>
> 在本章的许多示例中，我们将使用操作系统的 CLI（也称为 shell），通过终端应用程序访问。shell 将显示一个提示符；您键入一个命令，shell 会响应一些文本和一个用于您的下一个命令的新提示符。提示符在您的系统上可能看起来不同，但在以下示例中，它由一个 $ 符号表示。在示例中，当您看到 $ 符号后的文本时，不要键入 $ 符号，而是键入紧随其后的命令（以粗体显示），然后按 Enter 键执行该命令。在示例中，每个命令下面的行是操作系统对该命令的响应。当您看到下一个 $ 前缀时，您就会知道这是一个新命令，您应该重复该过程。

在我们开始之前，您可能需要安装一些软件。如果您从未在当前使用的计算机上进行过任何软件开发，您可能需要安装一些基本工具。对于以下示例，您将需要安装 git（源代码管理系统）、golang（Go 编程语言和标准库）和 Rust（一种系统编程语言）。

以下是我们将在本示例中使用的四个客户端的文档页面：

- [Geth](https://geth.ethereum.org/docs)
- [Prysm](https://prysm.offchainlabs.com/docs/)
- [Reth](https://reth.rs/intro.html)
- [Lighthouse](https://lighthouse-book.sigmaprime.io/intro.html)

请随时查阅这些网站以了解有关每个客户端架构的更多详细信息，以及在安装期间进行故障排除。

### 准备阶段

从您的主目录开始，在您的计算机中创建一个名为 *ethereum-node1* 的文件夹，然后在其中创建两个子文件夹，分别名为 *execution* 和 *consensus*：

```bash
$ mkdir ethereum-node1
$ cd ethereum-node1
$ mkdir execution
$ mkdir consensus
```

现在您应该具有如下文件夹结构：

```bash
ethereum-node1
├── consensus
└── execution
```

使用一个名为 *ethereum-node2* 的新文件夹重复上一步：

```bash
$ cd .. # 此命令用于返回您的主目录
$ mkdir ethereum-node2
$ cd ethereum-node2
$ mkdir execution
$ mkdir consensus
```

最后，您应该有两个根文件夹——*ethereum-node1* 和 *ethereum-node2*——每个根文件夹内有两个子文件夹：*execution* 和 *consensus*。

您还需要安装 [Go](https://golang.org/) 和 [Rust](https://www.rust-lang.org/)。您可以查看他们的官方网站，了解如何安装它们的指南。

### Geth-Prysm

进入新创建的文件夹 *ethereum-node1*：

```bash
$ cd ethereum-node1
```

#### Geth

首先，我们将通过从源代码构建 Geth 来安装它。Geth 是 Go 语言实现的执行规范，由以太坊基金会积极开发，因此它被认为是以太坊客户端的“官方”实现。通常，每个基于以太坊的区块链都有自己的 Geth 实现。如果您正在运行 Geth，那么您需要确保使用以下存储库链接之一获取适用于您的区块链的正确版本：

- [Ethereum](https://github.com/ethereum/go-ethereum)
- [BNB Chain](https://github.com/bnb-chain/bsc)
- [Polygon PoS](https://github.com/0xPolygon/bor)

> **注意**
>
> 您可以跳过这些说明并为您选择的平台安装预编译的二进制文件。预编译版本更容易安装，并且可以在此处列出的任何存储库的“releases”部分中找到。但是，您可以通过自己下载和编译软件来了解更多信息。

**克隆存储库**。第一步是克隆 Git 存储库以获取源代码的副本。要制作您选择的存储库的本地副本，请在 execution 子文件夹中使用 git 命令，如下所示：

```bash
$ cd execution
$ git clone https://github.com/ethereum/go-ethereum.git
```

当存储库复制到您的本地系统时，您应该会看到一个进度报告：

```bash
Cloning into 'go-ethereum'...
remote: Enumerating objects: 130745, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 130745 (delta 1), reused 6 (delta 0), pack-reused 130734
Receiving objects: 100% (130745/130745), 204.15 MiB | 6.13 MiB/s, done.
Resolving deltas: 100% (80729/80729), done.
```

太棒了！现在您有了一个 Geth 的本地副本，您可以为您的平台编译一个可执行文件。

**从源代码构建 Geth**。要构建 Geth，请更改为下载源代码的目录，并在选择最新版本后使用 make 命令——现在是 v1.14.3，但您可以随时查看最新版本：

```bash
$ cd go-ethereum
$ git checkout v1.14.3
$ make geth
```

如果一切顺利，您将看到 Go 编译器构建每个组件，直到它生成 Geth 可执行文件：

```bash
go run build/ci.go install ./cmd/geth
go: downloading golang.org/x/crypto v0.22.0
go: downloading golang.org/x/net v0.24.0
[...]
github.com/ethereum/go-ethereum/cmd/utils
github.com/ethereum/go-ethereum/beacon/blsync
github.com/ethereum/go-ethereum/cmd/geth
Done building.
Run "./build/bin/geth" to launch geth.
```

让我们确保 Geth 正常工作，而无需实际启动它：

```bash
$ ./build/bin/geth version

GethVersion: 1.14.3-stable
Git Commit: ab48ba42f4f34873d65fd1737fabac5c680baff6
Architecture: arm64
Go Version: go1.22.2
Operating System: darwin
[...]
```

您的 `geth version` 命令可能会显示略有不同的信息，但您应该看到与此处显示的报告非常相似的版本报告。

暂时不要运行 Geth，因为我们仍然需要安装一个共识客户端，以使以太坊节点同步到链的顶端。

#### Prysm

现在轮到共识客户端了。Prysm 是 Go 语言实现的共识规范，由 Offchain Labs 积极开发。最初，它是 The Merge 之后使用最广泛的共识客户端。现在，由于社区为促进客户端多样性做出的巨大努力，其市场份额已大大降低，为 37%。

**安装二进制文件**。Prysm 可以像我们为 Geth 所做的那样从源代码构建，但这有点复杂。建议的安装方法是以下方法。首先，转到 *consensus* 文件夹：

```bash
$ cd ../.. # 此命令用于返回 ethereum-node1 文件夹
$ cd consensus
```

现在，运行以下命令：

```bash
$ curl https://raw.githubusercontent.com/prysmaticlabs/prysm/master/prysm.sh --output prysm.sh && chmod +x prysm.sh
```

**生成 JWT Secret**。组成以太坊节点的执行客户端和共识客户端是两个不同的软件，但它们始终必须相互交互。为实现这一点，执行客户端和共识客户端都使用一种密码来验证它们的连接。现在我们需要生成它：

```bash
$ ./prysm.sh beacon-chain generate-auth-secret
```

应该会出现一个 *jwt.hex* 文件。让我们将其移动到父文件夹：

```bash
$ mv jwt.hex ../jwt.hex
```

#### 运行节点

现在您有了执行客户端和共识客户端，并且已正确生成 JWT secret，您可以启动客户端并运行以太坊完整节点。

**运行执行客户端**。首先，您需要运行执行客户端 Geth。导航回到 *execution* 文件夹并运行此命令：

```bash
$ cd .. # 此命令用于返回 ethereum-node1 文件夹
$ cd execution
$ ./go-ethereum/build/bin/geth --mainnet \
	--http \
	--http.api eth,net,engine,admin \
	--authrpc.jwtsecret=../jwt.hex
```

如果您看到类似这样的内容，则一切运行正常：

```bash
INFO [06-08|17:56:38.738] Starting Geth on Ethereum mainnet...
INFO [06-08|17:56:38.738] Bumping default cache on mainnet         provided=1024 updated=4096
INFO [06-08|17:56:38.740] Maximum peer count                       ETH=50 total=50
INFO [06-08|17:56:38.745] Set global gas cap                       cap=50,000,000
INFO [06-08|17:56:38.752] Initializing the KZG library             backend=gokzg
INFO [06-08|17:56:38.771] Allocated trie memory caches             clean=614.00MiB dirty=1024.00MiB
INFO [06-08|17:56:38.772] Using pebble as the backing database…
```

**运行共识客户端**。现在您应该运行共识客户端 Prysm。不要关闭执行客户端所在的终端选项卡。只需打开一个新的终端窗口或选项卡并导航到 *consensus* 文件夹：

```bash
$ cd ethereum-node1
$ cd consensus
$ ./prysm.sh beacon-chain \
	--execution-endpoint=http://localhost:8551 \
	--mainnet \
	--jwt-secret=../jwt.hex \
	--checkpoint-sync-url=https://beaconstate.info \
	--genesis-beacon-api-url=https://beaconstate.info
```

您可能会被要求接受 Prysm 的条款和条件。如果是这种情况，请键入 **accept**，您应该就完成了：

```bash
Prysm Terms of Use
By downloading, accessing or using the Prysm implementation (“Prysm”), you (referenced
herein as “you” or the “user”) certify that you have read and agreed to the terms and
conditions below.
TERMS AND CONDITIONS: https://github.com/prysmaticlabs/prysm/blob/develop/TERMS_OF_SERVICE.md
Type “accept” to accept this terms and conditions [accept/decline]: (default: decline):
```

您就完成了！您应该看到执行客户端和共识客户端都开始在终端上记录大量数据。

执行客户端：

```bash
INFO [06-08|18:08:49.039] Forkchoice requested sync to new head    number=20,048,206 hash=8df21a..4afb49 finalized=unknown
INFO [06-08|18:08:52.507] Syncing beacon headers                   downloaded=322,560 left=19,725,577 eta=42m4.183s
INFO [06-08|18:08:57.515] Looking for peers                        peercount=1 tried=42 static=0
INFO [06-08|18:09:00.508] Syncing beacon headers                   downloaded=370,688 left=19,677,449 eta=43m35.827s
INFO [06-08|18:09:01.637] Forkchoice requested sync to new head    number=20,048,207 hash=d99dab..0293c9 finalized=unknown
```

共识客户端：

```bash
[2024-06-08 18:09:24]  INFO blockchain: Called new payload with optimistic block payloadBlockHash=0xd44520a09a7a slot=9253245
[2024-06-08 18:09:24]  INFO blockchain: Called fork choice updated with optimistic block finalizedPayloadBlockHash=0x38916be8a559 headPayloadBlockHash=0xd44520a09a7a headSlot=9253245
[2024-06-08 18:09:24]  INFO blockchain: Synced new block block=0xec930e7c... epoch=289163finalizedEpoch=289161 finalizedRoot=0xb8065a78... slot=9253245
[2024-06-08 18:09:24]  INFO blockchain: Finished applying state transition attestations=123 payloadHash=0xd44520a09a7a slot=9253245 syncBitsCount=510 txCount=212
[2024-06-08 18:09:24]  INFO p2p: Peer summary activePeers=64 inbound=0 outbound=63
[2024-06-08 18:09:28]  INFO sync: Subscribed to topic=/eth2/6a95a1a9/beacon_attestation_35/ssz_snappy[2024-06-08 18:09:36]  INFO blockchain: Called new payload with optimistic block payloadBlockHash=0xff879102f29e slot=9253246
```

现在您有了一个以太坊完整节点，它正在同步到链的顶端。请注意，同步可能需要很长时间（根据您的硬件和互联网连接情况，需要数小时或数天）。

> **注意**
>
> 如果您想了解更多关于我们在此示例中使用的特定命令和 CLI 标志的信息，[Geth](https://geth.ethereum.org/docs) 和 [Prysm](https://prysm.offchainlabs.com/docs/) 的官方文档是最好的查找位置。

### Reth-Lighthouse

让我们做同样的事情，但使用两个不同的客户端：Reth 作为执行客户端，Lighthouse 作为共识客户端。

#### Reth

首先，您需要安装 Reth。进入 *ethereum-node2* 文件夹，然后进入 execution 文件夹。

**克隆存储库**。第一步是克隆 Git 存储库以获取源代码的副本。返回您的主目录并键入以下命令：

```bash
$ cd ethereum-node2
$ cd execution
$ git clone https://github.com/paradigmxyz/reth
```

太棒了！现在您有了一个 Reth 的本地副本，您可以为您的平台编译一个可执行文件。

**Reth 从源代码建设**。要构建 Reth，您需要运行以下命令：

```bash
$ cd reth
$ cargo install --locked --path bin/reth --bin reth
```

完成安装可能需要 10 多分钟。完成后，您可以通过运行以下命令来检查 Reth 是否已正确安装：

```bash
$ reth --version
```

您应该看到类似以下内容（版本可能会更改）：

```bash
reth Version: 0.2.0-beta.6-dev
Commit SHA: ac29b4b73
Build Timestamp: 2024-04-22T17:29:01.000000000Z
Build Features: jemallocBuild Profile: maxperf+
```

#### 灯塔（Lighthouse）

现在您需要安装灯塔（Lighthouse），共识客户端。返回 *ethereum-node2* 文件夹并进入 *consensus* 文件夹：

```bash
$ cd .. # 此命令用于返回 ethereum-node2 文件夹
$ cd consensus
```

您必须先安装一些依赖项。如果您使用的是 macOS，则需要运行：

```bash
$ brew install cmake
```

如果您使用的是其他操作系统，您可以参考 [Lighthouse 官方文档](https://lighthouse-book.sigmaprime.io)。

**克隆仓库**。第一步是克隆 Git 仓库以获取源代码的副本：

```bash
$ git clone https://github.com/sigp/lighthouse.git
```

太棒了！现在您拥有了 Lighthouse 的本地副本，您可以为您的平台编译可执行文件。

**从源代码构建 Lighthouse**。要构建 Lighthouse，您需要运行以下命令：

```bash
$ cd lighthouse
$ git checkout stable
$ make
```

这可能需要 10 多分钟才能完成。

#### 运行节点

同样，您需要先运行执行客户端 Reth。

**运行执行客户端**。导航回到 *execution* 文件夹并运行此命令：

```bash
$ cd ../.. # 此命令用于返回 ethereum-node2 文件夹
$ cp ../ethereum-node1/jwt.hex ./jwt.hex # 我们使用之前生成的相同 jwt.hex 文件
$ cd execution
$ reth node --full --http --http.api all --authrpc.jwtsecret=../jwt.hex
```

如果您看到类似这样的内容，则一切运行正常：

```bash
2024-06-08T16:58:43.498297Z  INFO Starting reth version="0.2.0-beta.6-dev (ac29b4b73)"
2024-06-08T16:58:43.498434Z  INFO Opening database path="/Users/alessandromazza/Library/Application Support/reth/mainnet/db"
2024-06-08T16:58:43.514141Z  INFO Configuration loaded path="/Users/alessandromazza/Library/Application Support/reth/mainnet/reth.toml"
2024-06-08T16:58:43.514778Z  INFO Database opened
2024-06-08T16:58:43.514917Z  INFO Pre-merge hard forks (block based):…
```

**运行共识客户端**。现在您应该运行共识客户端 Lighthouse。不要关闭执行客户端所在的终端选项卡。只需打开一个新的终端窗口或选项卡并导航到 *consensus* 文件夹：

```bash
$ cd ethereum-node2
$ cd consensus
$ lighthouse bn \
	--checkpoint-sync-url https://mainnet.checkpoint.sigp.io \
	--execution-endpoint http://localhost:8551 \
	--execution-jwt ../jwt.hex \
	--genesis-beacon-api-url=https://beaconstate.info
```

您就完成了！您应该看到执行客户端和共识客户端都开始在终端上记录大量数据。

执行客户端：

```bash
2024-06-08T17:03:03.355648Z  INFO Received headers total=10000 from_block=18458372 to_block=18448373
2024-06-08T17:03:04.792262Z  INFO Received headers total=10000 from_block=18448372 to_block=18438373
2024-06-08T17:03:04.800043Z  INFO Received headers total=10000 from_block=18438372 to_block=18428373
2024-06-08T17:03:04.913377Z  INFO Received headers total=10000 from_block=18428372 to_block=18418373
```

共识客户端：

```bash
Jun 08 17:03:24.929 INFO New block received                      root: 0xa49c057026cea3190df38548d49963e271ebdc4d6f93d2301adc4034d6563113, slot: 9253515
Jun 08 17:03:29.001 WARN Head is optimistic                      execution_block_hash: 0x5a14bfcb9e74c5b3a5121f99ef461ae066262200c269b5d11475274eb78aa7a5, info: chain not fully verified, block and attestation production disabled untilexecution engine syncs, service: slot_notifier
Jun 08 17:03:29.001 INFO Synced                                  slot: 9253515, block: 0xa49c…3113, epoch: 289172, finalized_epoch: 289170, finalized_root: 0xca35…2b06, exec_hash: 0x5a14…a7a5 (unverified), peers: 31, service: slot_notifier
```

现在您有了一个以太坊完整节点，它正在同步到链的顶端。请注意，同步可能需要很长时间（根据您的硬件和互联网连接情况，需要数小时或数天）。

> **注意**
>
> 如果您想了解更多关于我们在此示例中使用的特定命令和 CLI 标志的信息，[Reth](https://reth.rs) 和 [L许多基于以太坊的区块链在2016年底遭受了 DoS 攻击。受影响的区块链在进行完整同步时往往会同步缓慢。例如，在以太坊上，一个新的客户端会快速进展，直到达到区块 2,283,397。该区块于2016年9月18日被挖掘出来，标志着 DoS 攻击的开始。从该区块到区块 2,700,031（2016年11月26日），交易的验证变得极其缓慢，内存密集且 I/O 密集。这导致在2016年的当代硬件上，每个区块的验证时间超过一分钟。以太坊实施了一系列升级，使用硬分叉来解决 DoS 攻击中利用的潜在漏洞。这些升级还清理了区块链，通过移除由垃圾邮件交易创建的约2000万个空账户。

如果您正在进行完整验证同步，您的客户端将会变慢，并且可能需要几天，甚至更长时间，才能验证受 DoS 攻击影响的区块。幸运的是，大多数以太坊客户端都包含一个选项，可以执行“快速”同步，跳过交易的完整验证，直到同步到区块链的顶端，然后从链的新顶端恢复完整验证。对于执行客户端，启用快速同步的选项通常是 snap sync。对于共识客户端，快速同步的选项是 checkpoint sync。

在本教程中，我们默认使用快速同步，包括执行客户端上的 snap sync 和共识客户端上的 checkpoint sync，除了 Reth，截至2025年6月，它还不支持 snap sync。

## JSON-RPC 接口

以太坊客户端提供了一个 API 和一组 RPC 命令，这些命令被编码为 JSON。您会看到这被称为 JSON-RPC API。本质上，JSON-RPC API 是一个接口，允许我们编写程序，使用以太坊客户端作为以太坊网络和区块链的网关。

通常，RPC 接口以 HTTP 服务的形式在端口 8545 上提供。出于安全原因，默认情况下，它被限制为仅接受来自 localhost（您自己计算机的 IP 地址，即 127.0.0.1）的连接。

要访问 JSON-RPC API，您可以使用一个专门的库（用您选择的编程语言编写），该库提供与每个可用的 RPC 命令相对应的“桩（stub）”函数调用，或者您可以手动构建 HTTP 请求并发送/接收 JSON 编码的请求。您甚至可以使用像 curl 这样的通用命令行 HTTP 客户端来调用 RPC 接口。让我们尝试一下。首先，确保您已配置并运行了执行客户端。然后，切换到一个新的终端窗口并键入以下命令：

```bash
$ curl -X POST -H "Content-Type: application/json" --data \
	'{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}' \
	http://localhost:8545

{"jsonrpc":"2.0","id":1,"result":"Geth/1.14.3-stable/darwin-arm64/go1.22.2"}
```

在这个例子中，我们使用 curl 来建立与地址 *http://localhost:8545* 的 HTTP 连接。我们已经在运行执行客户端，它在端口 8545 上以 HTTP 服务的形式提供 JSON-RPC API。我们指示 curl 使用 HTTP POST 方法，并将内容标识为 **application/json** 类型。最后，我们将一个 JSON 编码的请求作为 HTTP 请求的数据组件传递。我们的大部分命令行只是设置 curl 以正确地建立 HTTP 连接。有趣的部分是我们发出的实际 JSON-RPC 命令：

```bash
{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}
```

JSON-RPC 请求根据 [JSON-RPC 2.0 规范](https://www.jsonrpc.org/specification) 进行格式化。每个请求包含四个元素：

**jsonrpc**

JSON-RPC 协议的版本。必须完全是 "2.0"。

**method**

要调用的方法的名称。

**params**

一个结构化的值，包含在调用方法期间要使用的参数值。此成员可以省略。

**id**

客户端建立的标识符，如果包含，则必须包含字符串、数字或 NULL 值。如果包含，服务器必须在响应对象中使用相同的值进行回复。此成员用于关联两个对象之间的上下文。

> **提示**
>
> id 参数主要在单个 JSON-RPC 调用中发出多个请求时使用，这种做法称为批处理。批处理用于避免为每个请求都建立新的 HTTP 和 TCP 连接的开销。例如，在以太坊上下文中，如果我们想通过一个 HTTP 连接检索数千个交易，我们将使用批处理。进行批处理时，您为每个请求设置不同的 id，然后将其与来自 JSON-RPC 服务器的每个响应中的 id 匹配。实现此目的的最简单方法是维护一个计数器，并为每个请求递增该值。

我们收到的响应是：

```bash
{"jsonrpc":"2.0","id":1,"result":"Geth/1.14.3-stable/darwin-arm64/go1.22.2"}
```

这告诉我们 JSON-RPC API 由 Geth 客户端版本 1.14.3-stable 提供服务。

让我们尝试一些更有趣的事情。在下一个示例中，我们要求 JSON-RPC API 提供当前 gas 的 wei 价格：

```bash
$ curl -X POST -H "Content-Type: application/json" --data \
	'{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":4213}' \
	http://localhost:8545
	
{"jsonrpc":"2.0","id":4213,"result":"0x1B1717FC7"}
```

响应 0x1B1717FC7 告诉我们当前的 gas 价格是 7.27 gwei（gigawei 或十亿 wei）。如果像我们一样，您不擅长十六进制，您可以使用一点 Bash-fu 在命令行上将其转换为十进制：

```bash
$ echo $((0x1B1717FC7))7271972807
```

完整的 JSON-RPC API 可以在 [Ethereum wiki](https://ethereum.org/developers/docs/apis/json-rpc/) 上进行研究。

> **提示**
>
> 在本节中，我们使用原始 curl 请求来展示以太坊 JSON-RPC 接口。在现实生活中，您可能希望通过更好、更程序化的方式来访问它。这就是库发挥作用的地方。请随意探索以下三个最著名和最常用的库：
>
> - [ethers.js](https://github.com/ethers-io/ethers.js)
>
> - [web3.py](https://github.com/ethereum/web3.py)
>
> - [alloy](https://alloy.rs)

## 远程以太坊客户端

远程客户端提供完整客户端功能的子集。它们不存储完整的以太坊区块链，因此设置速度更快，并且需要的数据存储量也少得多。

这些客户端通常提供以下一种或多种能力：

- 在钱包中管理私钥和以太坊地址
- 创建、签名和广播交易
- 使用数据有效载荷与智能合约交互
- 浏览并与 DApp 交互
- 提供指向外部服务的链接，例如区块浏览器
- 转换以太币单位并从外部来源检索汇率
- 将 Web3 实例作为 JavaScript 对象注入到 Web 浏览器中
- 使用由另一个客户端提供或注入到浏览器中的 Web3 实例
- 访问本地或远程以太坊节点上的 RPC 服务

远程客户端通常提供完整节点以太坊客户端的某些功能，而无需同步以太坊区块链的本地副本，而是连接到在其他地方运行的完整节点——例如，由您本地在您的机器上或在 Web 服务器上，或由第三方在其服务器上运行。

让我们看一下一些最流行的远程客户端及其提供的功能。

### 移动（智能手机）钱包

大多数生产移动钱包都作为远程客户端运行，因为智能手机没有足够的资源来运行完整的以太坊客户端。轻客户端正在开发中，并且尚未普遍用于以太坊。最著名的是 [Helios](https://github.com/a16z/helios),，它仍然是实验性软件。

流行的移动钱包包括以下几种（我们仅将这些列为示例；这不是对这些钱包的认可，也不是对这些钱包的安全或功能的指示）：

**Coinbase Wallet**

一款移动钱包，支持多种不同的链，例如以太坊（以及所有 L2）、与 EVM 兼容的 L1、比特币、Solana、莱特币和狗狗币。它还可以连接到 Coinbase 帐户。

**Phantom**

Phantom 是另一个多链钱包，与以太坊、Solana、比特币和 Polygon 兼容。

**Trust Wallet**

一款移动多链钱包，支持一百多个区块链。Trust Wallet 适用于 iOS 和 Android。

**Uniswap Wallet**

一款移动钱包，仅支持以太坊和与 EVM 兼容的 L2 和 L1。它由 Uniswap 团队制作。它非常新，适用于 iOS 和 Android。

### 浏览器钱包

各种钱包和 DApp 浏览器可以作为 Chrome 和 Firefox 等 Web 浏览器的插件或扩展程序使用。这些是在您的浏览器中运行的远程客户端。一些比较流行的包括：

**MetaMask**

// TODO: 在此处添加第2章参考链接
[MetaMask](https://metamask.io)，在[第2章](add-link)中介绍，是一个多功能的基于浏览器的钱包、RPC 客户端和基本合约浏览器。它可在 Chrome、Firefox、Opera 和 Brave 浏览器上使用。

**Phantom**

Phantom 也有一个 Web 浏览器钱包，它具有非常漂亮和简洁的 UI。

**Rabby Wallet**

Rabby 是一款新的多链 Web 浏览器钱包，支持一百多个不同的区块链（与 EVM 兼容的链）。

**Coinbase Wallet**

Coinbase Wallet 也有 Web 浏览器钱包。它具有与移动版本相同的功能。

### 硬件钱包

大多数移动和浏览器钱包都可以与更高安全性的硬件钱包结合使用：离线设备旨在永不连接到互联网，并且旨在抵抗篡改和其他形式的物理攻击，从而提供更高级别的安全性。几家公司正在构建此类设备，但两种最广泛使用的是 Ledger 和 Trezor。

## 结论

在本章中，我们探讨了以太坊客户端。您下载、安装并同步了一个客户端，从而成为以太坊网络的参与者，并通过在您自己的计算机上复制区块链来为系统的健康和稳定做出贡献。

将来，由于围绕以太坊的研究和开发非常庞大，因此将提供新型的以太坊客户端。有趣的领域包括：

**历史修剪**

修剪历史数据以降低完整节点的存储需求

**Verkle 树和无状态性**

能够验证一个区块而无需拥有完整的以太坊状态

**zk-EVM**

通过验证零知识证明来验证区块的正确性，而无需重新执行区块中的所有交易

我们将在以下章节中探讨这些概念，但首先，我们需要揭示使这一切成为可能的真正魔力：密码学。
