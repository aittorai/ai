import type { SystemStyleObject } from '@aittorai/ui-library';
import { Box, Flex, Icon, Text, Tooltip } from '@aittorai/ui-library';
import { useAppDispatch, useAppSelector } from 'app/store/storeHooks';
import IAIDroppable from 'common/components/IAIDroppable';
import type { RemoveFromBoardDropData } from 'features/dnd/types';
import { AutoAddBadge } from 'features/gallery/components/Boards/AutoAddBadge';
import { BoardTooltip } from 'features/gallery/components/Boards/BoardsList/BoardTooltip';
import NoBoardBoardContextMenu from 'features/gallery/components/Boards/NoBoardBoardContextMenu';
import {
  selectAutoAddBoardId,
  selectAutoAssignBoardOnClick,
  selectBoardSearchText,
} from 'features/gallery/store/gallerySelectors';
import { autoAddBoardIdChanged, boardIdSelected } from 'features/gallery/store/gallerySlice';
import { memo, useCallback, useMemo } from 'react';
import { useTranslation } from 'react-i18next';
import { useGetBoardImagesTotalQuery } from 'services/api/endpoints/boards';
import { useBoardName } from 'services/api/hooks/useBoardName';

interface Props {
  isSelected: boolean;
}

const _hover: SystemStyleObject = {
  bg: 'base.850',
};

const NoBoardBoard = memo(({ isSelected }: Props) => {
  const dispatch = useAppDispatch();
  const { imagesTotal } = useGetBoardImagesTotalQuery('none', {
    selectFromResult: ({ data }) => {
      return { imagesTotal: data?.total ?? 0 };
    },
  });
  const autoAddBoardId = useAppSelector(selectAutoAddBoardId);
  const autoAssignBoardOnClick = useAppSelector(selectAutoAssignBoardOnClick);
  const boardSearchText = useAppSelector(selectBoardSearchText);
  const boardName = useBoardName('none');
  const handleSelectBoard = useCallback(() => {
    dispatch(boardIdSelected({ boardId: 'none' }));
    if (autoAssignBoardOnClick) {
      dispatch(autoAddBoardIdChanged('none'));
    }
  }, [dispatch, autoAssignBoardOnClick]);

  const droppableData: RemoveFromBoardDropData = useMemo(
    () => ({
      id: 'no_board',
      actionType: 'REMOVE_FROM_BOARD',
    }),
    []
  );

  const { t } = useTranslation();

  if (boardSearchText.length) {
    return null;
  }

  return (
    <Box position="relative" w="full" h={12}>
      <NoBoardBoardContextMenu>
        {(ref) => (
          <Tooltip label={<BoardTooltip board={null} />} openDelay={1000} placement="left" closeOnScroll>
            <Flex
              ref={ref}
              onClick={handleSelectBoard}
              w="full"
              h="full"
              alignItems="center"
              borderRadius="base"
              cursor="pointer"
              py={1}
              ps={1}
              pe={4}
              gap={4}
              bg={isSelected ? 'base.850' : undefined}
              _hover={_hover}
            >
              <Flex w="10" justifyContent="space-around">
                {/* iconified from public/assets/images/app-symbol-wht-lrg.svg */}
              <Icon boxSize={8} opacity={1} stroke="base.500" viewBox="0 0 24 24" fill="none">
                <path
                  d="M4 14h8v7l8-11h-8V3z"
                  strokeWidth="2"
                />
              </Icon>
              </Flex>

              <Text
                fontSize="sm"
                color={isSelected ? 'base.100' : 'base.300'}
                fontWeight="semibold"
                noOfLines={1}
                flexGrow={1}
              >
                {boardName}
              </Text>
              {autoAddBoardId === 'none' && <AutoAddBadge />}
              <Text variant="subtext">{imagesTotal}</Text>
            </Flex>
          </Tooltip>
        )}
      </NoBoardBoardContextMenu>
      <IAIDroppable data={droppableData} dropLabel={t('gallery.move')} />
    </Box>
  );
});

NoBoardBoard.displayName = 'HoverableBoard';

export default memo(NoBoardBoard);
