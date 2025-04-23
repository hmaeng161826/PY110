'''
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
'''
'''
Implementation:
'''
def calculate_leftover_blocks(available_blocks):
    remaining_blocks =  available_blocks
    current_layer = 0
    required_blocks_upcoming_layer = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks_upcoming_layer:
        remaining_blocks -= required_blocks_upcoming_layer
        current_layer += 1
        required_blocks_upcoming_layer = (current_layer + 1) ** 2
        

    return remaining_blocks


print(calculate_leftover_blocks(0))
print(calculate_leftover_blocks(1))
print(calculate_leftover_blocks(2))
print(calculate_leftover_blocks(4))
print(calculate_leftover_blocks(5))
print(calculate_leftover_blocks(6))
print(calculate_leftover_blocks(14))