from aittor.app.invocations.baseinvocation import BaseInvocation, BaseInvocationOutput, invocation, invocation_output
from aittor.app.invocations.fields import (
    FieldDescriptions,
    InputField,
    OutputField,
    UIType,
)
from aittor.app.services.shared.invocation_context import InvocationContext
from aittor.backend.stable_diffusion.schedulers.schedulers import SCHEDULER_NAME_VALUES


@invocation_output("scheduler_output")
class SchedulerOutput(BaseInvocationOutput):
    scheduler: SCHEDULER_NAME_VALUES = OutputField(description=FieldDescriptions.scheduler, ui_type=UIType.Scheduler)


@invocation(
    "scheduler",
    title="Scheduler",
    tags=["scheduler"],
    category="latents",
    version="1.0.0",
)
class SchedulerInvocation(BaseInvocation):
    """Selects a scheduler."""

    scheduler: SCHEDULER_NAME_VALUES = InputField(
        default="euler",
        description=FieldDescriptions.scheduler,
        ui_type=UIType.Scheduler,
    )

    def proceed(self, context: InvocationContext) -> SchedulerOutput:
        return SchedulerOutput(scheduler=self.scheduler)
