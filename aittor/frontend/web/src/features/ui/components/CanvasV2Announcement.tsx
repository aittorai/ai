import { ExternalLink, Flex, ListItem, UnorderedList } from '@aittorai/ui-library';
import { createSelector } from '@reduxjs/toolkit';
import { useAppSelector } from 'app/store/storeHooks';
import { selectConfigSlice } from 'features/system/store/configSlice';
import { useTranslation } from 'react-i18next';

const selectIsLocal = createSelector(selectConfigSlice, (config) => config.isLocal);

export const CanvasV2Announcement = () => {
  const { t } = useTranslation();
  const isLocal = useAppSelector(selectIsLocal);

  return (
    <Flex gap={4} flexDir="column">
      <UnorderedList fontSize="sm">
        <ListItem>{t('whatsNew.canvasV2Announcement.newCanvas')}</ListItem>
        <ListItem>{t('whatsNew.canvasV2Announcement.newLayerTypes')}</ListItem>
        <ListItem>{t('whatsNew.canvasV2Announcement.fluxSupport')}</ListItem>
      </UnorderedList>
      <Flex flexDir="column" gap={1}>
      </Flex>
    </Flex>
  );
};
