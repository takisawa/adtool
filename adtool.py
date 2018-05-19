

def calc_ctr(imp, click):
    return click / imp


def calc_ecpm(imp, click, cpc):
    ctr = calc_ctr(imp, click)
    return ctr * cpc * 1000

imp = 50000 # 30万IMP
click = 200
cpc = 30

print("CTC: %f" % calc_ctr(imp, click))
print("eCPM: %f" % calc_ecpm(imp, click, cpc))
