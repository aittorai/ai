import { Flex, ListItem, UnorderedList } from '@aittorai/ui-library';
import { useTranslation } from 'react-i18next';

export const CanvasV2Announcement = () => {
  const { t } = useTranslation();

  return (
    <Flex gap={4} flexDir="column">
      <UnorderedList fontSize="sm">
        <ListItem>{t('whatsNew.canvasV2Announcement.newCanvas')}</ListItem>
        <ListItem>{t('whatsNew.canvasV2Announcement.newLayerTypes')}</ListItem>
        <ListItem>{t('whatsNew.canvasV2Announcement.fluxSupport')}</ListItem>
      </UnorderedList>
    </Flex>
  );
};
