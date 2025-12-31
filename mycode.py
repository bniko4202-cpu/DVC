import pandas as pd 
import os 

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)


new_row_loc = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}

df = pd.concat([df, pd.DataFrame([new_row_loc])], ignore_index=True)


os.makedirs('data', exist_ok = True)


file_path = os.path.join('data', 'sample_data.csv')

df.to_csv(file_path, index = False)

print(f"CSV file saved at: {file_path}")