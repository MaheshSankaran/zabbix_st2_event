import sys
from st2common.runners.base_action import Action

class MyEchoAction(Action):
    def run(self, message, subject):
        print("Subject:", subject)
        print("Message:", message)

        # Check if subject contains "Zabbix agent"
        if "Zabbix agent" in subject:
            self.handle_zabbix_agent_subject(subject)

    def handle_zabbix_agent_subject(self, subject):
        # Implement logic for handling subject containing "Zabbix agent"
        print("Handling Issues for 'Zabbix agent':", subject)
