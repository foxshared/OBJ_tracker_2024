     
import os

def generate_negative_description_file():
    with open("Train_app/neg.txt","w") as f:
        for filename in os.listdir("Train_app/negative"):
            f.write("negative/" + filename + "\n")

generate_negative_description_file()