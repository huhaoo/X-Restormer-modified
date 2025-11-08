# compat_tv.py
import sys, types
from torchvision.transforms import functional as F

m = types.ModuleType("torchvision.transforms.functional_tensor")
m.rgb_to_grayscale = F.rgb_to_grayscale  # 按需再补别的函数
sys.modules["torchvision.transforms.functional_tensor"] = m

# flake8: noqa
import os.path as osp

import xrestormer.archs
import xrestormer.data
import xrestormer.models
from basicsr.test import test_pipeline

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    test_pipeline(root_path)
