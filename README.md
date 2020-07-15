# Paypal Transaction Visualizer
This visualizer is a tool that can be used to track and analyze all your PayPal expenditures.

This project was used as a way to try out many more advanced python features such as:
- functools.reduce()
- map()
- dict and list comprehensions

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library is used for  HTML Parsing, while all visualization
is done using [Matplotlib](https://matplotlib.org/).

## 1. Installation
To run this notebook follow these steps
1. First clone the repository: ```git clone https://github.com/bjoernpl/PaypalTransactionVisualizer.git```
2. Navigate to src directory: ```cd PaypalTransactionVisualizer```
3. Launch the notebook with ```jupyter notebook src/TransactionVisualizer.ipynb```
4. Exchange the html in ```payments.html``` with you PayPal transaction html
5. Run all cells to see the results

## 2. Retrieving Paypal transaction html
1. Log in to your account at [paypal.com](paypal.com)
2. Navigate to [paypal.com/myaccount/transactions](https://www.paypal.com/myaccount/transactions/)
3. Choose the time frame you want to analyze
4. Right-click the completed transactions section and select ``inspect``
5. Right-click 
    ````html
    <ul class="transactionList js_transactionList">
    ````
6. Select ``Edit as html`` followed by ``ctrl+a ctrl+c``
7. Replace all text in ``payments.html`` with the copied text