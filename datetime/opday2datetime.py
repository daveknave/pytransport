import datetime as dt

class opday:

    def __init__(self):
        self.datetime_obj = self.rawdate2datetime()
        pass

    def rawdate2datetime(self, orig):
        out_datetime = ''
        ### TODO: pick up correct time format

        ### TODO: If 32 > H >= 24: next calendar day same, operation day

        return out_datetime