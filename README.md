# DatasetHarvester
*Easily download and set up Video Object Segmentation (VOS) datasets.*

### Overview

| Dataset | Status | Version(s) | Attributes |
| :--- | :--- | :--- | :--- |
| **SA-V** | ✅ Semi-Auto | - | - |
| **LVOS** | ✅ Auto | v1, v2 | Long-Term |
| **MOSE** | ✅ Auto | v1, v2 | Complex Scenarios |
| **OVIS** | ✅ Auto | - | - |
| **BURST** | ✅ Auto | - | - |
| **PUMaVOS** | ✅ Auto | - | Partial Masks|
| **VOST** | ✅ Auto | - | - |
| **Static** | ✅ Auto | - | Only for Training |
| **DiDi** | ⚠️ Manual | - | Distractor Heavy |
| **DAVIS** | ⚠️ Not Supported | 2016-2019 | - |
| **YouTube-VOS**| ⚠️ Not Supported | 2018-2022 | - |

> [!TIPS]  
> Descriptions, Official Repos & citations in [DATASETS.md](DATASETS.md).
> URLs for [supported_datasets.yaml](supported_datasets.yaml) and [not_supported_datasets.yaml](not_supported_datasets.yaml).


### Download LVOS, MOSE, OVIS, BURST, PUMaVOS, VOST & Static

```fish
python WizHarvester.py
```

### Download the Meta's [SA-V Dataset](https://ai.meta.com/datasets/segment-anything-video/)

1. Fill this [Meta document](https://ai.meta.com/datasets/segment-anything-video-downloads/) out to get access to the URLs.
2. Adapt [download_SA_V.yaml](./scripts/SA_V/download_SA_V.yaml) with the URLs.
3. Adapt the paths in [line 44 of download_SA_V.py](./scripts/SA_V/download_SA_V.py#L44)
4. Run
     ```fish
     cd scripts/SA_V/
     python download_SA_V.py
     ```
5. More stuff [**HERE**](https://github.com/facebookresearch/segment-anything-2/blob/main/sav_dataset)


### Download DAVIS & YouTube-VOS

Use this [script](https://github.com/hkchengrex/Mask-Propagation/blob/main/download_datasets.py) to download YouTubeVOS and DAVIS.


### Manual Downloads

Download and extract [DiDi](not_supported_datasets.yaml#9) manually.

---

> [!NOTE]  
> Contributions are welcome to help keep this repo up to date. 🤗

> [!TIP]  
> Modifed versions to act as pip packages for local evaluations:  
> vos-benchmark: https://github.com/hkchengrex/vos-benchmark.git  
> lvos-api: https://github.com/Vujas-Eteph/lvos-evaluation  
> mose-api: https://github.com/Vujas-Eteph/MOSE-api