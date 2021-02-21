# WiFi_auto_changer
windows笔记本电脑自动切换强信号wifi用
————码于醒与睡之间，代码可读性什么的...忘掉吧，有兴趣就大概看看吧。功能实现了就行。。。

有几种使用方法
代码+服务使用方法：
1.配置好python3环境，安装comtypes,pywifi,subprocess两个第三方库
2.nssm中添加服务时输入python路径，参数填代码路径

打包exe+服务使用方法：
1.nssm添加exe可执行文件路径
注意打包exe在win10上运行可能出现问题因为我是在win7旗舰版上打包的~

除此以外，无论是代码还是exe都可以在开机之后手动开启（需要以管理员权限运行）

另附 
nssm添加服务的方法：https://jingyan.baidu.com/article/d2b1d102e0ee6a5c7e37d4b9.html
nssm下载地址：http://www.nssm.cc/download

谢谢使用！
