import pandas as pd
import subprocess

# Read the CSV file and convert it to JSON format
csv_file = 'bmi_patients.csv'
json_file = 'data.json'

df = pd.read_csv(csv_file, encoding='utf-8')
df.to_json(json_file, orient="records", force_ascii=False, indent=2)

# Running a Node.js script
js_file = "my_convert.js"
working_dir = r"c:/Users/USER/Documents/Sample_to_FHIR"

try:
    result = subprocess.run(
        ['node', js_file],
        cwd=working_dir,
        capture_output=True,
        text=True,
        check=True,
        encoding='utf-8'
    )
    # Output the result of the Node.js script
    print("my_convert.js output:\n", result.stdout)
    if result.stderr:
        print("my_convert.js errors:\n", result.stderr)
except subprocess.CalledProcessError as e:
    print("Error running my_convert.js:")
    print(e.stderr)
