
def calculateGrade():
    score = input("Enter score:")
    try:
        if float(score) >= 0.9:
            print('A')
        elif float(score) >= 0.8:
            print('B')
        elif float(score) >= 0.7:
            print('C')
        elif float(score) >= 0.6:
            print('D')
        elif float(score) < 0.6:
            print('F')
    except:
        print('Bad grade')
    
    # Implement your solution in between the two comment blocks
##print("Calculating Grade")
    # This first line is provided for you

    


    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()