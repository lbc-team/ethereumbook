# 精通以太坊 - 第二版前言

本书是我（Carlo Parisi，又名 Blackie）、Alessandro Mazza 和 Niccolò Pozzolini 共同合作完成的。第一版由 Andreas M. Antonopoulos 和 Gavin Wood 博士于 2016 年至 2019 年间撰写，当然，它对我们的工作产生了重大影响。

2023 年 11 月，一系列非常幸运的巧合将 Andreas 和我在格拉斯哥联系在一起。在那里，在喝了几杯啤酒和签了几个名后，我问他是否有意撰写第二版《精通以太坊》。这是因为，即使第一版是杰作，但它并没有很好地适应时代；它于 2019 年出版，当时以太坊仍在采用工作量证明，并且有着截然不同的路线图。

Andreas 的回答是他没有计划撰写第二版，但我们的谈话最终激发了一个想法，促使我承担了这个项目。在格拉斯哥会面后不到一天，我就在与 O'Reilly 讨论撰写第二版的可能性。

我立刻意识到这将是一项重要而艰巨的任务。虽然我很荣幸能获得这个机会，但也担心自己可能无法胜任。多年来，我一直是 Andreas 作品的粉丝；他是我在 2014 年至 2015 年间能够如此深刻地理解比特币的原因，所以我知道我需要帮助。

我首先想到的人是 Alessandro。他在最初的几个小时内就参与了这个项目。机会一旦变得真实，我就发短信问他是否愿意加入我。他立刻愉快地答应了（甚至不知道任何条件，也不知道是否有报酬）。

说服 Niccolò 稍微难一些。我花了整整一个月的时间才说服他加入。幸运的是，我非常固执，不愿接受拒绝。一个月后，他终于同意了。至此，我们的完整团队已经准备就绪，《精通以太坊：第二版》项目正式启动。

我希望本书的每一位读者都能从中获得至少一点知识。《精通以太坊》这本书教会了我——以及成千上万的其他人——很多东西，我们努力保持同样的质量水平。我们花了两年时间进行研究和写作才完成，如果我说这很容易，那就是在撒谎。

我们也很自豪能成为这个项目中的全意大利团队。希望这也能给意大利加密货币社区带来一些自豪感。

## 如何使用本书

本书既可用作参考手册，也可用作对以太坊的全面探索。前两章提供了一个温和的介绍，适合新手用户，并且这些章节中的示例可以由任何具有一定技术技能的人完成。这两章将使您很好地掌握基础知识，并允许您使用以太坊的基本工具。第 3 章及以后的部分是为程序员准备的，包括许多技术主题和编程示例，但它们在很大程度上仍然应该易于任何人理解。

为了既作为参考手册，又作为关于以太坊的全面叙述，本书不可避免地包含一些重复。有些主题，例如 gas，必须尽早介绍，以便其余主题有意义，但也会在它们自己的部分中进行深入研究。

最后，本书的索引允许读者通过关键字轻松地找到非常具体的主题和相关的部分。

## 目标读者

这本书主要面向所有人。本书将教您[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)区块链如何工作，如何使用它们，以及如何使用它们开发[智能合约](https://learnblockchain.cn/tags/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6)和去中心化应用程序。前几章也适合作为对以太坊的深入介绍，面向初学者。

## 代码示例

这些示例使用 [Solidity](https://learnblockchain.cn/tags/Solidity?map=EVM)、[Vyper](https://learnblockchain.cn/tags/Vyper?map=EVM) 和 [JavaScript](https://learnblockchain.cn/tags/JavaScript) 说明，并使用类似 Unix 的操作系统的命令行。所有代码片段都可以在大多数操作系统上复制，只需最少的编译器、解释器和相应语言的库的安装。在必要时，我们提供基本的安装说明和这些说明输出的逐步示例。

所有代码片段都尽可能使用真实值和计算，因此您可以从一个示例构建到另一个示例，并在您编写的任何代码中看到相同的结果来计算相同的值。例如，私钥以及相应的公钥和地址都是真实的。示例交易、合约、区块和区块链引用都已引入到实际的以太坊区块链中，并且是公共账本的一部分，因此您可以查看它们。

## 本书中的以太坊地址和交易

本书中使用的以太坊地址、交易、密钥、QR 码和区块链数据在很大程度上都是真实的。这意味着您可以浏览区块链，查看作为示例提供的交易，使用您自己的脚本或程序检索它们，等等。

但是，请注意，用于构建本书中打印的地址的私钥已被“烧毁”。这意味着如果您将钱发送到这些地址中的任何一个，这些钱将永远丢失或（更有可能）被盗用，因为任何阅读本书的人都可以使用此处打印的私钥来获取它。

> **警告**
>
> 不要将钱发送到本书中的任何地址。您的钱将被其他读者拿走或永远丢失。

## 本书使用的约定

本书使用以下印刷约定：

*斜体*

表示新术语、URL、电子邮件地址、文件名和文件扩展名。

`等宽字体`

用于程序列表，以及在段落中引用程序元素，例如变量或函数名称、数据库、数据类型、环境变量、语句和关键字。

**`等宽字体粗体`**

显示用户应按字面键入的命令或其他文本。

*`等宽字体斜体`*

显示应替换为用户提供的值或由上下文确定的值的文本。

> **提示**
>
> 此元素表示提示或建议。

> **注意**
>
> 此元素表示一般说明。

> **警告**
>
> 此元素表示警告或注意事项。

## 使用代码示例

为了履行我们对协作的承诺，我们与 O'Reilly Media 合作，以 Creative Commons 许可提供本书。

如果您在使用代码示例时遇到技术问题或问题，请发送电子邮件至 <support@oreilly.com>。

本书旨在帮助您完成工作。通常，如果本书提供了示例代码，您可以在您的程序和文档中使用它。除非您要复制大部分代码，否则无需联系我们获得许可。例如，编写一个使用本书中几个代码块的程序不需要许可。出售或分发 O'Reilly 书籍中的示例需要许可。通过引用本书并引用示例代码来回答问题不需要许可。将本书中的大量示例代码纳入您产品的文档中需要许可。

我们感谢但不通常要求署名。署名通常包括标题、作者、出版商和 ISBN。例如：“*精通以太坊*，第 2 版，Andreas M. Antonopoulos、Gavin Wood、Carlo Parisi、Alessandro Mazza 和 Niccolò Pozzolini（O'Reilly）。版权所有 2026 Carlo Parisi、Alessandro Mazza 和 Niccolò Pozzolini，978-1-098-16842-1。”

如果您觉得您对代码示例的使用超出了合理使用范围或上述许可范围，请随时通过 permissions@oreilly.com 联系我们。

## O'Reilly 在线学习

> **注意**
>
> 40 多年来，O'Reilly Media 一直提供技术和业务培训、知识和见解，以帮助公司取得成功。

我们独特的专家和创新者网络通过书籍、文章和我们的在线学习平台分享他们的知识和专业知识。O'Reilly 的在线学习平台让您可以按需访问实时培训[课程](https://learnblockchain.cn/courses)、深入的学习路径、交互式编码环境，以及来自 O'Reilly 和 200 多家其他出版商的大量文本和视频。有关更多信息，请访问 [oreilly.com](https://oreilly.com)。

## 如何联系我们

请将有关本书的意见和问题发送给出版商：

O'Reilly Media, Inc.

141 Stony Circle, Suite 195

Santa Rosa, CA 95401

800-889-8969（在美国或加拿大）

707-827-7019（国际或本地）

707-829-0104（传真）

<support@oreilly.com>

[oreilly.com/about/contact.html](https://oreilly.com/about/contact.html)

我们有一个关于本书的网页，我们在其中列出勘误表和任何其他信息。您可以通过 [https://www.oreilly.com/library/view/mastering-ethereum-2nd/9781098168414/](https://www.oreilly.com/library/view/mastering-ethereum-2nd/9781098168414/) 访问此页面。

有关我们的书籍和[课程](https://learnblockchain.cn/courses)的新闻和信息，请访问 [https://oreilly.com](https://oreilly.com)。

在 [LinkedIn](https://linkedin.com/company/oreilly-media) 上找到我们

在 [YouTube](https://youtube.com/oreillymedia) 上观看我们

## 联系 Carlo

订阅 Carlo 在 [YouTube](https://www.youtube.com/@BlackieCrypto) 上的频道

在 [Twitter/X](https://x.com/ManInBlackie) 上关注 Carlo

在 [LinkedIn](https://www.linkedin.com/in/carloparisis) 上与 Carlo 联系

电子邮件：<carlo.parisi01234@gmail.com>

## 联系 Alessandro

在 [GitHub](https://github.com/alessandromazza98) 上关注 Alessandro

在 [LinkedIn](https://www.linkedin.com/in/alessandro-mazza-a8b181320) 上与 Alessandro 联系

在 [Twitter/X (意大利语个人资料)](https://x.com/crypto_ita2) 上关注 Alessandro

在 [Twitter/X (英语个人资料)](https://x.com/alemaz98) 上关注 Alessandro

订阅 Alessandro 的 [YouTube 频道](https://www.youtube.com/@alessandro-mazza)

## 联系 Niccolò

在 [Twitter/X](https://x.com/idrocortisone) 上关注 Niccolò

在 [LinkedIn](https://www.linkedin.com/in/niccolo-pozzolini) 上与 Niccolò 联系

## Carlo 的致谢

我的职业生涯和个人生活中的许多成就都归功于 Andreas 的工作。感谢第一版《精通比特币》，早在 2014 年和 2015 年，我就能够真正理解比特币的潜力。正因为如此，我决定从事加密货币事业。当时，没有太多完整的资源可用，《精通[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)》对整个社区来说是一份令人难以置信的礼物。如果没有那项令人难以置信的工作，我今天就不会拥有现在的职业生涯，我的生活可能会大不相同。《精通以太坊》也是如此。因此，Andreas，非常感谢你。

感谢我的高中计算机科学教授 Nicola Luigi Guglielmo Di Nanna。没有你，我可能不会发现我对编程的热情，也可能不会发现我对区块链的热情。人们说一位好教授可以改变学生的生活；你确实做到了。感谢你分享你对计算机科学的热情，并成为如此鼓舞人心的榜样。

还要感谢 Alessandro 和 Niccolò，他们在本书的写作中提供了很多帮助，以及我们所有出色的技术审阅者。

感谢 O'Reilly 的 Michelle Smith 和 Shira Evans，他们一路支持我们。

感谢意大利社区，特别是我在 Discord、YouTube 和 Twitter 上的社区，他们给了我信心来承担这个和许多其他项目。

感谢令人惊叹的[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)社区。如果没有你们持续的支持和贡献，我们就无法进行如此多的研究或写出如此深刻的内容。

最后但并非最不重要的是，感谢我出色的家人，他们支持我所做的一切，并允许我自由地探索我的热情和兴趣。

## Alessandro 的致谢

有很多事情让我心存感激。首先，我要感谢 Carlo 联系我，给了我撰写本书的绝佳机会。我还记得我们第一次在线下见面，在意大利的卡坦扎罗。

感谢我的大学教授 Luca Giuzzi 博士，他允许我将我的论文献给[比特币](https://learnblockchain.cn/tags/比特币?map=BTC)和 Schnorr 数字签名算法。那是我在加密货币领域职业生涯的开始。

衷心感谢我的意大利社区，他们给了我信心，并间接把我带到了今天的位置。如果没有他们的支持，我可能就不会遇到 Carlo。

感谢 O'Reilly，特别是 Shira Evans 和 Michelle Smith，他们在这段旅程中指导我们。他们细致的协调和支持，以及所有审阅者的帮助，使本书成为可能。

最后，我要感谢我的家人和我的女朋友 Alessandra，他们一直支持和爱我。

## Niccolò 的致谢

我要感谢 Carlo 让我有机会与他一起撰写本书。在过去的两年里，我们一起完成了许多项目，一起分享了许多欢笑、出国旅行，现在还有这本书。与你一起工作让这段旅程既有趣又充满回报。

我很感谢 Andreas 和 Gavin 创建了第一版《精通[以太坊](https://learnblockchain.cn/tags/以太坊?map=EVM)》。他们的书让我看到了区块链的世界，并为其他许多人也带来了同样的体验。他们的工作帮助建立和发展了我们今天都是其中一员的这个令人惊叹的区块链社区。

非常感谢 O'Reilly 的 Michelle Smith 和 Shira Evans，感谢你们从头到尾对我们的支持。你们帮助处理了所有的文书工作，让我们按计划进行，并指导我们完成了使本书成为现实的整个过程。

对于我的家人、我的朋友和我的女朋友 Giuditta，我再怎么感谢你们也不为过。在写作的几个月里，你们容忍了我繁忙的日程和压力。当我想讨论想法时，你们倾听着；当因为截止日期而无法参加聚会时，你们理解我；当事情变得艰难时，你们不断鼓励我。你们持续的支持给了我继续前进的力量和专注力。你手中的这本书不仅仅是我的作品；它的存在是因为你们一直以来对我的爱和支持。

## 贡献

我们都想感谢我们的技术审阅者：

- Ben Edgington
- Caleb Lent
- Brian Wu
- Gonçalo Magalhães

他们极大地帮助我们提高了本书的质量。非常感谢我们出色的技术审阅者。
