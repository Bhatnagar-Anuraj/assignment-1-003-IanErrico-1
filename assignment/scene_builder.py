#Assignment 1:

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# Object 2 -- Tree (cylinder)
# ---------------------------------------------------------------------------
tree_height = 5
tree_radius = 0.5
tree_x = 5
tree_z = 3

tree = cmds.polyCylinder(
    name="tree",
    height=tree_height,
    radius=tree_radius
)[0]

cmds.move(tree_x, tree_height / 2.0, tree_z, tree)

# ---------------------------------------------------------------------------
# Object 3 -- Crate (cube)
# ---------------------------------------------------------------------------
crate_size = 2
crate_x = 2
crate_z = 6

crate = cmds.polyCube(
    name="wood_crate",
    width=crate_size,
    height=crate_size,
    depth=crate_size
)[0]

cmds.move(crate_x, crate_size / 2.0, crate_z, crate)

# ---------------------------------------------------------------------------
# Object 4 -- Pillar (cylinder)
# ---------------------------------------------------------------------------
pillar_height = 6
pillar_radius = 1
pillar_x = -2
pillar_z = -5

pillar = cmds.polyCylinder(
    name="stone_pillar",
    height=pillar_height,
    radius=pillar_radius
)[0]

cmds.move(pillar_x, pillar_height / 2.0, pillar_z, pillar)

# ---------------------------------------------------------------------------
# Object 5 -- Fence (cube)
# ---------------------------------------------------------------------------
fence_width = 6
fence_height = 1
fence_depth = 0.3
fence_x = 8
fence_z = -2

fence = cmds.polyCube(
    name="fence_section",
    width=fence_width,
    height=fence_height,
    depth=fence_depth
)[0]

cmds.move(fence_x, fence_height / 2.0, fence_z, fence)

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")

