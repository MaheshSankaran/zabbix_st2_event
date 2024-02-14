import sys
from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message, subject):
        print(subject)
        print(message)

        # Check if subject contains "Zabbix agent"
        #if "Zabbix agent" in subject:
        #    self.handle_zabbix_agent_subject(message)

    #def handle_zabbix_agent_subject(self, message):
    #    # Parse the message to extract relevant details
    #    lines = message.split("\r\n")
    #    for line in lines:
    #        print (line)
