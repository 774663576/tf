retrain.py is an example script that shows how one can adapt a pretrained
network for other classification problems. A detailed overview of this script
can be found at:
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

The script also shows how one can train layers
with quantized weights and activations instead of taking a pre-trained floating
point model and then quantizing weights and activations.
The output graphdef produced by this script is compatible with the TensorFlow
Lite Optimizing Converter and can be converted to TFLite format.


 retrain.py --bottleneck_dir bottleneck --how_many_training_steps 200 --model_dir model/ --output_graph output_graph.pb --output_labels output_labels.txt --image_dir flower_photos