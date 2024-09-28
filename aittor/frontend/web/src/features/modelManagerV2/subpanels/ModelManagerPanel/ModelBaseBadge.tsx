import { Badge } from '@aittorai/ui-library';
import { MODEL_TYPE_SHORT_MAP } from 'features/parameters/types/constants';
import { memo } from 'react';
import type { BaseModelType } from 'services/api/types';

type Props = {
  base: BaseModelType;
};

const BASE_COLOR_MAP: Record<BaseModelType, string> = {
  any: 'base',
  'sd-1': 'green',
  'sd-2': 'teal',
  sdxl: 'appBlue',
  'sdxl-refiner': 'appBlue',
  flux: 'gold',
};

const ModelBaseBadge = ({ base }: Props) => {
  return (
    <Badge flexGrow={0} colorScheme={BASE_COLOR_MAP[base]} variant="subtle" h="min-content">
      {MODEL_TYPE_SHORT_MAP[base]}
    </Badge>
  );
};

export default memo(ModelBaseBadge);
