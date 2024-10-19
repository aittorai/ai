import '@fontsource-variable/inter';
import 'overlayscrollbars/overlayscrollbars.css';

import { ChakraProvider, DarkMode, extendTheme, theme as _theme, TOAST_OPTIONS } from '@aittorai/ui-library';
import type { ReactNode } from 'react';
import { memo, useEffect, useMemo } from 'react';
import { useTranslation } from 'react-i18next';

type ThemeLocaleProviderProps = {
  children: ReactNode;
};

function ThemeLocaleProvider({ children }: ThemeLocaleProviderProps) {
  const { i18n } = useTranslation();

  const direction = i18n.dir();

  const theme = useMemo(() => {
    return extendTheme({
      ..._theme,
      direction,
      shadows: {
        ..._theme.shadows,
        selected:
          'inset 0px 0px 0px 3px var(--app-colors-appBlue-500), inset 0px 0px 0px 4px var(--app-colors-appBlue-800)',
        hoverSelected:
          'inset 0px 0px 0px 3px var(--app-colors-appBlue-400), inset 0px 0px 0px 4px var(--app-colors-appBlue-800)',
        hoverUnselected:
          'inset 0px 0px 0px 2px var(--app-colors-appBlue-300), inset 0px 0px 0px 3px var(--app-colors-appBlue-800)',
        selectedForCompare:
          'inset 0px 0px 0px 3px var(--app-colors-appGreen-300), inset 0px 0px 0px 4px var(--app-colors-appGreen-800)',
        hoverSelectedForCompare:
          'inset 0px 0px 0px 3px var(--app-colors-appGreen-200), inset 0px 0px 0px 4px var(--app-colors-appGreen-800)',
      },
    });
  }, [direction]);

  useEffect(() => {
    document.body.dir = direction;
  }, [direction]);

  return (
    <ChakraProvider theme={theme} toastOptions={TOAST_OPTIONS}>
      <DarkMode>{children}</DarkMode>
    </ChakraProvider>
  );
}

export default memo(ThemeLocaleProvider);
