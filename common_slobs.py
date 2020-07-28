# These classes are used to represent SLOBS itself.

class SLOBS():
    def __init__(self):
        self.scene_collections = None

class SLOBSSceneCollection():
    def __init__(self):
        self.scenes = None

class SLOBSScene():
    def __init__(self):
        self.scene = None
        self.sources = None

class SLOBSSource():
    def __init__(self):
        self.source = None