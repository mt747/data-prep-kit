class DigestTransformConfiguration(TransformConfiguration):
    def __init__(self):
        super().__init__(
            name='diget',
            transform_class=DigestTransform,
        )

    def add_input_params(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "--digest_algorithm",
            type="str",
            choices=['sha256'],
            help="Specify the digest algorithm to use for calculating the hash value.",
            default="sha256"
        )

    def apply_input_params(self, args: Namespace) -> bool:
        captured = CLIArgumentProvider.capture_parameters(args, 'digest', False)
        self.params = self.params | captured
        return True
