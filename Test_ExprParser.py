from ExpressionsParser import *

#nu test
vsh=0
vsh=1
StrLst = ["sinh", "sin", "(", ")", "+", "-", "*", "/"]
StrExpr = "-5+2E-1*sinh(0.5)+sin(-0.5)+(5-3)"
rslt=SplitExpr(StrExpr, StrLst, vsh)
print(rslt)
