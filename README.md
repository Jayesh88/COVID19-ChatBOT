# COVID19-ChatBOT

![1__c7tuMIYZsbuwcf7gOS5SQ](https://user-images.githubusercontent.com/61301712/89108122-0a8a1280-d404-11ea-9136-35764c4943b9.png)


RASA is the best framework for implementing chatBOT's. In this repository i have demonstrated a simple chatbot creation for understanding covid cases across the nations.

For installation and implementation i have followed this tutorial by rasa : https://rasa.com/docs/rasa/user-guide/installation/

## For Installation :
 ### Step-1: 
 ![rasa-1](https://user-images.githubusercontent.com/61301712/89107812-9cdce700-d401-11ea-8ecc-94314cb62e11.PNG)
 
 ### Step-2:
 ![activate rasa](https://user-images.githubusercontent.com/61301712/89107879-18d72f00-d402-11ea-8821-5f0cfba5d956.PNG)
 
 ### Step-3:
 ![install rasa](https://user-images.githubusercontent.com/61301712/89107841-dca3ce80-d401-11ea-96e9-fe7e156b1099.PNG)

After installation is complete. You can check one more thing, rasa also has a basic chatbot which is designed to know how it works, to initiate it you can simply type 
        
        rasa init
 ### Step-4:
![rasa init](https://user-images.githubusercontent.com/61301712/89107927-723f5e00-d402-11ea-8b65-ccad5e208840.PNG)


## About this COVID19 project:
This project is divided into two parts:
 1. Web scrapping: For data, i have scrapped data from live data stream from the world-o-meter and utilised that data for creating chatbot. So whenever you run this chatbot you can get the data based on the live cases reported over the countries.
 
 2. ChatBot creation: To understand this there are 3 files "nlu", "stories" and "domains". In whhich nlu takes the intent of the user and through the stored result it helps to supply appropriate result. Wereas "domains" is the medium where all the data parameters from both in "nlu" and "stories" must be specified in "Domains" file. 
 The Actions.py file is where we write our actual code to make our chatbot work.
 
 ![Output](https://user-images.githubusercontent.com/61301712/89108082-cbf45800-d403-11ea-8a95-0ef54273d103.PNG)
 
 Note: For final execution you have to open two anaconda prompt tabs as shown in above figure.
 
 

