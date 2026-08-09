# Run: python medica_validator.py
import re

# Sample medical records
medical_records = [
    {
        "patient_id": "P1001",
        "age": 34,
        "gender": "Female",
        "diagnosis": "Hypertension",
        "medications": ["Lisinopril"],
        "last_visit_id": "V2301"
    },
    {
        "patient_id": "1002",          # Invalid
        "age": -10,                    # Invalid
        "gender": "Unknown",           # Invalid
        "diagnosis": "",
        "medications": "Metformin",    # Invalid
        "last_visit_id": "2302"        # Invalid
    },
    {
        "patient_id": "P1003",
        "age": 29,
        "gender": "Female",
        "diagnosis": "Asthma",
        "medications": ["Albuterol"],
        "last_visit_id": "V2303"
    }
]

#--------------------------------------
# Validate one medical record
#--------------------------------------
def find_invalid_records(patient_id,
                         age,
                         gender,
                         diagnosis,
                         medications,
                         last_visit_id):

    constraints = {

        "patient_id":
            isinstance(patient_id, str)
            and re.fullmatch(r"P\d+", patient_id),

        "age":
            isinstance(age, int)
            and age > 0,

        "gender":
            isinstance(gender, str)
            and gender.lower() in ["male", "female"],

        "diagnosis":
            isinstance(diagnosis, str)
            and len(diagnosis.strip()) > 0,

        "medications":
            isinstance(medications, list),

        "last_visit_id":
            isinstance(last_visit_id, str)
            and re.fullmatch(r"V\d+", last_visit_id)
    }

    invalid = []

    for key, value in constraints.items():
        if not value:
            invalid.append(key)

    return invalid


#--------------------------------------
# Validate entire dataset
#--------------------------------------
def validate(data):

    if not isinstance(data, (list, tuple)):
        print("Invalid format: expected a list or tuple.")
        return False

    required_keys = {
        "patient_id",
        "age",
        "gender",
        "diagnosis",
        "medications",
        "last_visit_id"
    }

    valid = True

    for index, record in enumerate(data):

        if not isinstance(record, dict):
            print(f"Record {index} is not a dictionary.")
            valid = False
            continue

        if set(record.keys()) != required_keys:
            print(f"Record {index} has incorrect fields.")
            valid = False
            continue

        invalid_fields = find_invalid_records(**record)

        if invalid_fields:
            print(f"\nRecord {index} has invalid data:")

            for field in invalid_fields:
                print(f"   {field} --> {record[field]}")

            valid = False

    if valid:
        print("\nAll medical records are valid.")

    return valid


# Run validation
validate(medical_records)