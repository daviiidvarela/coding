#import pandas as pd
#data = pd.io.stata.read_stata('MA2.dta')
#data.to_csv('MA2.csv')

import os
import pandas as pd

folder_path = '/Users/davidvarela/Downloads/SIGI/BF and UG/SIGI Uganda/SIGI Uganda Individual Questionnaire Data'
for filename in os.listdir(folder_path):
    if filename.endswith('.dta'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_stata(file_path)
        csv_file = os.path.splitext(file_path)[0] + '.csv'
        df.to_csv(csv_file, index=False)
