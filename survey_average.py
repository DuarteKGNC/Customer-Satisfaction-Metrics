import pandas as pd
import numpy as np
from sys import argv
from pathlib import Path

# Current path
current_path = Path(__file__).parent.absolute()

def calc(filename):

    try:

        file = pd.read_csv(str(current_path) + "/" + filename)
        dframe = pd.DataFrame(file)
        
        table = dframe['How satisfied are you with the support you received from Kognic?']

        number_of_replies = len(table)
        total_score = np.sum(table.array)

        score = "{:.2F}".format(np.abs(total_score / number_of_replies))

        print(f"""
              
    Score: {score} / 10
              
              """)

    except Exception as error:

        print("An error as occured")
        print(error)


if __name__ == '__main__':
    
    try:
        filename = argv[1]

        calc(filename=filename)
    except:
        if len(argv) <= 1:
            print("""
                  
                  [!][!]Don't forget to add the path to your file[!][!]
                  """)
            print(f"""
                  Use -> python3 survey_average.py [ path to your file ]
                  """)
            exit(1)

