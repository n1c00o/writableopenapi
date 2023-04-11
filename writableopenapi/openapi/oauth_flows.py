# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional
from specification_extension import SpecificationExtension
from oauth_flow import OAuthFlow


@dataclass
class OAuthFlows(SpecificationExtension):
    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    clientCredentials: Optional[OAuthFlow] = None
    authorizationCode: Optional[OAuthFlow] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flows into a dictionary."""
        data = self.extensions
        if self.implicit is not None:
            data["implicit"] = self.implicit.dump()
        if self.password is not None:
            data["password"] = self.password.dump()
        if self.clientCredentials is not None:
            data["clientCredentials"] = self.clientCredentials.dump()
        if self.authorizationCode is not None:
            data["authorizationCode"] = self.authorizationCode.dump()

        return data
