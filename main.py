import csv



def read_data():
    aux = ""
    dic = {}
    with open('stops_data.csv', 'r') as file:
        reader = csv.reader(file, delimiter = "\t")
        for row in reader:
            print(row)
            for x in row:
                for y in x:
                    aux +=y
                    print(aux)
            exit()



read_data()