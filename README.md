# DatasetHarvester
*A collection of scripts to easily download Video Object Segmentation (VOS) datasets for my research.* 

---
> [!NOTE]
> Contributions are welcomed to improve this repo 🤗
---

## - Download the [SA-V Dataset](https://ai.meta.com/datasets/segment-anything-video/)
*Introduced in [SAM 2: Segment Anything in Images and Videos Paper](https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/) / [Code](https://github.com/facebookresearch/segment-anything-2)*
1. Fill this [Meta document](https://ai.meta.com/datasets/segment-anything-video-downloads/) out to get access to the URLs
2. Adapt the corresponding [download_SA_V.yaml](./scripts/SA_V/download_SA_V.yaml) with the URLs
3. Adapt the paths in [download_SA_V.py](https://github.com/Vujas-Eteph/DatasetHarvester/blob/6c785a019b467b36622d348fb4f87f4256f960ba/scripts/SA_V/download_SA_V.py#L44) - line 44
4. Run
     ```zsh
     cd scripts/SA_V/
     python download_SA_V.py
     ```
5. More stuff [**HERE**](https://github.com/facebookresearch/segment-anything-2/blob/main/sav_dataset)

- Citation
  ```bibtex
  @article{ravi2024sam2,
    title={SAM 2: Segment Anything in Images and Videos},
    author={Ravi, Nikhila and Gabeur, Valentin and Hu, Yuan-Ting and Hu, Ronghang and Ryali, Chaitanya and Ma, Tengyu and Khedr, Haitham and R{\"a}dle, Roman and Rolland, Chloe and Gustafson, Laura and Mintun, Eric and Pan, Junting and Alwala, Kalyan Vasudev and Carion, Nicolas and Wu, Chao-Yuan and Girshick, Ross and Doll{\'a}r, Piotr and Feichtenhofer, Christoph},
    journal={arXiv preprint arXiv:2408.00714},
    url={https://arxiv.org/abs/2408.00714},
    year={2024}
  }
  ```

> [!NOTE]  
> It took me circa 3h30min to download the complete dataset (using a single core)


## - Download the [LVOS Dataset (v1 and v2)](https://github.com/LingyiHongfd/LVOS)
*Introduced in [LVOS: A Benchmark for Large-scale
Long-term Video Object Segmentation](https://arxiv.org/pdf/2404.19326)*

1. Adapt [the path in l. 15](https://github.com/Vujas-Eteph/DatasetHarvester/blob/fba7f31ecb6380566afac1c48ab5bcbcc5273bc1/scripts/LVOS/config.yaml#L15)
2. Run 
     ```zsh
     cd scripts/LVOS/
     python download_LVOS.py
     ```
     ***Optional:** Run the following script if needed*
     ```zsh
     python annotation_first_only.py
     ```
3. [Official Evaluation ToolKit](https://github.com/LingyiHongfd/lvos-evaluation)

- Citation
  ```bibtex
  @InProceedings{Hong_2023_ICCV,
      author    = {Hong, Lingyi and Chen, Wenchao and Liu, Zhongying and Zhang, Wei and Guo, Pinxue and Chen, Zhaoyu and Zhang, Wenqiang},
      title     = {LVOS: A Benchmark for Long-term Video Object Segmentation},
      booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
      month     = {October},
      year      = {2023},
      pages     = {13480-13492}
  }
  ```

> [!NOTE]  
> Don't run too many times on the same day the download on the same PC...

## - Download the [VOST Dataset](https://www.vostdataset.org/index.html)
