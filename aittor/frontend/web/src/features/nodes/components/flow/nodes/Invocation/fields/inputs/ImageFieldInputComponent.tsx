import { Flex, Text } from '@aittorai/ui-library';
import { useStore } from '@nanostores/react';
import { skipToken } from '@reduxjs/toolkit/query';
import { useAppDispatch } from 'app/store/storeHooks';
import IAIDndImage from 'common/components/IAIDndImage';
import IAIDndImageIcon from 'common/components/IAIDndImageIcon';
import type { TypesafeDraggableData, TypesafeDroppableData } from 'features/dnd/types';
import { fieldImageValueChanged } from 'features/nodes/store/nodesSlice';
import type { ImageFieldInputInstance, ImageFieldInputTemplate } from 'features/nodes/types/field';
import { memo, useCallback, useEffect, useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { PiArrowCounterClockwiseBold } from 'react-icons/pi';
import { useGetImageDTOQuery } from 'services/api/endpoints/images';
import type { PostUploadAction } from 'services/api/types';
import { $isConnected } from 'services/events/stores';

import type { FieldComponentProps } from './types';

const ImageFieldInputComponent = (props: FieldComponentProps<ImageFieldInputInstance, ImageFieldInputTemplate>) => {
  const { nodeId, field, fieldTemplate } = props;
  const dispatch = useAppDispatch();
  const isConnected = useStore($isConnected);
  const { currentData: imageDTO, isError } = useGetImageDTOQuery(field.value?.image_name ?? skipToken);

  const handleReset = useCallback(() => {
    dispatch(
      fieldImageValueChanged({
        nodeId,
        fieldName: field.name,
        value: undefined,
      })
    );
  }, [dispatch, field.name, nodeId]);

  const draggableData = useMemo<TypesafeDraggableData | undefined>(() => {
    if (imageDTO) {
      return {
        id: `node-${nodeId}-${field.name}`,
        payloadType: 'IMAGE_DTO',
        payload: { imageDTO },
      };
    }
  }, [field.name, imageDTO, nodeId]);

  const droppableData = useMemo<TypesafeDroppableData | undefined>(
    () => ({
      id: `node-${nodeId}-${field.name}`,
      actionType: 'SET_NODES_IMAGE',
      context: { nodeId, fieldName: field.name },
    }),
    [field.name, nodeId]
  );

  const postUploadAction = useMemo<PostUploadAction>(
    () => ({
      type: 'SET_NODES_IMAGE',
      nodeId,
      fieldName: field.name,
    }),
    [nodeId, field.name]
  );

  useEffect(() => {
    if (isConnected && isError) {
      handleReset();
    }
  }, [handleReset, isConnected, isError]);

  return (
    <Flex
      className="nodrag"
      w="full"
      h="full"
      alignItems="center"
      justifyContent="center"
      borderColor="error.500"
      borderStyle="solid"
      borderWidth={fieldTemplate.required && !field.value ? 1 : 0}
      borderRadius="base"
    >
      <IAIDndImage
        imageDTO={imageDTO}
        droppableData={droppableData}
        draggableData={draggableData}
        postUploadAction={postUploadAction}
        useThumbailFallback
        uploadElement={<UploadElement />}
        minSize={8}
      >
        <IAIDndImageIcon
          onClick={handleReset}
          icon={imageDTO ? <PiArrowCounterClockwiseBold /> : undefined}
          tooltip="Reset Image"
        />
      </IAIDndImage>
    </Flex>
  );
};

export default memo(ImageFieldInputComponent);

const UploadElement = memo(() => {
  const { t } = useTranslation();
  return (
    <Flex h={16} w="full" alignItems="center" justifyContent="center">
      <Text fontSize={16} fontWeight="semibold">
        {t('gallery.dropOrUpload')}
      </Text>
    </Flex>
  );
});

UploadElement.displayName = 'UploadElement';
