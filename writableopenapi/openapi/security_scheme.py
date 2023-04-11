# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass, fields
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from oauth_flows import OAuthFlows


@dataclass
class SecurityScheme(SpecificationExtension):
    type: str = ""
    description: Optional[str] = None
    name: Optional[str] = None
    in_: Optional[str] = None
    scheme: Optional[str] = None
    bearerFormat: Optional[str] = None
    flows: Optional[OAuthFlows] = None
    openIdConnectUrl: Optional[str] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the security scheme into a dictionary."""
        return {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
