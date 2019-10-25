# ZlgCanDriver
The zlg can driver writting by python

用来驱动周立功系列的python 库

#python 版本 
python3

# 使用方式
文件夹内保存了 ZLG CAN系列驱动，适用于x64 ，windows系统,建议没有弄熟之前不要进行改动，
代码尾行有展示代码。我已尽量做到抽象。

基本使用如下
 ```python 
        #新建对象
        c = Communication() 
        #配置CAN卡, 型号：USB_CAN_2EU, CAN卡索引: 0, CAN卡通道：channel_0, 波特率: 500kbps
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        #打开CAN卡'
        c.open_new()
        
        # 注意发送函数默认发送数据长度为8个字节
        
        # 发送标准帧 id 为0x110
        data = [1,2,3,4,5,6,7,8]    
        c.Transmit(0x110,data)
        
        # 发送拓展帧
        data = [1,2,3,4,5,6,7,8]    
        c.Transmit(0x110,data,extern_flag = True)
        
        # 发送长度为6的帧 , 根据周立功官方手册，CAN帧最大发送数据长度为8，当然我对此表示怀疑，
        # 但既然周立功所提供驱动貌似只能发送最大长度为8 byte的帧，因此，请保证数据长度不大于8即可。
        data = [1,2,3,4,5,6]    
        c.Transmit(0x110,data,data_len=6)
        
        # 新建线程，不断读取CAN卡上的报文并且打印出来
        cycle_read_thread = threading.Thread(target=c.PrintReceiveData)
        cycle_read_thread.start()
        
        
 ```      
 ## CAN 卡型号支持
 - can 卡型号格式
   + usb_can_2eu
   + usb_can_2
   + pci_5010_u
   + pci_5020_u
   + usb_can_eu
   + usb_can_4eu
   + pci_5121
   + pci_9810i
   + pci_9820
   + can_232
   + pci_5110
   + candtu
   
   如
```python
    c.set_can_board_configuration(can_type="usb_can_2",can_idx=0,chn=0,baud_rate=500)
    c.set_can_board_configuration(can_type="pci_5121",can_idx=0,chn=0,baud_rate=500)
    c.set_can_board_configuration(can_type="candtu",can_idx=0,chn=0,baud_rate=500)
```
   周立功很多CAN卡已经不再支持， 相信经典型号大多为 usb-can-2eu/eu usb-can-2 系列，当前python库驱动
   usb-can-2eu, usb-can-eu,usb-can-2,usb-can-8eu成功
   
   can 卡型号最终会被转换为一个特定数字，可参考源码。
     ZLGCanControl.py
   ```python
 
   
   class CanBoardTypeDefines:
    VCI_PCI5121 = 1
    VCI_PCI9810 = 2
    VCI_USBCAN1 = 3
    VCI_USBCAN2 = 4
    VCI_USBCAN2A = 4
    VCI_PCI9820 = 5
    VCI_CAN232 = 6
    VCI_PCI5110 = 7
    VCI_CANLITE = 8
    VCI_ISA9620 = 9
    VCI_ISA5420 = 10
    VCI_PC104CAN = 11
    VCI_CANETUDP = 12
    VCI_CANETE = 12
    VCI_DNP9810 = 13
    VCI_PCI9840 = 14
    VCI_PC104CAN2 = 15
    VCI_PCI9820I = 16
    VCI_CANETTCP = 17
    VCI_PEC9920 = 18
    VCI_PCIE_9220 = 18
    VCI_PCI5010U = 19
    VCI_USBCAN_E_U = 20
    VCI_USBCAN_2E_U = 21
    VCI_PCI5020U = 22
    VCI_EG20T_CAN = 23
    VCI_PCIE9221 = 24
    VCI_WIFICAN_TCP = 25
    VCI_WIFICAN_UDP = 26
    VCI_PCIe9120 = 27
    VCI_PCIe9110 = 28
    VCI_PCIe9140 = 29
    VCI_USBCAN_4E_U = 31
    VCI_CANDTU_200UR = 32
    VCI_CANDTU_MINI = 33
    VCI_USBCAN_8E_U = 34
    VCI_CANREPLAY = 35
    VCI_CANDTU_NET = 36
    VCI_CANDTU_100UR = 37
    group1 = [VCI_USBCAN_2E_U, VCI_USBCAN_E_U,
                   VCI_PCI5010U, VCI_PCI5020U]
    group2 = [VCI_USBCAN_4E_U]
   ```
   
   ## 波特率设置
   波特率设置请参考，周立功官方手册， 代码中并未对CAN卡是否支持某种波特率进行判断，
   当然 1000， 500， 250， 100等常用波特率应该是支持的。
   
   对于某些特殊波特率需要联系周立功官方，进行特殊参数写入。
   
   - 1000kpbs -----1000
   - 500kpbs -----500
  ## 通道设置
  无论你的CAN卡通道有多少，请记住，最小通道号在在此以0为代表，然后依次递增 
   
# enjoy it

# 下一步
- 考虑支持多种帧发送
- 完善动态解析模块
- 完善配置文件




