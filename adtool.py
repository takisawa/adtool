import logging

class AdTool():

    def calc_ctr(self, imp, click):
        return click / imp

    def calc_cvr(self, click, conversion):
        return conversion / click

    def calc_ecpm(self, imp, click, cpc):
        ctr = self.calc_ctr(imp, click)
        return ctr * cpc * 1000

    def calc_cpa(self, click, cpc, conversion):
        logging.warn("called calc_cpa")
        cvr = self.calc_cvr(click, conversion)

        return cpc / cvr



if __name__ == '__main__':
    imp = 50000 # 30万IMP
    click = 200
    cpc = 30
    conversion = 2

    adtool = AdTool()

    ctr = adtool.calc_ctr(imp, click)
    print("CTR: %f (%.2f%%)" % (ctr, ctr*100))
    print("eCPM: %f" % adtool.calc_ecpm(imp, click, cpc))
    print("CVR: %f" % adtool.calc_cvr(click, conversion))
    print("CPA: %f" % adtool.calc_cpa(click, cpc, conversion))
