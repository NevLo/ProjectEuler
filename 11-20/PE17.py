# Project Euler problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numDict =    {1: "One",         2: "Two",       3: "Three", 
              4: "Four",        5: "Five",      6: "Six", 
              7: "Seven",       8: "Eight",     9: "Nine",      
              11: "Eleven",     12: "Twelve",   13: "Thirteen", 
              14: "Fourteen",   15: "Fifteen",  16: "Sixteen",  
              17: "Seventeen",  18: "Eighteen", 19: "Nineteen", 
              10: "Ten",        20: "Twenty",   30: "Thirty",   
              40: "Forty",      50: "Fifty",    60: "Sixty",    
              70: "Seventy",    80: "Eighty",   90: "Ninety",   
              100: "Hundred",   1000: "OneThousand"}

if __name__ == "__main__":
    sum = 0
    for i in range(1,1001):
        if(i < 101):
            if(i not in numDict):
                tens = i // 10 * 10
                ones = i % 10
                letterSum = numDict.get(tens) + numDict.get(ones)
                numDict.update({i:letterSum})    
        elif(i<1001):
            if(i not in numDict):
                hundreds = i // 100
                tens = i % 100
                letterSum = numDict.get(hundreds) + numDict.get(100)
                if(tens != 0):
                    letterSum += "And" + numDict.get(tens)
                numDict.update({i:letterSum})
    numDict.update({100:"OneHundred"})
    for i in range(1,len(numDict)+1):
        #print(f"i: {i} > {numDict.get(i)} \t> {len(numDict.get(i))}")
        sum += len(numDict.get(i))
    print(f"The number of letters used in the words from 1-1000 is: {sum}")