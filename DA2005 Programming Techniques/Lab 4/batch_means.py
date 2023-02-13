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
                    
        except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
            print("File not found, please input another file name") 
            filename = input('Which csv file should be analyzed? ')
            continue
        break
 
    print("Batch\t Average")
    sorted_data = sorted(data.items(), key=lambda x:x[0])
    for batch, sample in sorted_data: 
        n = 0
        x_sum = 0
        for (x, y, value) in sample:
            '''
            This is the part of the function in charge of the calculations of the average
            '''
            if x**2 + y**2 <= 1:
                x_sum += value
                n += 1
        if n == 0: # This if function prints that there is not data from a given batch
            print(f"Warning: No valid data for batch {batch}") 
            continue # Then the program continues without the unusable data
        average = x_sum/n
        print(batch, "\t", average)

        import matplotlib.pyplot as plt # Imports matplotlib to plot the graph

        def plot_data(data, filename):
            for batch, sample in data.items():
                x = [x for (x, y, value) in sample if x**2 + y**2 <= 1] # The x value of each measurement
                y = [y for (x, y, value) in sample if x**2 + y**2 <= 1] # The y value of each measurement
                plt.scatter(x, y)
            plt.title("Unit Circle Plot") # Title
            plt.xlabel("X") # X and Y labels respectively
            plt.ylabel("Y")
            plt.savefig(filename) # Saves the data into a chosen filename
            plt.show() # Shows the graph



        

# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()
    plot_data(data, 'sample4pdf')

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
    
