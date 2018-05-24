
class AdTool():

    def calc_ctr(self, imp, click):
        return click / imp

    def calc_cvr(self, click, conversion):
        return conversion / click

    def calc_ecpm(self, imp, click, cpc):
        ctr = self.calc_ctr(imp, click)
        return ctr * cpc * 1000



imp = 50000 # 30万IMP
click = 200
cpc = 30
conversion = 2


adtool = AdTool()

ctr = adtool.calc_ctr(imp, click)
print("CTC: %f (%.2f%%)" % (ctr, ctr*100))
print("eCPM: %f" % adtool.calc_ecpm(imp, click, cpc))
print("CVR: %f" % adtool.calc_cvr(click, conversion))
