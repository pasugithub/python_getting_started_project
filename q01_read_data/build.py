import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    fname = './data/ipl_match.yaml'
    opn = open(fname,'r')
    data = yaml.load(opn)


    # return data variable
    return data

print read_data()
