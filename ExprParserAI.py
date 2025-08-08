import re

#def split_by_tokens(expr: str, tokens: List[str]) -> List[str]:
#    # Ñîğòèğóåì òîêåíû ïî óáûâàíèş äëèíû, ÷òîáû "sinh" ø¸ë ïåğåä "sin"
#    sorted_tokens = sorted(tokens, key=len, reverse=True)
#    # İêğàíèğóåì òîêåíû äëÿ èñïîëüçîâàíèÿ â ğåãóëÿğíîì âûğàæåíèè
#    escaped_tokens = [re.escape(tok) for tok in sorted_tokens]
#    # Ñîçäàåì øàáëîí ğåãóëÿğíîãî âûğàæåíèÿ, îáúåäèíÿÿ òîêåíû è ëîâÿ âñ¸ îñòàëüíîå
#    pattern = f"({'|'.join(escaped_tokens)})"
#    # Ğàçáèâàåì ñòğîêó, ñîõğàíÿÿ ğàçäåëèòåëè (òîêåíû)
#    parts = re.split(pattern, expr)
#    # Óáèğàåì ïóñòûå ñòğîêè è ïğîáåëû
#    return [p for p in parts if p and not p.isspace()]

def split_by_tokens(expr, tokens):
    # Ñîğòèğîâêà ïî óáûâàíèş äëèíû, ÷òîáû áîëåå äëèííûå òîêåíû øëè ğàíüøå
    sorted_tokens = sorted(tokens, key=len, reverse=True)
    # İêğàíèğóåì ñïåöñèìâîëû
    escaped_tokens = [re.escape(tok) for tok in sorted_tokens]
    # Ñîçäàåì ğåãóëÿğíîå âûğàæåíèå
    pattern = '(' + '|'.join(escaped_tokens) + ')'
    # Ğàçáèâàåì ñòğîêó ñ ñîõğàíåíèåì òîêåíîâ
    parts = re.split(pattern, expr)
    # Óáèğàåì ïóñòûå ñòğîêè è ïğîáåëû
    return [p for p in parts if p and not p.isspace()]

def split_by_tokens_CorrSignsMath(expr, tokens):
    iniparts=split_by_tokens(expr, tokens)
    NsToDel=[]
    NToDel=0
    finalParts=[]
    pchar="01234567890"
    QIni=len(iniparts)
    if QIni>0:
        for i in range (1, QIni+1):
            inipart=iniparts[i-1]
            if inipart=="+" or inipart=="-":
                if i>1:
                    pL=len(iniparts[i-1-1])
                    pchar=iniparts[i-1-1][pL-1]
                #
                if i==1 or (i>1 and iniparts[i-1-1]=="("):#out of range
                    iniparts[i-1+1]=iniparts[i-1]+iniparts[i-1+1]
                    NsToDel.append(i)
                elif i>1 and i<QIni and(pchar=="E" or pchar=="e" or pchar=="@"):
                    iniparts[i-1+1]=iniparts[i-1-1]+iniparts[i-1]+iniparts[i-1+1]
                    NsToDel.append(i-1)
                    NsToDel.append(i)
                #
            #
        #
        Mode_Del1Sel2=2
        QToDel=len(NsToDel)
        if Mode_Del1Sel2==1:
            for i in range(1, NsToDel):
                NToDel=QToDel-i+1
                del(rowP[NToDel:NToDel+1])
            #
            newParts=iniParts
        elif Mode_Del1Sel2==2:
            isMarkedN=0
            for i in range(1, QIni+1):
                isMarkedN=0
                for j in range(1, QToDel+1):
                    if NsToDel[j-1]==i:
                        isMarkedN=1
                    #
                #
                #
                if isMarkedN==0:
                    iniPart=iniparts[i-1]
                    finalParts.append(iniPart)
                #
            #
        #        
    #
    return finalParts
#



StrLst = ["sinh", "sin", "(", ")", "+", "-", "*", "/"]
StrExpr = "-5+2E-1*sinh(0.5)+sin(-0.5)+(5-3)"
result = split_by_tokens(StrExpr, StrLst)
print(result)
result = split_by_tokens_CorrSignsMath(StrExpr, StrLst)
print(result)

