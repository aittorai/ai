import { Tag, TagCloseButton, TagLabel } from '@aittorai/ui-library';
import { useStore } from '@nanostores/react';
import { useAppDispatch, useAppSelector } from 'app/store/storeHooks';
import { $activeScopes } from 'common/hooks/interactionScopes';
import { useGalleryImages } from 'features/gallery/hooks/useGalleryImages';
import { selectionChanged } from 'features/gallery/store/gallerySlice';
import { useRegisteredHotkeys } from 'features/system/components/HotkeysModal/useHotkeyData';
import { $isRightPanelOpen } from 'features/ui/store/uiSlice';
import { computed } from 'nanostores';
import { useCallback } from 'react';
import { useTranslation } from 'react-i18next';

const $isSelectAllEnabled = computed([$activeScopes, $isRightPanelOpen], (activeScopes, isGalleryPanelOpen) => {
  return activeScopes.has('gallery') && !activeScopes.has('workflows') && isGalleryPanelOpen;
});

export const GallerySelectionCountTag = () => {
  const dispatch = useAppDispatch();
  const { selection } = useAppSelector((s) => s.gallery);
  const { t } = useTranslation();
  const { imageDTOs } = useGalleryImages();
  const isSelectAllEnabled = useStore($isSelectAllEnabled);

  const onClearSelection = useCallback(() => {
    const firstImage = selection[0];
    if (firstImage) {
      dispatch(selectionChanged([firstImage]));
    }
  }, [dispatch, selection]);

  const onSelectPage = useCallback(() => {
    dispatch(selectionChanged([...selection, ...imageDTOs]));
  }, [dispatch, selection, imageDTOs]);

  useRegisteredHotkeys({
    id: 'selectAllOnPage',
    category: 'gallery',
    callback: onSelectPage,
    options: { preventDefault: true, enabled: isSelectAllEnabled },
    dependencies: [onSelectPage, isSelectAllEnabled],
  });

  useRegisteredHotkeys({
    id: 'clearSelection',
    category: 'gallery',
    callback: onClearSelection,
    options: { enabled: selection.length > 0 && isSelectAllEnabled },
    dependencies: [onClearSelection, selection, isSelectAllEnabled],
  });

  if (selection.length <= 1) {
    return null;
  }

  return (
    <Tag
      position="absolute"
      bg="appBlue.800"
      color="base.50"
      py={2}
      px={4}
      userSelect="none"
      shadow="dark-lg"
      fontWeight="semibold"
      border={1}
      borderStyle="solid"
      borderColor="whiteAlpha.300"
    >
      <TagLabel>
        {selection.length} {t('common.selected')}
      </TagLabel>
      <TagCloseButton onClick={onClearSelection} />
    </Tag>
  );
};
