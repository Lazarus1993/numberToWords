class Int2Words(object):
    def writtenwords(self, num):
        units={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
        tens={0:'',1:'Ten',2:'Twenty ',3:'Thirty ',4:'Forty ',5:'Fifty ',6:'Sixty ',7:'Seventy ',8:'Eighty ',9:'Ninety '}
        teens={10:'Ten ',11:'Eleven ',12:'Twelve ',13:'Thirteen ',14:'Fourteen ',15:'Fifteen ',16:'Sixteen ',17:'Seventeen ',18:'Eighteen ',19:'Nineteen '}
        hundreds='Hundred'
        place = 0
        words=''
        teencheck=num%100
        if num in teens.keys():
            return teens[num].rstrip()
        while num!=0:
            word = ''
            if teencheck<20 and teencheck>10:
                words=teens[num%100]
                num=num/100
                place=2
            n=num%10
            num=int(num/10)
            if place == 0:
                word = units[n]
            elif place == 1:
                word = tens[n]
            elif place == 2:
                word = units[n]
                word = word+' '+hundreds+" "
            words= word+words
            place+=1
        return words.rstrip()
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if int(num) == 0:
            return "Zero"
        thenumber = str(num)
        powers = {0:"",1:" Thousand ",2:" Million ",3:" Billion "}
        shift = 1
        result = ""
        pointer = -1
        
        while pointer!=0:
            incr = 3
            pointer = len(thenumber)-3*shift
            if pointer<0:
                incr = 3 - abs(pointer)
            pointer = max(pointer,0)
            tripletword = self.writtenwords(int(thenumber[pointer:pointer+incr]))
            result = tripletword + ("" if tripletword == "" else powers[shift-1])+result
            shift+=1
        return result.rstrip()
def main():
    import sys
    num = sys.argv
    ret = Int2Words().numberToWords(int(num[1]))
    out = (ret)
    print out

if __name__ == '__main__':
    main()