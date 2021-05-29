class NonRepeatingChar():

    def nonRepeatingChar(self,s):    
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                 d[i]= 1
        #print(d)
        if self.isMinusOne(d)==1:
            for j in range(len(s)):
                if d[s[j]]== 1:
                    print("Non repeating char is:",s[j]+ ", and index value is: ",j)
                    return s[j],j
        else:
            #self.index=-1
            print("No non repeating char found, hence index is: ",-1)
            #return -1
            
            
    def isMinusOne(self,d):
        flag= 2
        for i in d.values():
            
            if i>1 and flag:
                continue
            else:
                flag=flag-1
                return flag
        
        return -1

if __name__=="__main__":
    obj = NonRepeatingChar()
    obj.nonRepeatingChar("abc")
    obj.nonRepeatingChar("abca")
    obj.nonRepeatingChar("abcab")
    obj.nonRepeatingChar("abcabc")