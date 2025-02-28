import { Flex, Image, Spinner } from '@aittorai/ui-library';
import AppLogoWhite from 'public/assets/images/app-symbol-wht-lrg.svg';
import { memo } from 'react';

// This component loads before the theme so we cannot use theme tokens here

const Loading = () => {
  return (
    <Flex position="relative" width="100dvw" height="100dvh" alignItems="center" justifyContent="center" bg="#151519">
      <Image src={AppLogoWhite} w="8rem" h="8rem" />
      <Spinner
        label="Loading"
        color="grey"
        position="absolute"
        size="sm"
        width="24px !important"
        height="24px !important"
        right="1.5rem"
        bottom="1.5rem"
      />
    </Flex>
  );
};

export default memo(Loading);
