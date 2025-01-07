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
from data_processing.transform import AbstractBinaryTransform
from data_processing.utils import  TransformUtils



class DigestTransform(AbstractBinaryTransform):
    def __init__(self, config: dict[str, Any]):
        super().__init__(config)

        self.algorithm = config.get('digest_algorithm', "sha256")

    def transform_binary(self, 
            file_name: str, 
            byte_array: bytes) -> tuple[list[tuple[bytes, str]], dict[str, Any]]:
        """
        """        
        h = hashlib.new(self.algorithm)
        h.update(byte_array)
        digest=h.hexdigest()
        data = [{'file_name':file_name, 'digest':h.hexdigest()}]
        table = pa.Table.from_pylist(data)
        parquet=TransformUtils.convert_arrow_to_binary(table=table)

        metadata = { "algorithm": self.algorithm}
        return [(parquet, ".parquet")], metadata
    




