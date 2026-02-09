import re
import dateutil.parser

class PartialDate:

    def __init__(self, value):
        self.value = value

    def isoformat(self):
        return self.value

def parse(datestr):
    datestr = getattr(datestr, "value", datestr)
    if re.search("^[0-9]{1,6}$", datestr):
        if len(datestr) > 4:
            return PartialDate(datestr[0:4] + "-" + datestr[4:])
        else:
            return PartialDate(datestr)
    elif len(datestr.split("-")) == 2:
        return PartialDate(datestr)
    else:
        return dateutil.parser.parse(datestr)
