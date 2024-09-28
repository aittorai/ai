import { Button, Flex, Spacer, useShiftModifier } from '@aittorai/ui-library';
import { useAppSelector } from 'app/store/storeHooks';
import { selectDynamicPromptsIsLoading } from 'features/dynamicPrompts/store/dynamicPromptsSlice';
import { QueueIterationsNumberInput } from 'features/queue/components/QueueIterationsNumberInput';
import { useApp } from 'features/queue/hooks/useApp';
import { memo } from 'react';
import { PiLightningFill, PiSparkleFill } from 'react-icons/pi';

import { QueueButtonTooltip } from './QueueButtonTooltip';

const action = 'Action';

export const AppButton = memo(() => {
  const queue = useApp();
  const shift = useShiftModifier();
  const isLoadingDynamicPrompts = useAppSelector(selectDynamicPromptsIsLoading);

  return (
    <Flex pos="relative" w="200px">
      <QueueIterationsNumberInput />
      <QueueButtonTooltip prepend={shift}>
        <Button
          onClick={shift ? queue.queueFront : queue.queueBack}
          isLoading={queue.isLoading || isLoadingDynamicPrompts}
          loadingText={action}
          isDisabled={queue.isDisabled}
          rightIcon={shift ? <PiLightningFill /> : <PiSparkleFill />}
          variant="solid"
          colorScheme="appYellow"
          size="lg"
          w="calc(100% - 60px)"
          flexShrink={0}
          justifyContent="space-between"
          spinnerPlacement="end"
        >
          <span>{action}</span>
          <Spacer />
        </Button>
      </QueueButtonTooltip>
    </Flex>
  );
});

AppButton.displayName = 'AppQueueBackButton';
