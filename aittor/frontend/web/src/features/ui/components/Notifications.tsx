import {
  Flex,
  IconButton,
  Image,
  Popover,
  PopoverArrow,
  PopoverBody,
  PopoverCloseButton,
  PopoverContent,
  PopoverHeader,
  PopoverTrigger,
  Text,
} from '@aittorai/ui-library';
import { useAppDispatch, useAppSelector } from 'app/store/storeHooks';
import { shouldShowNotificationChanged } from 'features/ui/store/uiSlice';
import AppSymbol from 'public/assets/images/app-favicon.png';
import { useCallback } from 'react';
import { useTranslation } from 'react-i18next';
import { PiLightbulbFilamentBold } from 'react-icons/pi';
import { useGetAppVersionQuery } from 'services/api/endpoints/appInfo';

import { CanvasV2Announcement } from './CanvasV2Announcement';

export const Notifications = () => {
  const { t } = useTranslation();
  const dispatch = useAppDispatch();
  const shouldShowNotification = useAppSelector((s) => s.ui.shouldShowNotification);
  const resetIndicator = useCallback(() => {
    dispatch(shouldShowNotificationChanged(false));
  }, [dispatch]);
  const { data } = useGetAppVersionQuery();

  if (!data) {
    return null;
  }

  return (
    <Popover onClose={resetIndicator} placement="top-start" autoFocus={false} defaultIsOpen={shouldShowNotification}>
      <PopoverTrigger>
        <Flex pos="relative">
          <IconButton
            aria-label="Notifications"
            variant="link"
            icon={<PiLightbulbFilamentBold fontSize={20} />}
            boxSize={8}
          />
        </Flex>
      </PopoverTrigger>
      <PopoverContent p={2}>
        <PopoverArrow />
        <PopoverCloseButton />
        <PopoverHeader fontSize="md" fontWeight="semibold" pt={5}>
          <Flex alignItems="center" gap={3}>
            <Image src={AppSymbol} boxSize={6} />
            {t('whatsNew.whatsNewInApp')}
            <Text variant="subtext">{`v${data.version}`}</Text>
          </Flex>
        </PopoverHeader>
        <PopoverBody p={2}>
          <CanvasV2Announcement />
        </PopoverBody>
      </PopoverContent>
    </Popover>
  );
};
