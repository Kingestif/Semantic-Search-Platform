import streamlit.watcher.local_sources_watcher as local_sources_watcher

# Patch to skip torch module
original_get_module_paths = local_sources_watcher.get_module_paths

def patched_get_module_paths(module):
    try:
        return original_get_module_paths(module)
    except Exception as e:
        if "torch" in str(module):
            return []
        else:
            raise e

local_sources_watcher.get_module_paths = patched_get_module_paths
