import csv

def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'Revision': details[0].strip(),
                'Author': details[1].strip().replace('/OU=Domain Control Validated/CN=svn.company.net','Domain Control').replace('ajon0002','Jon').replace('murari.krishnan','Murari'),  #tidy up domain control
                'Date': details[2].strip(),
                'Number_of_lines': details[3].strip().split(' ')[0] #had to change dict to zero otherwise would show line or lines in CSV
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python_RF.log'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    # print(len(data))
    # print(commits)
    # print(commits[0])
    # print(commits[1]['author'])
    # print(len(commits))
    
keys = commits[0].keys()
with open('CA4_programming_output.csv','wb') as csv_CA4:
    write_to_dict = csv.DictWriter(csv_CA4,keys)
    write_to_dict.writeheader()
    write_to_dict.writerows(commits)