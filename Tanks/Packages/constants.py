PIXEL_SIZE = 2

DIRECTIONS = {'straight': 'w',
              'left': 'a',
              'back': 's',
              'right': 'd'}
# Doesn't depend on the current 'head' position

START_HEAD_POS = {'i': 1,
                  'j': 3,
                  'eye_direct': 'd'}
# i, j or y, x (according to school program)

FIELD_SIZE = (20, 20)
# Game field size (length, width)

# tank_pattern = ((1, 1, 1),
#                 (1, 1, 1, 1),
#                 (1, 1, 1))
# tank_pattern_coordinates = {(0, 0), (0, 1), (0, 2),
#                             (1, 0), (1, 1), (1, 2), (1, 3),
#                             (2, 0), (2, 1), (2, 2)}
# i = head_pos[0]
# j = head_pos[1]
# tank_pattern_coordinates = {(i - 1, j - 3), (i - 1, j - 2), (i - 1, j - 1),
#                             (i, j - 3), (i, j - 2), (i, j - 1), (i, j),
#                             (i + 1, j - 3), (i + 1, j - 2), (i + 1, j - 1)}
