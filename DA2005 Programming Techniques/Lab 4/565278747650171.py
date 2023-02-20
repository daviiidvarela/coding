'''
Comment on work:
    I broke the initial app into smaller functions. My thoughtprocess was that each function could be used for something else later in a project, so I wanted each function do only one specific thing. 
'''

import matplotlib.pyplot as plt

def main():
    '''
    This is the main body of the program.
    '''        
    
    while True:
        filename = input('Which csv file should be analyzed? ')    
        file_content = read_file(filename)
        if file_content == None:
            continue
        if cleanup_data_in_batch_file(file_content) != True:
            continue
        break
        
    sorted_readings_within_scope = sort_datapoints_by_batch(remove_datapoints_outside_scope(file_content))
    
    if len(sorted_readings_within_scope) < 1:
        print("There was no data within the scope in this file")
    else:
        print(datapoints_to_string(sorted_readings_within_scope))
    
    while True:
        save_file_location = input('location to store plotted data (filename.pdf): ')
        if save_file_location != None:
            break;
        
    sorted_readings_complete = sort_datapoints_by_batch(file_content)
    plot_data(sorted_readings_complete, save_file_location)
            

def read_file(filename):
    '''
    Parameters
    ----------
    filename : Type: string, refers to filepath of target CSV file.

    Returns
    -------
    file_content : [[string]], refers to the conntent of filepath. Returns None if unsuccessfull
    
    Does
    ------
    Reads the content of a CSV file and returns a list of lists with its content.
    ignores lines with less or more 4 values per line, threated as invalid. 
    

    '''
    file_content = []
    
    try:
        with open (filename, 'r') as file:
            for line in file:
                current_batch = line.strip().split(',')    
                if len(current_batch) != 4: #Strips corrupt lines of data.
                    print("INFO ===> Invalid format of current line, will _not_ be loaded: " + str(current_batch))
                    continue
                file_content.append(current_batch)
    except:
        print("Unable to open a file on that filepath")
        return None
    
    if len(file_content) < 1:
        print("Could not load, found no valid data in input file")
        return None
        
    return file_content

def cleanup_data_in_batch_file(file_content):
    '''
    Parameters
    ----------
    file_content : [[string]]

    Returns
    -------
    True if successfull, False if fails or there is no valid data in file_content
    
    Does
    ------
    
    Takes the readings from read_file() and turns the data into correct formats

    '''
    invalid_entries = []
    
    for entry in file_content:
        try:
            entry[0] = int(entry[0])
        except:
            invalid_entries.append(entry)
            continue
        
        try:
            entry[1] = float(entry[1])
        except:
            invalid_entries.append(entry)
            continue
        
        try:
            entry[2] = float(entry[2])
        except:
            invalid_entries.append(entry)
            continue
        
        try:
            entry[3] = float(entry[3])
        except:
            invalid_entries.append(entry)
            continue
        
    if len(file_content) - len(invalid_entries) < 1:
         print("ERROR ===> No valid data found")
         return False
        
    if len(invalid_entries) > 0:
        print("INFO ===> Following entry contains corrupt data, is removed:")
        for entry in invalid_entries:
            print("=>\t\t " + str(entry))
            file_content.remove(entry)
    
    return True      

                
def avg_data_per_batch(batch_of_datapoints):
    '''
    Parameters
    ----------
    batch_of_datapoints : Type: [[int, float, float, float]], refers to a single batch of multiple readvalues
        
    Returns
    -------
    TYPE : Float, refers to the avg of all readvalues. Returns None if unsuccessfull 
    
    Does
    ------
    Sums the values of the last value in all input lists. returns the avg of those values.
    '''
    
    total_value = 0.0
    for measurment in batch_of_datapoints:
        try:
            total_value += measurment[2]
        except:
            print("Error ===> Cannot calculate avg on value: " + measurment[2])
            batch_of_datapoints.remove(measurment)
        
        if len(batch_of_datapoints) < 1:
            return None
        
    return total_value/len(batch_of_datapoints)
    
            
def remove_datapoints_outside_scope(file_content):
    '''
    Parameters
    ----------
    file_content : [[int, float, float, float]]

    Returns
    -------
    list_of_readings_within_scope : [[int, float, float, float]]. If no datapoints within scope, returns None
    
    Does
    -----
    Iterates over input datapoints and remove those who are outside of the target scope. 

    '''
    SCOPE = 1
    
    list_of_readings_removed = []
    list_of_readings_within_scope = []
    
    for batch in file_content:
        if batch[1]**2 + batch[2]**2 > SCOPE:
            list_of_readings_removed.append(batch)
        else:
            list_of_readings_within_scope.append(batch)             
    
    if len(file_content) - len(list_of_readings_removed) < 1:
        print("Error ===> No valid data found")
        return None
    
    if len(list_of_readings_removed) > 0:
        print("INFO ===> Following datapoints are out of scope, is ignored: ")
        for batch in list_of_readings_removed:
            print("=>\t\t " + str(batch))
            
    return list_of_readings_within_scope

def sort_datapoints_by_batch(batches_of_datapoints):
    '''

    Parameters
    ----------
    batches_of_datapoints : [[int, float, float, float]], refers to one or more batches of readvalues. Multiple readvalues from same batch will appear in multiple lines

    Returns
    -------
    sorted_dict_of_datapoints : Dict (Key = integer, value = list[float, float, float]). Adds all readings as values to their batch (key)
    
    Does
    ------
    Sorts data in a dict with batches (first value in every list) as keys and x-, y- coordinates and value as a list as value. 

    '''

    sorted_dict_of_datapoints = {}
    for batch in batches_of_datapoints:
        if int(batch[0]) in sorted_dict_of_datapoints.keys():
            sorted_dict_of_datapoints[batch[0]].append([batch[1], batch[2], batch[3]])
        else:                                                     
            sorted_dict_of_datapoints[batch[0]] = [[batch[1], batch[2], batch[3]]]     
    return sorted_dict_of_datapoints


def datapoints_to_string(sorted_dict_of_datapoints):
    '''
    Parameters
    ----------
    sorted_dict_of_datapoints :  Dict (Key = integer, value = [[int, float, float, float]]), refers to batches of readvalues

    Returns
    -------
    String of input values to presented to user in some form. 
    
    '''
    
    string_to_return = "Batch\t Average\n" 
    
    ## Sorts keys in order to present them in descending order 
    keys_in_dict = list(sorted_dict_of_datapoints.keys())
    keys_in_dict.sort()
    
    ##Loops through each key and adds it and its avg_data to the return string
    for key in keys_in_dict:
        string_to_return += str(key)
        string_to_return += "\t\t\t"
        string_to_return += str(avg_data_per_batch(sorted_dict_of_datapoints[key]))
        string_to_return += "\n"
    return string_to_return
            

def plot_data(data, save_file_location):
    '''
    Parameters
    ----------
    data : Dict with int as key and [[float, float,float]] as values
    save_file_location : String
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    list_of_colors = ["#FF5733", "#BE33FF", "#FFBD33", "#DBFF33", "#33FFBD", "#FDFF33" ]   
    
    #Loops through batches if input and plots them and their values. 
    color_counter = 0   
    for key, value in data.items():
        for readings in value:
            plt.text(readings[0], readings[1], str(readings[2]))
            plt.plot(readings[0], readings[1], 'ro', color = list_of_colors[color_counter])
        color_counter +=1
    
    #Circle code is "stolen" from: https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot
    circle = plt.Circle((0,0), radius = 1.0, color='#99FFFF')
    plt.gca().add_patch(circle)
    plt.show()
    
    try:
        plt.savefig(save_file_location)  
    except:
        print("ERROR ===> Invalid savelocation. Saving as sample_print.pdf instead")
        plt.savefig("sample_print.pdf") 


# Start the main program: this is idiomatic python
if __name__ == '__main__':
    main()


# Try it out by importing this file into another project!
    
