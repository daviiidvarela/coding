class train_sim:
    def __init__(self):
        self.data = {}
        self.stops = set()
        self.connections = ""
        self.current_time = 0
        self.trains = []

    def station_check(self):
        stations = input("Enter name of stations file: ")
        while True:
            try:
                with open(stations, 'r') as h:
                    data = {}
                    '''
                    Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                    '''
                    for line in h:
                        try:
                            location, delay_prob = line.strip().split(',')
                            delay_prob = float(delay_prob)
                            if isinstance(location, int):
                                raise TypeError("There is row that contains an integer in the location column, the location column can only contain letters or words.")
                            if 0 <= delay_prob <= 1:
                                if location not in self.stops:
                                    self.stops.add(location)
                                if not location in self.data:
                                   self.data[location] = []
                                self.data[location]+= [(float(delay_prob))]
                        except TypeError as e:
                            print("Warning:", e)
                            continue
                return self.data

            except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
                print("File not found, please input another file name.") 
                stations = input('Enter name of stations file: ')
                continue
            break

    def connections_check(self):
        self.connections = input("Enter name of connections file: ")    
        while True:
            try:
                with open(self.connections, 'r') as h:
                    '''
                    Opens the specified file and goes line by line to add entries in the new dictionary called 'data'
                    '''
                    for line in h:
                        try:
                            self.start_connection, self.end_connection, self.line_color, self.direction = line.strip().split(',') 
                            if isinstance(self.start_connection or self.end_connection or self.line_color or self.direction, int):
                                raise TypeError("There is row that contains an integer in one of the columns, the connections columns can only contain letters or words.")
                        except TypeError as e:
                            print("Warning:", e)
                            continue
                        return self.start_connection, self.end_connection, self.line_color, self.direction

            except FileNotFoundError: # When FileNotFoundError arrises, then the program asks the user to put in another file name
                print("File not found, please input another file name.") 
                self.connections = input('Enter name of connections file: ')
                continue
            break

    def trains_check(self):
        while True:
            trains = input("Enter how many trains to simulate: ")
            try:
                self.integer_input = int(trains)
            except ValueError:
                print("Invalid input. Please enter an integer.")
            return self.integer_input
    
    def create_trains(self):
        import random
        trains = self.integer_input
        stations = self.data

        self.train_dict = {}
        directions = {'N', 'S'}
        for i in range(1, trains+1):
            station = random.choice(list(stations.keys()))
            self.train_dict[f"train{i}"] = station
            
        return self.train_dict

    def user_decision(self):
        user_decision = print('Continue simulation [1], train info [2], exit [q].')
        try:
            if user_decision == 1:
                self.move_train()
            elif user_decision == 2:
                divmo
            elif user_decision == 'q':
                pass
        except TypeError as e:
            print("Warning:", e)
        

            
    def move_train(self, current_location, destination):
        import random
        """
        Moves the train from the current location to the specified destination.
        Returns True if the move was successful, False otherwise.
        """
        # Check if the specified destination is a valid connection from the current location
        if destination not in self.data[current_location]:
            print(f"Error: {destination} is not a valid destination from {current_location}.")
            return False
        
        # Move the train to the new location
        self.train_location = destination
        
        # Update the train's delay based on the delay probability of the new location
        delay_prob = self.data[destination]
        if random.random() < delay_prob:
            self.train_delayed = True
            print(f"Train is delayed at {destination}!")
        else:
            self.train_delayed = False
        
        # Print a message indicating that the train has moved
        #print(f"Train moved from {current_location} to {destination}.")
        return True
    
    def advance_time(self):
        # update the current time by one unit
        self.current_time += 1
        # or you might move trains along their routes based on the current time and the schedule



def traincode():
    train_functions = train_sim()
    train_functions.station_check()
    train_functions.connections_check()
    train_functions.trains_check()
    train_functions.create_trains()


traincode()