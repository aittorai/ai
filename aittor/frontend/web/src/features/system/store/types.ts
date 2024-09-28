import type { LogLevel, LogNamespace } from 'app/logging/logger';
import { z } from 'zod';


const zLanguage = z.enum([
  'en',
  'zh_CN',
]);

export type Language = z.infer<typeof zLanguage>;
export const isLanguage = (v: unknown): v is Language => zLanguage.safeParse(v).success;

export interface SystemState {
  _version: 1;
  shouldConfirmOnDelete: boolean;
  shouldAntialiasProgressImage: boolean;
  language: Language;
  shouldUseNSFWChecker: boolean;
  shouldUseWatermarker: boolean;
  shouldEnableInformationalPopovers: boolean;
  logIsEnabled: boolean;
  logLevel: LogLevel;
  logNamespaces: LogNamespace[];
}
