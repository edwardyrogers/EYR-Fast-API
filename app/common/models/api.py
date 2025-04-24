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


# Define the generic request model
class ApiRequest(BaseModel, Generic[T]):
    meta: Meta
    payload: T

    def to_json(self) -> Dict[str, Any]:
        return {"meta": self.meta.to_json(), "payload": self.payload.dict()}

    @classmethod
    def from_json(
        cls, source: Dict[str, Any], payload_type: type[T]
    ) -> "ApiRequest[T]":
        return cls(
            meta=Meta.from_json(source["meta"]),
            payload=payload_type(**source["payload"]),
        )
