import { Flex, Icon, MenuItem, Text, Tooltip } from '@aittorai/ui-library';
import { useTranslation } from 'react-i18next';
import type { IconType } from 'react-icons';
import { PiArrowUpBold } from 'react-icons/pi';

export const SettingsUpsellMenuItem = ({ menuText, menuIcon }: { menuText: string; menuIcon: IconType }) => {
  const { t } = useTranslation();

  return (
    <Tooltip label={t('upsell.professionalUpsell')} placement="right" gutter={16}>
      <MenuItem as="a" http://aittor.com" target="_blank" icon={menuIcon({})}>
        <Flex gap="1" alignItems="center" justifyContent="space-between">
          <Text>{menuText}</Text>
          <Icon as={PiArrowUpBold} color="appYellow.500" />
        </Flex>
      </MenuItem>
    </Tooltip>
  );
};
