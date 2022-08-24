from abc import ABC, abstractmethod

from engine import Engine
from battery import Battery
from engine.model.carfactory import carFactory

class Car(ABC):
    def generator(carfactory):
        carFactory.create_calliope()