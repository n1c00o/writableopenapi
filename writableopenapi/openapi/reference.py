# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Dict
from specification_extension import SpecificationExtension


@dataclass
class Reference(SpecificationExtension):
    ref: str = ""

    def dump(self) -> Dict[str, str]:
        return {"$ref": self.ref}
