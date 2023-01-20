import pymongo 
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://raisjalia:1234@cluster0.aulercz.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH=r"/workspace/Insurance-Premium-Prediction/insurance.csv"
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="INSURANCE_TEST_PROJECT"
if __name__ == "__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")

    df.reset_index(drop=True,inplace = True)
    json_record=list(json.loads(df.T.to_json()).values())
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
