from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def str(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions
    pass


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents.sort(key=lambda x: x.load)

        return agents[0]


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        