import math

class Calculate:
    def bracket(self,s,x):
        self.dr=x
        self.S=s
        self.i1=0
        self.i2=0
        temp=''
        while '(' in self.S:
           self.i1=self.S.rfind('(')
           self.i2=self.S.find(')',self.i1)
           self.evaluate()
           temp=self.S.replace(self.org,self.sub)
           self.S=temp
        self.i1=0
        self.i2=len(self.S)-1
        self.evaluate()
        temp=self.S.replace(self.org,self.sub)
        self.S=temp
        return self.S
    def evaluate(self):
        self.sub=self.S[self.i1:self.i2+1]
        self.org=self.sub
        self.i=0
        self.typ=''
        st=''
        while self.i<len(self.sub):
            if self.sub[self.i]=='e':
                if self.i==0 or not(self.sub[self.i-1].isnumeric()):
                    st=self.sub.replace('e',str(math.e))
                elif self.sub[self.i-1].isnumeric():
                    if self.sub[self.i+1:self.i+2]=='-0':
                        st=self.sub.replace('-0','-')
                        self.sub=st
                    E='*'+str(math.e)+'**'
                    st=self.sub.replace('e',E)
                self.sub=st
                continue
            elif self.sub[self.i]=='p':
                st=self.sub.replace('pi',str(math.pi))
                self.sub=st
                continue
            self.i+=1
        self.i=0
        while self.i<len(self.sub):
            if self.sub[self.i]=='s':
                self.typ='s'
                self.search()
                continue
            elif self.sub[self.i]=='c':
                self.typ='c'
                self.search()
                continue
            elif self.sub[self.i]=='t':
                self.typ='t'
                self.search()
                continue
            elif self.sub[self.i]=='a':
                if self.sub[self.i+1]=='s':
                    self.typ='as'
                elif self.sub[self.i+1]=='c':
                    self.typ='ac'
                elif self.sub[self.i+1]=='t':
                    self.typ='at'
                self.search()
            elif self.sub[self.i]=='l':
                if self.sub[self.i+1]=='o':
                    self.typ='l'
                elif self.sub[self.i+1]=='n':
                    self.typ='n'
                self.search()
                continue
            elif self.sub[self.i]=='^':
                st=self.sub.replace('^','**')
                self.sub=st
                continue
            elif self.sub[self.i]=='m':
                st=self.sub.replace('mod','%')
                self.sub=st
                continue
            elif self.sub[self.i]=='√':
                self.typ='r'
                self.search()
                continue
            elif self.sub[self.i]=='!':
                x=self.i-1
                fac=''
                t=''
                while self.sub[x].isnumeric():
                    fac=self.sub[x]+fac
                    x-=1
                    if x<0:
                        break
                t=str(math.factorial(int(fac)))
                fac=fac+'!'
                st=self.sub.replace(fac,t)
                self.sub=st
                continue
            self.i+=1
        n=eval(self.sub)
        self.sub=str(n)
    def search(self):
        temp=''
        f=self.i
        j=self.i
        if self.typ in 'sctl':
            j+=3
            f+=3
        elif self.typ == 'n':
            j+=2
            f+=2
        elif self.typ in 'r':
            j+=1
            f+=1
        elif self.typ[0]=='a':
            j+=4
            f+=4
        l=j
        while self.sub[j].isnumeric() or self.sub[j] in '.' or self.sub[l]=='-':
            j+=1
            if j>=len(self.sub):
                break
        n=0.0
        n=format(n,'.20f')
        n=eval(self.sub[f:j])
        s=''
        rep=''
        if self.typ=='s':
            if self.dr==1:
                if math.cos(math.radians(n))==1 or math.cos(math.radians(n))==-1:
                    rep=0.0
                else:
                    rep=math.sin(math.radians(n))
            else:
                if math.cos(n)==1 or math.cos(n)==-1:
                    rep=0.0
                else:
                    rep=math.sin(n)
            s='sin'+str(n)
        elif self.typ=='c':
            if self.dr==1:
                if math.sin(math.radians(n))==1 or math.sin(math.radians(n))==-1:
                    rep=0.0
                else:
                    rep=math.cos(math.radians(n))
            else:
                if math.sin(n)==1 or math.sin(n)==-1:
                    rep=0.0
                else:
                    rep=math.cos(n)
            s='cos'+str(n)
        elif self.typ=='t':
            if self.dr==1:
                if math.cos(math.radians(n))==1 or math.cos(math.radians(n))==-1:
                    rep=0.0
                elif math.sin(math.radians(n))==1 or math.sin(math.radians(n))==-1:
                    raise Exception("not defined")
                else:
                    rep=math.tan(math.radians(n))
            else:
                if math.cos(n)==1 or math.cos(n)==-1:
                    rep=0.0
                elif math.sin(n)==1 or math.sin(n)==-1:
                    raise Exception("not defined")
                else:
                    rep=math.tan(n)
            s='tan'+str(n)
        elif self.typ=='as':
            if self.dr==1:
                rep=math.degrees(math.asin(n))
            else:
                rep=math.asin(n)
            s='asin'+str(n)
        elif self.typ=='ac':
            if self.dr==1:
                rep=math.degrees(math.acos(n))
            else:
                rep=math.acos(n)
            s='acos'+str(n)
        elif self.typ=='at':
            if self.dr==1:
                rep=math.degrees(math.atan(n))
            else:
                rep=math.atan(n)
            s='atan'+str(n)
        elif self.typ=='l':
            rep=math.log10(n)
            s='log'+str(n)
        elif self.typ=='n':
            rep=math.log(n)
            s='ln'+str(n)
        elif self.typ=='r':
            rep=math.sqrt(n)
            s='√'+str(n)
        temp=self.sub.replace(s,str(rep))
        self.sub=temp
        
