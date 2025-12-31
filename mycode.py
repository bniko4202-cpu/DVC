import pandas as pd 
import os 

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)



os.makedirs('data', exist_ok = True)


file_path = os.path.join('data', 'sample_data.csv')

df.to_csv(file_path, index = False)

print(f"CSV file saved at: {file_path}")