import obspython as S

scenes = S.obs_frontend_get_scenes()

def Cam():
    current_scene = S.obs_scene_from_source(S.obs_frontend_get_current_scene())
    current_scene_name = S.obs_source_get_name(S.obs_frontend_get_current_scene())
    if current_scene_name == "Game No Cam":
        for scene in scenes:
            name = S.obs_source_get_name(scene)
            if name == "Game (W/ Cam":
                S.obs_frontend_set_current_scene(scene)

def noCam():
    current_scene = S.obs_scene_from_source(S.obs_frontend_get_current_scene())
    current_scene_name = S.obs_source_get_name(S.obs_frontend_get_current_scene())
    if current_scene_name == "Game (W/ Cam)":
        for scene in scenes:
            name = S.obs_source_get_name(scene)
            if name == "Game (W/ Cam":
                S.obs_frontend_set_current_scene(scene)



'''

def script_properties():  # ui
    props = S.obs_properties_create()
    p = S.obs_properties_add_list(
        props,
        "source",
        "Text Source",
        S.OBS_COMBO_TYPE_EDITABLE,
        S.OBS_COMBO_FORMAT_STRING,
    )
    sources = S.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = S.obs_source_get_unversioned_id(source)
            name = S.obs_source_get_name(source)
            S.obs_property_list_add_string(p, name, name)

        S.source_list_release(sources)
    S.obs_properties_add_button(props, "button", "Toggle", toggle_pressed)
    return props
'''