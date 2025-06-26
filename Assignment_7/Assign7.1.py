import pandas as pd

df = pd.DataFrame({
    'email': ['riya@gmail.com','invalid-2343','aggarwal@skit.org'],
    'mobile':['7627011073','343525','abdg4355'],
    'password': ['Pass@1234', 'weakpass', 'Strong!1'],
    'date': ['26/06/2025', '99/99/9999', '01/01/2022'],
    'filename': ['file.pdf', 'image.png', 'wrongfile.txtt'],
})

email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
mobile = r'^[6-9]\d{9}$'
password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
### ?=.* is used for look ahead that anywhere in the string it is available or not
date = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
filename = r'^.+\.(jpg|png|pdf|docx|xlsx)$'

df['valid_email'] = df['email'].str.fullmatch(email)
df['valid_mobile'] = df['mobile'].str.fullmatch(mobile)
df['valid_date'] = df['date'].str.fullmatch(date)
df['valid_password'] = df['password'].str.fullmatch(password)
df['valid_filename'] = df['filename'].str.fullmatch(filename)

print(df.to_string())