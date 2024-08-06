# DataHarvester
*A collection of scripts to easily (automatically) download datasets for my research.* 

---

## ↪️ Download the [SA-V Dataset](https://ai.meta.com/datasets/segment-anything-video/)
*Introduced in the [SAM 2: Segment Anything in Images and Videos Paper](https://ai.meta.com/research/publications/sam-2-segment-anything-in-images-and-videos/) / [Code](https://github.com/facebookresearch/segment-anything-2)*
1. Fill this [Meta document](https://ai.meta.com/datasets/segment-anything-video-downloads/) out to get access to the URLs
2. Adapt the corresponding [download_SA_V.yaml]() with the URLs
3. Adapt the paths in [download_SA_V.py]()
4. Run
     ```zsh
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
> It took me circa 3h30min to download the complete dataset

</details>
