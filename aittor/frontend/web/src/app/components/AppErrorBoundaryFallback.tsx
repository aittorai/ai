import { Button, Flex, Heading, Image, Text } from '@aittorai/ui-library';
import { toast } from 'features/toast/toast';
import AppLogoYellow from 'public/assets/images/app-symbol-ylw-lrg.svg';
import { memo, useCallback } from 'react';
import { useTranslation } from 'react-i18next';
import { PiArrowCounterClockwiseBold, PiCopyBold } from 'react-icons/pi';
import { serializeError } from 'serialize-error';

type Props = {
  error: Error;
  resetErrorBoundary: () => void;
};

const AppErrorBoundaryFallback = ({ error, resetErrorBoundary }: Props) => {
  const { t } = useTranslation();

  const handleCopy = useCallback(() => {
    const text = JSON.stringify(serializeError(error), null, 2);
    navigator.clipboard.writeText(`\`\`\`\n${text}\n\`\`\``);
    toast({
      id: 'ERROR_COPIED',
      title: t('toast.errorCopied'),
    });
  }, [error, t]);

  const url = useMemo(() => {
    if (isLocal) {
      return newGithubIssueUrl({
        user: 'aittorai',
        repo: 'AI',
        template: 'BUG_REPORT.yml',
        title: `[bug]: ${error.name}: ${error.message}`,
      });
    } else {
      return 'https://support.aittor.com/support';
    }
  }, [error.message, error.name, isLocal]);

  return (
    <Flex layerStyle="body" w="100dvw" h="100dvh" alignItems="center" justifyContent="center" p={4}>
      <Flex layerStyle="first" flexDir="column" borderRadius="base" justifyContent="center" gap={8} p={16}>
        <Flex alignItems="center" gap="2">
          <Image src={AppLogoYellow} alt="app-logo" w="24px" h="24px" minW="24px" minH="24px" userSelect="none" />
          <Heading fontSize="2xl">{t('common.somethingWentWrong')}</Heading>
        </Flex>

        <Flex
          layerStyle="second"
          px={8}
          py={4}
          gap={4}
          borderRadius="base"
          justifyContent="space-between"
          alignItems="center"
        >
          <Text fontWeight="semibold" color="error.400">
            {error.name}: {error.message}
          </Text>
        </Flex>
        <Flex gap={4}>
          <Button leftIcon={<PiArrowCounterClockwiseBold />} onClick={resetErrorBoundary}>
            {t('accessibility.resetUI')}
          </Button>
          <Button leftIcon={<PiCopyBold />} onClick={handleCopy}>
            {t('common.copyError')}
          </Button>

        </Flex>
      </Flex>
    </Flex>
  );
};

export default memo(AppErrorBoundaryFallback);
