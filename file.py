import numpy as np


# initialize student records with random value

def initialize_data():

    # create a subject array

    subject = np.array(['English', 'Maths', 'Science', 'Social', 'History'])

    # create a student array

    students = np.array(['Alice', 'Bob', 'Charlie', 'Dan'])

    marks = np.array([[81, 78, 80, 60, 63],

                      [50, 40, 65, 48, 65],

                      [30, 83, 97, 97, 75],

                      [99, 55, 60, 58, 30]])


    # generate random marks for each student and subject

    # marks = np.random.randint(30, 101, size=(len(students), len(subject)))


    return subject, students, marks


# add new student record by taking input from user

def add_record(studentArray, subjectArray, marksArray):

    print('\n Add New Student Data\n')

    # get student's name

    studentName = input('Student Name : ')

    # initialize an empty marks array of same length as subject

    marks = np.empty(len(subjectArray), dtype=int)

    # get inputs from the user

    for i in range(len(subjectArray)):

        marks[i] = int(input(f"Enter marks for {subjectArray[i]}: "))

    # append new student to studentArray

    studentArray = np.append(studentArray, studentName)

    # append marks of new student to studentArray

    marksArray = np.vstack((marksArray, marks))

    return studentArray, marksArray


# display the record in visually pleasing form

def display_record(studentArray, subjectArray, marksArray):

    

    # create a new Array for Total, Average and Result    

    # calculate total marks for each student

    totalArray = np.sum(marksArray, axis=1)

    # calculate average marks for each student

    avgArray = np.mean(marksArray, axis=1)

    # check if all marks in a row are >= 40 and assign 'Pass' or 'Fail' accordingly

    resultArray = np.where(np.all(marksArray >= 40, axis=1), 'Pass', 'Fail')

    

    # add Total, Average and Grade to header

    headerArray = np.hstack(('Student/Subject', subjectArray, np.array(['Total', 'Average', 'Result'])))

    header = "|".join(headerArray)

    print(header)

    

    # create a lengthArray for formatting purpose

    lengthArray = np.array([len(element) for element in headerArray])

    

    # print the separator line

    separator = "+".join(["-" * length for length in lengthArray])

    print(separator)

    

    # print the marks for each student

    for i, student in enumerate(studentArray):

        row = f"{student :<{lengthArray[0]}}"

        row += ''.join(f"|{mark:<{lengthArray[col+1]}}" for col, mark in enumerate(marksArray[i]))

        # add Total, Average and Pass result for each student

        row += "|" + f"{totalArray[i]:<{lengthArray[6]}}" 

        row += "|" + f"{avgArray[i]:<{lengthArray[7]}}" 

        row += "|" + f"{resultArray[i]:<{lengthArray[8]}}" 

        print(row)

    print(separator)


def obtain_results(studentArray, subjectArray, marksArray):

    

    # data part

    #  average marks for each subject

    avgSubject = np.mean(marksArray, axis=0)

    

    # deviation and variation of marks

    stdSubject = np.std(marksArray, axis = 0)

    varSubject = np.var(marksArray, axis = 0)

    stdStudents = np.std(marksArray, axis = 1)

    varStudents = np.var(marksArray, axis = 1)

    

    # top and bottom performing student 

    topPerformer =  studentArray[np.argmax(np.sum(marksArray, axis=1))]

    bottomPerformer =  studentArray[np.argmin(np.sum(marksArray, axis=1))]

    

    # subject comparison

    easiestSubject = subjectArray[np.argmax(avgSubject)]

    hardestSubject = subjectArray[np.argmin(avgSubject)]

    

    # overall performance

    totalAverage = np.mean(marksArray)

    totalStd = np.std(marksArray)

    totalVar = np.var(marksArray)

    

    # analysis and visualization part

    # total number of students

    print('Total Number of students: ', len(studentArray))

    

    # average marks for each subject

    print('\nAverage Marks in Each Subject')

    for i,subject in enumerate(subjectArray):

        print('\t',subject,':', avgSubject[i])

    

    # deviation and variation of marks

    print('\nStandard Deviation and Variance per Subject')

    header = np.array(['Subject Name','Standard Deviation','Variance'])

    print("|".join(header))

    # print the separator line

    separator = "+".join(["-" * len(item) for item in header])

    print(separator)

    for i, subject in enumerate(subjectArray):

        row = f"{subject :<{len(header[0])}}" +'|'+ f"{stdSubject[i] :<{len(header[1])}}" + '|' + f"{varSubject[i] :<{len(header[2])}}"

        print(row) 

    

    print('\nStandard Deviation and Variance per Student')

    print("|".join(header))

    # print the separator line

    print(separator)

    for i, student in enumerate(studentArray):

        row = f"{student :<{len(header[0])}}" +'|'+ f"{stdStudents[i] :<{len(header[1])}}" + '|' + f"{varStudents[i] :<{len(header[2])}}"

        print(row)

   

    # top and bottom performing student 

    print('\nTop performer: ', topPerformer)

    print('Bottom performer:', bottomPerformer)

    

    # subject comparison

    print('\nEasiest Subject:',easiestSubject, '\nHardest Subject:',hardestSubject)

    

    # overall performance

    print('\nMetrics across all Students and Subjects')

    print('Average Marks: ',totalAverage, '\nStandard Deviation: ',totalStd, '\nVariance: ',totalVar)

    

def main():

    subject, students, marks = initialize_data()

    while(1):

        print('-'* 75)

        choice = int(input('1. Press 1 to Display Student Results\n2. Press 2 to Add a new Student Record\n3. Press 3 to Display Analyzed Results\n4. Press 4 to Exit\n\n'))

        print('-'* 75)

        if(choice == 1):

            display_record(students, subject, marks)

        elif(choice == 2):

            students,marks = add_record(students, subject, marks)

        elif(choice == 3):

            obtain_results(students, subject, marks)

        elif(choice == 4):

            break

        else:

            print('Invalid Choice')

main()