export const colorTokenToCssVar = (colorToken: string) => `var(--app-colors-${colorToken.split('.').join('-')})`;
