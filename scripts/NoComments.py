# Copyright (c) 2015 Jaime van Kessel, Ultimaker B.V.
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.
from ..Script import Script

class NoComments(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return ''

    def execute(self, data: list):
        ''' Data is a list with each layer as an element '''
        temp = []
        for layer in data:
            lines = layer.split("\n")
            for line in lines:
                if line.startswith(';'):
                    continue
                temp.append(line)
        data = temp
        return data
