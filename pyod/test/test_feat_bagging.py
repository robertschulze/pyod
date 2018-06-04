# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import os
import sys

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_greater
from sklearn.utils.testing import assert_greater_equal
from sklearn.utils.testing import assert_less_equal
from sklearn.utils.testing import assert_raises
from sklearn.utils.estimator_checks import check_estimator
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from scipy.io import loadmat

from pyod.models.feat_bagging import FeatureBagging
from pyod.models.lof import LOF


# TODO: finish the tests once the main model is ready
#       Placeholder only
class TestFeatureBagging(unittest.TestCase):
    def setUp(self):
        mat_file = 'cardio.mat'
        mat = loadmat(os.path.join('test_data', mat_file))
        X = mat['X']
        y = mat['y'].ravel()

        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.4)

        self.clf = FeatureBagging(base_estimator=LOF(),
                                  contamination=self.contamination)
        self.clf.fit(self.X_train)

    # def test_sklearn_estimator(self):
    #     check_estimator(self.clf)
    #
    # def test_parameters(self):
    #     if not hasattr(self.clf,
    #                    'decision_scores_') or self.clf.decision_scores_ is None:
    #         self.assertRaises(AttributeError, 'decision_scores_ is not set')
    #     if not hasattr(self.clf, 'labels_') or self.clf.labels_ is None:
    #         self.assertRaises(AttributeError, 'labels_ is not set')
    #     if not hasattr(self.clf, 'threshold_') or self.clf.threshold_ is None:
    #         self.assertRaises(AttributeError, 'threshold_ is not set')
    #     if not hasattr(self.clf, '_mu') or self.clf._mu is None:
    #         self.assertRaises(AttributeError, '_mu is not set')
    #     if not hasattr(self.clf, '_sigma') or self.clf._sigma is None:
    #         self.assertRaises(AttributeError, '_sigma is not set')
    #
    # def test_train_scores(self):
    #     assert_equal(len(self.clf.decision_scores_), self.X_train.shape[0])
    #
    # def test_prediction_scores(self):
    #     pred_scores = self.clf.decision_function(self.X_test)
    #
    #     # check score shapes
    #     assert_equal(pred_scores.shape[0], self.X_test.shape[0])
    #
    #     # check performance
    #     assert_greater(roc_auc_score(self.y_test, pred_scores), self.roc_floor)
    #
    # def test_prediction_labels(self):
    #     pred_labels = self.clf.predict(self.X_test)
    #     assert_equal(pred_labels.shape, self.y_test.shape)
    #
    # def test_prediction_proba(self):
    #     pred_proba = self.clf.predict_proba(self.X_test)
    #     assert_greater_equal(pred_proba.min(), 0)
    #     assert_less_equal(pred_proba.max(), 1)
    #
    # def test_prediction_proba_linear(self):
    #     pred_proba = self.clf.predict_proba(self.X_test, method='linear')
    #     assert_greater_equal(pred_proba.min(), 0)
    #     assert_less_equal(pred_proba.max(), 1)
    #
    # def test_prediction_proba_unify(self):
    #     pred_proba = self.clf.predict_proba(self.X_test, method='unify')
    #     assert_greater_equal(pred_proba.min(), 0)
    #     assert_less_equal(pred_proba.max(), 1)
    #
    # def test_prediction_proba_parameter(self):
    #     with assert_raises(ValueError):
    #         self.clf.predict_proba(self.X_test, method='something')
    #
    # def test_fit_predict(self):
    #     pred_labels = self.clf.fit_predict(self.X_train)
    #     assert_equal(pred_labels.shape, self.y_train.shape)
    #
    # def test_evaluate(self):
    #     self.clf.fit_predict_evaluate(self.X_test, self.y_test)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
