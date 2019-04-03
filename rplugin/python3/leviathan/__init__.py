import pynvim


@pynvim.plugin
class LeviathanPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function('LeviathanInit', sync=True)
    def initialize(self, args):
        self.nvim.out_write('init\n')
