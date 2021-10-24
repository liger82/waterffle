# Experiments Info

## Architecture References

* [vggblock](https://github.com/pytorch/fairseq/blob/c36294ea4fd35eac757f417de9668b32c57d4b3d/fairseq/modules/vggblock.py#L22)
* [Transformers with convolutional context for ASR](https://arxiv.org/pdf/1904.11660.pdf)
* [poly-encoder](https://arxiv.org/abs/1905.01969)
* [poly-encoder in ParlAI website](https://parl.ai/projects/polyencoder/)
* [ausil](https://github.com/mever-team/ausil/tree/51dc3b87bc412cd231aa7fc40703b8f4f582d2ec)

## .ipynb file brief description

* AudioEncoder_poly.ipynb : vggblock + polyencoder(multiheadattention 직접 클래스 구현)
* modeling-transformer.ipynb : vggblock + polyencoder(torch.nn.TransformerEncoderLayer 사용)
* modeling-pytorch_ignite.ipynb : vggblock + polyencoder + pytorch ignite
* modeling-dotpro-mha.ipynb
* modeling-basic_chiames.ipynb
* modeling-chijames.ipynb