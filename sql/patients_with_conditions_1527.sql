select * from Patients
where conditions ~ '^DIAB1.*| DIAB1.*

-- alternative with a crazy lookaround ( postgress has posix compliant regex, hence doesn't support \b )
select * from Patients
where conditions ~ '(?<=^|[^a-zA-Z0-9_])DIAB1\w+'

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]
