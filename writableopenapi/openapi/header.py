# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from schema import Schema
from example import Example
from media_type import MediaType


@dataclass
class Header(SpecificationExtension):
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allowEmptyValue: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema: Optional[Schema] = None
    example: Optional[Any] = None
    examples: Optional[Dict[str, Example]] = None
    content: Optional[Dict[str, MediaType]] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the header into a dictionary."""
        data = self.extensions
        if self.description is not None:
            data["description"] = self.description
        if self.required is not None:
            data["required"] = self.required
        if self.deprecated is not None:
            data["deprecated"] = self.deprecated
        if self.allowEmptyValue is not None:
            data["allowEmptyValue"] = self.allowEmptyValue
        if self.style is not None:
            data["style"] = self.style
        if self.explode is not None:
            data["explode"] = self.explode
        if self.allowReserved is not None:
            data["allowReserved"] = self.allowReserved
        if self.schema is not None:
            data["schema"] = self.schema.dump()
        if self.example is not None:
            data["example"] = self.example.__str__()
        if self.examples is not None:
            data["examples"] = {k: v.dump() for k, v in self.examples.items()}
        if self.content is not None:
            data["content"] = {k: v.dump() for k, v in self.content.items()}

        return data
