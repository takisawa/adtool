

def calc_ctr(imp, click):
    return click / imp


imp = 30000 # 30万IMP
click = 100

print("CTC: %f" % calc_ctr(imp, click))
