import requests
import datetime as dt
import os
from dotenv import load_dotenv


load_dotenv("C:/Users/sangeeth/PycharmProjects/EnvironmentVariables/.env.txt")


APP_ID =os.getenv("app_id_nutritionix")
API_Key = os.getenv("api_key_nutritionix")

exercise_endpont =os.getenv("nutritionix_endpont")

BEARER_TOKEN =os.getenv("bearer_token_sheety")



header = {

    "x-app-id":APP_ID,
    "x-app-key":API_Key,
    "gender":"malle",
    "weight_kg":"60",
    "height_cm":"173",
    "age":"24"

}

parameters = {
    "query": input("Tell me which exercise you did ?")
}

response = requests.post(url=exercise_endpont,json=parameters,headers=header)
data = response.json()

work_out_data_list = data["exercises"]


work_out = [item for item in data["exercises"]]



###Sheety##


post = os.getenv("sheety_post")



today = dt.datetime.now()
formated = today.strftime("%Y/%m/%d")
now_time = today.time()
formated_time = now_time.strftime("%H:%M:%S")


for exercise in work_out:
    parameters = {
        "sheet1":{
            "date":formated,
            "duration":exercise["duration_min"],
            "exercise":exercise["user_input"].title(),
            "time": formated_time,
            "calories":exercise["nf_calories"],
            "id":exercise["tag_id"]


        }
    }

    header = {
        "Authorization": f"Bearer {BEARER_TOKEN} "
    }

    response = requests.post(url=post,json=parameters,headers=header)
  

