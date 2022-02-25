from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC 
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable(ABCMeta)):
    @abstractmethod
    def is_due():
        pass


class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due():
        pass
        


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = date.parse(dayfirst=True)
        self.text = text
            
    def is_due(self,text):
        if self.date <= datetime.now():
            formatted_date = self.date.isoformat()
            iter([text, formatted_date])
            

    