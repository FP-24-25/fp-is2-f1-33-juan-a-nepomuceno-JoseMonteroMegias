from typing import List, TypeVar, Generic

E = TypeVar('E')
P = TypeVar('P')

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []
    
    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return self._elements
    
    def add(self, e: E, priority: P) -> None:
        index = self._index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)
    
    def add_all(self, ls: List[tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)
    
    def remove(self) -> E:
        assert len(self._elements) > 0
        return self._elements.pop(0)
    
    def remove_all(self) -> List[E]:
        removed_elements = self._elements[:]
        self._elements.clear()
        self._priorities.clear()
        return removed_elements
    
    def _index_order(self, priority: P) -> int:
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._elements)
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            old_priority = self._priorities[index]
            if new_priority < old_priority:
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)

    def __repr__(self) -> str:
        return f"ColaPrioridad" + str(list(zip(self._elements, self._priorities)))