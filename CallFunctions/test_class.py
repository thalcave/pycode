from ftf.data import *

class Data(BaseIncrementalData):
    def __init__(self, name, lstage0, lstage1):
        BaseIncrementalData.__init__(self, name)

        self.func_stage_0 = globals()[lstage0]
        self.func_stage_1 = globals()[lstage1]

    class Stage0(BaseStage):
        def update_files(self, target):
            self.data.func_stage_0(target)
            generate_summary(target, os.path.join(self.cache, 'summary'))


    class Stage1(BaseStage):
        def update_files(self, target):
            self.data.func_stage_1(target)
            generate_summary(target, os.path.join(self.cache, 'summary'))
