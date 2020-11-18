# Study on predictability of diabetes.

The Pima Indians of Arizona have the highest reported prevalence of diabetes of any population in the world. A small study has been conducted to analyse their medical records to assess if it is possible to predict the onset of diabetes based on diagnostic measures.

### The problem:
The objective is to explore the dataset and understand the data and the different distribution of the features, then to build machine learning models that predict based on diagnostic measurements whether a patient has diabetes. This is a binary (2-class) classification problem. There are 768 observations with 8 medical predictor variables (input) and 1 target variable.

#### Output:
0 : "Negative" 
1 : "Positive"

#### Code:
A documented notebook is available with the EDA and all the different models and optimizations perfermed for this task. I also encluded the code to deploy the "Best" model (a MLP) using Flask server and be able to perform prediction using a GUI.

#### Setup:
```sh
$ pip3 install -r requirements.txt
```

#### Dataset:
https://www.kaggle.com/uciml/pima-indians-diabetes-database





