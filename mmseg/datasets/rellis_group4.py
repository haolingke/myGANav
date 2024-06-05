
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class RELLISDataset_Group4(BaseSegDataset):
    """RELLIS dataset.

    """

    METAINFO = dict(
        classes = ("background", "L1 (Smooth)", "non-Nav (Forbidden)", "obstacle"),
        palette = [[ 0, 0, 0 ], [ 0,128,0 ],
            [ 255, 0, 0 ],[  0, 0, 128] ])

    

    def __init__(self,img_suffix='.jpg',
            seg_map_suffix='_group4.png',
            **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            **kwargs)
