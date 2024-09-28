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
    href: '',
  },
  controlNet: {
    href: '',
  },
  controlNetBeginEnd: {
    href: '',
  },
  controlNetWeight: {
    href: '',
  },
  lora: {
    href: '',
  },
  loraWeight: {
    href: '',
  },
  compositingMaskBlur: {
    href: '',
  },
  compositingBlurMethod: {
    href: '',
  },
  compositingCoherenceMode: {
    href: '',
  },
  infillMethod: {
    href: '',
  },
  scaleBeforeProcessing: {
    href: '',
  },
  paramCFGScale: {
    href: '',
  },
  paramCFGRescaleMultiplier: {
    href: '',
  },
  paramDenoisingStrength: {
    href: '',
  },
  paramHrf: {
    href: '',
  },
  paramIterations: {
    href: '',
  },
  paramPositiveConditioning: {
    href: '',
    placement: 'right',
  },
  paramScheduler: {
    placement: 'right',
    href: '',
  },
  paramSeed: {
    href: '',
  },
  paramModel: {
    placement: 'right',
    href: '',
  },
  paramRatio: {
    gutter: 16,
  },
  controlNetControlMode: {
    placement: 'right',
    href: '',
  },
  controlNetProcessor: {
    placement: 'right',
    href: '-using-controlnet',
  },
  controlNetResizeMode: {
    placement: 'right',
    href: '',
  },
  paramVAE: {
    placement: 'right',
    href: '',
  },
  paramVAEPrecision: {
    placement: 'right',
    href: '',
  },
  paramUpscaleMethod: {
    href: '',
  },
  refinerModel: {
    href: '',
  },
  refinerNegativeAestheticScore: {
    href: '',
  },
  refinerPositiveAestheticScore: {
    href: '',
  },
  refinerScheduler: {
    href: '',
  },
  refinerStart: {
    href: '',
  },
  refinerSteps: {
    href: '',
  },
  refinerCfgScale: {
    href: '',
  },
  seamlessTilingXAxis: {
    href: '',
  },
  seamlessTilingYAxis: {
    href: '',
  },
  fluxDevLicense: {
    href: https://support.aittor.com,
    image: commercialLicenseBg,
  },
} as const;

export const OPEN_DELAY = 1000; // in milliseconds

export const POPPER_MODIFIERS: PopoverProps['modifiers'] = [{ name: 'preventOverflow', options: { padding: 10 } }];
