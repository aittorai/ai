# Copyright (c) 2022 APP Development Team


from aittor.app.services.invocation_services import InvocationServices


class Operator:
    """The operator, used to execute invocations"""

    services: InvocationServices

    def __init__(self, services: InvocationServices):
        self.services = services
        self._start()

    def __start_service(self, service) -> None:
        # Call start() method on any services that have it
        start_op = getattr(service, "start", None)
        if callable(start_op):
            start_op(self)

    def __stop_service(self, service) -> None:
        # Call stop() method on any services that have it
        stop_op = getattr(service, "stop", None)
        if callable(stop_op):
            stop_op(self)

    def _start(self) -> None:
        """Starts the operator. This is called automatically when the operator is created."""
        for service in vars(self.services):
            self.__start_service(getattr(self.services, service))

    def stop(self) -> None:
        """Stops the operator. A new Operator will have to be created to execute further."""
        # First stop all services
        for service in vars(self.services):
            self.__stop_service(getattr(self.services, service))
