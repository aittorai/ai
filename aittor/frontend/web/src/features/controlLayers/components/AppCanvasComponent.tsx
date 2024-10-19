import { Box } from '@aittorai/ui-library';
import { useAppCanvas } from 'features/controlLayers/hooks/useAppCanvas';
import { memo } from 'react';

export const AppCanvasComponent = memo(() => {
  const ref = useAppCanvas();

  return (
    <Box
      position="absolute"
      top={0}
      right={0}
      bottom={0}
      left={0}
      ref={ref}
      borderRadius="base"
      overflow="hidden"
      data-testid="control-layers-canvas"
    />
  );
});

AppCanvasComponent.displayName = 'AppCanvasComponent';
