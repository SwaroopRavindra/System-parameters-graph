import textfsm
import os

cmd = 'top -bn 1 > /home/swaroop/POC/top_output.txt'
os.system(cmd)

# Load the input file to a variable
input_file = open("top_output.txt", encoding='utf-8')
raw_text_data = input_file.read()
# print('\n***Raw data***\n', raw_text_data)
input_file.close()

# Run the text through the FSM. 
# The argument 'template' is a file handle and 'raw_text_data' is a 
# string with the content from the top_output.txt file
template = open("top.textfsm")
re_table = textfsm.TextFSM(template)
# print(re_table)
fsm_results = re_table.ParseText(raw_text_data)

# print("\n##########\n")
# print(fsm_results)
current_cpu = fsm_results[1][1]
current_memory = fsm_results[2][7]
# print("current_cpu : ",current_cpu)
# print("current_mem : ",current_memory)
# # The results are written to a CSV file
# outfile_name = open("outfile.csv", "w+")
# outfile = outfile_name

# # Display result as CSV and write it to the output file
# # First the column headers...
# #import pdb; pdb.set_trace()
# print(re_table.header)
# for s in re_table.header:
#     outfile.write("%s;" % s)
# outfile.write("\n")

# #...now all row's which were parsed by TextFSM
# counter = 0
# for row in fsm_results:
#     print(row)
#     for s in row:
#         outfile.write("%s;" % s)
#     outfile.write("\n")
#     counter += 1