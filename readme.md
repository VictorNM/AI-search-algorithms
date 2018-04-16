# INSTRUCTIONS

1) The aim of the game is to get the block to fall into the square hole at the end of each stage. There are 33 stages to complete.

2) To move the block around the world, use the left, right, up and down arrow keys. Be careful not to fall off the edges. The level will be restarted if this happens.

3) Bridges and switches are located in many levels. The switches are activated when they are pressed down by the block. You do not need to stay resting on the switch to keep bridges closed.

4) There are two types of switches: "Heavy" x-shaped ones and "soft" octagon ones... Soft switches (octagons) are activated when any part of your block presses it. Hard switches (x's) require much more pressure, so your block must be standing on its end to activate them.

5) When activated, each switch may behave differently. Some will swap the bridges from open to closed to open each time it is used. Some will create bridges permanently. Green or red colored squares will flash to indicate which bridges are being operated.

6) Orange tiles are more fragile than the rest of the land. If your block stands up vertically on an orange tile, the tile will give way and your block will fall through.

7) Finally, there is a third type of switch shaped like this: ( ) It teleports your block to different locations, splitting it into two smaller blocks at the same time. These can be controlled individually and will rejoin into a normal block when both are places next to each other.

8) You can select which small block to use at any time by pressing the spacebar. Small blocks can still operate soft switches, but they aren't big enough to activate heavy switches. Also, small blocks cannot go through the exit hole -- only a complete block can finish the stage.

9) Remember the passcode for each stage. It is located in the top right corner. You can skip straight back to each stage later on by going to "Load Stage" in the main menu and entering the 6 digit level code.

Enjoy!

# MODELLING

![alt text](https://raw.githubusercontent.com/NguyenMauVinh1627058/AI-Assignment-1/master/illustration.png)

## Map:

- A matrix has size: x*y
- Cell value is determined as follow:
	+ EMPTY 		:	EMPT	: 0
	+ HARD_TILE		:	H_TI 	: 1
	+ SOFT_TILE		:	S_TI 	: 2
	+ HARD_SWITCH	:	H_SW 	: 3
	+ SOFT_SWITCH	: 	S_SW 	: 4
	+ SPLIT_PORT 	:	SPLI 	: 5
	+ GOAL_HOLE 	:	GOAL 	: 6

## Some necessary resources:

- List of Bridge's positions: [(xb_1, yb_1), (xb_2, yb_2), ..., (xb_n, yb_n)]
- Mapping between switch - bridge - action (close -1, toggle 0, open 1)
	+ example: switch (1,1) will open bridge index 1 and close bridge index 
	2	=> ~~( (1,1) , (1,1) , (2,-1) )~~ {(1,1):{1:1,2:-1}}
	+ explain: {switch_position:{tile_position:action,...}}
- Mapping between split port - split destination

## State:

- List of 2 sub-lists [block_positions, bridge_status]
- block_positions = [(x_1, y_1), (x_2, y_2)] : positions of 2 blocks
- bridge_status = [s_1, s_2, ..., s_n] : s = [EMPTY,HARD_TILE]

## Initial state:
- Base on each stage

## Goal state:
- (map[x_1][y_1] == GOAL_HOLE) and (map[x_2][y_2] == GOAL_HOLE)
- x_1, y_1, x_2, y_2: positions of 2 blocks

## Legal moves:

- 2 steps: move -> consequence
- 2 type of moves:
	+ move all
	+ move single
- 4 moves / type
	+ UP 	:	up_all() 	/ up_single(block_position)
	+ DOWN 	: 	down_all() 	/ down_single(block_position)
	+ LEFT 	: 	left_all()	/ left_single(block_position)
	+ RIGHT : 	right_all() / right_single(block_position)
- 3 consequences
	+ is_on_soft_switch => turn bridge on / off
	+ is_on_hard_switch => turn bridge on / off
	+ is_on_split_port  => split and teleport to SPLIT_DEST

## Valid states:
- All block is not on EMPTY	: (map[x_1][y_1] != EMPTY) and (map[x_2][y_2] != EMPTY)
- Not stand on SOFT_TILE	: not ((x_1, y_1) == (x_2, y_2) and map[x_1][y_1] == SOFT_TILE)

## Heuristic:
- Distance	(main heuristic)
- Number of open bridge (optional)
- // Have path to GOAL_HOLE?

# STAGE MODELING

## Stage 1:

1. Passcode: 780464
2. Init stage:
3. Map:

## Stage 2:

1. Passcode: 290299

2. Init stage: ~~((4,1), (4,1), (0,0,0,0))~~ [[(4,1),(4,1)],[0,0,0,0]]

3. Map: matrix 6x15

	[[EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI],  
	 [H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_SW, H_TI, EMPT, EMPT, H_TI, GOAL, H_TI],  
	 [H_TI, H_TI, S_SW, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI],  
	 [H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI],  
	 [H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI],  
	 [H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT]]

4. List bridge's position:
	- 4 bridges:
	[(4,4), (4,5), (4,10), (4,11)]

5. Mapping Switch - Bridge:
	- 2 switches vs 4 bridge
	~~{
		(2,2) : [(0,0), (1,0)]
		(1,8) : [(2,0), (3,0)]
	}~~
	{
	 	(2,2):{0:0,1:0},
	 	(1,8):{2:0,3:0}
	}

6. Mapping Split port - Split destination:
	- None

## Stage 3:

1. Passcode: 918660
2. Init stage:[[(1,3),(1,3)],[]]
3. Matrix: 15x6
		[
		[EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,EMPT,EMPT],
		[H_TI,H_TI,H_TI,H_TI,EMPT,EMPT,H_TI,H_TI,H_TI,EMPT,EMPT,H_TI,H_TI,EMPT,EMPT],
		[H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,H_TI,EMPT,EMPT,H_TI,H_TI,H_TI,H_TI],
		[H_TI,H_TI,H_TI,H_TI,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,H_TI,H_TI,GOAL,H_TI],
		[H_TI,H_TI,H_TI,H_TI,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,H_TI,H_TI,H_TI,H_TI],
		[EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,H_TI,H_TI,H_TI],
		]
3. Goal stage:
	[[(13,3),(13,3)],[]]
4. Brides: None

## Stage 4:

1. Passcode: 520967
2. Init stage:
3. Goal stage:

## Stage 5:

1. Passcode: 528431
2. Init stage: ((1,14),(1,14), (1,1,1,1,1,1))
3. Map: 10x16

	[[EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI],
	 [EMPT, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, S_SW, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI],
	 [EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, H_TI, H_TI, H_TI],
	 [EMPT, H_TI, H_TI, S_SW, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT],
	 [EMPT, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT],
	 [EMPT, EMPT, EMPT, H_TI, H_TI, H_TI, S_SW, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT],
	 [EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, S_SW],
	 [H_TI, H_TI, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, H_TI, H_TI, H_TI, H_TI, H_TI],
	 [H_TI, GOAL, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, H_TI, EMPT, EMPT],
	 [H_TI, H_TI, H_TI, H_TI, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT, EMPT]]
4. List bridge's position:
	- 6 bridges
	[[(1,5),(1,6)],[(5,8),(5,9)],[(8,5),(8,6)]	
5. Mapping Switch - Bridge:
	- 4 switches and 6 bridges
	{(1,8):[(1,0)]
	(3,3): [(3,-1)] //close
	(5,6): [(3,1] //open
	(6,15):[(3,0)]}
6. Mapping Split port - Split destination:
	None
## Stage 6:

1. Passcode: 524383
2. Init stage:
3. Goal stage:

## Stage 7:

1. Passcode: 189493
2. Init stage:
3. Goal stage:

## Stage 8:

1. Passcode: 499707
2. Init stage:
3. Goal stage:

## Stage 9:

1. Passcode: 074355
2. Init stage:
3. Goal stage:

## Stage 10:

1. Passcode: 300590
2. Init stage:
3. Goal stage:

## Stage 11:

1. Passcode: 291709
2. Init stage:
3. Goal stage:

## Stage 12:

1. Passcode: 958640
2. Init stage:
3. Goal stage:

## Stage 13:

1. Passcode: 448106
2. Init stage:
3. Goal stage:

## Stage 14:

1. Passcode: 210362
2. Init stage:
3. Goal stage:

## Stage 15:

1. Passcode: 098598
2. Init stage:
3. Goal stage:

## Stage 16:

1. Passcode: 000241
2. Init stage:
3. Goal stage:

## Stage 17:

1. Passcode: 683596
2. Init stage:
3. Goal stage:

## Stage 18:

1. Passcode: 284933
2. Init stage:
3. Goal stage:
4. Map:

## Stage 19:

1. Passcode: 119785
2. Init stage:
3. Goal stage:
4. Map:

## Stage 20:

1. Passcode: 543019
2. Init stage:
3. Goal stage:
4. Map:

## Stage 21:

1. Passcode: 728724
2. Init stage:
3. Goal stage:
4. Map:

## Stage 22:

1. Passcode: 987329
2. Init stage:
3. Goal stage:
4. Map:

## Stage 23:

1. Passcode: 293486
2. Init stage:
3. Goal stage:
4. Map:

## Stage 24:

1. Passcode: 088198
2. Init stage:
3. Goal stage:
4. Map:

## Stage 25:

1. Passcode: 250453
2. Init stage:
3. Goal stage:
4. Map:

## Stage 26:

1. Passcode: 426329
2. Init stage:
3. Goal stage:
4. Map:

## Stage 27:

1. Passcode: 660141
2. Init stage:
3. Goal stage:
4. Map:

## Stage 28:

1. Passcode: 769721
2. Init stage:
3. Goal stage:
4. Map:

## Stage 29:

1. Passcode: 691859
2. Init stage:
3. Goal stage:
4. Map:

## Stage 30:

1. Passcode: 280351
2. Init stage:
3. Goal stage:
4. Map:

## Stage 31:

1. Passcode: 138620
2. Init stage:
3. Goal stage:
4. Map:

## Stage 32:

1. Passcode: 879021
2. Init stage:
3. Goal stage:
4. Map:

## Stage 33:

1. Passcode: 614955
2. Init stage:
3. Goal stage:
4. Map: