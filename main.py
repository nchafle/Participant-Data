
ParticipantNumber = 10
participantData = []
outputFile = open("ParticipantData.txt","w")

registeredParticipant = 0

while (registeredParticipant < ParticipantNumber):
    tempPartData = []  # name of the country of origin,age
    name = input("Please enter the your name: ")
    tempPartData.append(name)
    country = input("Please enter you country name: ")
    tempPartData.append(country)
    age = int(input("please enter your age: "))  #int("25") => 25
    tempPartData.append(age)


    participantData.append(tempPartData) #[tempPartData] = [[name, country, age]]
    registeredParticipant +=1
    print(participantData)

for participant in participantData:
    for data in participant:
        outputFile.write(str(data))  #str(25) => "25"
        outputFile.write(" ")          # nk nk 25
                                        #teja teja 30
    outputFile.write("\n")
outputFile.close()

inputFile = open("ParticipantData.txt",'r')
inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()  #"NK NK 26 \n".strip('\n') => "NK Nk 21"
                                                #"NK NK 26".split() => ["NK","NK",26]
    print(tempParticipant)
    inputList.append(tempParticipant)

Age = {}
for part in inputList:
    tempAge = int(part[-1]) #int('26') => 26
    if tempAge in Age:
        Age[tempAge] +=1
    else:
        Age[tempAge] = 1
print(Age)

oldest = 0
youngest = 100
mostOccutingAge = 0
counter = 0
for tempAge in Age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge <youngest:
        youngest = tempAge
    if Age[tempAge]>= counter:
        counter = Age[tempAge]
        mostOccutingAge = tempAge

print("oldest member:",oldest)
print("youngest member:",youngest)
print("most occuring ",mostOccutingAge)


Countries = {}
for part in inputList:
    tempCountry = part[1]
    if tempCountry in Countries:
        Countries[tempCountry] +=1
    else:
        Countries[tempCountry] = 1
print("Countries that attened",  Countries)
inputFile.close()






