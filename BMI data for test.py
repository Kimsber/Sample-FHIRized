from faker import Faker
import pandas as pd

fake = Faker('zh_TW')
def generate_bmi_data(num_records, filename):
    fake = Faker('zh_TW')
    data = []
    for _ in range(num_records):
        gender = fake.passport_gender()
        if gender == 'M':
            last_name = fake.last_name_male()
            first_name = fake.first_name_male()
        else:
            last_name = fake.last_name_female()
            first_name = fake.first_name_female()
        dob = fake.date_of_birth()
        # Use gender-specific normal distributions for height and weight
        if gender == 'M':
            height_cm = round(max(150, min(200, fake.random.normalvariate(172, 7))), 1)
            weight_kg = round(max(50, min(120, fake.random.normalvariate(70, 10))), 1)
        else:
            height_cm = round(max(140, min(185, fake.random.normalvariate(160, 6))), 1)
            weight_kg = round(max(40, min(100, fake.random.normalvariate(58, 8))), 1)
        data.append({
            'Last Name': last_name,
            'First Name': first_name,
            'Gender': gender,
            'Date of Birth': dob,
            'Height (cm)': height_cm,
            'Weight (kg)': weight_kg,
        })
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Example usage:
# generate_bmi_data(10, 'bmi_patients.csv')