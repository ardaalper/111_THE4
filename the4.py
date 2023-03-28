def construct_forest(Defs):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","q","w",
              "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","Q","W"]
    def lister(string):#düzenleyici
        answer=[]
        strL=list(string)
        a=string[0:strL.index("(")]
        for i in a:
            if not i==" ":
                answer.append(i)
        for i in strL:
            if i=="+":
                answer.append("+")
                op_index=strL.index("+")
            elif i=="-":
                answer.append("-")
                op_index=strL.index("-")
            elif i=="*":
                answer.append("*")
                op_index=strL.index("*")
            elif i=="^":
                answer.append("^")
                op_index=strL.index("^")
        b=string[strL.index("=")+1:op_index]
        b_new=b.replace(" ","")
        c=string[op_index+1:]
        c_new=c.replace(" ","")
        if "(" in b_new:
            b_new=b_new[0]
        if "(" in c_new:
            c_new=c_new[0]
        answer.append([b_new])
        answer.append([c_new])
        return answer
    branches=[]
    for i in Defs:
        branches.append(lister(i))
    altdal=[]       #root bulma
    for alt in branches:
        altdal.append(alt[2][0])
        altdal.append(alt[3][0])
    roots=[]
    for isroot in branches:
        if not (isroot[0] in altdal):
            roots.append(isroot)
    def isleft(x):
        for i in alphabet:
            if x[2][0]==i:
                return True
        else:
            return False
    def isright(x):
        for i in alphabet:
            if x[3][0]==i:
                return True
        else:
            return False      
    def recursive(root,branches):
        if (not isleft(root)) and (not isright(root)):#devamsız
            return root            
        elif (isleft(root)) and (not isright(root)):#solundan devam
            for i in branches:
                if i[0]==root[2][0]:
                    return [root[0],root[1],recursive(i,branches),root[3]]
        elif (not isleft(root)) and (isright(root)):#sağından devam
            for i in branches:
                if i[0]==root[3][0]:
                    return [root[0],root[1],root[2],recursive(i,branches)]        
        elif (isleft(root)) and (isright(root)):
            for l in branches:
                for r in branches:
                    if l[0]==root[2][0] and r[0]==root[3][0]:
                        return [root[0],root[1],recursive(l,branches),recursive(r,branches)]   
    answer=[]
    for root in roots:
        answer.append(recursive(root,branches))
    return answer
