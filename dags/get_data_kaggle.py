# import os
# import json
# import zipfile
# import pandas as pd
# from kaggle.api.kaggle_api_extended import KaggleApi
import os
import json
import zipfile
import time
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from kaggle.rest import ApiException

def get_data_kaggle():
    kaggle_json_path = '/home/airflow/.kaggle/kaggle.json'

    # Verify the kaggle.json file exists
    if not os.path.exists(kaggle_json_path):
        raise FileNotFoundError(f"File not found: {kaggle_json_path}")

    # Load the kaggle.json file
    with open(kaggle_json_path, 'r') as f:
        kaggle_creds = json.load(f)

    # Set the environment variables
    os.environ['KAGGLE_USERNAME'] = kaggle_creds['username']
    os.environ['KAGGLE_KEY'] =kaggle_creds['key']

    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define the competition name
    competition_name = 'playground-series-s4e6'

    download_path = 'data/'
    
    api.competition_download_files(competition_name, path=download_path)

    for item in os.listdir(download_path):
        if item.endswith('.zip'):
            zip_ref = zipfile.ZipFile(os.path.join(download_path, item), 'r')
            zip_ref.extractall(download_path)
            zip_ref.close()
            print(f"Unzipped {item}")

    # Download the competition dataset
    # api.competition_download_files(competition_name, path='.')

    # Extract the downloaded zip file
    # with zipfile.ZipFile(f'{competition_name}.zip', 'r') as zip_ref:
    #     zip_ref.extractall(competition_name)

    # # Load the dataset into DataFrames
    # train_df = pd.read_csv(f'{competition_name}/train.csv')
    # test_df = pd.read_csv(f'{competition_name}/test.csv')








    

# kaggle_json_path = '/home/airflow/.kaggle/kaggle.json'

# # Verify the kaggle.json file exists
# if not os.path.exists(kaggle_json_path):
#     raise FileNotFoundError(f"File not found: {kaggle_json_path}")

# # Load the kaggle.json file
# with open(kaggle_json_path, 'r') as f:
#     kaggle_creds = json.load(f)
# # Load the kaggle.json file
# # with open('kaggle.json', 'r') as f:
# # with open('/home/airflow/.kaggle/kaggle.json', 'r') as f:
# #     kaggle_creds = json.load(f)

# # Set the environment variables
# os.environ['KAGGLE_USERNAME'] = kaggle_creds['username']
# os.environ['KAGGLE_KEY'] = kaggle_creds['key']

# # Initialize the Kaggle API
# api = KaggleApi()
# api.authenticate()

# # Define the competition name
# competition_name = 'playground-series-s4e6'

# # Download the competition dataset
# api.competition_download_files(competition_name, path='.')

# # Extract the downloaded zip file
# with zipfile.ZipFile(f'{competition_name}.zip', 'r') as zip_ref:
#     zip_ref.extractall(competition_name)

# # Load the dataset into DataFrames
# train_df = pd.read_csv(f'{competition_name}/train.csv')
# test_df = pd.read_csv(f'{competition_name}/test.csv')

# import os
# from kaggle.api.kaggle_api_extended import KaggleApi
# import zipfile

# def get_data_kaggle():
#     api = KaggleApi()
#     api.authenticate()
    
#     competition_name = 'playground-series-s4e6'
#     download_path = 'data/'
    
#     api.competition_download_files(competition_name, path=download_path)
    
#     for item in os.listdir(download_path):
#         if item.endswith('.zip'):
#             zip_ref = zipfile.ZipFile(os.path.join(download_path, item), 'r')
#             zip_ref.extractall(download_path)
#             zip_ref.close()
#             print(f"Unzipped {item}")

