# Toni Dumancic Test Task
# Mar 14
from hashlib import sha256
import sys

string = sys.argv[1]

complete = False
n = 0
print("Statred script!")
# While loop for finding right hash
while complete == False:
    #format(n, 'x') is to make n to hex
    curr_string = format(n, 'x') + string
    # this is our current hash
    curr_hash = sha256(curr_string.encode()).hexdigest()
    n = n + 1
    #this is to print everything
    print('prefix: ' + format(n, 'x') + ' original_string: ' + string + ' current_hash: ' + curr_hash + ' ' + curr_hash[-4:])
    if curr_hash[-4:] == "cafe":

        print('prefix: ' + format(n, 'x') + ' original_string: ' + string + ' current_hash: ' + curr_hash + ' ' + curr_hash[-4:])
        print(curr_hash)

        # to stop loop
        complete = True
