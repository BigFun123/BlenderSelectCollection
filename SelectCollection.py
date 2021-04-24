bl_info = {
    "name": "Select Collection",
    "blender": (2, 80, 0),
    "category": "Object",
    "author": "John Liebe"
}

import bpy

# Works in Blender 2.8.x and 2.9.x

class SelectCollection(bpy.types.Operator):
    """Object Select Collection"""
    bl_idname = "object.cursor_array"
    bl_label = "Select Collection"
    bl_options = {'REGISTER', 'UNDO'}

    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=100)

    def execute(self, context):
        bpy.ops.object.select_grouped(type='COLLECTION')
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(SelectCollection)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addona
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(SelectCollection.bl_idname, 'LEFTMOUSE', 'PRESS', alt=True)
        kmi.properties.total = 4
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(SelectCollection)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()