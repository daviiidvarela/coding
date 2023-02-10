# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, -0.01, 17
# 2, 0.9, 0.82, 23
#
# Pretend this is taken from two (or more) different experiments:
# batch 1 and batch 2.

            
def main():
    '''
    This is the main body of the program.
    '''
    
    filename = input('Which csv file should be analyzed? ')

    data = dict()               # Or data = {}
    with open(filename, 'r') as h:
        '''
        Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
        '''
        for line in h:
            four_values = line.split(',') # Takes all the commas away from the .csv file and leaves only the raw data
            batch = four_values[0]
            if not batch in data:
                data[batch] = []
            data[batch] += [(float(four_values[1]), float(four_values[2]), float(four_values[3]))] # Collect data from an experiment

    print("Batch\t Average")
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
            average = x_sum/n
        print(batch, "\t", average)

        

# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()

# The idea with this idiom is that if this code is loaded as a module,
# then the __name__ variable (internal to Python) is not __main__ and
# the body of the program is not executed. Consider what would happen
# if the main function was not in a function: an import statement (for
# example "import o4") would load the functions and then executed
# "filename = input(...)" and that is probably not what you want. The
# idiom is simply an easy way of ensuring that some code is only
# executed when run as an actual program.
#
# Try it out by importing this file into another project!
    
