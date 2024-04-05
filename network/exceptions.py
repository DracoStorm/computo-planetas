class ComponentError(Exception):
    def __init__(self) -> None:
        super().__init__(
            f'The component has an unexpected error')


class UnexpectedShutdown(Exception):
    def __init__(self) -> None:
        super().__init__('The component has an unexpected shutdown')


class BadNetType(Exception):
    def __init__(self) -> None:
        super().__init__('The type of the recived data is\'nt valid')


class FailedComponentConexion(Exception):
    def __init__(self) -> None:
        super().__init__('The component coundn\'t connect')
