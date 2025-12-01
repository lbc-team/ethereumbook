# 第12章. 去中心化应用

在这一章中，我们将揭秘 DApp，解释它们是什么，如何工作，以及它们的核心架构是如何构建的。在介绍了基础知识之后，我们将通过一个实践性的例子，从头开始构建你的第一个 DApp。这包括部署必要的智能合约，集成前端，并为近生产环境准备整个堆栈。最后，你将拥有一个可用的 DApp，并且对这些创新应用背后的核心概念有深刻的理解。

## 什么是 DApp？

*DApp* 代表 *去中心化应用*；它与传统的应用程序相比，是一个完全的范式转变，传统的应用程序通常具有以下架构，如图 12-1 所示：

- 应用程序逻辑部分的闭源代码
- 用于存储应用程序数据的中心化数据库
- 允许用户访问应用程序的唯一前端

![传统应用程序的通用架构](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1201.png)

图 12-1. 传统应用程序的通用架构

想想 Instagram、TikTok、你的银行，或者你手机上的任何应用程序。它们可能依赖于非常相似的架构。只有当其背后的团队允许你访问时，你才能访问该应用程序；如果官方网站无法使用，你无法访问其他网站来登录你的 Instagram 账户。

DApp 有两个明确的目标：不要有单点故障，并且即使整个团队消失，人们仍然可以使用该产品。它们的架构可以简化为以下方式，如图 12-2 所示：

- 一些以太坊智能合约构成了 DApp 逻辑部分的基础。大多数情况下，Solidity (或 Vyper) 代码也是开源的。
- 智能合约也可以包含数据，充当适当的数据库，并收集所有必要的用户信息。
- 人们可以通过官方前端访问应用程序，如果主前端由于任何原因无法工作，可以很容易地用替代前端（甚至是由社区制作的）替换。

![DApp 的通用架构](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1202.png)

图 12-2. DApp 的通用架构

> **注意**
>
> DApp 也可以有一些具有一定程度中心化的链下组件，但通常这些组件对于应用程序的核心逻辑来说不是根本的。它们可能有助于在一般情况下加速应用程序，但在最坏的情况下，应该始终可以完全依赖链上数据。这并非总是如此，而且肯定有一些 DApp 的核心逻辑部分依赖于中心化组件。它们不是真正的去中心化应用程序，而更像是传统应用程序和完全去中心化应用程序之间的混合形式。

在接下来的章节中，我们将进一步探讨 DApp 堆栈的每个组件，以更好地理解它们是如何工作的，以及它们如何相互关联和与以太坊协议相关联。

## 后端（智能合约）

在 DApp 中，核心业务逻辑和数据存储被编码到智能合约中，并在以太坊区块链上运行，而不是驻留在中心化服务器上。区块链充当去中心化后端，交易执行、状态更改和记录保存由网络可信地强制执行，而不是由单个实体强制执行。

用户不需要信任任何中心化团队来访问 DApp，因为他们可以期望以太坊网络始终正常工作，处理他们的所有交易并正确更新智能合约的状态，无论白天或黑夜。

此外，这种架构引入了一个非常强大的属性：*抗审查性*。使用传统的应用程序，你经常会看到一个禁止访问该应用程序的国家/地区列表，因为政府法律或其他原因。例如，截至 2025 年，Facebook 在巴西、中国、伊朗、朝鲜、缅甸、俄罗斯、土库曼斯坦和乌干达被禁止。这些国家/地区的人们无法创建个人资料或登录该平台。

对于建立在以太坊上的 DApp，这种类型的审查制度不再能够实现。即使仍然可以禁止特定 DApp 的官方网站，但没有人可以阻止某个地址与链上的一些随机智能合约进行交互。任何人都可以加入并为 DApp 创建一个替代前端，并且每个人都可以使用它再次与 DApp 交互。

### Tornado Cash 传奇

值得在这里提及 Tornado Cash 的故事。Tornado Cash 是一种去中心化的混合服务，它使任何地方的任何人都可以将可追溯或“受污染”的加密货币与其他加密货币混合，通过打破资金的实际发送者和接收者之间的所有联系来掩盖其原始来源。

2022 年 8 月 8 日，美国财政部外国资产控制办公室将 Tornado Cash 列入黑名单，实际上禁止美国公民和公司使用它。该平台被指控洗钱超过 70 亿美元的加密货币。两天后，8 月 10 日，Tornado Cash 的一名开发人员 Alexey Pertsev 在阿姆斯特丹被捕，罪名仅是创建该平台本身。官方 GitHub 存储库被删除，开发人员帐户被暂停。截至 2024 年 12 月，官方网站仍然无法访问。

鉴于所有这些，你可能会认为 Tornado Cash DApp 已停止运营，但这与事实相去甚远。虽然自这些事件以来，该服务受到的关注（和流动性）有所减少，但该协议仍然完全可以运行，并且可以通过各种 IPFS 托管的网关访问。换句话说，世界上任何人仍然可以像以前一样使用 Tornado Cash，即使没有原始的官方网站。

## 数据存储

数据存储是指用于保存用户数据的解决方案。将数据存储和读取到智能合约中是可能的，但这是一项昂贵的操作，并且无法很好地扩展；此外，并非所有内容都需要保存在链上。

通常，智能合约存储关键状态信息并强制执行 DApp 逻辑。诸如帐户余额、所有权记录或计算结果等关键信息直接存储在智能合约中。这确保了敏感的和有价值的数据保持完全透明、防篡改，并且任何拥有以太坊节点的人都可以访问。

所有其他信息都可以保存在不太去中心化的数据存储解决方案中，例如传统的数据库。例如，DApp 开发人员通常使用索引器来快速数据查询，或者使用中心化数据库来存储用户数据，因此前端根本不需要与以太坊链交互。

> **注意**
>
> *区块链索引器* 是一种工具，它允许开发人员以快速有效的方式查询和分析存储在区块链上的数据。它获取事务数据，将其转换为机器和人类可读的数据，并将其加载到数据库中以方便查询。
>
> 实际上，你不能直接在区块链中“搜索”数据。例如，假设你想知道某个帐户在区块 15364050 上持有多少 USDC 代币。你不能直接访问 USDC 智能合约并查找它，因为它不存储历史数据。你可以获取从该区块到现在发生的所有交易，过滤它们，并提取与该帐户相关的所有 USDC 转账信息，然后你最终可以得到你的答案。你可以想象，这不是一个理想的方法。这就是索引器发挥作用的地方。它们维护一个类似数据库的结构，允许你立即运行查询以获取所需的任何信息，包括历史信息，并快速获得答案。

我们的想法是，你只需要在链上存储基本数据和应用程序逻辑，以便任何人都可以验证 DApp 是否正常工作；任何其他内容都可以而且应该留在链下。

### IPFS

*IPFS* 是一种去中心化的、内容寻址的存储系统，它在 P2P 网络中的对等方之间分发存储的对象。*内容寻址* 意味着每个内容（文件）都被散列，并且该散列用于标识该文件。然后，你可以通过按其散列请求任何 IPFS 节点来检索任何文件。

IPFS 旨在取代 HTTP 作为 Web 应用程序交付的首选协议。与将 Web 应用程序存储在单个服务器上不同，这些文件存储在 IPFS 上，并且可以从任何 IPFS 节点检索。阅读 IPFS 文档以了解更多信息。

### Merkle 树

一个有趣且经常使用的解决方案是以 Merkle 树结构将数据保存在链下，并且仅将 Merkle 根存储在链上。这样，你不必将所有数据存储在智能合约中，这会花费你大量的 gas 费，但你仍然能够执行某种链上验证。

> **注意**
>
> 编者注：以下代码示例在非常特定的技术上下文中引用“白名单”。尽管此术语具有成问题的含义，但它也已广泛应用于整个行业及其文档中。虽然我们非常重视包容性，但作者选择在此处保留该术语的现状，以使对技术概念的介绍更加清晰。

最常见的用例是当你创建一个 NFT 集合并且想要将不同的地址列入白名单，以便他们可以在公开销售向所有人开放之前以较低的价格铸造这些 NFT 时。你有两个选项。

第一个是在智能合约中创建一个存储变量，该变量将每个地址映射到一个布尔值，该布尔值对于所有列入白名单的地址都为 true。然后，你可以使用此映射来验证某个地址是否确实已列入白名单。用户在提交 mint 交易时无需提供任何信息；合约只需检查 `msg.sender` 是否包含在白名单映射中，如下所示：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

// import OpenZeppelin contracts.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simplified NFT contract with a whitelist mint function that uses a mapping to 
// store whitelisted addresses.
// 带有使用映射存储在白名单中的地址的白名单 mint 功能的简化 NFT 合约。
contract MyWhitelistNFT is ERC721, Ownable {
    // ... rest of the contract
    // ... 合约的其余部分
    
    // mapping for whitelisted addresses
    // 用于白名单地址的映射
    mapping(address => bool) public isWhitelisted;
    
    /**
     * @notice Whitelist mint function.
     * @notice 白名单 mint 函数。
     */
    function whitelistMint() payable {
        // ... rest of the function
        // ... 函数的其余部分
        
        // check if the user is whitelisted.
        // 检查用户是否在白名单中。
        require(isWhitelisted[msg.sender], "You are not whitelisted");
        
        // mint the NFT.
        // mint NFT
        _safeMint(msg.sender, nextTokenId);
        nextTokenId++;
    }
}
```

第二个是创建一个链下 Merkle 树，并将 Merkle 根存储在链上的合约中。然后，你为每个列入白名单的用户提供其 Merkle 证明。用户将 Merkle 证明提交给合约，合约在链上验证该证明的有效性（通常通过某些库），如下所示：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity 0.8.28;

// import OpenZeppelin contracts.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

// A simplified NFT contract with a whitelist mint function that uses a merkle tree to 
// store whitelisted addresses.
// 带有使用 Merkle 树存储在白名单中的地址的白名单 mint 功能的简化 NFT 合约。
contract MyWhitelistNFT is ERC721, Ownable {
    // ... rest of the contract
    // ... 合约的其余部分
    
    // the merkle root of the off-chain generated Merkle Tree.
    // 链下生成的 Merkle 树的 Merkle 根。
    bytes32 public merkleRoot;
    
    /**
     * @notice Whitelist mint function.
     * @notice 白名单 mint 函数。
     * @dev User must provide a merkle proof to prove they are whitelisted.
     * @dev 用户必须提供 Merkle 证明才能证明他们已列入白名单。
     * @param _merkleProof The proof that msg.sender is whitelisted.
     * @param _merkleProof msg.sender 已列入白名单的证明。
     */
    function whitelistMint(bytes32[] calldata _merkleProof) external payable {
        // ... rest of the function
        // ... 函数的其余部分
        
        // verify that (msg.sender) is in the merkle tree using the provided proof.
        // 使用提供的证明验证 (msg.sender) 是否在 Merkle 树中。
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        bool isValidLeaf = MerkleProof.verify(_merkleProof, merkleRoot, leaf);
        require(isValidLeaf, "Invalid Merkle Proof: Not whitelisted");
               
        // mint the NFT.
        // mint NFT
        _safeMint(msg.sender, nextTokenId);
    }  
}
```

第二种选择比第一种选择便宜得多，也有效得多，特别是对于大型白名单。

> **注意**
>
> 这种方法大大降低了 gas 成本，但也引入了不诚实的白名单创建者的潜在风险，除非树和证明是可审计的。理想情况下，用于生成树的原始列表应该是开源且可访问的，以便任何人都可以验证生成的 Merkle 根的有效性。

## 前端（Web 用户界面）

DApp 的前端是通过使用任何最著名的 Web2 框架创建的，例如 React、Angular 或 Vue。与以太坊链的交互（如果需要）通过 `viem` 或 `ethers.js` 等库进行抽象。

构建 DApp 前端的一种幼稚的方法是仅直接从链中读取数据以更新所有组件。例如，如果你需要显示某个帐户持有的某些代币的余额，你可以查询区块链并获得答案，为每个新区块重复此步骤。

这种幼稚方法的主要问题是你的网站变得非常慢，并且用户与这样的前端进行交互可能会非常令人沮丧。这就是为什么正如我们之前提到的，开发人员经常在其 DApp 架构中使用集中式数据存储组件，从而最大限度地减少与链的交互：它使整个用户体验更好。因此，你通常会得到一个依赖于某些集中式组件的前端，但你始终可以通过在区块链上仔细检查来验证所有信息。最终，如果你不信任官方前端或者根本不喜欢它，你可以为特定的 DApp 创建自己的替代前端。

图 12-3 显示了一个完整的（简化的）DApp 架构。

![完整的 DApp 架构](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1203.png)

图 12-3. 完整的 DApp 架构

## 一个基本的 DApp 示例

到目前为止，我们已经探讨了 DApp 背后的基本概念。现在，是时候卷起袖子，亲自构建一个 DApp 了。

你可以在网上找到许多教程，帮助你从头开始在以太坊上构建你的第一个 DApp，但我们真正推荐 [SpeedRunEthereum](https://oreil.ly/Onygc)。这是快速学习并立即开始构建酷东西的最有效方法。为了增加你构建以太坊上 DApp 的知识，我们建议你完成你可以在 Speed Run Ethereum 上找到的所有挑战，并加入 [BuidlGuidl 社区](https://buidlguidl.com)。

在本节中，我们将构建一个非常基本的去中心化应用程序，一种“Hello World”DApp。你不需要任何先前的经验；你所需要的只是一台电脑和互联网连接。

### 安装要求

要遵循本教程，你需要安装 [node.js](http://node.js) 和 [yarn](https://oreil.ly/dq_hw) 在你的电脑上。有关下载和安装它们，请参阅官方网站。我们将使用 [Scaffold-ETH 2](https://scaffoldeth.io)，这是一个很酷的工具，可以让你非常快速地创建你的开发环境。

### 创建 DApp

让我们打开一个终端并运行以下命令：

```bash
$ npx create-eth@latest
```

它会要求一个项目名称。我们为本次演示选择了“mastering-ethereum”：

```
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
 | Create Scaffold-ETH 2 app | 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+

? Your project name: mastering-ethereum
```

然后，它会询问我们要使用的 Solidity 框架。我们将在这里使用 Hardhat，但你可以随意选择你更熟悉的那个：

```
? What solidity framework do you want to use?
? 你想使用什么 Solidity 框架？
❯ hardhat
   foundry
  none
```

几秒钟后，你应该会看到一个“Congratulations”和一些类似于以下的“Next steps”：

```
  Congratulations! Your project has been scaffolded! 🎉
  恭喜！你的项目已经完成搭建！🎉

  Next steps:
  下一步：

  cd mastering-ethereum
  
        Start the local development node
        启动本地开发节点
  
        yarn chain
  
        In a new terminal window, deploy your contracts
        在一个新的终端窗口中，部署你的合约
  
        yarn deploy
  
    In a new terminal window, start the frontend
    在一个新的终端窗口中，启动前端
  
    yarn start
  
 Thanks for using Scaffold-ETH 2 🙏 , Happy Building!
 感谢你使用 Scaffold-ETH 2 🙏，祝你构建愉快！
```

### 启动链

我们现在已经准备好一切来开始构建我们的 DApp。输入项目文件夹：

```bash
$ cd mastering-ethereum
```

在这里，如果你进入 `packages/hardhat/contracts`，你可以找到一个名为 `YourContract.sol` 的示例智能合约。`contracts` 文件夹是你应该放置你的 DApp 项目所需的所有智能合约的地方。

在 `packages/nextjs` 中，你将找到已经为你的 DApp 前端准备好的 nextjs 框架结构。

由于这是一个非常基本的教程，我们将不从头开始编写任何合约或修改前端。我们将坚持使用默认值来快速展示通常的工作流程。

首先，你需要启动一个链以进行本地开发。实际上，即使最终的产品将使用部署在以太坊主网上的智能合约，你也不应该使用真正的链来构建和测试你的 DApp。这会非常慢，而且会浪费很多钱。Scaffold-ETH 带有一个非常有用的且简单的命令，可以立即启动一个用于本地开发的新链。你只需要运行：

```bash
$ yarn chain
```

### 部署你的合约

现在，你需要将你的合约部署到你在上一步中设置的本地链上。同样，Scaffold-ETH 有一个简单的命令可以做到这一点。打开一个新终端并输入：

```bash
$ yarn deploy
```

你应该看到类似这样的内容：

```
Generating typings for: 2 artifacts in dir: typechain-types for target: ethers-v6
为以下对象生成类型：目录中 2 个 artifact: typechain-types 用于目标：ethers-v6
Successfully generated 6 typings!
成功生成了 6 个类型！
Compiled 2 Solidity files successfully (evm target: paris).
成功编译了 2 个 Solidity 文件(evm target: paris)。
deploying "YourContract" (tx: 0x8ec9ba16869588c2826118a0043f63bc679a4e947f739e8032e911475e77dcb4)...: deployed at 0x5FbDB2315678afecb367f032d93F642f64180aa3 with 532743 gas
正在部署“YourContract”(tx: 0x8ec9ba16869588c2826118a0043f63bc679a4e947f739e8032e911475e77dcb4)...: 部署在 0x5FbDB2315678afecb367f032d93F642f64180aa3，gas 消耗为 532743
👋  Initial greeting: Building Unstoppable Apps!!!
👋 初始问候语：构建不可阻挡的应用程序！！！
📝  Updated TypeScript contract definition file on ../nextjs/contracts/deployedContracts.ts
📝 更新了../nextjs/contracts/deployedContracts.ts上的 TypeScript 合约定义文件
```

正如你所看到的，此命令将名为 `YourContract` 的合约（示例智能合约）部署到本地链上。将来，当你构建新的 DApp 时，你需要转到 `packages/hardhat/deploy` 并更改 `00_deploy_your_contract.ts` 文件，以便你可以部署你实际需要的所有合约。

如果你回到之前运行命令 `yarn chain` 的终端，你应该有一些新的日志，特别是类似于以下的日志：

```
eth_sendTransaction
eth_sendTransaction
  Contract deployment: <UnrecognizedContract>
  合约部署：<未识别的合约>
  Contract address:    0x5fbdb2315678afecb367f032d93f642f64180aa3
  合约地址：0x5fbdb2315678afecb367f032d93f642f64180aa3
  Transaction:         0x8ec9ba16869588c2826118a0043f63bc679a4e947f739e8032e911475e77dcb4
  交易：0x8ec9ba16869588c2826118a0043f63bc679a4e947f739e8032e911475e77dcb4
  From:                0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266
  来自：0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266
  Value:               0 ETH
  值：0 ETH
  Gas used:            532743 of 532743
  Gas 使用：532743 / 532743
  Block #1:            0xa7b8e3b6f82eccb3542279573dbf8efa2b876ff00807a8619feef191007e06d9
  区块#1：0xa7b8e3b6f82eccb3542279573dbf8efa2b876ff00807a8619feef191007e06d9
```

请注意 `Contract deployment` 和 `Contract address` 行。这证明你已将你的合约成功地部署到本地链上的特定合约地址。

### 启动前端

Scaffold-ETH 示例带有一个基本的内置前端，因此你可以立即开始与你的合约进行图形界面方面的交互。打开一个新终端窗口并键入：

```bash
$ yarn start
```

它应该返回类似以下的内容：

```
yarn start
  ▲ Next.js 14.2.21
  - Local:        http://localhost:3000
 
 ✓ Starting...
 ✓ Ready in 1767ms
```

现在复制 localhost URL，打开你的浏览器，然后粘贴链接。你应该会看到前端，如图 12-4 所示。

![Scaffold-ETH 前端](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1204.png)

图 12-4. Scaffold-ETH 前端

### 与你的合约交互

恭喜，你已经准备就绪。你现在可以试验并与你的 DApp 交互。有几个非常有用的功能，你会发现它们对你的开发工作流程至关重要：

- Burner wallets
- Debug Contracts section

正如你在图 12-4 中看到的，在右上角，我们已经通过一个钱包连接到网站，该钱包看起来对我们来说可能随机且不熟悉。这是因为这是一个 *burner wallet*：一个自动生成的地址，其私钥暂时保存在你的 Web 浏览器中。事实上，如果你尝试更新页面，你会注意到你的 burner 地址不会更改。

Burner 钱包是你开发工作流程的一个杀手级功能，因为你无需每次都打开你的 Web3 钱包并将其连接到网站。你仍然可以在准备好后这样做：你只需单击下拉菜单并选择 Disconnect；然后，你可以单击 Connect Wallet 并从列表中选择你喜欢的钱包，如图 12-5、12-6 和 12-7 所示。

![断开 burner 钱包的连接](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1205.png)

图 12-5. 断开 burner 钱包的连接

![Connect Wallet 按钮](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1206.png)

图 12-6. Connect Wallet 按钮

![选择钱包](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1207.png)

图 12-7. 选择钱包

第二个杀手级功能是 Debug Contracts 部分。要打开它，只需单击页面中心的 Debug Contracts 链接。使用默认示例，你现在应该看到类似图 12-8 的内容。

![Debug Contracts 部分](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1208.png)

图 12-8. Debug Contracts 部分

在这里，你可以轻松地与你的所有合约进行交互，而无需在其之上构建任何类型的前端。这在开发过程中非常有用，可以不断检查你的合约是否如你所期望的那样工作。

让我们做一个小演示。首先，我们需要为我们的 burner 钱包充值，以便我们稍后可以发送一些交易来与已部署的合约进行交互。为此，你只需要单击最右边的按钮，如图 12-9 所示。你几乎会立即收到一些 ETH，并且你会看到你的 ETH 余额增加。

![Grab funds 按钮](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1209.png)

图 12-9. Grab funds 按钮

现在转到 `setGreeting` 部分，并在 "_newGreeting" 字段中键入 `hello world`，并在 "payable value" 字段中键入 `0.1`。然后，单击你可以在 "payable value" 字段右侧找到的星号：它会将 ETH 值转换为以 wei 表示的相同金额（1 ETH = 10<sup>18</sup> wei）。最后，你可以单击 Send 发送你的交易，并查看它如何更改你的合约状态。

图 12-10 显示了点击 Send 按钮之前的合约状态。你可以看到你的合约持有 0 ETH，“greeting”是“Building Unstoppable Apps!!!”，premium 为 false，totalCounter 等于 0。

![交易前的合约状态](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1210.png)

图 12-10. 交易前的合约状态

图 12-11 捕获了发送交易后的合约状态。你可以立即看到你的合约现在持有 0.1 ETH，“greeting”是“hello world”，premium 为 true，totalCounter 等于 1。

![交易后的合约状态](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1211.png)

图 12-11. 交易后的合约状态

你可以尝试一下，看看你的合约如何根据你的输入和操作做出反应。

### 部署到 Vercel

当你对你的去中心化应用程序感到满意时，你可以将其发布到生产环境，例如 Vercel。Vercel 是一种非常有用的前端即服务工具，可让你轻松地将你的应用程序部署到互联网。你还可以附加你购买的自定义域名，以便人们只需键入域名即可访问你的 DApp。

Scaffold-ETH 通过提供一个命令来立即将你的 DApp 部署到 Vercel，再次为你提供帮助。打开一个终端并键入：

```bash
$ yarn vercel:yolo
```

你需要链接你的 Vercel 帐户（或者创建一个新的帐户，如果你没有的话），并为你的项目选择一个名称即可。几分钟后，你就可以将整个 DApp 部署到 Vercel，并且世界上任何人都可以尝试一下。

如果你转到你的 Vercel 个人资料，你现在可以看到你新创建的项目。如图 12-12 所示，有一个 Domains 字段，你可以在其中找到 Vercel 为你自动生成的网站域名。

![Vercel 项目页面](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1212.png)

图 12-12. Vercel 项目页面

## 进一步去中心化 DApp

在上一节中，我们将我们的 DApp 部署到 Vercel。虽然 Vercel 是托管 DApp 最流行的解决方案之一，但它不是一种去中心化的服务。所有内容都驻留在其专有服务器上，这意味着 Vercel 可能会根据其策略审查任何用户，并跟踪与你的 DApp 交互的每个人的 IP 地址。

为了进一步去中心化我们的 DApp，我们可以将前端托管在诸如 IPFS 之类的解决方案上，IPFS 是一个全球 P2P 节点网络。一个值得一提的新兴服务是 `eth.limo`，它旨在将主流网站的用户体验（通常通过中心化平台提供）与 IPFS 和类似技术提供的稳健性和去中心化相匹配。

### 去中心化网站

[Eth.limo](https://eth.limo/) 是创建更好的去中心化网站（也称为 *DWebsite*）的缺失环节，这些网站可以像访问经典应用程序一样访问。它基于 ENS 技术，该技术使以太坊地址可以通过 `.eth` 域名对用户友好。以太坊的联合创始人之一 Vitalik Buterin 使用 ENS 将他的钱包地址 `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` 与易于记忆的名称 `vitalik.eth` 链接起来。

ENS 不仅仅是将域名与以太坊地址链接起来：它还可以解析为 IPFS 网站（实际上是内容哈希），例如 `bafybeif3dy…ga4zu`。与 IPFS 网站相关的主要问题是，大多数流行的 Web 浏览器无法正确解析它们并向用户显示它们的内容。这就是 `eth.limo` 发挥作用的地方：它为 ENS 名称和 IPFS 内容运行反向代理。它捕获所有对 `*.eth.limo`（基本上是所有以 `.eth.limo` 结尾的网站）的请求，并自动解析请求的 ENS 记录的 IPFS 内容哈希，并通过 HTTPS 返回相应的静态内容。例如，当你访问 [Vitalik Buterin 的官方博客](https://vitalik.eth.limo) 时，以下是底层发生的事情：

1. Eth.limo 看到传入的对 `vitalik.eth` ENS 域名的请求。
2. 它将其解析为 IPFS 内容哈希（Buterin 先前设置的），其中包含他网站的主页。
3. 它通过 HTTPS 返回相应的静态内容。

这样，世界上任何拥有 Web 浏览器的人都可以轻松访问存储在 IPFS 上的内容，而无需任何配置或设置。

### 局限性

即使 DWebsite 通常（尤其是 `eth.limo`）是一种不断发展的技术，并且发展很快，但在撰写本章时（2025 年 6 月）仍然存在一些局限性。首先，IPFS 只能处理静态文件，因此它无法执行任何类型的服务器端计算。此外，要使用 `eth.limo`，你需要购买一个 ENS 并将其链接到你的前端的 IPFS 内容哈希。并且你必须始终使用 `*.eth.limo` 自定义域名；你不能剪掉 `.limo` 的最后一部分，否则你的 Web 浏览器将无法将你的 ENS 名称解析为你的 DApp 的 IPFS 前端。这可能就是大多数 DApp 不使用 `eth.limo` 的原因。

> **提示**
>
> 虽然大多数 Web 浏览器还不兼容 ENS 和 IPFS，但某些浏览器已开始添加对它们的支持。其中一个例子是 [Brave](https://oreil.ly/LlJT7)。

必须说明的是，`eth.limo` 是另一个潜在的中心化第三方，可能会在没有任何通知的情况下停止工作。如果发生这种情况，你的 DApp 仍然可以通过 IPFS 访问，但 `.eth.limo` URL 不再将用户重定向到它们。

如果你有兴趣并且想深入了解这种构建完全去中心化网站的解决方案，你可以在 [官方网站](https://eth.limo) 上找到更多详细信息。

### 部署到 IPFS

Scaffold-ETH 2 具有另一个简单的命令，可以让你快速将你的 DApp 推送到 IPFS。你只需要打开一个新终端并键入：

```bash
$ yarn ipfs
```

这就完成了！你应该会看到类似以下的内容：

```
   Creating an optimized production build ...
   正在创建优化的生产版本...
 
 ✓ Compiled successfully
 ✓ 验证成功
 ✓ Linting and checking validity of types
 ✓ Linting 和检查类型有效性
    
 ✓ Collecting page data
 ✓ 收集页面数据
    
 ✓ Generating static pages (8/8)
 ✓ 生成静态页面(8/8)
 ✓ Collecting build traces
 ✓ 收集构建过程
    
 ✓ Finalizing page optimization
 ✓ 完成页面优化

…

🚀  Upload complete! Your site is now available at: https://community.bgipfs.com/ipfs/bafybei…
🚀 上传完成！ 你的网站现在可以访问：https://community.bgipfs.com/ipfs/bafybei…
```

如果你访问显示的网站，你应该会看到你的 DApp 在 IPFS 上托管的前端正常工作。“bafy…”字符串是 IPFS 内容哈希。如果你有个人 ENS，并且想将其重定向到此 IPFS 托管的站点，你仍然需要配置 `eth.limo`。

以下是此 `yarn ipfs` 命令幕后实际发生的事情：

1. 构建前端以使静态文件准备好上传到 IPFS。
2. 通过 BuidlGuidl（Scaffold-ETH 2 的维护者）IPFS 社区节点将静态文件上传到 IPFS。
3. 返回一个 URL，该 URL 重定向到静态文件，作为 IPFS 内容的反向代理 (`community.bgipfs.com/<ipfs-content-hash>`)。

请参阅 [BuidlGuidl IPFS](https://www.bgipfs.com)，如果你想了解如何运行你自己的 IPFS 节点并固定一个集群。

## 从 App 到 DApp

在过去的几节中，我们逐步构建了一个去中心化应用程序。我们使用了一个名为 Scaffold-ETH 的工具来促进我们的开发工作流程：我们启动了一个本地链，部署了我们的合约，并启动了一个本地前端，以立即开始与我们的 DApp 进行交互和测试。接下来，我们将 DApp 的前端发布到 Vercel，以展示在生产就绪环境中部署 DApp 是多么简单。最后，我们探讨了如何通过将前端发布到 IPFS 并使用诸如 ENS 和 `eth.limo` 之类的解决方案来进一步去中心化我们的 DApp，从而允许任何人无需安装特殊应用程序即可访问它。

图 12-13 简要概述了创建完全去中心化应用程序所需的工程堆栈。

![DApp 工程堆栈](https://img.learnblockchain.cn/masterethereumbook/images/ch12/maet_1213.png)

图 12-13. DApp 完整工程堆栈的简要概述

## 结论

在本章中，我们探讨了如何使用现代工具从头开始构建一个基本的 DApp，以简化开发工作流程。在下一章中，我们将更仔细地研究以太坊上一些最重要的 DApp（以及 DApp 的类别），它们共同创建了所谓的 DeFi。
