from process_changes_RF import Commit

output = open("CA4_programming_output",'w')
index = 0
for commit in commits:
    output.write(commits[index]['author'])
    output.write(';')
    output.write(commits[index]['revision'])
    output.write(';')
    output.write(commits[index]['date'])
    output.write(';')
    output.write(commits[index]['number_of_lines'])
    output.write(';')
    output.write(commits[index]['comment'])
    output.write(';')
    output.write(commits[index]['change'])
    output.write('\n')
    index += 1
output.close()