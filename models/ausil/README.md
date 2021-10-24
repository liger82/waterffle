# AuSiL
Audio Similarity Learning
참고 : [AuSiL github](https://github.com/mever-team/ausil/tree/51dc3b87bc412cd231aa7fc40703b8f4f582d2e)

mel spectogram을 입력으로 받아 lagre scale audio set으로 pre-train 된 CNN 사용하여 feature extraction
PCA, attention을 사용하여 두 audio feature를 합친후 AuSiL model을 거쳐 유사도 분석

## Code

- [`ausil_feature_extraction.ipynb`]: extract features from mel spectogram using pre-trained CNN (trained large scale audio set)
- [`ausil_for_waterffle.ipynb`]: AuSiL learning code 
- [`preprocessing.py`]: load the datesets

[`ausil_feature_extraction.ipynb`]: ausil_feature_extraction.ipynb
[`ausil_for_waterffle.ipynb`]: ausil_for_waterffle.ipynb
[`preprocessing.py`]: preprocessing.py
