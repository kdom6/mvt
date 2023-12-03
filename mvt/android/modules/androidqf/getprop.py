# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 The MVT Authors.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.artifacts.getprop import GetProp as GetPropArtifact

from .base import AndroidQFModule


class Getprop(GetPropArtifact, AndroidQFModule):
    """This module extracts data from get properties."""

    def __init__(
        self,
        file_path: Optional[str] = None,
        target_path: Optional[str] = None,
        results_path: Optional[str] = None,
        module_options: Optional[dict] = None,
        log: logging.Logger = logging.getLogger(__name__),
        results: Optional[list] = None,
    ) -> None:
        super().__init__(
            file_path=file_path,
            target_path=target_path,
            results_path=results_path,
            module_options=module_options,
            log=log,
            results=results,
        )
        self.results = []

    def run(self) -> None:
        getprop_files = self._get_files_by_pattern("*/getprop.txt")
        if not getprop_files:
            self.log.info("getprop.txt file not found")
            return

        data = self._get_file_content(getprop_files[0]).decode("utf-8")

        self.parse(data)
        self.log.info("Extracted a total of %d properties", len(self.results))
