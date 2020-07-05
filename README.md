# Python-Synology-UPS-Shutdown
Synology群晖UPS关机检测脚本


1，上传脚本到NAS任意目录，并对文件右键属性，复制物理路径，如/volume1/web/ping.py


2，控制面板→任务计划→新增→触发的任务，默认为root用户（也必须为root用户）
任务名称随意，用户账号必须为root，设定好之后进入任务设置


3，粘贴刚才的物理路径/volume1/web/ping.py，改为下列脚本

cd /volume1/web/
python ping.py 192.168.1.1 10 10 True



--------------------------参数详解--------------------------

python ping.py 192.168.1.1 10 10 True

第1个参数：192.168.1.1，为被检测的ip地址，可填写光猫或者某台主机的ip地址

第2个参数：10，检测周期（秒），10秒ping一次

第3个参数：10，超时次数（次），当ping超过10次无反应则关机

第4个参数：True或False，是否写出日志，日志名为pinglog_xxxxxxxxxx.txt


其他说明：

如想要终止已运行的检测脚本，请到当前目录下创建文件名为stop或stop.txt，则脚本终止

可在日志中看到exit退出

--------------------------参数详解--------------------------



4，最后把新建的任务打上勾，保存即可

5，最后我们可以提前运行测试下，直接点击运行，可以看到目录下生成了pinglog_xxxxxxxxxx.txt日志，这就成功了

（如果运行失败，则在当前目录出现error文件）




最后可以关闭路由器进行脚本测试^_^ 

也可参考本人博客图文说明

http://www.wx256.com/html/techdoc/27.html

or

http://www.wecent.com.cn/html/techdoc/27.html
