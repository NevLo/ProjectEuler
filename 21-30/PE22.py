# Project Euler problem 22

# Using PE22_names.txt, a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

alphanumeric = {'a':1, 'b':2, 'c':3, 'd':4,
                'e':5, 'f':6, 'g':7, 'h':8,
                'i':9, 'j':10,'k':11,'l':12,
                'm':13,'n':14,'o':15,'p':16,
                'q':17,'r':18,'s':19,'t':20,
                'u':21,'v':22,'w':23,'x':24,
                'y':25,'z':26}

def findNameScore(str, ind):
    sum = 0
    for i in range(len(str)):
        sum += alphanumeric.get(str[i])
    return sum * (ind + 1)

if __name__ == "__main__":
    filepath = "C:\\Users\\39241\\OneDrive - Renown Health\\Desktop\\PE\\ProjectEuler\\21-30\\PE22_names.txt"
    f = open(filepath, "r")
    names = f.read()
    names = names.replace("\"", "")
    names = names.lower()
    names = names.split(",")
    names.sort()
    sum = 0
    for i in range(len(names)):
        sum += findNameScore(names[i],i)

    print(f"The total namescore of the list is: {sum}")