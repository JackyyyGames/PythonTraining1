class Accumulator:
    def __init__(self, Bezeichnung):
        self._Bezeichnung = Bezeichnung
        self._Voltage = None
        self._Capacity = None
        self._rm_Capacity = None

    def set_voltage(self, Voltage):
        self._Voltage = Voltage

    def set_capacity(self, Capacity):
        self._Capacity = Capacity

    def set_remaining_capacity(self, rm_Capacity):
        self._rm_Capacity = rm_Capacity

    def ToString(self):
        return f"BZ: {self._Bezeichnung} Voltage: {self._Voltage}V Capacity:{self._Capacity}mAh Remaining Capacity: {self._rm_Capacity}mAh"
