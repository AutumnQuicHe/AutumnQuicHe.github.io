---
title: "QUIC四层"
anchor: "QUIC_for_Transport_Layer"
weight: 210
rank: "h2"
---

已经定稿的QUIC四层文档共11篇，原文及中译如下：

### RFC8999：《[QUIC版本通用属性（Version-Independent Properties of QUIC）](https://www.rfc-editor.org/rfc/rfc8999.html)》
中译：《[RFC8999中译：QUIC版本通用属性](/RFC8999_Chinese_Translation)》。

RFC8999定下了QUIC协议版本升级及协商所需要遵守的规范，后世所有QUIC版本均须遵守，故译“QUIC版本通用属性”。

### RFC9000：《[QUIC，一种基于UDP的安全多路复用传输协议（QUIC: A UDP-Based Multiplexed and Secure Transport）](https://www.rfc-editor.org/rfc/rfc9000.html)》
中译：《[RFC9000中译：QUIC传输协议](/RFC9000_Chinese_Translation)》

RFC9000详细描绘了QUIC四层可靠传输协议，一般简称为“QUIC传输协议”。同时，由于该文是自QUIC问世以来的发版的第一份RFC正式文档，因此其定义的QUIC协议也称被为“QUIC版本1”。

### RFC9001：《[使用TLS保护QUIC（Using TLS to Secure QUIC）](https://www.rfc-editor.org/rfc/rfc9001.html)》
中译：《[RFC9001中译：QUIC TLS](/RFC9001_Chinese_Translation)》

RFC9001描述了如何使用TLS加密QUIC。

### RFC9002：《[QUIC丢包检测和拥塞控制（QUIC Loss Detection and Congestion Control）](https://www.rfc-editor.org/rfc/rfc9002.html)》
中译：《[RFC9002中译：QUIC恢复](/RFC9002_Chinese_Translation)》

RFC9002描述了QUIC的丢包检测与恢复算法有关内容，其中提出了PTO机制用以取代RTO和TLP机制管理数据包超时重传。

### RFC9221：《[QUIC不可靠数据报文传输扩展（QAn Unreliable Datagram Extension to QUIC）](https://www.rfc-editor.org/rfc/rfc9221.html)》
中译：《[RFC9221中译：QUIC不可靠数据传输](/RFC9221_Chinese_Simplified)》

RFC9221描述了如何使用QUIC进行不可靠数据传输。

### RFC9287：《[QUIC位转义（Greasing the QUIC Bit）](https://www.rfc-editor.org/rfc/rfc9287.html)》
中译：《[RFC9221中译：QUIC位转义](/RFC9287_Chinese_Simplified)》

描述QUIC位转义。

### RFC9308：《[QUIC协议的适用范围（Applicability of the QUIC Transport Protocol）](https://www.rfc-editor.org/rfc/rfc9308.html)》
中译：《[RFC9308中译：QUIC协议的适用范围](/RFC9308_Chinese_Simplified)》

讨论了QUIC的适用性。

### RFC9312：《[QUIC协议的可管理性（Manageability of the QUIC Transport Protocol）](https://www.rfc-editor.org/rfc/rfc9312.html)》
中译：《[RFC9312中译：QUIC协议的可管理性](/RFC9312_Chinese_Simplified)》

讨论了QUIC的可管理性。

### RFC9368：《[QUIC兼容版本协商（Compatible Version Negotiation for QUIC）](https://www.rfc-editor.org/rfc/rfc9368.html)》
中译：《[RFC9368中译：QUIC兼容版本协商](/RFC9368_Chinese_Simplified)》

具体定义了QUIC的版本协商机制，包括双端如何协商出一个兼容版本。

### RFC9369：《[QUIC版本2（QUIC Version 2）](https://www.rfc-editor.org/rfc/rfc9369.html)》
中译：《[RFC9369中译：QUIC版本2](/RFC9369_Chinese_Simplified)》

发布了QUIC版本2。

### RFC9443：《[QUIC的多路复用更新（Multiplexing Scheme Updates for QUIC）](https://www.rfc-editor.org/rfc/rfc9443.html)》
中译：《[RFC9443中译：QUIC多路复用](/RFC9443_Chinese_Simplified)》

描述QUIC针对多路复用进行的更新。
