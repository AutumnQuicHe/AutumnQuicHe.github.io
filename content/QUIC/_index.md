---
title: "QUIC全集"
anchor: "QUIC"
weight: 200
rank: "h1"
---

QUIC是新一代传输协议。

[QUIC工作组（QUIC Work Group, quicwg）](https://quicwg.org/)是QUIC协议撰写小组，其站点详细列出了围绕该协议已发版或正在撰写阶段的全部IETF文档及草稿。目前已经完稿的是QUIC协议涉及四层的部分，总共四篇文档，它们分别是：
- RFC8999：《[QUIC版本通用属性（Version-Independent Properties of QUIC）](https://www.rfc-editor.org/rfc/rfc8999.html)》
- RFC9000：《[QUIC：一种基于UDP的安全多路复用传输协议（QUIC: A UDP-Based Multiplexed and Secure Transport）](https://www.rfc-editor.org/rfc/rfc9000.html)》
- RFC9001：《[使用TLS保护QUIC（Using TLS to Secure QUIC）](https://www.rfc-editor.org/rfc/rfc9001.html)》
- RFC9002：《[QUIC丢包检测和拥塞控制（QUIC Loss Detection and Congestion Control）](https://www.rfc-editor.org/rfc/rfc9002.html)》

这四篇文档囊括了QUIC四层协议的各个方面：版本通用属性（为QUIC后续升级版本制定规范）、可靠传输协议规范、使用TLS进行加密保护，以及可靠传输协议最重要的部分——丢包重传及拥塞控制。这样，一种可以取代TCP的四层可靠传输协议最终问世了。本人优先翻译这四篇已定稿的文档，目前已完成RFC8999的翻译，正在翻译RFC9000，欢迎指正。

而QUIC七层相关文档则尚未定稿，尤其是炙手可热的HTTP相关两篇文稿：[HTTP/3](https://datatracker.ietf.org/doc/html/draft-ietf-quic-http)及[QPack](https://datatracker.ietf.org/doc/html/draft-ietf-quic-qpack)。除了协议栈相关文档外，还有一些杂七杂八的文档也尚未定稿，包括负载均衡设计、版本协商、日志qlog等等，详情还请移步[quicwg站点](https://quicwg.org/)。鉴于此，暂不做相关翻译。