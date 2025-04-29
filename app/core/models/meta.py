from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel

# Create a generic type for the payload
T = TypeVar("T", bound=BaseModel)


class Meta(BaseModel):
    lang: Optional[str] = ""
    session_id: Optional[str] = ""
    device_id: Optional[str] = ""
    cpt_key: Optional[str] = ""
    api_key: Optional[str] = ""
    client: Optional[str] = ""

    def to_json(self) -> Dict[str, Any]:
        """Convert the MetaData instance to a dictionary."""
        return self.model_dump()

    @classmethod
    def from_json(cls, source: Dict[str, Any]) -> "Meta":
        """Create a MetaData instance from a dictionary."""
        return cls(**source)
