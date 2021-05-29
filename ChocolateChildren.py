class ChocolateChildren:

    def distChocolate(self,candy,children): 
        d={}
        div=candy//children 
        rem=candy%children 
        for i in range(1,children+1):
            if i<=rem:
                d[i]=div+1
            else:
                d[i]=div
        
        print(d)

if __name__=="__main__":
	obj = ChocolateChildren()
	obj.distChocolate(3,3)
	obj.distChocolate(7,5)