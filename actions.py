# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import Coronavirus_webscrapping

class ActionRespondCoroanStateCity(Action):
     def name(self):
      return "action_corona_state"

     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]):
      # last_message = tracker.latest_message.get("text", "") 
      cor_virus=Coronavirus_webscrapping.df
      entities = tracker.latest_message['entities']
      print("Last Message Now ", entities)
      country = None
      for e in entities:
            if e['entity'] == "country":
                country = e['value']
                               
      message="Please enter correct country name"
      #print("State ", country.title())   
      for i in range(8,len(cor_virus)):
          if (cor_virus['Country,Other'][i]).lower()==(country).lower():
              message= "Total cases: "+cor_virus["TotalCases"][i] +" Total Deaths: " + cor_virus["TotalDeaths"] [i]+" Total Recovered: " + cor_virus["TotalRecovered"][i] +" Active Cases: "+cor_virus["ActiveCases"][i]
              break

      dispatcher.utter_message(text=message) 

      return []
  



