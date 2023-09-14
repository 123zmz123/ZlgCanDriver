import ctypes
from  ctypes import *
import time
import traceback
from DecodeCanFrame import iDecodeCanFrame
import re
from enum import *
import threading
from array import *

class S19Line:
    def __init__(self):
        self.DataType = ""
        self.DataID = ""
        self.DataItem=""

dll = ctypes.WinDLL("ControlCAN.dll")


class VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_ulong),
                ("AccMask", c_ulong),
                ("Reserved", c_ulong),
                ("Filter", c_ubyte),
                ("Timing0", c_ubyte),
                ("Timing1", c_ubyte),
                ("Mode", c_ubyte)
                ]


class VCI_CAN_OBJ(Structure):
    _fields_ = [("ID", c_uint),
                ("TimeStamp", c_uint),
                ("TimeFlag", c_byte),
                ("SendType", c_byte),
                ("RemoteFlag", c_byte),
                ("ExternFlag", c_byte),
                ("DataLen", c_ubyte),
                ("Data",  c_ubyte*8),
                ("Reserved", c_ubyte*3)
                ]

class VCI_CAN_OBJ_SEND(Structure):
    _fields_ = [("ID", c_uint),
                ("TimeStamp", c_uint),
                ("TimeFlag", c_byte),
                ("SendType", c_byte),
                ("RemoteFlag", c_byte),
                ("ExternFlag", c_byte),
                ("DataLen", c_byte),
                ("Data",  c_ubyte*8),
                ("Reserved", c_ubyte*3)
                ]


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





class CanBaudrateDefines:
    def group1_baud_rate(self,baud_rate: int):
        if baud_rate == 1000:
            return True,0x060003,"ok"
        elif baud_rate == 800:
            return True,0x060004,"ok"
        elif baud_rate == 500:
            return True,0x060007,"ok"
        elif baud_rate == 250:
            return True,0x1c0008,"ok"
        elif baud_rate == 125:
            return True,0x1c0011,"ok"
        elif baud_rate == 100:
            return True,0x160023,"ok"
        elif baud_rate == 50:
            return True,0x1c002c,"ok"
        elif baud_rate == 20:
            return True,0x1600b3,"ok"
        elif baud_rate == 10:
            return True,0x1c00e0,"ok"
        elif baud_rate == 5:
            return True,0x1c01c1,"ok"
        else:
            return False, 0, "baud rate is not supported!"

    def group2_baud_rate(self,baud_rate: int):
        if baud_rate == 1000:
            return True, baud_rate*1000, "ok"
        elif baud_rate == 800:
            return True, baud_rate*1000, "ok"
        elif baud_rate == 500:
            return True, baud_rate*1000, "ok"
        elif baud_rate == 250:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 125:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 100:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 50:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 20:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 10:
            return True,  baud_rate*1000, "ok"
        elif baud_rate == 5:
            return True,  baud_rate*1000, "ok"
        else:
            return False, 0, "baud rate is not supported"
    def get_baud_rate_group_1_2(self,can_type: int, baud_rate: int):
        if can_type in CanBoardTypeDefines.group1:
            stat,bd ,msg= self.group1_baud_rate(baud_rate)
            return stat,bd, msg
        elif can_type in CanBoardTypeDefines.group2:
            stat,bd, msg = self.group2_baud_rate(baud_rate)
            return stat, bd, msg
        else:
            return False,0, "can type not supporrted"

    def get_baud_rate_group_3(self, baud_rate: int):
        try:
            if baud_rate == 10:
                timing0 = 0x31
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 20:
                timing0 = 0x18
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 40:
                timing0 = 0x87
                timing1 = 0xff
                return timing0,timing1
            elif baud_rate == 50:
                timing0 = 0x09
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 80:
                timing0 = 0x83
                timing1 = 0xff
                return timing0,timing1
            elif baud_rate == 100:
                timing0 = 0x04
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 125:
                timing0 = 0x03
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 200:
                timing0 = 0x81
                timing1 = 0xfa
                return timing0,timing1
            elif baud_rate == 250:
                timing0 = 0x01
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 400:
                timing0 = 0x80
                timing1 = 0xfa
                return timing0,timing1
            elif baud_rate == 500:
                timing0 = 0x00
                timing1 = 0x1c
                return timing0,timing1
            elif baud_rate == 666:
                timing0 = 0x80
                timing1 = 0xb6
                return timing0,timing1
            elif baud_rate == 800:
                timing0 = 0x00
                timing1 = 0x16
                return timing0,timing1
            elif baud_rate == 1000:
                timing0 = 0x00
                timing1 = 0x14
                return timing0,timing1
            else:
                raise Exception("group3 CAN卡所设置的波特率暂不被支持 波特率为"+ str(baud_rate))
        except Exception as e:
            raise e
# PCI-5010-U、PCI-5020-U、USBCAN-E-U、 USBCAN-2E-U、 USBCAN-4E-U、CANDTU


class CanConfigGroup1:
    def __init__(self):
        self.BaudRate = 0
        self.CanType = 0
        self.Chn = 0
        self.CanIndex = 0
        self.init_config = VCI_INIT_CONFIG()


class CanConfigGroup2:
    def __init__(self):
        self.BaudRate = 0
        self.CanType = 0
        self.Chn = 0
        self.CanIndex = 0
        self.init_config = VCI_INIT_CONFIG()


class Communication():
    baud_rate_define = CanBaudrateDefines()
    initconfig = VCI_INIT_CONFIG(0x00000000,0xffffffff, 0, 1, 0x00, 0x14, 0)#
    CanInfor = VCI_CAN_OBJ()
    ReceiveBuffer = (VCI_CAN_OBJ*1000)()

    def __init__(self, can_type=23, chn=0, ind=0):
        super().__init__()
        self.BaudRate = 0x60007
        self.CanType = can_type
        self.Chn = chn
        self.CanIndex = ind
        self.config1 = CanConfigGroup1()
        self.config2 = CanConfigGroup2()
        self.decode = iDecodeCanFrame()
        self.run_flag = False
    def _error_msg(self, msg: str):
        return msg

    def _trans_can_type(self, typename: str):
        if typename.lower() == "usb_can_2eu":  # 此处应当用 re 去解析
            return True, CanBoardTypeDefines.VCI_USBCAN_2E_U, "ok"
        elif typename.lower() == "usb_can_1" or typename.lower() == "usb_can_i":
            return True, CanBoardTypeDefines.VCI_USBCAN1, "ok"
        elif typename.lower() == "usb_can_2" or typename.lower() == "usb_can_ii":
            return True, CanBoardTypeDefines.VCI_USBCAN2, "ok"
        elif typename.lower() == "pci_5010_u" or typename.lower() == "pci-5010-u":
            return True, CanBoardTypeDefines.VCI_PCI5010U, "ok"
        elif typename.lower() == "pci_5020_u" or typename.lower() == "pci-5020-u":
            return True, CanBoardTypeDefines.VCI_PCI5020U, "ok"
        elif typename.lower() == "usb_can_eu" or typename.lower() == "usb-can-eu":
            return True, CanBoardTypeDefines.VCI_USBCAN_E_U, "ok"
        elif typename.lower() == "usb_can_4eu" or typename.lower() == "usb-can-4eu":
            return True, CanBoardTypeDefines.VCI_USBCAN_E_U, "ok"
        elif typename.lower() == "pci_5121" or typename.lower() == "pci-5121":
            return True, CanBoardTypeDefines.VCI_PCI5121, "ok"
        elif typename.lower() == "pci_9810i" or typename.lower() == "pci-9810i":
            return True, CanBoardTypeDefines.VCI_PCI9810, "ok"
        elif typename.lower() == "pci_9820" or typename.lower() == "pci-9820":
            return True, CanBoardTypeDefines.VCI_PCI9820, "ok"
        elif typename.lower() == "can_232" or typename.lower() == "can232":
            return True, CanBoardTypeDefines.VCI_CAN232, "ok"
        elif typename.lower() == "pci_5110" or typename.lower() == "pci5110":
            return True, CanBoardTypeDefines.VCI_PCI5110, "ok"
        elif typename.lower() == "candtu":
            return True, CanBoardTypeDefines.VCI_CANDTU_MINI, "ok"
        else:
            return False, 0, "InputType is not satisfied! At GetCANBoardConfigurtaion Function"

    def set_can_board_configuration(self, can_type: str, can_idx: int, chn: int, baud_rate: int):
        try:
            if type(can_type) != str or type(chn) != int or type(baud_rate) != int:
                return False, self._error_msg(" InputType is not satisfied! At GetCANBoardConfigurtaion Function")

            # if can type like usb_can_2eu
                # CAN Type 解析
            stat, self.CanType, msg = self._trans_can_type(can_type)

            if not stat:
                return False, self._error_msg(msg)

            if self.CanType in CanBoardTypeDefines.group1 or self.CanType in CanBoardTypeDefines.group2:

                stat, self.config1.CanType , msg = self._trans_can_type(can_type)
                # CAN Board Index 解析
                self.CanIndex = can_idx
                self.config1.CanIndex = can_idx

                # CAN Board Channel 解析
                if chn <= 4:
                    self.Chn = chn
                    self.config1.Chn = chn
                else:
                    return False, self._error_msg("CAN channel is larger then 4")

                stat, self.BaudRate, msg = self.baud_rate_define.get_baud_rate_group_1_2 \
                    (self.CanType, baud_rate)

                stat, self.config1.BaudRate , msg = self.baud_rate_define.get_baud_rate_group_1_2 \
                    (self.config1.CanType, baud_rate)

                self.config1.init_config.AccCode = 0x00000000
                self.config1.init_config.AccMask = 0xffffffff
                self.config1.init_config.Reserved = 0
                self.config1.init_config.Filter = 1
                self.config1.init_config.Timing0 = 0x00
                self.config1.init_config.Timing1 = 0x14
                self.config1.init_config.Mode = 0

                if not stat:
                    return False, self._error_msg(msg)
                return True, self._error_msg("ok")
            else:
                stat, self.config2.CanType, msg = self._trans_can_type(can_type)
                self.config2.CanIndex = can_idx

                if chn <= 4:
                    self.config2.Chn = chn
                else:
                    raise Exception("Can 通道设置大于4")
                self.config2.init_config.AccCode = 0x00000000
                self.config2.init_config.AccMask = 0xffffffff
                self.config2.init_config.Filter = 1
                self.config2.init_config.Timing0 , self.config2.init_config.Timing1 = self.baud_rate_define.\
                    get_baud_rate_group_3(baud_rate)

                self.config2.init_config.Mode = 0

        except Exception as e:
            raise e
            print(e)





    def Open(self):
        if dll.VCI_OpenDevice(self.CanType, 0, 0) == 0:
            print("打开设备失败,请检查设备类型和设备索引号是否正确!")
            return
        if (self.CanType == 21 or self.CanType == 20):
            if dll.VCI_SetReference(self.CanType,self.CanIndex,self.Chn, 0, byref(c_int(self.BaudRate))) == 0:
                dll.VCI_CloseDevice(self.CanType,0)
                print("配置波特率失败!")
                return
            if dll.VCI_InitCAN(self.CanType, self.CanIndex, self.Chn, pointer(self.initconfig)) == 0:
                print("初始化CAN失败")
                return
        elif self.CanType == 4:
            vic = VCI_INIT_CONFIG()
            vic.AccCode = 0x00000000
            vic.AccMask = 0xffffffff
            vic.Filter = 1
            vic.Timing0 = 0x00
            vic.Timing1 = 0x1c
            vic.Mode = 0
            if dll.VCI_InitCAN(4,0,0,pointer(vic))== 0:
                print("初始化CAN卡失败！")
        if dll.VCI_StartCAN(self.CanType,self.CanIndex,self.Chn)==0:
            print("打开CAN失败！")
            return

    def Openx(self):
        if dll.VCI_OpenDevice(self.config1.CanType, 0, 0) == 0:
            print("打开设备失败,请检查设备类型和设备索引号是否正确!")
            return
        if (self.CanType == 21 or self.CanType == 20):
            if dll.VCI_SetReference(self.config1.CanType,self.config1.CanIndex,self.config1.Chn, 0, byref(c_int(self.config1.BaudRate))) == 0:
                dll.VCI_CloseDevice(self.config1.CanType,0)
                print("配置波特率失败!")
                return
            if dll.VCI_InitCAN(self.config1.CanType, self.config1.CanIndex, self.config1.Chn, pointer(self.config1.init_config)) == 0:
                print("初始化CAN失败")
                return
        elif self.CanType == 4:
            vic = VCI_INIT_CONFIG()
            vic.AccCode = 0x00000000
            vic.AccMask = 0xffffffff
            vic.Filter = 1
            vic.Timing0 = 0x00
            vic.Timing1 = 0x1c
            vic.Mode = 0
            if dll.VCI_InitCAN(4,0,0,pointer(vic))== 0:
                print("初始化CAN卡失败！")
        if dll.VCI_StartCAN(self.CanType,self.CanIndex,self.Chn)==0:
            print("打开CAN失败！")
            return
    def open_new(self):
        try:
            if self.config1.CanType == 0 and self.config2.CanType == 0:
                raise Exception("do not set Can type in Open_new func")

            if self.config1.CanType != 0:

                if dll.VCI_OpenDevice(self.config1.CanType, self.config1.CanIndex, 0) == 0:
                    raise Exception("打开CAN卡失败，请检查设备索引和设备类型是否准确")

                if dll.VCI_SetReference(self.config1.CanType, self.config1.CanIndex, self.config1.Chn, 0,
                                        byref(c_int(self.config1.BaudRate))) == 0:
                    dll.VCI_CloseDevice(self.config1.CanType, 0)
                    raise Exception("配置波特率失败")

                if dll.VCI_InitCAN(self.config1.CanType, self.config1.CanIndex, self.config1.Chn,
                                   pointer(self.config1.init_config)) == 0:
                    raise Exception("初始化失败")

                if dll.VCI_StartCAN(self.config1.CanType,self.config1.CanIndex,self.config1.Chn)==0:
                    raise Exception("打开CAN卡失败")

            elif self.config2.CanType != 0:
                if dll.VCI_OpenDevice(self.config2.CanType, self.config2.CanIndex, 0) == 0:
                    raise Exception("打开CAN卡失败，请检查设备索引和设备类型是否准确")

                if dll.VCI_InitCAN(self.config2.CanType,self.config2.CanIndex,0, pointer(self.config2.init_config))== 0:
                    raise Exception("初始化CAN卡失败")

                if dll.VCI_StartCAN(self.config2.CanType,self.config2.CanIndex, self.config2.Chn)==0:
                    raise Exception("打开CAN卡失败")

        except Exception as e:
            raise e
            return traceback.format_exc()


    def ReceiveData(self):
        RecvSize = dll.VCI_GetReceiveNum(self.CanType, self.CanIndex, self.Chn)
        respond = dll.VCI_Receive(self.CanType, self.CanIndex, self.Chn, byref(self.ReceiveBuffer), RecvSize, 10)
        if respond == 0xFFFFFFFF:
            print("读取数据失败")
        elif respond == 0:
            pass
        elif respond > 0:
            for i in range(0, respond):
                if self.ReceiveBuffer[i].ID == (self.m_AdrReceiveID + 0):
                    print(hex(self.ReceiveBuffer[i].Data[0]),
                          hex(self.ReceiveBuffer[i].Data[1]),
                          hex(self.ReceiveBuffer[i].Data[2]),
                          hex(self.ReceiveBuffer[i].Data[3]),
                          hex(self.ReceiveBuffer[i].Data[4]),
                          hex(self.ReceiveBuffer[i].Data[5]),
                          hex(self.ReceiveBuffer[i].Data[6]),
                          hex(self.ReceiveBuffer[i].Data[7]))
                    self.GetLengthOfBlock(self.ReceiveBuffer[i].Data[0:])
                    self.CheckIsBlockWriterOver(self.ReceiveBuffer[i].Data[0:])
                    for j in range(0,len(self.m_ReturnData)):
                        if self.CheckIsReturn(self.m_ReturnData[j],self.ReceiveBuffer[i].Data[0:]):
                            self.m_ReturnResult[j] = True
                            if j == self._MessageName.ReturnConstantMessage.value:
                                print("收到保持通讯消息")

    def _PrintReceiveData(self):
        RecvSize = dll.VCI_GetReceiveNum(self.CanType, self.CanIndex, self.Chn)
        respond = dll.VCI_Receive(self.CanType, self.CanIndex, self.Chn, byref(self.ReceiveBuffer), RecvSize, 10)
        if respond == 0xFFFFFFFF:
            print("读取数据失败")
        elif respond == 0:
            pass
        elif respond > 0:
            for i in range(0, respond):
                print(hex(self.ReceiveBuffer[i].Data[0]),
                      hex(self.ReceiveBuffer[i].Data[1]),
                      hex(self.ReceiveBuffer[i].Data[2]),
                      hex(self.ReceiveBuffer[i].Data[3]),
                      hex(self.ReceiveBuffer[i].Data[4]),
                      hex(self.ReceiveBuffer[i].Data[5]),
                      hex(self.ReceiveBuffer[i].Data[6]),
                      hex(self.ReceiveBuffer[i].Data[7]))
    def PrintReciveData(self):
        while True:
            self._PrintReceiveData()
            time.sleep(0.1)
    def ReceiveDataAndDecode(self):
        RecvSize = dll.VCI_GetReceiveNum(self.CanType, self.CanIndex, self.Chn)
        respond = dll.VCI_Receive(self.CanType, self.CanIndex, self.Chn, byref(self.ReceiveBuffer), RecvSize, 10)
        if respond == 0xFFFFFFFF:
            print("读取数据失败")
        elif respond == 0:
            pass
        elif respond > 0:
            for i in range(0, respond):
                self.decode.decode_can_frame_and_store(i_d=self.ReceiveBuffer[i].ID, dt=self.ReceiveBuffer[i].Data)
    def thread_begin(self):
        self.run_flag = True
    def thread_end(self):
        self.run_flag = False
    def receive(self):
        while True:
            # self.ReceiveData()
            self.ReceiveDataAndDecode()
            time.sleep(0.5)
            di = self.decode.get_decode_msg()
            print(di)


    def printx(self):
        while True:
            print("fuck fuck")
            time.sleep(0.1)




    def Close(self):
        dll.VCI_CloseDevice(self.CanType,0)
    def Transmit(self, ID, data,remote_flag=False,extern_flag = False,data_len = 8): #最基本的发送函数
        a = VCI_CAN_OBJ_SEND()
        a.ID = ID
        a.DataLen = data_len
        if remote_flag == True:
            a.RemoteFlag = 1
        if extern_flag == True:
            a.ExternFlag = 1
        if len(data)<8:
            data+=(8-len(data))*[0]
        #a.Data = (c_ubyte*8)(0x02,0x01,0x01,0x01,0x01,0x01,0x01,0x01)
        a.Data = (c_ubyte*8)(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7] )# 终于尼玛搞定了
        # a.Data = (c_ubyte*8)(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]) # 终于尼玛搞定了
        # a.Data = (c_ubyte*8)(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]) # 终于尼玛搞定了
        res = 0
        if self.config1.CanType != 0:
            res = dll.VCI_Transmit(self.CanType, self.config1.CanIndex, self.config1.Chn, pointer(a), 1)
        elif self.config2.CanType != 0:
            res = dll.VCI_Transmit(self.CanType, self.config2.CanIndex, self.config2.Chn, pointer(a), 1)
        if res !=1:
            print("发送失败！")
    def TranExtentedSession(self): # 切换到扩展模式
        data =(0x02,0x10,0x03,0,0,0,0,0)
        self.Transmit(self.m_SendID,data)
        print("尝试切换到拓展模式")

    def TimeHandle(self,msg):
        pass
    def RoutineSend(self):#周期发送用来和BMS保持连接！
        while True:
            self.m_ReturnResult[self._MessageName.ReturnConstantMessage.value] = False
            self.SendConstantCommand()
            m_Time = time.clock()
            while self.m_ReturnResult[self._MessageName.ReturnConstantMessage.value] != True:
                if (time.clock()-m_Time)>1000:
                    print("保持通讯失败")
                    return
                time.sleep(1)
            print("保持通讯成功")
            time.sleep(2)

class HowToUse():
    def open_it(self):
        c = Communication()
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        c.open_new()
    def send_frames(self):
        c = Communication()
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        c.open_new()
        data = [1,2,3,4,5,6,7,8]
        for i in range(1000):
            time.sleep(5)
            c.Transmit(0x110,data)
    def send_extend_frames(self):
        c = Communication()
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        c.open_new()
        data = [1,2,3,4,5,6]
        for i in range(50):
            c.Transmit(0x111,data,extern_flag=True,data_len=7)
    def close_it(self):
        c = Communication()
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        c.open_new()
        time.sleep(10)
        c.Close()
    def receive_with_thread(self):
        c = Communication()
        c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
        c.open_new()
        cycle_read_thread = threading.Thread(target=c.PrintReceiveData)
        cycle_read_thread.start()
        while True:
            pass




if __name__ == "__main__":
    i_will_help_you = HowToUse()
    i_will_help_you.send_extend_frames()
    # i_will_help_you.open_it()
    # i_will_help_you.send_frames()
    # i_will_help_you.close_it()
    # i_will_help_you.receive_with_thread()





