"""Problem statement:A Portuguese bank conducted marketing campaigns to promote term deposit subscriptions. The goal is to
predict whether a client will subscribe (yes or no) to a term deposit based on their profile and campaign
interaction details."""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
from sklearn.metrics import roc_curve,auc,roc_auc_score
from sklearn.preprocessing import StandardScaler,LabelEncoder

BORDER="-"*65

def loadDataFile(dataFilePath):
    
    dfBank=pd.read_csv(dataFilePath,sep=";")
    print(BORDER)
    print("Bank Term deposit susbsciprtion prediction data set loaded successfully...")
    print(BORDER)
    print("First five rows in dataset:")
    print(dfBank.head())
    print(BORDER)
    print("Shape of dataset is:")
    print(dfBank.shape)
    print(BORDER)
    return dfBank

def displayDatasetStatistics(dfBank):
    
    print("Data set columns details...")
    print(BORDER)
    print(dfBank.columns)
   
    #dfBank.dropna(inplace=True)

    print(BORDER)
    print("Bank details ststistics")
    print(BORDER)
    print(dfBank.describe())
    print(BORDER)
    return dfBank

def unknownValProcessing(dfBank):
    print("\t\tunknown values in column report")
    print(BORDER)
    colUnknown=[]
    colZero=[]
    unknownZeroValuesDF={"ColName":[],"Unknown Value Count":[],"Zero Value Count":[]}


    for colName in dfBank.columns:
        unknownValCount=(dfBank[colName]=='unknown').sum()
        unknownZeroValuesDF['ColName'].append(colName)
        unknownZeroValuesDF["Unknown Value Count"].append(unknownValCount)

        zeroValCount=(dfBank[colName]==0).sum()
        unknownZeroValuesDF["Zero Value Count"].append(zeroValCount)

        if unknownValCount > 0:
            colUnknown.append(colName)
        if zeroValCount > 0:
            colZero.append(colName)
    
    unknownZeroValuesDF=pd.DataFrame(unknownZeroValuesDF)
    
    print(BORDER)
    print("Column statitics for 'unknown' and '0' values")
    print(BORDER)

    print(unknownZeroValuesDF)
    print(BORDER)

    """Replace unknown and zero values with mean() """
    #colZero=['balance','duration',previous']
    #colUnknown=['job','education','contact','poutcome']
    print(BORDER)
    print("Col Name with 0 values :",colZero)
    print("Col Name with 'unknown' values :",colUnknown)
    print(BORDER)

    """Replacing 0 values with mean() of the column"""
    for colName in colZero:
        dfBank[colName]=dfBank[colName].replace(0,dfBank[colName].mean())


    """Different method 'unknown' values"""

    for colName in colUnknown:
        categoryList=dfBank[colName].value_counts().index.tolist()
        print(f"Col name 2 :{colName}")
        print(f"categoryList :{categoryList}")
        if(categoryList[0]!='unknown'):
            unknownCategoryName=categoryList[0]
        if(categoryList[0]=='unknown'):
            unknownCategoryName=categoryList[1]
        print(f"Col Name 2: {colName} Unknown Category Name  :{unknownCategoryName}")
        dfBank[colName]=dfBank[colName].replace('unknown',unknownCategoryName)

    print(BORDER)

    print(dfBank)
    dfBank.to_csv("replacedUnknownValues.csv")
    print(dfBank.shape)

def displayCorrelationMatrix(dfBank):
    plt.figure(figsize=(10,6))
    sns.heatmap(dfBank.corr(),annot=True,cmap="coolwarm")
    plt.title("Feature co-relation heatmap")
    plt.show()

def EncodeDataSet(dfBank):
    #Label enconding for all data set coulmns
    for colName in dfBank.select_dtypes(include=['object']).columns:
        #print(colName)
        labelEncoder = LabelEncoder()
        dfBank[colName]=labelEncoder.fit_transform(dfBank[colName])
        dfBank[colName].unique()
    print(BORDER)
    print("Creating encoded csv file for refernce with name 'BankTermDataEncoded.csv'")
    dfBank.to_csv("BankTermDataEncoded.csv")
    print(BORDER)
    print("Encoded Data frame")
    print(BORDER)
    print(dfBank.head())
    print(BORDER)
    return dfBank

def LoadAndExploreDataset():

    dfBankDeposit=loadDataFile("bank-full.csv")
   
    displayDatasetStatistics(dfBankDeposit)
    
    unknownValProcessing(dfBankDeposit)
    return dfBankDeposit


def prepareDataset(dfBank):
    xFeatures=dfBank.drop(columns=['y'])
    yLabel=dfBank['y']
    scalar=StandardScaler()
    x_scale=scalar.fit_transform(xFeatures)
    return x_scale,yLabel

def preprocessDataSet(dfBank):
     EncodeDataSet(dfBank)
     print(dfBank.head())
     displayCorrelationMatrix(dfBank)
     xIndependent,yDependent=prepareDataset(dfBank)
     return xIndependent ,yDependent

def bankTermSubscriptionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF):
    print(BORDER)
    print("Calculations using Logistic Regression Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Logistic Regression")
    logModel=LogisticRegression()
    logModel.fit(xTrainDS,yTrainDS)
    yPredictOutput=logModel.predict(xTestDS)
    y_predPositiveClassLR = logModel.predict_proba(xTestDS)[:, 1]
    aucScoreLR = roc_auc_score(yTestDS, y_predPositiveClassLR)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreLR)

    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)

    return yPredictOutput,y_predPositiveClassLR

def accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF):
    """Calculate Accuracy"""
   
    dsAccuracy=accuracy_score(yTestDS,yPredictOutput)
    print(BORDER)
    print("Accuracy is :",dsAccuracy)
    algorithmCompareDF["Accuracy Score"].append(dsAccuracy*100)

    """Calculate confusion Matrix """
    dsConfusionMatrix=confusion_matrix(yTestDS,yPredictOutput)
    print("Confusion Matrix is :\n",dsConfusionMatrix)
    algorithmCompareDF["Confusion Matrix"].append(dsConfusionMatrix)

    #precision    recall  f1-score   support
    print("Classification report...")
    print(BORDER)
    confusionMatrixReport=classification_report(yTestDS,yPredictOutput)
    print(confusionMatrixReport)


def bankTermSubscriptionUsingKNN(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,k=3):
    print(BORDER)
    print("Calculations using KNN Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("KNN")

    kNNModel=KNeighborsClassifier(n_neighbors=k)
    """Bulding the model"""
    kNNModel.fit(xTrainDS,yTrainDS)

    """Testing phase"""
    yPredictOutput=kNNModel.predict(xTestDS)
    
    """Positive y predictions"""
    yPredictPositiveKNN=kNNModel.predict_proba(xTestDS)[:,1]
    """ROC-AUC Score"""
    aucScoreKNN = roc_auc_score(yTestDS, yPredictPositiveKNN)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreKNN)


    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    return yPredictOutput,yPredictPositiveKNN 

def bankTermSubscriptionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,xIndependent):
    print(BORDER)
    print("Calculations using Random Forest Algorithm")
    print(BORDER)
    algorithmCompareDF["Algorithm Name"].append("Random Forest")

    randomForestModel=RandomForestClassifier(n_estimators=150,max_depth=7,random_state=42)

    """Bulding the model"""
    randomForestModel.fit(xTrainDS,yTrainDS)
    """Testing phase"""
    yPredictOutput=randomForestModel.predict(xTestDS)

    """Positive predictions"""
    ypredPositiveRF = randomForestModel.predict_proba(xTestDS)[:,1]

    """ROC-AUC Score"""
    aucScoreRF = roc_auc_score(yTestDS,ypredPositiveRF)
    algorithmCompareDF["ROC-AUC Score"].append(aucScoreRF)

    """Accuracy calculations"""
    accuracyCalculations(yTestDS,yPredictOutput,algorithmCompareDF)
    """Feature importance"""
    importance=pd.Series(randomForestModel.feature_importances_,index=pd.DataFrame(xIndependent).columns)

    importance=importance.sort_values(ascending=False)

    print("Feature importance:")

    importance.plot(kind="bar",figsize=(10,6),title="Feature Importance")
    plt.show()

    return yPredictOutput,ypredPositiveRF    

def plotAndCompareConfusionMatrixROC(algorithmCompareDF,actualVsPredicted):
    x=algorithmCompareDF['Algorithm Name']
    y=algorithmCompareDF['Accuracy Score']
    plt.bar(x,y,width=0.4)
    plt.title('Accuracy of algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.grid(True)
    plt.show()

    """Confusion Matrix using sub plots"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for cnt in range(len(algorithmCompareDF)):
        confuMatrix = ConfusionMatrixDisplay(confusion_matrix=algorithmCompareDF["Confusion Matrix"][cnt], 
                                             display_labels=["Subscribed","Non Subscribed"])
        confuMatrix.plot(ax=axes[cnt])
        axes[cnt].set_title(algorithmCompareDF["Algorithm Name"][cnt])
    plt.tight_layout()
    plt.show()


    print(actualVsPredicted)
    """Output in the CSV file"""
    actualVsPredicted.to_csv("BankPredictedVsActualResults.csv")


    """ROC Curve using sub plots"""
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(22, 5)) 

    for algoCnt in range(len(algorithmCompareDF)):
        algoName=algorithmCompareDF['Algorithm Name'][algoCnt]
        falsePositiveRate, truePositiveRate, threshold = roc_curve(actualVsPredicted['Actual'], actualVsPredicted[algoName])
        
        rocAuc = auc(falsePositiveRate, falsePositiveRate)
       
        axes[algoCnt].plot(falsePositiveRate,truePositiveRate,label=f"{algoName} (ROC-AUC Score {rocAuc})")
        axes[algoCnt].plot([0, 1], [0, 1], color="Red", label='Base Line',linestyle='--')

        axes[algoCnt].set_xlabel('False Positive Rate')
        axes[algoCnt].set_ylabel('True Positive Rate')
        axes[algoCnt].set_title('ROC Curves : Logistice Regression,KNN and Random Forest')
        #confuMatrix.plot(ax=axes[algoName])
        axes[algoCnt].set_title(algorithmCompareDF["Algorithm Name"][algoCnt])
        axes[algoCnt].legend()

    plt.tight_layout()
    plt.show()

    """ROC-AUC Curve"""
    plt.figure(figsize=(10, 6))
    
    for algoName in algorithmCompareDF['Algorithm Name']:
        falsePositiveRate, truePositiveRate, threshold = roc_curve(actualVsPredicted['Actual'], actualVsPredicted[algoName])
        rocAuc = auc(falsePositiveRate, truePositiveRate)
        plt.plot(falsePositiveRate,truePositiveRate,label=f"{algoName} (ROC-AUC Score {rocAuc})")
    plt.plot([0, 1], [0, 1], color="Red", label='Base Line',linestyle='--')

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves : Logistice Regression,KNN and Random Forest')
    plt.legend()
    plt.show()
"""---------------------------------------------------------------------------------
Task 3 : Train and Test using classification algorithm
         3.1 Logistic Regression
         3.2 KNN Algorithm
         3.3 Random Forest
#---------------------------------------------------------------------------------"""
def trainClassificationModel(xIndependent,yDependent):

    """Step 3 Split data set into training and testing part"""
    xTrainDS,xTestDS,yTrainDS,yTestDS=train_test_split(xIndependent,yDependent,test_size=0.2,random_state=42)
    
    algorithmCompareDF={"Algorithm Name":[],"Accuracy Score":[],"Confusion Matrix":[],"ROC-AUC Score":[]}
    
    """YPredictions Calculations using 'Logistic Regression' """
    yPredictedLR,ypredPositiveLR=bankTermSubscriptionUsingLogisticRegression(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF)
   
    """YPredictions using 'KNN """
    yPredictedKNN,yPredictPositiveKNN=bankTermSubscriptionUsingKNN(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,3)
   
    """Y Predictions using 'Random Forest"""
    yPredictionRF,yPredictPositiveRF=bankTermSubscriptionUsingRandomForest(xTrainDS,yTrainDS,xTestDS,yTestDS,algorithmCompareDF,xIndependent)

    actualVsPredicted={"Actual":yTestDS,
                       "RF":yPredictionRF,
                       "KNN":yPredictedKNN,
                       "LR":yPredictedLR,
                       "Logistic Regression":ypredPositiveLR,
                       "KNN":yPredictPositiveKNN,
                       "Random Forest":yPredictPositiveRF}
    
    print(BORDER)
    print("\t\tComparision matrix for all algorithm....")
    print(BORDER)
    algoDetails=pd.DataFrame(algorithmCompareDF)
    print(algoDetails)
    print("Predicted....")
    predictedDF=pd.DataFrame(actualVsPredicted,)
    print(BORDER)
    """Plotting comparision"""
    plotAndCompareConfusionMatrixROC(algoDetails,predictedDF)

def BankTermDepositSubscriptionPrediction():
    """1.Load and explore data set"""
    dfBankDeposit=LoadAndExploreDataset()
    """2. Preprocess Data set"""
    xIndependent,yDependent=preprocessDataSet(dfBankDeposit)
    
    """Split data set and Train Classification Models"""
    trainClassificationModel(xIndependent,yDependent)


def main():
    BankTermDepositSubscriptionPrediction()

if __name__=="__main__":
    main()