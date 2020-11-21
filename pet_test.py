import requests
import base64
import pandas as pd
from sqlalchemy import create_engine
import os
# Create engine to connect to local sqlite3
engine = create_engine('sqlite:///save_output.db', echo=True)
con = engine.connect()
#
#
#




#Create a list of pets....

my_pet_list=[

{
    "petName": ["Lucy"],
    "aboutPet": ["cat, British Shorthair, yellow eyes, grey"],
    "dateLost": ["12/09/2019"],
    "reunited": [True],
    "user": ["Tim Krammer"],
    "photo": ["https://www.petful.com/wp-content/uploads/2016/07/british-shorthair-750x419.jpg"],
    "status": ["found"],
    "zipCode":["30157"]
    },

{
    "petName": ["Buddy"],
    "aboutPet": ["dog, Labrador, golden color"],
    "dateLost": ["10/04/2020"],
    "reunited": [False],
    "user": ["Michael Johnson"],
    "photo": ["https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/220px-Labrador_on_Quantock_%282175262184%29.jpg"],
    "status": ["still missing"],
    "zipCode":["30064"]
},
{
    "petName": ["Oliver"],
    "aboutPet": ["dog, Samoyed, white fur, black eyes"],
    "dateLost": ["09/21/2020"],
    "reunited": [False],
    "user": ["Takisha Williams"],
    "photo": ["https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/20122208/Samoyed-standing-in-the-forest.jpg"],
    "status": ["still missing"],
    "zipCode":["30121"]
},

{
    "petName": ["Molly"],
    "aboutPet": ["cat, went away and never came back, white fluffy fur, green eyes"],
    "dateLost": ["04/24/2020"],
    "reunited": [False],
    "user": ["Sheila Thompson"],
    "photo": ["https://upload.wikimedia.org/wikipedia/commons/1/15/White_Persian_Cat.jpg"],
    "status": ["still missing"],
    "zipCode":["30066"]
}
]


new_animal_dict=[] #Create empty list... my loops saves to this list with str image columns
n=0
for my_im in my_pet_list:
    n=n+1
    #my_im['photo'][0]

    #Scrape image from internet and save locally
    response = requests.get(my_im['photo'][0])# scrpe


    my_image='my_sample_image_{}.png'.format(n)#save file locally
    file = open(my_image, 'wb')
    file.write(response.content)

    #Now for each saved picture read in the image and convert to string
    with open(my_image, 'rb') as imageFile:
        str = base64.b64encode(imageFile.read()).decode("utf-8")
        #Now create new column to dictionary
    my_im['my_image_string']=str
    my_im['my_image_name']=my_image
    new_animal_dict.append(pd.DataFrame.from_dict(my_im)) #I can save straight to database instead

# delete the file using python
    if os.path.exists(my_image):
        os.remove(my_image)
#    else: 
#         print("The file does not exist")

final_df=pd.concat(new_animal_dict)
final_df.to_csv('my_sample_db.csv', index=False)
#final_df.to_sql('sample_table', engine=engine)

# to db:
final_df.to_sql('my_new_table',
con=engine, if_exists='append', index=False)
