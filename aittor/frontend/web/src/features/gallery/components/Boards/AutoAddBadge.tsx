import { Badge } from '@aittorai/ui-library';
import { memo } from 'react';
import { useTranslation } from 'react-i18next';

export const AutoAddBadge = memo(() => {
  const { t } = useTranslation();
  return (
    <Badge color="appBlue.400" borderColor="appBlue.700" borderWidth={1} bg="transparent" flexShrink={0}>
      {t('common.auto')}
    </Badge>
  );
});

AutoAddBadge.displayName = 'AutoAddBadge';
