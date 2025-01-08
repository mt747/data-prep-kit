# (C) Copyright IBM Corp. 2024.
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

from typing import Any

import pyarrow as pa
import hashlib
from data_processing.transform import AbstractTableTransform
from data_processing.utils import  TransformUtils



class DigestTransform(AbstractTableTransform):
    def __init__(self, config: dict[str, Any]):
        super().__init__(config)

        self.algorithm = config.get('digest_algorithm', "sha256")

    def transform(self, 
                  table: pa.Table, 
                  file_name: str = None) -> tuple[list[pa.Table], dict[str, Any]]:
        """
        """        
        tf_digest = []
        for elt in table['contents'].to_pylist():
            h = hashlib.new(self.algorithm)
            h.update(elt.encode('utf-8'))
            tf_digest.append(h.hexdigest())

        table = TransformUtils.add_column(table=table, 
                                           name='digest', 
                                           content=tf_digest)
        
        metadata = {"nrows": len(table)}
        return [table], metadata
    







