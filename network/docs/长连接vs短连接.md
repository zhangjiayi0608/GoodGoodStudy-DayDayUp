#### 0.HTTP协议 vs TCP/IP协议
HTTP的长连接、短连接，本质上是TCP的长连接、短连接。
HTTP属于应用层协议，在传输层使用TCP，在网络层使用IP
![image](https://pic4.zhimg.com/80/v2-3edf5e7e8e451f350d578a7ccd7c562b_720w.jpg)
HTTP协议的无状态：对于事务处理没有记忆能力，server不知道client是什么状态；无状态不代表不能保持TCP连接，更不能代表HTTP使用的是UDP

#### 1.HTTP连接 
**在HTTP1.0中，默认使用的是短连接**：
- client每和server进行一次HTTP操作，就建立一次连接，任务结束就中断连接；
- 如果访问的资源中包含其他资源，每遇到一个要访问的资源，就建立一个HTTP会话

**从HTTP1.1起，默认使用的是长连接**：
- 响应头增加代码：`Connection:keep-alive`。
- 当client向server请求连接后，TCP连接不会关闭
- 如果client再次访问该server上的资源，会继续使用已经建立的连接
- keep-alive也不会永久保持连接，会有会话保持时间
- 长连接要求server与client均能支持

#### 2.TCP连接
![image](https://user-gold-cdn.xitu.io/2018/5/20/1637c49f4746b404?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

##### 2.1 TCP短连接
`建立连接——数据传输——关闭连接...建立连接——数据传输——关闭连接
`
1. Client向server发起连接请求
2. server接到请求
3. 双方建立连接（1-3走三次握手）
4. client向server发送消息
5. server回应client
6. 4-5完成一次读写
7. server或client发起close（四次挥手，断开连接，一般为client）

- 短连接一般只在client、server间传递一次读写
- 易于管理、存在即有用
- 请求频繁时资源消耗大
- web网站的http服务一般都是短连接，用以承担亿万级客户访问

##### 2.2 TCP长连接
`建立连接——数据传输...（保持连接）...数据传输——关闭连接`

1-3. 同短连接，建立连接通道
4. 连接保持，不主动关闭——TCP保活
5. client发起断开

- 节省频繁的TCP建立、关闭的资源消耗
- 适用于请求频繁、点对点的客户场景
- 存活功能的探测周期过长，难以避免恶意的连接
- client一般不主动关闭，server容易扛不住：为client设置最大连接数、关闭长时间没有IO的连接
- 一般会有心跳来维护，wireshark抓包可以看到

#### 3.Socket连接
##### 3.1 Socket的定义
- 是支持TCP/IP协议的网络通信的基本操作单元
- 包含网络通信必须的五种信息：协议、本地IP、本地协议端口、远端IP、远端协议端口
- 用于TCP为多个应用进程提供并发服务的情况（如：多个TCP连接/应用程序进程通过同一个TCP协议端口传输数据），区分不同的应用程序进程及连接
- 应用层和传输层通过socket接口，实现数据传输的并发服务

##### 3.2 socket连接
建立socket连接至少需要一对套接字：clientsocket、serversocket，连接过程如下
1. 服务器监听：不定位具体的clientsocket，处于等待连接的状态，实时监控网络状态，等待连接请求
2. 客户端请求：clientsocket主动提出连接请求，连接目标是serversocket。所以，clientsocket需要描述serversocket，指出地址和端口，提出连接请求
3. 连接确认：当serversocket收到连接请求时，响应并建立新线程，把serversocket发送给client，当client确认后，建立连接；此时，serversocke仍处于监听状态，继续接收其他clientsocket的请求
 

##### 3.3 Socket连接和TCP连接的关系
- 当创建socket连接时，可以指定传输层协议（TCP/UDP）
- 如果使用的是TCP协议建立连接，那么该socket连接就是一个TCP连接
- socket是对TCP/IP协议的封装和应用（程序员层面上）,它提供了一组基本的函数接口（比如：create、listen、accept等），使得程序员更方便地使用TCP/IP协议栈
