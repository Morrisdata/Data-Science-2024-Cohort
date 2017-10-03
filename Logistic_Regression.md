### Class 9: Logistic Regression

**After this lesson you will be able to:**
* Describe the kind of problem Logistic regression can solve
* Create a logistic regression model
* Describe the elements of a Confusion Matrix

**Topics/Highlights:**
* Logistic regression ([notebook](notebooks/09_logistic_regression.ipynb))
    * [Glass identification dataset](https://archive.ics.uci.edu/ml/datasets/Glass+Identification)
    * [e and natural log - what are they?](notebooks/09_e_log_examples.ipynb)
* Exercise with Titanic data ([notebook](notebooks/09_titanic_logistic_regression_exercise.ipynb), [data](data/titanic.csv), [data dictionary](https://www.kaggle.com/c/titanic/data))
* Confusion matrix ([slides](slides/09_confusion_matrix.pdf), [notebook](notebooks/09_confusion_matrix.ipynb))

**Homework:**
* Work through the code samples in the "Confusion matrix of Titanic predictions" section in [the 09_confusion_matrix.ipynb notebook](notebooks/09_confusion_matrix.ipynb) to see an example of changing a threshhold to get the desired behavior in the confusion matrix.
* If you aren't yet comfortable with all of the confusion matrix terminology, watch Rahul Patwari's videos on [Intuitive sensitivity and specificity](https://www.youtube.com/watch?v=U4_3fditnWg) (9 minutes) and [The tradeoff between sensitivity and specificity](https://www.youtube.com/watch?v=vtYDyGGeQyo) (13 minutes).
* Video/reading assignment on [ROC curves and AUC](homework/10_roc_auc.md)
* Video/reading assignment on [cross-validation](homework/10_cross_validation.md)

**Logistic Regression Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), or watch the [first three videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) (30 minutes) from that chapter.
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of four classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes) and one classifier we do not cover (Support Vector Machines).
