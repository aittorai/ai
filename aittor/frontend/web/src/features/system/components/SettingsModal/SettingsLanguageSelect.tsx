import type { ComboboxOnChange } from '@aittorai/ui-library';
import { Combobox, FormControl, FormLabel } from '@aittorai/ui-library';
import { useAppDispatch, useAppSelector } from 'app/store/storeHooks';
import { useFeatureStatus } from 'features/system/hooks/useFeatureStatus';
import { selectLanguage } from 'features/system/store/systemSelectors';
import { languageChanged } from 'features/system/store/systemSlice';
import type { Language } from 'features/system/store/types';
import { isLanguage } from 'features/system/store/types';
import { map } from 'lodash-es';
import { memo, useCallback, useMemo } from 'react';
import { useTranslation } from 'react-i18next';

const optionsObject: Record<Language, string> = {
  en: 'English',
  zh_CN: '简体中文',
};

const options = map(optionsObject, (label, value) => ({ label, value }));

export const SettingsLanguageSelect = memo(() => {
  const { t } = useTranslation();
  const dispatch = useAppDispatch();
  const language = useAppSelector(selectLanguage);
  const isLocalizationEnabled = useFeatureStatus('localization');

  const value = useMemo(() => options.find((o) => o.value === language), [language]);

  const onChange = useCallback<ComboboxOnChange>(
    (v) => {
      if (!isLanguage(v?.value)) {
        return;
      }
      dispatch(languageChanged(v.value));
    },
    [dispatch]
  );
  return (
    <FormControl isDisabled={!isLocalizationEnabled}>
      <FormLabel>{t('common.languagePickerLabel')}</FormLabel>
      <Combobox value={value} options={options} onChange={onChange} />
    </FormControl>
  );
});

SettingsLanguageSelect.displayName = 'SettingsLanguageSelect';
