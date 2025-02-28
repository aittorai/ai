import { Flex, FormControl, FormLabel, Tooltip } from '@aittorai/ui-library';
import { useConnectionState } from 'features/nodes/hooks/useConnectionState';
import { useFieldOutputTemplate } from 'features/nodes/hooks/useFieldOutputTemplate';
import { HANDLE_TOOLTIP_OPEN_DELAY } from 'features/nodes/types/constants';
import type { PropsWithChildren } from 'react';
import { memo } from 'react';
import { useTranslation } from 'react-i18next';

import FieldHandle from './FieldHandle';
import FieldTooltipContent from './FieldTooltipContent';

interface Props {
  nodeId: string;
  fieldName: string;
}

const OutputField = ({ nodeId, fieldName }: Props) => {
  const { t } = useTranslation();
  const fieldTemplate = useFieldOutputTemplate(nodeId, fieldName);

  const { isConnected, isConnectionInProgress, isConnectionStartField, validationResult, shouldDim } =
    useConnectionState({ nodeId, fieldName, kind: 'outputs' });

  if (!fieldTemplate) {
    return (
      <OutputFieldWrapper shouldDim={shouldDim}>
        <FormControl alignItems="stretch" justifyContent="space-between" gap={2} h="full" w="full">
          <FormLabel display="flex" alignItems="center" h="full" color="error.300" mb={0} px={1} gap={2}>
            {t('nodes.unknownOutput', {
              name: fieldName,
            })}
          </FormLabel>
        </FormControl>
      </OutputFieldWrapper>
    );
  }

  return (
    <OutputFieldWrapper shouldDim={shouldDim}>
      <Tooltip
        label={<FieldTooltipContent nodeId={nodeId} fieldName={fieldName} kind="outputs" />}
        openDelay={HANDLE_TOOLTIP_OPEN_DELAY}
        placement="top"
        shouldWrapChildren
      >
        <FormControl isDisabled={isConnected} pe={2}>
          <FormLabel mb={0}>{fieldTemplate?.title}</FormLabel>
        </FormControl>
      </Tooltip>
      <FieldHandle
        fieldTemplate={fieldTemplate}
        handleType="source"
        isConnectionInProgress={isConnectionInProgress}
        isConnectionStartField={isConnectionStartField}
        validationResult={validationResult}
      />
    </OutputFieldWrapper>
  );
};

export default memo(OutputField);

type OutputFieldWrapperProps = PropsWithChildren<{
  shouldDim: boolean;
}>;

const OutputFieldWrapper = memo(({ shouldDim, children }: OutputFieldWrapperProps) => (
  <Flex
    position="relative"
    minH={8}
    py={0.5}
    alignItems="center"
    opacity={shouldDim ? 0.5 : 1}
    transitionProperty="opacity"
    transitionDuration="0.1s"
    justifyContent="flex-end"
  >
    {children}
  </Flex>
));

OutputFieldWrapper.displayName = 'OutputFieldWrapper';
