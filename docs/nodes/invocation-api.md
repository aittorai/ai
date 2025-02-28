# Invocation API

Each invocation's `aittor` method is provided a single arg - the Invocation Context.

This object provides an API the invocation can use to interact with application services, for example:

- Saving images
- Logging messages
- Loading models

```py
class MyInvocation(BaseInvocation):
  ...
  def proceed(self, context: InvocationContext) -> ImageOutput:
      # Load an image
      image_pil = context.images.get_pil(self.image.image_name)
      # Do something to the image
      output_image = do_something_cool(image_pil)
      # Save the image
      image_dto = context.images.save(output_image)
      # Log a message
      context.logger.info(f"Did something cool, image saved!")
      # Return the output
      return ImageOutput.build(image_dto)
      ...
```

The full API is documented below.

## Mixins

Two important mixins are provided to facilitate working with metadata and gallery boards.

### `WithMetadata`

Inherit from this class (in addition to `BaseInvocation`) to add a `metadata` input to your node. When you do this, you can access the metadata dict from `self.metadata` in the `aittor()` function.

The dict will be populated via the node's input, and you can add any metadata you'd like to it. When you call `context.images.save()`, if the metadata dict has any data, it be automatically embedded in the image.

### `WithBoard`

Inherit from this class (in addition to `BaseInvocation`) to add a `board` input to your node. This renders as a drop-down to select a board. The user's selection will be accessible from `self.board` in the `aittor()` function.

When you call `context.images.save()`, if a board was selected, the image will added to that board as it is saved.

<!-- prettier-ignore-start -->
::: aittor.app.services.shared.invocation_context.InvocationContext
    options:
        members: false

::: aittor.app.services.shared.invocation_context.ImagesInterface

::: aittor.app.services.shared.invocation_context.TensorsInterface

::: aittor.app.services.shared.invocation_context.ConditioningInterface

::: aittor.app.services.shared.invocation_context.ModelsInterface

::: aittor.app.services.shared.invocation_context.LoggerInterface

::: aittor.app.services.shared.invocation_context.ConfigInterface

::: aittor.app.services.shared.invocation_context.UtilInterface

::: aittor.app.services.shared.invocation_context.BoardsInterface
<!-- prettier-ignore-end -->
