import obspython as S
import time


print("start")

scenes = S.obs_frontend_get_scenes()
print(scenes)

current_scene = S.obs_scene_from_source(S.obs_frontend_get_current_scene())
print(current_scene)
current_scene_name = S.obs_source_get_name(S.obs_frontend_get_current_scene())
print(current_scene_name)
if current_scene_name == "Game No Cam":
    for scene in scenes:
        name = S.obs_source_get_name(scene)
        if name == "Game (W/ Cam)":
            print("switching")
            S.obs_frontend_set_current_scene(scene)

print("done")
