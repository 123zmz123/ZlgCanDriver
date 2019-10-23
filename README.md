# ZlgCanDriver
The zlg can driver writting by python

用来驱动周立功系列的python 库

#python 版本 
python3

# 使用方式
文件夹内保存了 ZLG CAN系列驱动，适用于x64 ，windows系统,建议没有弄熟之前不要进行改动，
代码尾行有展示代码。我已尽量做到抽象。

如下： 
 ```python 
        #新建对象
        c = Communication() 
        #配置CAN卡, 型号：USB_CAN_2EU, CAN卡索引: 0, CAN卡通道：channel_0, 波特率: 500kbps
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        #打开CAN卡'
        c.open_new()
        
        # 发送标准帧 id 为0x110
        data = [1,2,3,4,5,6,7,8]    
        c.Transmit(0x110,data)
        
        # 新建线程，不断读取CAN卡上的报文并且打印出来
        cycle_read_thread = threading.Thread(target=c.PrintReceiveData)
        cycle_read_thread.start()
        
        
 ```      
# enjoy it

# 下一步
- 考虑支持多种帧发送
- 完善动态解析模块
- 完善配置文件




