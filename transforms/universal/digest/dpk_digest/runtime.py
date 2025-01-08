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
import sys
from dpk_digest.transform import DigestTransform
from data_processing.transform import TransformConfiguration
from data_processing.utils import ParamsUtils, CLIArgumentProvider, get_logger
from argparse import ArgumentParser, Namespace
from data_processing.runtime.pure_python import PythonTransformLauncher
from data_processing.runtime.pure_python.runtime_configuration import (
    PythonTransformRuntimeConfiguration,)

logger = get_logger(__name__)

class DigestTransformConfiguration(TransformConfiguration):
    def __init__(self):
        super().__init__(name='digest', transform_class=DigestTransform,)

    def add_input_params(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "--digest_algorithm",
            type=str,
            help="Specify the hash algorithm to use for calculating the digest value.",
        )

    def apply_input_params(self, args: Namespace) -> bool:
        captured = CLIArgumentProvider.capture_parameters(args, 'digest', True)
        self.params = self.params | captured
        if captured.get('digest_algorithm') not in ['sha256','SHA512', 'MD5']:
            logger.error(f"Parameter digest_algorithm cannot be other than ['sha256','SHA512', 'MD5']. You specified {args.digest_algorithm}")
            return False
        return True
    

class DigestPythonTransformConfiguration(PythonTransformRuntimeConfiguration):

    def __init__(self):
        super().__init__(transform_config=DigestTransformConfiguration())


class Digest:
    def __init__(self, **kwargs):
        self.params = {}
        for key in kwargs:
            self.params[key] = kwargs[key]
        # if input_folder and output_folder are specified, then assume it is represent data_local_config
        try:
            local_conf = {k: self.params[k] for k in ("input_folder", "output_folder")}
            self.params["data_local_config"] = ParamsUtils.convert_to_ast(local_conf)
            del self.params["input_folder"]
            del self.params["output_folder"]
        except:
            pass

    def transform(self):
        sys.argv = ParamsUtils.dict_to_req(d=(self.params))
        launcher = PythonTransformLauncher(DigestPythonTransformConfiguration())
        return_code = launcher.launch()
        return return_code


if __name__ == "__main__":
    launcher = PythonTransformLauncher(DigestPythonTransformConfiguration())
    launcher.launch()
