from heapq import heapify, heappop, heappush

class EventManager:
    def __init__(self, events: list[list[int]]):
        self._events = sorted([[-p, e] for e, p in events], key=lambda x: (x[0], x[1]))
        self._events_ord = {item[0]: item[1] for item in events}

    def updatePriority(self, eventId: int, newPriority: int) -> None:

        heappush(self._events, [-1 * newPriority, eventId])
        self._events_ord[eventId] = newPriority

    def pollHighest(self) -> int:
        while self._events:
            e_prt, e_id = heappop(self._events)

            if -e_prt == self._events_ord[e_id]:
                self._events_ord[e_id] = -1
                return e_id
               
        return -1