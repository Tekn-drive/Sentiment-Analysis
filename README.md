# Sentiment Analysis
This simple React JS based web application explores the power of NLP technology to classify sentiment based on the provided thoughts. 

## 🚀 Features
- Text sentiment classification
- Confidence score output
- NLP model powered by Transformers
- Full-stack React + Python API integration

## API Usage Instructions
1. For the NLP model, please download it from the **Releases** section. **Do not forget to put the entirety of the model folder inside the "backend" folder**.

2. Before running the **SentimentAnalysisAPI.py** file please make sure that you have switched directory to **backend** folder. Please do ```cd backend``` while inside this project's root folder. Also, do not forget to install all of the requirements in your python environment as what is specified in **requirements.txt**. Make sure that your Python version is **3.10.20**.

3. Now just execute ```uvicorn SentimentAnalysisAPI:app --reload 
--port 8000```

## Node Usage Instructions
1. Make sure that the Node used is version **22** because its the current tested stable Node version for this project. 

2. In this project's root folder directory, do ```npm install``` to install all necessary packages.

3. Once all the steps above are done, just do ```npm start```. Enjoy the app!!

### Make sure to execute both API and Node steps in order for this project to work. Preferably execute the API steps first.