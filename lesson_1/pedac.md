INPUT: integer of available blocks

OUTPUT: integer of blocks 'left over'  after building the talles possible valid 
structure

RULES:
1. Structure is built with building blocks
2. The building blocks are cubes
2-1 cubes are six sided square faced
3. The structure is built in layers
4. The top layer is a single block
5. A block in an upper layer must be supported by 4 blocks in a lower layer
6. A block in a lower layer can support more than 1 block in an upper layer
    (ex. 4 blocks in 1st layer and 2 or more blocks in 2nd layer)
7. no gaps between blocks

QUESTIONS:
1. what are cubes?

###    
def calculate_leftover_blocks(available_blocks):
    
    1st layer: layer * layer
    2nd layer: layer * layer
    repeat until next layer required number of blocks < remaining blocks
    return remaining_blocks

Define function(available_blocks):
    remaining blocks = available_blocks
    layer = 1
    required blocks of next layer = layer * layer
    while required nums of block < remaining blocks:
        used_blocks = layer ** layer
        remaining blocks -= used_blocks
        layer += 1
    return remaining_blocks
###    

ALGORITHM:
1. Build the structure one layer at a time that starts with 1 block and 
following layer containing 4 blocks (valid layer) until a number of remaining 
block is less than a number of blocks required.
2. Count the remaining numbers of blocks

Adjusted Algorithm:
1. Start with:
    -The "number of blocks remaining" is equal to the input(=available blocks)
    -The "current layer number" is 0.
2. Add 1 to the "current layer number" for the next layer
3. The "number of blocks required in this layer" is "current layer number" * "current layer number".r
4. Determine if updated "number of blocks remaining" is larger or equal than the "number of blocks required in this layer".
- If larger or equal:
Subtract "number of blocks required in this layer" from "number of blocks remaining" (to update a new "number of blocks remaining)"
go to step 2
-If not larger or equal:
Return the "number of blocks remaining"

TEST CASES:
number_of_blocks_remaining = 5
current_layer_number = 0
while True:
    current_layer_number = 1
    number_of_blocks_required_in_this_layer = 1
    if 5 > 1:
        num_blocks_remaining = 5-1