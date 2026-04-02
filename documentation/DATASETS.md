# Preamble
This file gives a brief description of each dataset present for the semi-automatic task (not a exhaustive list, but almost IMO).
For more details refer to the original material/publications/code.  
In addition we provide some documentations on the code we use for visualization and <other stuff to insert here\>.

*Misaligned comments:*
- Download links for youtube 2018 all validation (Need a CodaLab account): https://competitions.codalab.org/competitions/19544#participate. For the 2019 version : https://competitions.codalab.org/competitions/20127#participate
- Run this to get the tree structure (when all datasets are downloaded)
  ```console
  tree -L 2 -d > directory_structure.txt
  ```

---
:fire: TODO list

- [ ] Make a file for automatically download the datasets.
- [ ] Refine the description of each dataset.
- [ ] Add a table with each statistics.
- [ ] Add documentation on how to visualize the datasets.  
- [ ] Add documentation on how to compute and visualize some statistics.
- [ ] Automatic generation of the table needed for here and graphs.
- [ ] Make a separation between tracking and segmentation datasets. Other README.md file

---

Overview of the satasets (Downloaded + Extracted [images and annotations]):
- [x] DAVIS
- [x] Y-VOS
- [x] LV1
- [x] BURST
- [x] LVOS
- [x] MOSE
- [x] OVIS
- [x] BL30K
- [x] static
- [x] VOST (The Tracking version)
- [x] PUMaVOS
- [x] SA-V (the one Meta used to train SAM 2)
- [ ] LVOS 2 (Need to install)

Tracking datasets
- [x] VOTS2023
- [x] VOT2022
- [x] OTB 

---
# Datasets Description

### :arrow_right: Segmentation

<details><summary><b>DAVIS</b></summary>

[DAVIS](https://davischallenge.org/) is the vanilla dataset for sVOS evaluations. Methods achieve high performance now on this benchmark, and is not that competitive anymore.
However papers still integrated the DAVIS dataset as it is the most well-known dataset and other datasets have their repository structured in the same way. 
  
Tool for the evaluation ➡️ [VOS-benchmark](https://github.com/hkchengrex/vos-benchmark)


**BibTeX**
```bibtex
@Article{Caelles_arXiv_2019,
  author  = {Sergi Caelles and Jordi Pont-Tuset and Federico Perazzi and Alberto Montes and Kevis-Kokitsi Maninis and Luc {Van Gool}},
  journal = {arXiv:1905.00737},
  title   = {The 2019 DAVIS Challenge on VOS: Unsupervised Multi-Object Segmentation},
  year    = {2019},
  file    = {:paper/Caelles_arXiv_2019.pdf:PDF},
  groups  = {Datasets&Challenges, VOS, DAVIS},
}

@Article{Caelles_arXiv_2018,
  author  = {Sergi Caelles and Alberto Montes and Kevis-Kokitsi Maninis and Yuhua Chen and Luc {Van Gool} and Federico Perazzi and Jordi Pont-Tuset},
  journal = {arXiv:1803.00557},
  title   = {The 2018 DAVIS Challenge on Video Object Segmentation},
  year    = {2018},
  file    = {:paper/Caelles_arXiv_2018.pdf:PDF},
  groups  = {Datasets&Challenges, VOS, DAVIS},
}

@Article{Pont-Tuset_arXiv_2017,
  author  = {Jordi Pont-Tuset and Federico Perazzi and Sergi Caelles and Pablo Arbel\'aez and Alexander Sorkine-Hornung and Luc {Van Gool}},
  journal = {arXiv:1704.00675},
  title   = {The 2017 DAVIS Challenge on Video Object Segmentation},
  year    = {2017},
  file    = {:paper/Pont-Tuset_arXiv_2017.pdf:PDF},
  groups  = {Datasets&Challenges, VOS, DAVIS},
}

@inproceedings{perazzi2016benchmark,
  title={A benchmark dataset and evaluation methodology for video object segmentation},
  author={Perazzi, Federico and Pont-Tuset, Jordi and McWilliams, Brian and Van Gool, Luc and Gross, Markus and Sorkine-Hornung, Alexander},
  booktitle={CVPR},
  year={2016}
}
```

</details>

<details><summary><b>YVOS</b></summary>

[YVOS](https://youtube-vos.org/) is as popular VOS datasets (if DAVIS vanilla, then YVOS is the chocolate flavor) - It contains more sequences terms, but the sequences aren't that longer compared to DAVIS. 

If you wish to evaluate the results, you'll need to submit the results for the validation set on the following servers for [YTVOS-2019](https://codalab.lisn.upsaclay.fr/competitions/6066)(the name of the dataset is [YoutTube](./YouTube)) and [YTVOS-2018](https://codalab.lisn.upsaclay.fr/competitions/7685) (the dataset of the dataset is [YoutTube2018](./YouTube2018/)).

**BibTeX**
```bibtex
@inproceedings{xu2018youtubeVOS,
  title={Youtube-vos: A large-scale video object segmentation benchmark},
  author={Xu, Ning and Yang, Linjie and Fan, Yuchen and Yue, Dingcheng and Liang, Yuchen and Yang, Jianchao and Huang, Thomas},
  booktitle = {ECCV},
  year={2018}
}
```

</details>

<details><summary><b>LV1</b></summary>

The [LV1](https://www.kaggle.com/datasets/gvclsu/long-videos) dataset contains only 3 videos, but those videos are much more longer than those found in DAVIS or YVOS.  
Tool for the evaluation ➡️ [VOS-benchmark](https://github.com/hkchengrex/vos-benchmark)

**BibTeX**
```bibtex
@inproceedings{xu2018youtubeVOS,
  title={Youtube-vos: A large-scale video object segmentation benchmark},
  author={Xu, Ning and Yang, Linjie and Fan, Yuchen and Yue, Dingcheng and Liang, Yuchen and Yang, Jianchao and Huang, Thomas},
  booktitle = {ECCV},
  year={2018}
}
```

</details>
<details><summary><b>BURST</b></summary>

The recently introduced [BURST](https://github.com/Ali2500/BURST-benchmark) dataset also comes with its own toolkit for visualization and evaluation. This dataset is based on the [TAO](https://taodataset.org/) which has only BBox annotation types. Interestingly, the test data is available here for reporting the results on their benchmark page.
To download the complete dataset you also need these: https://motchallenge.net/tao_download_secure.php but you need have an account to download this.


**BibTeX**
```bibtex
@inproceedings{athar2023burst,
  title={BURST: A Benchmark for Unifying Object Recognition, Segmentation and Tracking in Video},
  author={Athar, Ali and Luiten, Jonathon and Voigtlaender, Paul and Khurana, Tarasha and Dave, Achal and Leibe, Bastian and Ramanan, Deva},
  booktitle={WACV},
  year={2023}
}
```

</details>
<details><summary><b>LVOS</b></summary> 

The [LVOS](https://lingyihongfd.github.io/lvos.github.io/) dataset is designed to be a long-term video object segmentation dataset, which each sequence lasting 1.59 minutes on average.

Have not tried the toolkit if any is available.

**BibTeX**
```bibtex
@article{hong2022lvos,
title={LVOS: A Benchmark for Long-term Video Object Segmentation},
author={Hong, Lingyi and Chen, Wenchao and Liu, Zhongying and Zhang, Wei and Guo, Pinxue and Chen, Zhaoyu and Zhang, Wenqiang},
journal={arXiv preprint arXiv:2211.10181},
year={2022},
}
```
</details>


<details><summary><b>static</b></summary> 

The static dataset is actually composed of multiple segmentation (small) datasets that only contains single images.
The dataset is composed of:
- [DUTS](http://saliencydetection.net/duts)
- [HRSOD](https://github.com/yi94code/HRSOD)
- [FGS](https://github.com/HKUSTCV/FSS-1000)
- [ECSSD](https://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/dataset.html)
- [BIG](https://github.com/hkchengrex/CascadePSP)

**BibTeX**
```bibtex
@inproceedings{wang2017DUTS,
  title={Learning to Detect Salient Objects with Image-level Supervision},
  author={Wang, Lijun and Lu, Huchuan and Wang, Yifan and Feng, Mengyang 
  and Wang, Dong, and Yin, Baocai and Ruan, Xiang}, 
  booktitle={CVPR},
  year={2017}
}

@InProceedings{Zeng_2019_ICCV,
  author = {Zeng, Yi and Zhang, Pingping and Zhang, Jianming and Lin, Zhe and Lu, Huchuan},
  title = {Towards High-Resolution Salient Object Detection},
  booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
  month = {October},
  year = {2019}
}


@inproceedings{FSS1000,
  title = {FSS-1000: A 1000-Class Dataset for Few-Shot Segmentation},
  author = {Li, Xiang and Wei, Tianhan and Chen, Yau Pun and Tai, Yu-Wing and Tang, Chi-Keung},
  booktitle={CVPR},
  year={2020}
}

@inproceedings{shi2015hierarchicalECSSD,
  title={Hierarchical image saliency detection on extended CSSD},
  author={Shi, Jianping and Yan, Qiong and Xu, Li and Jia, Jiaya},
  booktitle={TPAMI},
  year={2015},
}

@inproceedings{cheng2020cascadepsp,
  title={{CascadePSP}: Toward Class-Agnostic and Very High-Resolution Segmentation via Global and Local Refinement},
  author={Cheng, Ho Kei and Chung, Jihoon and Tai, Yu-Wing and Tang, Chi-Keung},
  booktitle={CVPR},
  year={2020}
}

@inproceedings{shapenet2015,
  title       = {{ShapeNet: An Information-Rich 3D Model Repository}},
  author      = {Chang, Angel Xuan and Funkhouser, Thomas and Guibas, Leonidas and Hanrahan, Pat and Huang, Qixing and Li, Zimo and Savarese, Silvio and Savva, Manolis and Song, Shuran and Su, Hao and Xiao, Jianxiong and Yi, Li and Yu, Fisher},
  booktitle   = {arXiv:1512.03012},
  year        = {2015}
}

@inproceedings{perazzi2016benchmark,
  title={A benchmark dataset and evaluation methodology for video object segmentation},
  author={Perazzi, Federico and Pont-Tuset, Jordi and McWilliams, Brian and Van Gool, Luc and Gross, Markus and Sorkine-Hornung, Alexander},
  booktitle={CVPR},
  year={2016}
}
```

</details>
<details><summary><b>BL30K</b></summary> 

[[BL30K]](https://github.com/hkchengrex/MiVOS/#bl30k) is a synthetic dataset rendered using Blender with ShapeNet's data. 
Download the dataset using this [script (download_bl30k.py)](https://github.com/hkchengrex/XMem/blob/main/scripts/download_bl30k.py).
⚠️ This is a very large dataset (more than 1TB). Ensure that you have the space to download this dataset.

Google Drive link to download this: [[Google Drive link]](https://drive.google.com/drive/folders/1KxriFZM8Y_-KbiA3D0PaMv6LQaatKFH-)

**BibTeX**
```bibtex
@inproceedings{cheng2021mivos,
  title={Modular Interactive Video Object Segmentation: Interaction-to-Mask, Propagation and Difference-Aware Fusion},
  author={Cheng, Ho Kei and Tai, Yu-Wing and Tang, Chi-Keung},
  booktitle={CVPR},
  year={2021}
}

@inproceedings{denninger2019blenderproc,
  title={BlenderProc},
  author={Denninger, Maximilian and Sundermeyer, Martin and Winkelbauer, Dominik and Zidan, Youssef and Olefir, Dmitry and Elbadrawy, Mohamad and Lodhi, Ahsan and Katam, Harinandan},
  booktitle={arXiv:1911.01911},
  year={2019}
}

@inproceedings{shapenet2015,
  title       = {{ShapeNet: An Information-Rich 3D Model Repository}},
  author      = {Chang, Angel Xuan and Funkhouser, Thomas and Guibas, Leonidas and Hanrahan, Pat and Huang, Qixing and Li, Zimo and Savarese, Silvio and Savva, Manolis and Song, Shuran and Su, Hao and Xiao, Jianxiong and Yi, Li and Yu, Fisher},
  booktitle   = {arXiv:1512.03012},
  year        = {2015}
}
```

</details>
<details><summary><b>MOSE</b></summary> 

The [MOSE](https://henghuiding.github.io/MOSE/) dataset should replace DAVIS and YVOS, as it is more complex (SOTA methods achieve a score of around ~55 on J&F), and targets the same short term context, as videos' don't last to long.
I really like it because it is fairly easy to integrate (just follows the [MOSE-api](https://github.com/henghuiding/MOSE-api)) with other sVOS methods, as it follows the patterns given by MiVOS/STCN/XMem and AOT/De-AOT
and to evaluation as it follows the DAVIS format.
Here is the [MOSE-api](https://github.com/

**BibTeX**
```bibtex
@inproceedings{MOSE,
  title={{MOSE}: A New Dataset for Video Object Segmentation in Complex Scenes},
  author={Ding, Henghui and Liu, Chang and He, Shuting and Jiang, Xudong and Torr, Philip HS and Bai, Song},
  booktitle={ICCV},
  year={2023}
}
```

</details>
<details><summary><b>OVIS</b></summary> 

The [OVIS](https://songbai.site/ovis/), present as workshops also, contains sequences where occlusion is abundantly present, hence more difficul and good for evaluation SOTA methods. But I have not seen the dataset used in many SOTA papers, or I've not been thorough during my reading sessions ?  
Also to read the dataset segmentation masks, use [their variante of the COCO API](https://github.com/qjy981010/cocoapi).

Here are some links:
- [Original Method](https://github.com/qjy981010/CMaskTrack-RCNN)
- [Evaluation code](https://github.com/qjy981010/cocoapi)

**BibTeX**
```bibtex
@article{qi2022occluded,
    title={Occluded Video Instance Segmentation: A Benchmark},
    author={Jiyang Qi and Yan Gao and Yao Hu and Xinggang Wang and Xiaoyu Liu and Xiang Bai and Serge Belongie and Alan Yuille and Philip Torr and Song Bai},
    journal={International Journal of Computer Vision},
    year={2022},
} 
```
</details>

<details><summary><b>PUMaVOS</b></summary>

[PUMaVOS](https://github.com/max810/XMem2): Partial and Unusual MAsk
Video Object Segmentation. Provides a new benchmark that covers use cases for
multipart partial segmentation with visually challenging sit-
Figure 5. Samples of our dataset (PUMaVOS). Best viewed
zoomed. See Fig. 9 in Appendix for more examples.
uations (segments of parts of the scene with little-to-no
pixel-level visual cues. We focus on partial objects such as half faces,
neck, tattoos, and pimples, which are frequently retouched
in film production as shown in Fig 5. Our dataset consists
of 24 clips 28.7 seconds long on average. To generate the
annotations, we adopted a similar approach to MOSE [8]
that used a framework with XMem [4] to create masks for
each frame, but instead we used our method, XMem++. In
MOSE the videos were annotated every 5th frame (20% of
the video), while in our case we noticed that complex scenes
require 8% to 10% and simple scenes required 4% to 6% of
total frames to be annotated.

**BibTeX**
```bibtex
@misc{bekuzarov2023xmem,
      title={XMem++: Production-level Video Segmentation From Few Annotated Frames}, 
      author={Maksym Bekuzarov and Ariana Bermudez and Joon-Young Lee and Hao Li},
      year={2023},
      eprint={2307.15958},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

```
</details>

---

### :arrow_right: Tracking

<details><summary><b>VOTS2023</b></summary>OVIS

This is actually a [Challenge](https://www.votchallenge.net/) that takes place every year at major CV conferences.
The official [terminology under Key concepts](https://github.com/votchallenge/toolkit/blob/master/docs/overview.rst)
Follow the guidlines from their [overview](https://www.votchallenge.net/howto/overview.html) to integrate and download a dataset.

**BibTeX**
```bibtex
@article {VOT_TPAMI,
    author = {Matej Kristan and Jiri Matas and Ale\v{s} Leonardis and Tomas Vojir and Roman Pflugfelder and Gustavo Fernandez and Georg Nebehay and Fatih Porikli and Luka \v{C}ehovin},
    journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
    title={A Novel Performance Evaluation Methodology for Single-Target Trackers},
    year={2016}, month={Nov}, volume={38}, number={11}, pages={2137-2155},
    doi={10.1109/TPAMI.2016.2516982}, ISSN={0162-8828}
}
```
</details>


<details><summary><b>VOST</b></summary> 

The official [repo link](https://www.vostdataset.org/).

*"VOST is a semi-supervised video object segmentation benchmark that focuses on complex object transformations. Differently from existing datasets, objects in VOST are broken, torn and molded into new shapes, dramatically changing their overall appearance. As our experiments demonstrate, this presents a major challenge for the mainstream, appearance-centric VOS methods. The dataset consists of more than 700 high-resolution videos, captured in diverse environments, which are 21 seconds long on average and densely labeled with instance masks. A careful, multi-step approach is adopted to ensure that these videos focus on complex transformations, capturing their full temporal extent. Below, we provide a few key statistics of the dataset."*

How to do evaluation? -> [GitHub link](https://github.com/TRI-ML/VOST)

**BibTeX**
```bibtex
@inproceedings{tokmakov2023breaking,
  title={Breaking the" Object" in Video Object Segmentation},
  author={Tokmakov, Pavel and Li, Jie and Gaidon, Adrien},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={22836--22845},
  year={2023}
}
```
</details>

# 🧰ToolBox Description

For the moment none.

<details><summary><b>Visualizations</b></summary></details>

<details><summary><b>Evaluations</b></summary></details>

<details><summary><b>Others</b></summary></details>
