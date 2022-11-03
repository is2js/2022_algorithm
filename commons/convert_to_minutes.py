def convert_min(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)