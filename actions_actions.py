from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionProvideExplanation(Action):

    def name(self) -> Text:
        return "action_provide_explanation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.get_slot("question")
        answer = tracker.get_slot("answer")
        explanation = self.get_explanation(question, answer)

        dispatcher.utter_message(text=f"The correct answer is {answer}. {explanation}")
        return []

    def get_explanation(self, question, answer):
        # Placeholder for actual explanation lookup
        return "Here's the explanation for the answer."

class ActionUpdateScore(Action):

    def name(self) -> Text:
        return "action_update_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        score = tracker.get_slot("score")
        new_score = score + 1  # Update score logic
        dispatcher.utter_message(text=f"Your score is now {new_score}.")
        return [SlotSet("score", new_score)]