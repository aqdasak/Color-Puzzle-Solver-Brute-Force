from dataclasses import dataclass
from typing import Self


@dataclass
class Content:
    type: str
    size: int

    def __add__(self, other: Self):
        if self.type != other.type:
            raise ValueError("Different type of contents can't be added")
        self.size += other.size
        return self


class Beaker:
    def __init__(self, content: list = [], max_size=4):
        """
        content: [top to bottom]
        """
        if len(content) > max_size:
            raise ValueError("Can't insert more than max size")

        self._content: list[Content] = self.compactify(content)
        self._max_size = max_size

    @staticmethod
    def compactify(content: list) -> list[Content]:
        if len(content) == 0:
            return []

        comp_content = [Content(content[0], 1)]
        prev = content[0]
        for current in content[1:]:
            if current == prev:
                comp_content[-1].size += 1
            else:
                comp_content.append(Content(current, 1))
            prev = current

        return comp_content

    @property
    def top(self) -> Content:
        return self._content[0]

    def pour_into(self, tube: Self) -> None:
        if tube is self:
            return
        if self.is_empty():
            return

        if tube.is_empty():
            tube._content.append(self.top)
            self._content.pop(0)

        elif self.top.type != tube.top.type:
            raise ValueError('Top values are not same')

        elif self.top.size + len(tube) > tube._max_size:
            raise ValueError('Pouring will lead to overflow')

        else:
            tube._content[0] += self._content.pop(0)

    def is_empty(self) -> bool:
        return len(self._content) == 0

    def is_complete(self) -> bool:
        return not self.is_empty() and (self.top.size == len(self) == self._max_size)

    def __getitem__(self, index):
        return self._content[index]

    def __len__(self):
        if self.is_empty():
            return 0

        return sum([e.size for e in self._content])

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self._content}'
