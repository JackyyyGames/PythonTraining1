from Class.Accumulator import Accumulator


class Program:
    Akku = Accumulator("Battterie 1")
    Akku.set_capacity(13)
    Akku.set_voltage(1)
    print(Akku.ToString())
