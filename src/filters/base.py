from typing import Optional


class BaseFilter:
    def to_dict(self) -> dict[str, Optional]:
        return {key: value for key, value in vars(self).items() if value is not None}
