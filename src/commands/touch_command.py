from commands.command import *

class TouchCommand(Command):

  def privates(self, message):
    return "Don't touch my privates you perverted dickcheese"

  def run(self, message):
    return "Don't touch me you pervert"

commandClass = TouchCommand