from functools import partialmethod
import string


class BaseConvert:

    characters = string.ascii_uppercase + string.ascii_lowercase
    dic = dict(zip(range(10,62), characters))


    def __init__(self, b1, b2, entry, round=10):
        if type(entry) != str:
            raise TypeError("Accept only numbers with 'str' type")
        
        num = entry.split(".") 
        integer = num[0]
        fraction = num[1] if '.' in entry else '0'
        exponent = len(integer) - 1
        
        self.entry = entry
        self.b1 = b1
        self.b2 = b2
        self.integer = integer
        self.fraction = fraction
        self.round = round
        self.exp = exponent
        

    def deci_to_grt(self, digit=None):
        if digit is None:
            digit = int(self.integer)

        l = []
        while digit > self.b2:
            remain = digit%self.b2
            digit = digit//self.b2

            if remain > 9 and remain < self.b2:
                remain = self.dic[remain]
            l.insert(0,str(remain))

        if digit > 9 and digit < self.b2:
            l.insert(0,self.dic[digit])
        else:
            l.insert(0,str(digit))
        new_int = ("").join(l)
        return new_int
 

    def deci_to_sml(self, digit=None):
        if digit is None:
            digit = int(self.integer)

        j = 0
        l = []
        while self.b2**j <= digit:
            l.append(j)
            j += 1

        new_int = ""
        for i in l[::-1]:
            new_int += str(digit//(self.b2**i))
            digit = digit%(self.b2**i)
        return new_int


    def deci_to_fr(self, digit=None):
        if digit is None:
            digit = float("0."+self.fraction)
            
        new_fraction = ""
        i = 0
        while i < self.round:
            x = int(self.b2*digit)
            fract_split = (str(self.b2*digit)).split(".")
            digit = float("0." + fract_split[1])

            if x > 9 and x < self.b2:
                x = self.dic[x]
            new_fraction += str(x)
            i += 1
        return new_fraction


    def to_deci(self, num=None, exp=None):
        if num is None and exp is None:
            num = self.integer
            exp = self.exp

        digit = 0
        for i in num:
            if i.isalpha():
                for key,value in self.dic.items():
                    if i == value:
                        i = key 

            digit += (int(i)*(self.b1**exp))
            exp -= 1
        
        if num == self.fraction:
            return self.deci_to_fr(digit)
        elif self.b2 > 10:
            return self.deci_to_grt(digit)
        else:
            return self.deci_to_sml(digit)
    

    def to_deci_fr(self):
        return self.to_deci(self.fraction, -1)


    
    def run(self):
        entry = self.integer + self.fraction
        digits = [int(d) for d in entry if d.isnumeric()]
        alphabets = [a for a in entry if a.isalpha()]
        
        cond_1 = (self.b1 < 10 and entry.isdigit()
                and all(d < self.b1 for d in digits))

        cond_2 = self.b1 == 10 and entry.isdigit()

        cond_3 = (self.b1 > 10 and self.b1 <= 62 and entry.isalnum()
         and all(a <= self.dic[self.b1 - 1] for a in alphabets))


        if self.b1 > 62 or self.b2 > 62:
            raise KeyError('Only bases from 2 to 62 are supported')
        elif (cond_1 or cond_2 or cond_3):
            self.function_call()
        else:
            raise ValueError('Invalid number with base {}'.format(self.b1))

    
    def function_call(self):
        f = [
            self.deci_to_grt,
            self.deci_to_sml,
            self.to_deci,
            self.to_deci_fr,
            self.deci_to_fr
            ]

        conditions = [
            lambda b1,b2: b1 != 10,
            lambda b1,b2: b1 == 10 and b2 > 10,
            lambda b1,b2: b1 == 10 and b2 <= 10
        ]
       
        calls = {
            (f[2],f[3]): conditions[0], 
            (f[0],f[4]): conditions[1],
            (f[1],f[4]): conditions[2]
        }

        for func, cond in calls.items():
            if cond(self.b1, self.b2):
                if '.' in self.entry:
                    print(func[0]() + '.' + func[1]())
                else:
                    print(func[0]())
