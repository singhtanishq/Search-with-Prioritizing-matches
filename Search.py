#Program that accepts number of lines from user
#Ask for keyword to search line
#Display lines one by one as per users demand
#In sequence of maximum matches intelligently

#importing time module
import time

#initialising identifiers
l=list()
upd_lst=list()
count_lst=list()
index_lst=list()
count=0
index=0    
ask='y'

#using while loop for accepting number of lines
while ask=='y':
    ent=input('Enter any sentence or phrase: ')
    print()
    #appending lines into a list
    l.append(ent)
    #asking if user needs to add more lines
    print('Do you want to add more sentence or phrase')
    ask=input('Enter (y/n): ')
    print()

#using for loop to eliminate duplicate lines    
for line in l:
    #only add lines in new list if it doesn't exist
    if line not in upd_lst:
        upd_lst.append(line)
    else:
        pass

#displaying the completion of task    
print('Data added successfully')
print()

#displaying all lines from updated list
print('Lines are as follows:-')
for line in upd_lst:
    print(line)
print()    

#asking for keyword to search line
key=input('Enter search key: ')

#using for loop for searching
for line in upd_lst:
    #updating count to be 0 each time in a loop
    #so that frequency can be counted for each line
    count=0
    #counting number of keyword matches
    for word in line.split():
        if word==key:
            count+=1
        else:
            pass
    #appending frequency of each line in count_lst
    #in their original sequence
    count_lst.append(count)

#using for loop to create list that contains index
#of line in order of frequency
for num in range(len(count_lst)):
    #finding maximum count each time
    max_count=max(count_lst)
    if max_count==0 or max_count==-1:
        None
    #if it's not zero or minus one
    else:
        #finding index of line having maximum matches
        index=count_lst.index(max_count)
        #changing it's value to be -1 to avoid repetition
        count_lst[index]=-1
        #appending index one by one
        #this list contains index of line
        #in order of frequency
        index_lst.append(index)

#to show some animation of searching for 2 seconds
#so that it looks even more realistic
print()
print('Searching...')
time.sleep(2)

#extracting the line having maximum matches
temp_index=index_lst[0]
temp_count=count_lst[temp_index]

#case of no matches
if temp_count==0:
    print('Oops! No results found')
#case in which some matches are found
else:
    print('Found Results as:')
    print('     ',upd_lst[index_lst[0]])

#deleting that line so that it could not be printed again    
del index_lst[0]

#showing results one by one
#asking user whether they found required result or not   
for num in index_lst:
    print('Is this the line you were searching for?')
    ask=input('Enter (y/n): ')
    #if user found what they were searching
    if ask=='y':
        #clearing index list to end process
        index_lst=[0]
        #printing successful completion
        print('Search Operation Completed Successfully')
        break
    #if user not satisfied with result
    #then showing next most appropriate result
    elif ask=='n':
        print('     ',upd_lst[num])
    #to handle error if user does
    else:
        print('ERROR')
        print('Invalid reply')

#if user does not find appropriate result
#and all results has been already shown
#then displaying operation completion        
if ask=='n':
    print('Search Operation Completed Successfully')
else:
    None
