from typing import List
import re
class FrameDefine:
    def __init__(self, start, length, i_d, name: str, resolution=1, offset=0):
        self.id = i_d
        self.name = name
        self.start = self.__start_trans(start)
        self.length = length
        self.resolution = resolution
        self.offset = offset

    def __start_trans(self, start):
        convert = [56, 58, 60, 62, 64, 66, 68, 70]
        return convert[start % 8] - start


class iDecodeCanFrame:
    def __init__(self):
        self.slave_num = 16
        self.not_use = 0
        self.temprature_msg_parse_define_list = []
        self.__can_frames_divide_by_id = {}
        self.decode_messages = {}
        self.volt_list  = [0]*150
        self.re_finCellVolt = re.compile("Cell_Voltage_\d*")
        self.re_findDigital = re.compile("\d*")
        self.__message_parse_list_init()
        pass

    def __message_parse_list_init(self):
        # slave temperatures can frames define
        for index in range(self.slave_num):
            slave_name = "_slave_board_" + str(index)
            self.__can_frames_divide_by_id[0x220 + index] = [
                FrameDefine(i_d=0x220 + index, name="CellTemperature_01" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x220 + index, name="Temprature_state_0" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x220 + index, name="CellTemperature_02" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x220 + index, name="Temprature_state_02" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x220 + index, name="CellTemperature_03" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x220 + index, name="Temprature_state_03" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x220 + index, name="CellTemperature_04" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x220 + index, name="Temprature_state_04" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]
            self.__can_frames_divide_by_id[0x230 + index] = [
                FrameDefine(i_d=0x230 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x230 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x230 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x230 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x230 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x230 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x230 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x230 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),

            ]
            self.__can_frames_divide_by_id[0x240 + index] = [
                FrameDefine(i_d=0x240 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x240 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x240 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x240 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x240 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x240 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x240 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x240 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]
            self.__can_frames_divide_by_id[0x250 + index] = [
                FrameDefine(i_d=0x250 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x250 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x250 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x250 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x250 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x250 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x250 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x250 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]
            self.__can_frames_divide_by_id[0x260 + index] = [
                FrameDefine(i_d=0x260 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x260 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x260 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x260 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x260 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x260 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x260 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x260 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]
            self.__can_frames_divide_by_id[0x270 + index] = [
                FrameDefine(i_d=0x270 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x270 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x270 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x270 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x270 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x270 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x270 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x270 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]
            self.__can_frames_divide_by_id[0x280 + index] = [
                FrameDefine(i_d=0x280 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x280 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x280 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x280 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x280 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x280 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x280 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x280 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]

            self.__can_frames_divide_by_id[0x2c0 + index] = [
                FrameDefine(i_d=0x2c0 + index, name="CellTemperature_05" + slave_name, start=8, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x2c0 + index, name="Temprature_state_05" + slave_name, start=6, length=2, resolution=1,
                            offset=0),

                FrameDefine(i_d=0x2c0 + index, name="CellTemperature_06" + slave_name, start=24, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x2c0 + index, name="Temprature_state_06" + slave_name, start=22, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x2c0 + index, name="CellTemperature_07" + slave_name, start=39, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x2c0 + index, name="Temprature_state_07" + slave_name, start=37, length=2,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x2c0 + index, name="CellTemperature_08" + slave_name, start=48, length=14,
                            resolution=0.1, offset=-40),
                FrameDefine(i_d=0x2c0 + index, name="Temprature_state_08" + slave_name, start=46, length=2,
                            resolution=1, offset=0),
            ]

        # slave voltage can frames define
        for index in range(self.slave_num):
            slave_name = "_slave_board_" + str(index)
            self.__can_frames_divide_by_id[0x110 + index] = [
                FrameDefine(i_d=0x110 + index, name="Cell_Voltage_Max" + slave_name, start=8, length=16,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x110 + index, name="Cell_Voltage_Min" + slave_name, start=24, length=16,
                            resolution=0.001,offset=0),

                FrameDefine(i_d=0x110 + index, name="Max_Min_Counter" + slave_name, start=40, length=16,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x110 + index, name="Max_Cell_Num" + slave_name, start=48, length=8,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x110 + index, name="Min_Cell_Num" + slave_name, start=58, length=8,
                            resolution=1, offset=0)
            ]

            base_cell_num = 1
            self.__can_frames_divide_by_id[0x120 + index] = [

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x120 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 5
            self.__can_frames_divide_by_id[0x130 + index] = [

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x130 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 9
            self.__can_frames_divide_by_id[0x140 + index] = [

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x140 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 13
            self.__can_frames_divide_by_id[0x150 + index] = [

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x150 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 17
            self.__can_frames_divide_by_id[0x160 + index] = [

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x160 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 21
            self.__can_frames_divide_by_id[0x170 + index] = [

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x170 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 25
            self.__can_frames_divide_by_id[0x180 + index] = [

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x180 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 29
            self.__can_frames_divide_by_id[0x190 + index] = [

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x190 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 33
            self.__can_frames_divide_by_id[0x1A0 + index] = [

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1A0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 33
            self.__can_frames_divide_by_id[0x1B0 + index] = [

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1B0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 37
            self.__can_frames_divide_by_id[0x1C0 + index] = [

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1C0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 41
            self.__can_frames_divide_by_id[0x1D0 + index] = [

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1D0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 45
            self.__can_frames_divide_by_id[0x1E0 + index] = [

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1E0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 49
            self.__can_frames_divide_by_id[0x1F0 + index] = [

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x1F0 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 53
            self.__can_frames_divide_by_id[0x500 + index] = [

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x500 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 57
            self.__can_frames_divide_by_id[0x510 + index] = [

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x510 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 61
            self.__can_frames_divide_by_id[0x520 + index] = [

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x520 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 65
            self.__can_frames_divide_by_id[0x530 + index] = [

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x530 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 69
            self.__can_frames_divide_by_id[0x540 + index] = [

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x540 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 73
            self.__can_frames_divide_by_id[0x550 + index] = [

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x550 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 77
            self.__can_frames_divide_by_id[0x560 + index] = [

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x560 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 81
            self.__can_frames_divide_by_id[0x570 + index] = [

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x570 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 85
            self.__can_frames_divide_by_id[0x580 + index] = [

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

            base_cell_num = 89
            self.__can_frames_divide_by_id[0x580 + index] = [

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_"+str(base_cell_num + 0) + slave_name, start=8, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_"+str(base_cell_num + 0) + slave_name, start=5, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" +str(base_cell_num + 1) + slave_name, start=24, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" +str(base_cell_num + 1)+ slave_name, start=21, length=3,
                            resolution=1, offset=0),


                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" + str(base_cell_num + 2)+ slave_name, start=40, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" + str(base_cell_num + 2)+ slave_name, start=37, length=3,
                            resolution=1, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_" + str(base_cell_num + 3)+ slave_name, start=56, length=13,
                            resolution=0.001, offset=0),

                FrameDefine(i_d=0x580 + index, name="Cell_Voltage_State_" + str(base_cell_num + 3)+ slave_name, start=53, length=3,
                            resolution=1, offset=0),

            ]

        # Cell voltage balance state can frame
        temp_id = 0x109
        self.__can_frames_divide_by_id[temp_id] = [FrameDefine(i_d=temp_id, name="V_BalanceEnable", start=0, length=1),
        FrameDefine(i_d=temp_id, name="V_BalanceTarget", start=16, length=15,resolution=0.001)]
        temp_id = 0x108
        self.__can_frames_divide_by_id[temp_id] = [FrameDefine(i_d=temp_id, name="Syn_Trigger", start=0, length=8)]

        temp_id = 0x10b
        self.__can_frames_divide_by_id[temp_id] = [FrameDefine(i_d=temp_id, name="Version_Trigger", start=0, length=8),
                                                   FrameDefine(i_d=temp_id, name="Version_Num", start=8, length=8)]

        for index in range(self.slave_num):
            self.__can_frames_divide_by_id[0x2b0 + index] = [FrameDefine(i_d=0x2b0+index, name="BMU"+str(index)+"_ID",
                                                                         start=0, length=8)]

            self.__can_frames_divide_by_id[0x0F0 + index] =[ FrameDefine(i_d=0x0F0+index, name= "Syn_Trigger_ACK_slave_"+ str(index),
                                                                         start=0, length=8)]

            self.__can_frames_divide_by_id[0x0F0 + index] =[ FrameDefine(i_d=0x0F0+index, name="Bum_ID_Num" + str(index),
                                                                         start=8, length=8)]

        temp_id = 0x201
        self.__can_frames_divide_by_id[temp_id] = [FrameDefine(i_d=temp_id, name="FCT_Function", start=0, length=8)]

        temp_id = 0x202
        self.__can_frames_divide_by_id[temp_id] = [
            FrameDefine(i_d=temp_id, name="IN_H_value", start=8, length=16, resolution=0.001, offset=0),
            FrameDefine(i_d=temp_id, name="IN_L_value", start=24, length=16, resolution=0.001, offset=0)
        ]

        temp_id = 0x203
        self.__can_frames_divide_by_id[temp_id] = [
            FrameDefine(i_d=temp_id,name="应答信号数据1", start=0,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据2", start=8,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据3", start=16,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据4", start=24,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据5", start=32,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据6", start=40,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据7", start=48,length=8),
            FrameDefine(i_d=temp_id,name="应答信号数据8", start=56,length=8),
        ]

        temp_id = 0x204
        self.__can_frames_divide_by_id[temp_id] = [
            FrameDefine(i_d=temp_id,name="TestModeKey1", start=0,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey2", start=8,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey3", start=16,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey4", start=24,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey5", start=32,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey6", start=40,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey7", start=48,length=8),
            FrameDefine(i_d=temp_id,name="TestModeKey8", start=56,length=8),
        ]

    # 把数字转换为2进制字符串
    def __trans_int_2_bin_str(self, dt: int):
        self.not_use
        old_str = str(bin(dt))
        old_str = old_str[2:]
        new_str = old_str.rjust(8, "0")
        return new_str
    # 将2进制字符串转换为数字

    def __trans_bin_str_2_int(self, dt: str):
        return int(dt, 2)

    def show_can_frame_as_bin(self, dt: List[int]):
        for items in dt:
            print(self.__trans_int_2_bin_str(items))
    # 摩托罗拉格式 低字节在
    # 返回值是右对齐 将收到的CAN报文转换为长度为64的，2进制字符串
    # data[0]                 X_07_63  X_06_62  X_05_61  X_04_60  X_03_59  X_02_58  X_01_57  X_00_56
    # data[1]                 X_15_55  X_14_54  X_13_53  X_12_52  X_11_51  X_10_50  X_09_49  X_08_48
    # data[2]                 X_23_47  X_22_46  X_21_45  X_20_44  X_19_43  X_18_42  X_17_41  X_16_40
    # data[3]                 X_31_39  X_30_38  X_29_37  X_28_36  X_27_35  X_26_34  X_25_33  X_24_32
    # data[4]                 X_39_31  X_38_30  X_37_29  X_36_28  X_35_27  X_34_26  X_33_25  X_32_24
    # data[5]                 X_47_23  X_46_22  X_45_21  X_44_20  X_43_19  X_42_18  X_41_17  X_40_16
    # data[6]                 X_55_15  X_54_14  X_53_13  X_52_12  X_51_11  X_50_10  X_49_09  X_48_08
    # data[7]                 X_63_07  X_62_06  X_61_05  X_60_04  X_59_03  X_58_02  X_57_01  X_56_00

    def msg_frame_2_bin_64bits_str(self, dt: []):
        ret = ""
        for items in dt:
            ret += self.__trans_int_2_bin_str(items)
        ret = ret.rjust(64, "0")
        return ret[::-1]

    def calc_value(self, data_str: str, frame_define: FrameDefine):
        st = frame_define.start
        e = frame_define.start+frame_define.length
        old_str = data_str[st:e]
        new_str = old_str[::-1]
        val = self.__trans_bin_str_2_int(new_str)
        return val*frame_define.resolution + frame_define.offset

    def calc_value_and_store_2_decode_msg(self,data_str:str, frame_define: FrameDefine):
        st = frame_define.start
        e = frame_define.start+frame_define.length
        old_str = data_str[st:e]
        new_str = old_str[::-1]
        val = self.__trans_bin_str_2_int(new_str)
        convert_val = val*frame_define.resolution + frame_define.offset
        self.decode_messages[frame_define.name] = convert_val


    def test_store_msg(self, frame_define: FrameDefine):
        self.decode_messages[frame_define.name] = 997
        self.decode_messages[frame_define.name] = 998
        pass

    def get_decode_msg(self):
        return self.decode_messages

    def test_find_ids(self, i_d: int) -> List[FrameDefine]:
        if self.__can_frames_divide_by_id.__contains__(i_d):
            return self.__can_frames_divide_by_id.get(i_d)

    def decode_can_frame_and_store(self, i_d: int, dt: List[int]):
        if self.__can_frames_divide_by_id.__contains__(i_d):
            frame_information = self.__can_frames_divide_by_id.get(i_d)
            d_str = self.msg_frame_2_bin_64bits_str(dt)
            for information in frame_information:
                self.calc_value_and_store_2_decode_msg(d_str, information)

if __name__ == '__main__':
    re_finCellVolt = re.compile("Cell_Voltage_\d*")
    re_findDigital = re.compile("\d*")
    s="Cell_Voltage_0_slave_board_15"
    print(re_finCellVolt.match(s).group(0))

    # can_frames_divide_by_id = {}
    # ids = 0x220
    # # can_frames_divide_by_id[ids]=[FrameDefine(name="温度1", start=8, length=12,i_d=ids, resolution=1,offset=40)]
    # frame = FrameDefine(name="温度1",start=56,length=12,i_d=0x111, resolution=1,offset=0)
    # data = [0x22,0x14,0x69,1,0x47,1,1,0xf0]
    # d = iDecodeCanFrame()
    # print(d.show_can_frame_as_bin(dt=data))
    # s = d.msg_frame_2_bin_64bits_str(data)
    # print(s)
    # print(bin(d.calc_value(s,frame)))
    # res = d.test_find_ids(0x220)
    # for item in res:
    #     print(item.name)
    # print(d.calc_value(s, frame))
    # print(can_frames_divide_by_id)
    pass


