# Copyright (c) 2023 Nicolas Paul All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Any, Dict, Optional

from oauth_flow import OAuthFlow
from specification_extension import SpecificationExtension


@dataclass
class OAuthFlows(SpecificationExtension):
    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    client_credentials: Optional[OAuthFlow] = None
    authorization_code: Optional[OAuthFlow] = None

    def dump(self) -> Dict[str, Any]:
        """Dumps the OAuth flows into a dictionary."""
        data = self.extensions
        if self.implicit is not None:
            data["implicit"] = self.implicit.dump()
        if self.password is not None:
            data["password"] = self.password.dump()
        if self.client_credentials is not None:
            data["clientCredentials"] = self.client_credentials.dump()
        if self.authorization_code is not None:
            data["authorizationCode"] = self.authorization_code.dump()

        return data
