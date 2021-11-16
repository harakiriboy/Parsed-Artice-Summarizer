# Parsed Article Summarizer
Python code that will scrap articles of news from 'coinmarketcap.com' cryptocurrency website and give the article summaries 


## Installation
To run this program, firstly install required packages and modules from requirements.txt file There will be needed packages like SQLAlchemy and jwt

to install packeges you can use this command:
```bash
$ pip install -r requirements.txt
```

also, in order to running it on your machine you must have available GPU. To get this download and install appropriate 'Nvidia' drivers, CUDA toolkit, cuDNN library that will be compatible with your OS and Tensorflow version to work with machine learning algorithms and neural networks. For me it was CUDA 11.2 and cuDNN 8.1.0

## Usage
First step. Is to run 'tableforass4.py' file to create needed tables on your postgresql database
![tables](https://user-images.githubusercontent.com/74262437/141940548-777530b4-cc61-45a6-bfa9-3e64c52059c4.jpg)

Second step. Run 'ass4server.py' file with Flask app inside
![image](https://user-images.githubusercontent.com/74262437/141940707-2ffef344-4665-4c80-bc68-c63b3fa7a501.png)

## Examples
1)
![image](https://user-images.githubusercontent.com/74262437/141940757-f0e5c315-9728-4d5f-b511-707db7418559.png)
2)
![image](https://user-images.githubusercontent.com/74262437/141940780-c6adc00e-09e8-4bd9-b073-69bdf72ec00f.png)
3)
![image](https://user-images.githubusercontent.com/74262437/141940850-464d881d-03f7-46f5-ae12-d3207a0aae97.png)
4)
![image](https://user-images.githubusercontent.com/74262437/141941067-70fcabf1-e8c3-4e0f-863c-db5b1bbdec75.png)
5)
![image](https://user-images.githubusercontent.com/74262437/141941437-f294e1f7-77d6-47e0-af01-6818418c5208.png)

