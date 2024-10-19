import type { IconProps } from '@aittorai/ui-library';
import { Icon } from '@aittorai/ui-library';
import { memo } from 'react';

export const AppLogoIcon = memo((props: IconProps) => {
  return (
    <Icon boxSize={8} opacity={1} stroke="base.500" viewBox="0 0 24 24" fill="none" {...props}>
      <path d="M4 14h8v7l8-11h-8V3z" strokeWidth="2" />
    </Icon>
  );
});

AppLogoIcon.displayName = 'AppLogoIcon';
