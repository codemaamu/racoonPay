// transaction.js
const transactionList = document.getElementById('transactionList');

// Display transactions
transactions.forEach((transaction) => {
  const listItem = document.createElement('li');
  listItem.textContent = transaction;
  transactionList.appendChild(listItem);
});
