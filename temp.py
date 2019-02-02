import random
import os
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

print("Enter the number of quizfiles you want to create")
n = int(input())
os.chdir('/home/rohit/Documents/quiz')
for quiznum in range(n):
    #create quizfile and answerfile 
    quizfile = open('quiz%s.txt' % (quiznum + 1), 'w')
    ansfile  = open('answers%s.txt' % (quiznum + 1), 'w')
    
    quizfile.write('NAME :      \nCLASS :      \n')
    quizfile.write((" "*20) + 'state capital quiz\n')
        
    states = list(capitals.keys())
    random.shuffle(states)
    
    #create question on the basis of states defined
    for ques in range(50):
        #get right and wrong ans
        correctans = capitals[states[ques]]
        wrongans = list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans = random.sample(wrongans, 3)
        answeroptions = wrongans + [correctans]
        random.shuffle(answeroptions)
        
        #crete ansfile and quizfile
        quizfile.write('%s What is the capital of %s :\n' % (ques + 1, states[ques]))
        #write options 
        for i in range(4):
            quizfile.write('\n %s. %s\n' %('ABCD'[i], answeroptions[i]))
        quizfile.write('\n\n\n\n')
        #write ansfile
        ansfile.write('%s. %s\n' %(ques + 1, 'ABCD'[answeroptions.index(correctans)]))
          
        
    ansfile.close()
    quizfile.close()    
        
        
        
        
        
        
        
        
        
    