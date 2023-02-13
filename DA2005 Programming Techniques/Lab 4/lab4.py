def main():
    '''
    This is the main body of the program.
    '''
    
    filename = input('Which csv file should be analyzed? ')

    data = dict()               # Or data = {}
    while True:
        try:
            with open(filename, 'r') as h:
                '''
                Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                '''
                for line in h:
                    try:
                        four_values = line.split(',') # Takes all the commas away from the .csv file and leaves only the raw data
                        if len(four_values) != 4:
                            raise ValueError("Line does not contain 4 values")
                        batch = four_values[0]
                        if not batch in data:
                            data[batch] = []
                        data[batch] += [(float(four_values[1]), float(four_values[2]), float(four_values[3]))] # Collect data from an experiment
                    except ValueError as e:
                        print("Warning:", e)
                        continue
                    print("Batch\t Average")
        except FileNotFoundError:
            print("File not found, please input another file name")
            filename = input('Which csv file should be analyzed? ')

        
    for batch, sample in data.items(): 
        n = 0
        x_sum = 0
        for (x, y, value) in sample:
            '''
            This is the part of the function in charge of the calculations of the average
            '''
            if x**2 + y**2 <= 1:
                x_sum += value
                n += 1
        if n == 0:
            print(f"Warning: No valid data for batch {batch}")
            continue
        average = x_sum/n
        print(batch, "\t", average)
            
        

# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()
