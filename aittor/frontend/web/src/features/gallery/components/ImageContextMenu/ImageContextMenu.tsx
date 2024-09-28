import type { ContextMenuProps } from '@aittorai/ui-library';
import { ContextMenu, MenuList } from '@aittorai/ui-library';
import { useAppSelector } from 'app/store/storeHooks';
import { selectSelectionCount } from 'features/gallery/store/gallerySelectors';
import { memo, useCallback } from 'react';
import type { ImageDTO } from 'services/api/types';

import MultipleSelectionMenuItems from './MultipleSelectionMenuItems';
import SingleSelectionMenuItems from './SingleSelectionMenuItems';

type Props = {
  imageDTO: ImageDTO | undefined;
  children: ContextMenuProps<HTMLDivElement>['children'];
};

const ImageContextMenu = ({ imageDTO, children }: Props) => {
  const selectionCount = useAppSelector(selectSelectionCount);

  const renderMenuFunc = useCallback(() => {
    if (!imageDTO) {
      return null;
    }

    if (selectionCount > 1) {
      return (
        <MenuList visibility="visible">
          <MultipleSelectionMenuItems />
        </MenuList>
      );
    }

    return (
      <MenuList visibility="visible">
        <SingleSelectionMenuItems imageDTO={imageDTO} />
      </MenuList>
    );
  }, [imageDTO, selectionCount]);

  return <ContextMenu renderMenu={renderMenuFunc}>{children}</ContextMenu>;
};

export default memo(ImageContextMenu);
