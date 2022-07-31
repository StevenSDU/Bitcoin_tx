import requests

url="https://api.blockcypher.com/v1/btc/main"

#get操作访问指定的url（这里即为有关比特币信息的网站）
response=requests.get(url)
response.encoding="utf-8"
message=response.text

#打开文件bitcoin.txt，将数据写入记事本中
with open("bitcoin.txt","wb") as f:
     f.write(message.encode("utf-8"))
