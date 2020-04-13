

import sys
import random

## Usage python3 dummy_code_generator.py [num_lines] [name of output file]
indivisible_cmds = ["print(Hello)","x = 1","print(this is a dummy program)"]
branch_cmds = ["for(something) {","while(something) {","if(something) {"]
MAX_NEST = 1
MAX_BRANCH_CALLS = 2

def write_cmd(file):
    file.write(random.choice(indivisible_cmds) + "\n")

def write_branch(file,nestedLevel):
    file.write(random.choice(branch_cmds) + "\n")
    branchCalls = 0
    for i in range(50):
        generate_branch = bool(random.getrandbits(1))
        if (generate_branch and nestedLevel < MAX_NEST and branchCalls < MAX_BRANCH_CALLS):
            branchCalls += 1
            write_branch(file,nestedLevel+1)
        else:
            write_cmd(file)
    file.write("}\n")


def gen_txt_file(num_lines,file_name):

    file = open(file_name,"w")
    for i in range(num_lines):
        generate_branch = bool(random.getrandbits(1))
        if (generate_branch):
            write_branch(file,0)
        else:
            write_cmd(file)

    file.close()


def main():
    # Number of cmds to generate. branch cmds are considered to be one command
    num_lines = int(sys.argv[1])
    file_name = sys.argv[2]
    gen_txt_file(num_lines,file_name)

if __name__ == "__main__":
    main()
