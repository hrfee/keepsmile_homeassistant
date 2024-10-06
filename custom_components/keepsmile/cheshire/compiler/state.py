from typing_extensions import TypedDict
import sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic.command import *

LightStateDict = TypedDict(
    'LightStateDict', 
    {
        'SwitchCommand': SwitchCommand,
        'BrightnessCommand': BrightnessCommand,
        'ColorTemperatureCommand': ColorTemperatureCommand,
        'RGBCommand': RGBCommand,
        'WhiteCommand': WhiteCommand,
        'EffectCommand': EffectCommand,
        'SpeedCommand': SpeedCommand
    },
    total=False
)

class LightState:
    """Represents the desired state of a light by collecting the latest of each 
    type of command."""
    def __init__(self) -> None:
        self._state: LightStateDict = {}

    def update(self, c: Command):
        self._state[c.get_type()] = c

    @property
    def state(self):
        return self._state 
