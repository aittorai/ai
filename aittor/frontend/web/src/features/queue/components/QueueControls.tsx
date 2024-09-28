import { Flex, Spacer } from '@aittorai/ui-library';
import { useAppSelector } from 'app/store/storeHooks';
import { CanvasManagerProviderGate } from 'features/controlLayers/contexts/CanvasManagerProviderGate';
import { ClearQueueIconButton } from 'features/queue/components/ClearQueueIconButton';
import { QueueActionsMenuButton } from 'features/queue/components/QueueActionsMenuButton';
import { SendToToggle } from 'features/queue/components/SendToToggle';
import ProgressBar from 'features/system/components/ProgressBar';
import { selectActiveTab } from 'features/ui/store/uiSelectors';
import { memo } from 'react';

import { AppButton } from './AppQueueBackButton';

const QueueControls = () => {
  const tab = useAppSelector(selectActiveTab);

  return (
    <Flex w="full" position="relative" borderRadius="base" gap={2} flexDir="column">
      <Flex gap={2}>
        <AppButton />
        <Spacer />
        {tab === 'canvas' && (
          <CanvasManagerProviderGate>
            <SendToToggle />
          </CanvasManagerProviderGate>
        )}
        <QueueActionsMenuButton />
        <ClearQueueIconButton />
      </Flex>
      <ProgressBar />
    </Flex>
  );
};

export default memo(QueueControls);
