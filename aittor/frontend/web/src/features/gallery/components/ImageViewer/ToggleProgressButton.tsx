import { IconButton } from '@aittorai/ui-library';
import { useAppDispatch, useAppSelector } from 'app/store/storeHooks';
import { selectShouldShowProgressInViewer } from 'features/ui/store/uiSelectors';
import { setShouldShowProgressInViewer } from 'features/ui/store/uiSlice';
import { memo, useCallback } from 'react';
import { useTranslation } from 'react-i18next';
import { PiHourglassHighBold } from 'react-icons/pi';

export const ToggleProgressButton = memo(() => {
  const dispatch = useAppDispatch();
  const shouldShowProgressInViewer = useAppSelector(selectShouldShowProgressInViewer);
  const { t } = useTranslation();

  const onClick = useCallback(() => {
    dispatch(setShouldShowProgressInViewer(!shouldShowProgressInViewer));
  }, [dispatch, shouldShowProgressInViewer]);

  return (
    <IconButton
      aria-label={t('settings.displayInProgress')}
      tooltip={t('settings.displayInProgress')}
      icon={<PiHourglassHighBold />}
      onClick={onClick}
      variant="outline"
      colorScheme={shouldShowProgressInViewer ? 'appBlue' : 'base'}
      data-testid="toggle-show-progress-button"
    />
  );
});

ToggleProgressButton.displayName = 'ToggleProgressButton';
