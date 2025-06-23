import csv

address_book = [['Name','Address','Mobile','email'],
                ['Riya Aggarwal','b-03 Dreamland Colony, HMH','7627011073','riya@gmail.com'],
                ['Parveen Kumar','a-143 Dharuhera','7374951161','parveen@gmail.com'],
                ['Shivani Faujdar','Railway Colony,Jaipur','6375752519','shivani@gmail.com'],
                ['Gayatri','ward 3,fatehgarh,HMH','9660802533','mitu@gmail.com']
                ]

with open("address_book.csv",'w',newline="") as file:
    writer = csv.writer(file)
    for details in address_book:
     writer.writerow(details)

print("CSV file created successfully.")