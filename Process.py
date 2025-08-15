import pandas as pd
import subprocess

# Read the CSV file and convert it to JSON format
csv_file = 'bmi_patients.csv'
json_file = 'data.json'

df = pd.read_csv(csv_file, encoding='utf-8')
df.to_json(json_file, orient="records", force_ascii=False, indent=2)

# Running a Node.js script
result = subprocess.run(
    ['node', 'my_convert.js'],
    cwd=r'c:\Users\USER\Documents\Sample_to_FHIR',
    capture_output=True,
    text=True
)

# Output the result of the Node.js script
print("my_convert.js output:")
print(result.stdout)
if result.stderr:
    print("Errors:")
    print(result.stderr)