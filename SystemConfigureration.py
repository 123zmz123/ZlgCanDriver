import json
import os
class Configuration():
    class Supported ():
        Type_USB_CAN_2EU = "usb_can_2eu"
        Type_USB_CAN_II = "usb_can_ii"

        Channel_CH0 = 0
        Channel_CH1 = 1
        Channel_CH2 = 2
        Channel_CH3 = 3
        Channel_CH4 = 4
        Channel_CH5 = 5
        Channel_CH6 = 6

        Baudrate_100k = 100
        Baudrate_250k = 250
        Baudrate_500k = 500
        Baudrate_1000k = 1000

        Index_0 = 0
        Index_1 = 1
        def __init__(self):
            pass

    def __init__(self):
        self.can_type = "usb_can_2eu" # CAN卡类型
        self.chn = 0  # CAN卡通道
        self.can_idx = 0 # CAN 卡 index
        self.baud_rate=500 # 波特率

    def setCan(self,can_type =Supported.Type_USB_CAN_2EU,  \
               chn = Supported.Channel_CH0,can_idx = Supported.Index_0, baud_rate = Supported.Baudrate_500k):
        self.can_type = can_type
        self.chn = chn
        self.can_idx = can_idx
        self.baud_rate = baud_rate
    def saveConfig(self):
        file_name = "config.json"
        try:
            with open(file_name,"w") as f:
                json.dump(self.__dict__,f)
        except Exception as e:
            print(e)
            pass
    def readConfig(self):
        file_name = "config.json"
        with open(file_name,"r") as f:
            self.__dict__=json.load(f)











if __name__ == '__main__':
    config = Configuration()
    config.readConfig()

    pass