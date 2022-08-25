from pprint import pprint
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from .bartlib import get_abbr, next_train, last_train

class BARTAction:
    def complete(self, dispatcher, station_name, nextLast='next'):
        bart_schedule_func = next_train if nextLast == 'next' else last_train
        if station_name is not None:
            time = bart_schedule_func('16TH', get_abbr(station_name))
            if time:
                h, m = time
                dispatcher.utter_message(text=f"The {nextLast} train to {station_name} is at {h}:{m:02d}")
            else:
                dispatcher.utter_message(text="Hmm, dunno")
        else:
            dispatcher.utter_message(text="Um, dunno.")   

    def diagnose(self, dispatcher, tracker, domain):
        print('-'*50)
        # print(dispatcher)
        # print(tracker)
        print('latest_message'); pprint(tracker.latest_message)
        # print('slots'); pprint(tracker.slots)
        # print('domain'); pprint(domain)
        print('-'*50)
        pass

class ActionAnswerNextTrainQuestion(Action, BARTAction):

    def name(self) -> Text:
        return "answer_next_train_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        self.diagnose(dispatcher, tracker, domain)
        station_name = tracker.get_slot('station_name')
        self.complete(dispatcher, station_name, 'next')

        return []

class ActionAnswerLastTrainQuestion(Action, BARTAction):

    def name(self) -> Text:
        return "answer_last_train_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        self.diagnose(dispatcher, tracker, domain)
        station_name = tracker.get_slot('station_name')
        self.complete(dispatcher, station_name, 'last')

        return []