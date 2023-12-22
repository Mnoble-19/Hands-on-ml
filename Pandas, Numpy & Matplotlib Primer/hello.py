#uploading csv to huggingface
from datasets import Dataset
airqo_data = Dataset.from_csv("/Users/noble/Downloads/airqo_data.csv")
airqo_data.push_to_hub("airqo_data")