# -*- coding: utf-8 -*-
import numpy as np
from gensim.models import LdaModel
from dataset import ArXivDataset


class TopicModel:

    """The topic model class.

    Attributes
    ----------
    model : gensim.models.LdaModel
        Trained Linear Dirichlet Allocation model.

    dataset : ArXivDataset
        Dataset used to pre-process and train the LDA model.

    num_topics : int
        Number of topics for the topic model.

    topic_names : array_like
        List of topic names.

    topics : array_like
        List of (topic_name, topic_terms) tuples.

    """

    def __init__(self, model_path, dataset_path):
        """Instantiate a TopicModel object."""
        self.model = LdaModel.load(model_path)
        self.dataset = ArXivDataset.load(dataset_path)
        self.num_topics = self.model.num_topics
        self.topic_names = list(range(self.num_topics))
        self.topics = self.model.show_topics(num_topics=self.num_topics)

    def set_topic_names(self, names):
        """Assign topic names."""
        self.topic_names = names
        topic_terms = self.model.show_topics(num_topics=self.num_topics)
        self.topics = []
        for i, name in enumerate(names):
            self.topics.append((name, topic_terms[i][1]))

class TopicModel:
    def __init__(self, model, dictionary, topic_names):
        self.model = model
        self.dictionary = dictionary
        self.topic_names = topic_names

    def predict(self, text):
        bow_transformed = self.dictionary.doc2bow(text)
        topic_predictions = self.model.get_document_topics(bow_transformed)
        sorted_predictions = sorted(topic_predictions, key=lambda x: x[1], reverse=True)
        
        # Ensure topic_idx is within bounds
        valid_predictions = []
        for (topic_idx, prob) in sorted_predictions:
            if topic_idx < len(self.topic_names):
                valid_predictions.append((self.topic_names[topic_idx], prob))
            else:
                print(f"Invalid topic_idx: {topic_idx}, exceeds topic_names length")
        
        return valid_predictions
