from dataclasses import dataclass


@dataclass
class Field:
    title: str
    series: list

    def __init__(self, series, title, **rest):
        self.series = series
        self.title = title if title is None else ''
        if len(rest):
            for key, value in rest.items():
                self.__dict__[key] = value
