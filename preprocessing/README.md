# preprocessing
preprocessing

## Dataset
We use FMA (Free Music Archive) dataset. \
Reference : <https://github.com/mdeff/fma>

## Dimensionality Reduction
We tested a number of models to find a suitable dimensionality reduction method for our data (common features extrated with librosa ). \
To check the result, the genre value was designated as a label for visualization and reduced to two dimensions.
Please refer to the [dimensionality_reduction_results](https://github.com/liger82/waterffle/tree/main/preprocessing/dimensionality_reduction_results) for the results.

## Clustering
우리는 Affinity Propagation 클러스터링을 사용했다.\
K-means와 그 유사한 알고리즘의 주요 단점은 클러스터의 개수를 정하고 최초 대표 점들을 선정해야 한다는 점이다.
AP([Affinity Propagation](https://liger82.github.io/the%20others/statistics/2021/05/01/affinity_propagation.html))는 데이터 포인트 쌍 간의 유사도를 측정하여 입력값으로 사용하고, 동시에 모든 데이터 포인트를 잠재적인 대표 데이터로 여긴다. 좋은 품질의 대표점들과 해당 클러스터들이 나타날 때까지 데이터 포인트 간에 실제 값 메시지가 교환된다.

## Code
The following notebooks, scripts, and modules have been developed for preprocessing.

- [`dimension_reduction_and_clustering.ipynb`]: shows how to load the datasets and test dimensionality reduction, clustering.

[`usage.ipynb`]: dimension_reduction_and_clustering.ipynb