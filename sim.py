import numpy as np
import classes
import prerequisite as pre

#Just some variables here
hun = 100   
code_location = [""] * hun
code_commands = [""] * hun
code_operand1 = [""] * hun
code_operand2 = [""] * hun


#Just some Functions
def code_input () :
    
    line = ""
    i = 0
    while line != "HLT ".upper() : #stops sim program when 'hlt' is the input
        line = input().upper() + " "
        
        
        if ":" in line:
            code_location[i] = line[ : line.find(":") ]
            code_commands[i] = line[ line.find(":")+1 : line.find(" ")]
        else :
            code_commands[i] = line[ : line.find(" ") ]
    
        command_end_index = line.find(" ")
        print( command_end_index,  line[ command_end_index+1 : line.find(" ", command_end_index-1) ])
        # if "," in line :
        #     code_operand1[i] =  line[ command_end_index : line.find(",", command_end_index) ]
        # else :    
            
        #     code_operand1[i] =  line[ command_end_index : line.find(" ", command_end_index) ]

        i += 1
    print(code_operand1)


#Main function
def main() :
    
    code_input();


if __name__ == '__main__':
    main()
