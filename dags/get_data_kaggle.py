import os
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

def get_data_kaggle():
    api = KaggleApi()
    api.authenticate()
    
    competition_name = 'playground-series-s4e6'
    download_path = 'data/'
    
    api.competition_download_files(competition_name, path=download_path)
    
    for item in os.listdir(download_path):
        if item.endswith('.zip'):
            zip_ref = zipfile.ZipFile(os.path.join(download_path, item), 'r')
            zip_ref.extractall(download_path)
            zip_ref.close()
            print(f"Unzipped {item}")

# import os
# from kaggle.api.kaggle_api_extended import KaggleApi
# import zipfile

# def get_data_kaggle():
#     os.environ['KAGGLE_USERNAME'] = 'carscudr@gmail.com'
#     os.environ['KAGGLE_KEY'] = 'Carlitos23101988'
    
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
