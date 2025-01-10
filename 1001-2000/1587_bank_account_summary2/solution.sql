select name, sum(amount) balance
from transactions
         inner join users using (account)
group by account, name
having sum(amount) > 10000;