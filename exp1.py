# -*- coding: utf-8 -*-
import random
def generateSamplesFromNormalDistribution(sampleNum):
    mean = 60
    std = 10
    samples = {}
    passClass = {}
    failClass = {} 
    print "Random select ",sampleNum," samples from Normal Distribution..."
    for i in range(0,sampleNum):
        score = random.normalvariate(mean,std)
        samples[i] = score
        if score >= 60:
            passClass[i] = score
        else:
            failClass[i] = score
    print "Sample from Normal Distribution is done..."
    print "The number of ",len(passClass)," students from samples pass the class"
    print "The number of ",len(failClass)," students from samples fail the class"
    return samples,passClass,failClass
def KNN(test_data,training_data):
    # using odd value to prevent conflict of determination in two classes
    k = 101
    distances = {}
    #compute the test data distances between each trainging_data
    misClassified = 0
    CorrectClassified = 0
    f = file("victim.txt","w")
    f.write('student_id:score\n')
    for test_num,test_score in test_data[0].iteritems():
        for num,score in training_data[0].iteritems():
            distance = abs(test_score-score)
            distances[num] = distance
        #In order to select the k neighborhood,we must sort the distance first (in ascending order)
        candidate = sorted(distances.iteritems(),key = lambda(k,v):(v,k))
        neighborhood = candidate[0:k]
        #now determine the class of test data from neighborhood
        ispass = 0
        isfail = 0
        for num,score in neighborhood:
            if num in training_data[1].keys():  #if the training data(neighborhood) in pass class
               ispass = ispass+1
            else:
               isfail = isfail+1
        if ispass>isfail:
        #take the student into PassClass
            if test_num not in test_data[1].keys():
                print "misClassified!!! Predict student id = ",test_num," score = ",test_score," into pass class"
                f.write(str(test_num))
                f.write(str(':'))
                f.write(str(test_score))
                f.write('\n')
                misClassified = misClassified+1
            else:
                print "Predict student id = ",test_num," score = ",test_score," into pass class"
                CorrectClassified = CorrectClassified+1
            #print "the student with score ",test_data," will pass"
        else:
            #print "the student with score ",test_data," will fail"
            if test_num not in test_data[2].keys():
                print "misClassified!!! Predict student id = ",test_num," score = ",test_score," into fail class"
                f.write(str(test_num))
                f.write(str(':'))
                f.write(str(test_score))
                f.write('\n')
                misClassified = misClassified+1
            else:
                print "Predict student id = ",test_num," score = ",test_score," into fail class"
                CorrectClassified = CorrectClassified+1
    f.close()
    return CorrectClassified,misClassified


print 'you can press <Ctrl-C> to terminate experiment'
training_data = generateSamplesFromNormalDistribution(100000)
test_data = generateSamplesFromNormalDistribution(1000)
performance = KNN(test_data,training_data)
