import type { PopoverProps } from '@aittorai/ui-library';
import commercialLicenseBg from 'public/assets/images/commercial-license-bg.png';

export type Feature =
  | 'clipSkip'
  | 'hrf'
  | 'paramNegativeConditioning'
  | 'paramPositiveConditioning'
  | 'paramScheduler'
  | 'compositingMaskBlur'
  | 'compositingBlurMethod'
  | 'compositingCoherencePass'
  | 'compositingCoherenceMode'
  | 'compositingCoherenceEdgeSize'
  | 'compositingCoherenceMinDenoise'
  | 'compositingMaskAdjustments'
  | 'controlNet'
  | 'controlNetBeginEnd'
  | 'controlNetControlMode'
  | 'controlNetProcessor'
  | 'controlNetResizeMode'
  | 'controlNetWeight'
  | 'dynamicPrompts'
  | 'dynamicPromptsMaxPrompts'
  | 'dynamicPromptsSeedBehaviour'
  | 'imageFit'
  | 'infillMethod'
  | 'ipAdapterMethod'
  | 'lora'
  | 'loraWeight'
  | 'noiseUseCPU'
  | 'paramAspect'
  | 'paramCFGScale'
  | 'paramGuidance'
  | 'paramCFGRescaleMultiplier'
  | 'paramDenoisingStrength'
  | 'paramHeight'
  | 'paramHrf'
  | 'paramIterations'
  | 'paramModel'
  | 'paramRatio'
  | 'paramSeed'
  | 'paramSteps'
  | 'paramUpscaleMethod'
  | 'paramVAE'
  | 'paramVAEPrecision'
  | 'paramWidth'
  | 'patchmatchDownScaleSize'
  | 'refinerModel'
  | 'refinerNegativeAestheticScore'
  | 'refinerPositiveAestheticScore'
  | 'refinerScheduler'
  | 'refinerStart'
  | 'refinerSteps'
  | 'refinerCfgScale'
  | 'scaleBeforeProcessing'
  | 'seamlessTilingXAxis'
  | 'seamlessTilingYAxis'
  | 'upscaleModel'
  | 'scale'
  | 'creativity'
  | 'structure'
  | 'optimizedDenoising'
  | 'fluxDevLicense';

export type PopoverData = PopoverProps & {
  image?: string;
  href?: string;
  buttonLabel?: string;
};

export const POPOVER_DATA: { [key in Feature]?: PopoverData } = {
  paramNegativeConditioning: {
    placement: 'right',
  },
  clipSkip: {
    href: 'https://support.aittor.com/support',
  },
  controlNet: {
    href: 'https://support.aittor.com/support',
  },
  controlNetBeginEnd: {
    href: 'https://support.aittor.com/support',
  },
  controlNetWeight: {
    href: 'https://support.aittor.com/support',
  },
  lora: {
    href: 'https://support.aittor.com/support',
  },
  loraWeight: {
    href: 'https://support.aittor.com/support',
  },
  compositingMaskBlur: {
    href: 'https://support.aittor.com/support',
  },
  compositingBlurMethod: {
    href: 'https://support.aittor.com/support',
  },
  compositingCoherenceMode: {
    href: 'https://support.aittor.com/support',
  },
  infillMethod: {
    href: 'https://support.aittor.com/support',
  },
  scaleBeforeProcessing: {
    href: 'https://support.aittor.com/support',
  },
  paramCFGScale: {
    href: 'https://support.aittor.com/support',
  },
  paramCFGRescaleMultiplier: {
    href: 'https://support.aittor.com/support',
  },
  paramDenoisingStrength: {
    href: 'https://support.aittor.com/support',
  },
  paramHrf: {
    href: 'https://support.aittor.com/support',
  },
  paramIterations: {
    href: 'https://support.aittor.com/support',
  },
  paramPositiveConditioning: {
    href: 'https://support.aittor.com/support',
    placement: 'right',
  },
  paramScheduler: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  paramSeed: {
    href: 'https://support.aittor.com/support',
  },
  paramModel: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  paramRatio: {
    gutter: 16,
  },
  controlNetControlMode: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  controlNetProcessor: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  controlNetResizeMode: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  paramVAE: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  paramVAEPrecision: {
    placement: 'right',
    href: 'https://support.aittor.com/support',
  },
  paramUpscaleMethod: {
    href: 'https://support.aittor.com/support',
  },
  refinerModel: {
    href: 'https://support.aittor.com/support',
  },
  refinerNegativeAestheticScore: {
    href: 'https://support.aittor.com/support',
  },
  refinerPositiveAestheticScore: {
    href: 'https://support.aittor.com/support',
  },
  refinerScheduler: {
    href: 'https://support.aittor.com/support',
  },
  refinerStart: {
    href: 'https://support.aittor.com/support',
  },
  refinerSteps: {
    href: 'https://support.aittor.com/support',
  },
  refinerCfgScale: {
    href: 'https://support.aittor.com/support',
  },
  seamlessTilingXAxis: {
    href: 'https://support.aittor.com/support',
  },
  seamlessTilingYAxis: {
    href: 'https://support.aittor.com/support',
  },
  fluxDevLicense: {
    href: 'https://support.aittor.com/support',
    image: commercialLicenseBg,
  },
} as const;

export const OPEN_DELAY = 1000; // in milliseconds

export const POPPER_MODIFIERS: PopoverProps['modifiers'] = [{ name: 'preventOverflow', options: { padding: 10 } }];
