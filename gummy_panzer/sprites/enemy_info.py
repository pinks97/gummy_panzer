
AERIAL_ENEMY_HEALTH = 10

PATTERN_STRAIGHT = [(-1,0)]
PATTERN_WAVE_MID_DOWN = [(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5)]
PATTERN_WAVE_MID_UP = [(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5)]
PATTERN_WAVE_TOP = [(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0),(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0)]
PATTERN_WAVE_BOTTOM = [(-2,0),(-2,-1),(-2,-2),(-2,-3),(-2,-4),(-2,-5),(-2,-5),(-2,-4),(-2,-3),(-2,-2),(-2,-1),(-2,0),(-2,0),(-2,1),(-2,2),(-2,3),(-2,4),(-2,5),(-2,5),(-2,4),(-2,3),(-2,2),(-2,1),(-2,0)]
PATTERN_DIAG_DOWN = [(-4,2)]
PATTERN_DIAG_UP = [(-4,-2)]

SPRITE_ONE = 'enemy_sprite.png'
SPRITE_TWO = ""
SPRITE_THREE = ""

STATE_MOVING = 0
STATE_SHOOTING = 1
STATE_DYING = 2

STATE_MOVING_LEN = 6
STATE_SHOOTING_LEN = 6
STATE_DYING_LEN = 6

ANIM_LEN = [STATE_MOVING_LEN,STATE_SHOOTING_LEN,STATE_DYING_LEN]

STATE_W = 50
STATE_H = 50