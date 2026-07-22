# Model Card

## Model
Random Forest Classifier

## Purpose
Predict the risk of late delivery in supply chain orders.

## Input
Customer, order, shipment and product information available before shipment.

## Output
- 0 = On-time Delivery
- 1 = Late Delivery

## Algorithms Tested
- Logistic Regression
- Random Forest

## Selected Model
Random Forest

## Evaluation Metrics
- Accuracy
- Classification Report
- Confusion Matrix

## Limitations
- Depends on historical data quality.
- Performance may decrease if future data changes significantly.
- Should assist decision-making, not replace human judgment.

