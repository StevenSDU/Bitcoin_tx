# Bitcoin_tx

1、项目思路：

（1）在比特币第三方API大全中，随便找一个第三方API接口，如下图所示：从中选择blockcypher.com比特币api

![image](https://user-images.githubusercontent.com/108848022/182008770-e257af4a-e5c2-43fa-b9d9-ce8034316f76.png)

![image](https://user-images.githubusercontent.com/108848022/182008785-980c220c-2d4f-4a06-8dcc-ef8342841634.png)

（2）在blockcypher.com中，可以看到 api.blockcypher.com作为API接口，因此点开之后发现如下界面：

![image](https://user-images.githubusercontent.com/108848022/182008814-ad76ed3a-0881-4af0-9be1-ef26ad9bb2ca.png)

![image](https://user-images.githubusercontent.com/108848022/182008832-0c7eec71-0426-4038-9e66-d88d738db402.png)

2、部分参数解释：

（1）name：表示该种比特币的名称，这里为BTC.main

（2）height：表示比特币块高度。区块链将一定时期内的交易数据一起存储为一个区块。该块按时间顺序连接到先前和随后的块。因此，区块链从头到尾都连接在一起。考虑到这是垂直堆叠，对块编号，代表高度的单位称为“块高度”。

（3）hash：表示该种比特币的哈希值

（4）time：表示查找该比特币信息时的时间（会随时更新）

（5）previous_hash和previous_url：表示之前（旧版本）的哈希值和对应的url界面

3、代码阐释：

（1）安装requests库。response=requests.get(url)利用get操作访问指定url，其中url即需要查找的API比特币接口。

（2）message表示response中的文本取值，将其写入txt文件中，文件名为bitcoin.txt

4、运行截图：

![image](https://user-images.githubusercontent.com/108848022/182008949-39d1224b-fc4c-499c-950c-1cd0939effb2.png)


