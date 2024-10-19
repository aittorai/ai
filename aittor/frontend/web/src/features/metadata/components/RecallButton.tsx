import type { IconButtonProps } from '@aittorai/ui-library';
import { IconButton, Tooltip } from '@aittorai/ui-library';
import { memo } from 'react';
import { useTranslation } from 'react-i18next';
import { PiArrowBendUpLeftBold } from 'react-icons/pi';

type MetadataItemProps = Omit<IconButtonProps, 'aria-label'> & {
  label: string;
};

export const RecallButton = memo(({ label, ...rest }: MetadataItemProps) => {
  const { t } = useTranslation();

  return (
    <Tooltip label={t('metadata.recallParameter', { label })}>
      <IconButton
        aria-label={t('metadata.recallParameter', { label })}
        icon={<PiArrowBendUpLeftBold />}
        size="xs"
        variant="ghost"
        {...rest}
      />
    </Tooltip>
  );
});

RecallButton.displayName = 'RecallButton';
