# Self-utils
#### Some common things that I am afraid of, but are easy to implement
- Plotting and visualizing images -- easy don't know why i am afraid
- By default all the modules are initialized to train mode (self.training = True).
- Also be aware that some layers have different behavior during train/and evaluation (like BatchNorm, Dropout) so setting it matters.  ?? what's this
-  try to explicitly state your intent and set model.train() and model.eval() when necessary.
```model = model.train()```

**Note** : Most of the things and utils are already implemented. Just look for relevant place , `Kaggle, Pytorch forum, Github`,etc.

- [CNN Ensembler- Kaggle](https://www.kaggle.com/c/statoil-iceberg-classifier-challenge/discussion/44849)

**Bad Mistake**
x = F.dropout(x, p=0.5, training=True)

Correct way
x = F.dropout(x, p=0.5, training=self.training)

Tip : if you use nn.Dropout() it handles this automatically.

- call train()
- epoch of training on the training set
- call eval()
- evaluate your model on the validation set
- repeat
<br/>
https://github.com/kuangliu/pytorch-retinanet/blob/master/test.py

1. Using squeeze and unsquueeze
2. [37 reasons]()
3. [Karpathy :most common neural net mistakes](https://twitter.com/karpathy/status/1013244313327681536): 
	1. you didn't try to overfit a single batch first. 
	2. you forgot to toggle train/eval mode for the net. 
	3. you forgot to .zero_grad() (in pytorch) before .backward(). 
	4. you passed softmaxed outputs to a loss that expects raw logits. ; others? oh: 
	5. you didn't use bias=False for your Linear/Conv2d layer when using BatchNorm, or conversely forget to include it for the output layer .This one won't make you silently fail, but they are spurious parameters 
	6. thinking view() and permute() are the same thing (& incorrectly using view)
	7. do not set at 0 the dropout ratio at test time
	8. Not initializing with noise (leaving zeros instead)
	9. initializing with way too high values
	10. not pulling the break when any parameter reaches NaN
	11. you forgot converting to float() after a comparison of tensors and summing on ByteTensors that have a buffer of 255 and zero out after that (should be fixed in new pytorch).
	12. Not double-checking the learning rate --> an initial learning rate that is (far) too high leading to "weird" results.
	13. ~bad image augmentation --> I've accidentally augmented (w/a minor zoom in a loop) data loaded in memory, not a copy of the data, leading to ~useless data
	14. Worst thing I ever did: I trained a détection algorithm with bounding boxes DRAWN on my training set 😬 No wonder it converged so fast!
	15. Not shuffling training data, or otherwise using batches that have too much correlation between the examples in each batch.
	16. Forget to load back the best model after early stopping.
	17. softmax or other loss operation over wrong dim 6) wrong sign for loss term 7) forgetting to pass hidden state from encoder to decoder 8) forgetting to clip gradients, esp for RNNs. All learned the hard way
	18. Not using the same input normalization during inference as during training. Happens a lot when people use networks trained by others.
	19. forgetting to specify the dim/axis when calling sum, avg or max. fails silently e.g. when you're averaging batch errors for your loss function :/
	20. Forgetting to tell TensorFlow to record the moving mean and variance of batchnorm layers, which it doesn't do automatically. And then in test mode they're still 0 and 1, respectively.
	21. Common mistake for fine-tuning/feature extraction: mismatched data preprocessing (e.g. mean/std values different than pretrained set). Hard to spot because you can still get decent results, but you'll lose a couple of % compared to the proper way.
	22. ou initialize parameters to zero as opposed to a truncated normal or xavier.
	23. Forgot to set random seeds everywhere to get consistent and replicable results between runs
	24. You left a relu activation before a softmax
	25. forget to set shuffle=False in model dot fit when the order matters, for instance in time series.
	26. Clipping the loss instead of the gradients ;)
	27. Using Sigmoids instead of Softmax for multiclass classification.
	28. For vision tasks I also like to run a few batches through where I plot the same image before and after data augmentation to check that the random transformation parameters are chosen sensibly, including how to handle border effects.
	29. you stopped training too early when you saw your loss plateau -- check the paper stating early stopping
	30. 

TIP : exactly. I like to start with the simplest possible sanity checks - e.g. also training on all zero data first to see what loss I get with the base output distribution, then gradually include more inputs and scale up the net, making sure I beat the previous thing each time.<br/>

Some really [interesting tips](https://pcc.cs.byu.edu/2017/10/02/practical-advice-for-building-deep-neural-networks/) on debugging and Initializing models <br/>
