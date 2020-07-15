# Paypal Transaction Visualizer
This visualizer is a tool that can be used to track and analyze all your PayPal expenditures.

This project was used as a way to try out many more advanced python features such as:
- functools.reduce()
- map()
- dict and list comprehensions

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library is used for  HTML Parsing, while all visualization
is done using [Matplotlib](https://matplotlib.org/).

## 1. Installation
To use this project you can:

1. Run it online using [DataLore](https://datalore.io/notebook/ZzZiQkJ5dGKsGciTsZaT0t/PsjMBL65cDv0ruSQKuPCGL/)
    * Follow the link to open the notebook virtual environment
    * Navigate to ``Tools -> Attached files`` and upload your ``payments.html``
     (see section 2. for more info on how to access your your PayPal transaction data)
    * Run all cells to see results
2. Or you can run the notebook locally
    * First clone the repository: ```git clone https://github.com/bjoernpl/PaypalTransactionVisualizer.git```
    * Navigate to src directory: ```cd PaypalTransactionVisualizer```
    * Launch the notebook with ```jupyter notebook src/TransactionVisualizer.ipynb```
    * Exchange the html in ```payments.html``` with you PayPal transaction html
    * Run all cells to see the results

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