---
title: "QUIC四层"
anchor: "QUIC_for_Transport_Layer"
weight: 210
rank: "h2"
---

已经定稿的QUIC四层文档共5篇，原文及中译如下：

### RFC8999：《[QUIC版本通用属性（Version-Independent Properties of QUIC）](https://www.rfc-editor.org/rfc/rfc8999.html)》
中译：《[RFC8999中译：QUIC版本通用属性](/RFC8999_Chinese_Translation)》。

RFC8999定下了QUIC协议版本升级及协商所需要遵守的规范，后世所有QUIC版本均须遵守，故译“QUIC版本通用属性”。

### RFC9000：《[QUIC，一种基于UDP的安全多路复用传输协议（QUIC: A UDP-Based Multiplexed and Secure Transport）](https://www.rfc-editor.org/rfc/rfc9000.html)》
中译：《[RFC9000中译：QUIC传输协议](/RFC9000_Chinese_Translation)》

RFC9000详细描绘了QUIC四层可靠传输协议，一般简称为“QUIC传输协议”。同时，由于该文是自QUIC问世以来的发版的第一份RFC正式文档，因此其定义的QUIC协议也称被为“QUIC第1版”。

### RFC9001：《[使用TLS保护QUIC（Using TLS to Secure QUIC）](https://www.rfc-editor.org/rfc/rfc9001.html)》
中译：《[RFC9001中译：QUIC TLS](/RFC9001_Chinese_Translation)》

RFC9001描述了如何使用TLS加密QUIC。

### RFC9002：《[QUIC丢包检测和拥塞控制（QUIC Loss Detection and Congestion Control）](https://www.rfc-editor.org/rfc/rfc9002.html)》
中译：《[RFC9002中译：QUIC恢复](/RFC9002_Chinese_Translation)》

RFC9002描述了QUIC的丢包检测与恢复算法有关内容，其中提出了PTO机制用以取代RTO和TLP机制管理数据包超时重传。

### RFC9221：《[QUIC不可靠数据报文传输扩展（QUIC Loss Detection and Congestion Control）](https://www.rfc-editor.org/rfc/rfc9221.html)》
中译：《[RFC9221中译：QUIC不可靠数据传输](/RFC9221_Chinese_Simplified)》

RFC9221描述了如何使用QUIC进行不可靠数据传输。
