import json
import nltk
from nltk.tag.perceptron import PerceptronTagger


tagger = PerceptronTagger()
model = tagger.model

print("expo pesos")
weights_dict = {}
for feature, tag_weights in model.weights.items():
    for tag, weight in tag_weights.items():
        key = f"{feature}|||{tag}"
        weights_dict[key] = weight

classes = list(model.classes)

output = {
    'weights': weights_dict,
    'classes': classes
}

with open('perceptron_model.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)


